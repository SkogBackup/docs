"""
Async worker pool for processing markdown files.

Workers consume files from a queue and generate frontmatter
using the LLM client.
"""

import asyncio
import logging
import time
from pathlib import Path
from typing import Callable, Optional

try:
    from .llm import generate_frontmatter, LLMError, ModelNotFoundError
    from .models import DocumentMeta, Frontmatter, ProcessingResult
    from .writer import inject_frontmatter, has_frontmatter
except ImportError:
    from llm import generate_frontmatter, LLMError, ModelNotFoundError
    from models import DocumentMeta, Frontmatter, ProcessingResult
    from writer import inject_frontmatter, has_frontmatter

logger = logging.getLogger(__name__)


class WorkerPool:
    """Pool of async workers for processing files."""

    def __init__(
        self,
        queue: asyncio.Queue,
        num_workers: int = 2,
        model: str = "qwen3:4b",
        skip_existing_frontmatter: bool = True,
        on_complete: Optional[Callable[[ProcessingResult], None]] = None,
    ):
        """Initialize the worker pool.

        Args:
            queue: Queue to consume files from
            num_workers: Number of concurrent workers
            model: Ollama model to use
            skip_existing_frontmatter: Skip files that already have frontmatter
            on_complete: Callback for each processed file
        """
        self.queue = queue
        self.num_workers = num_workers
        self.model = model
        self.skip_existing_frontmatter = skip_existing_frontmatter
        self.on_complete = on_complete

        self._workers: list = []
        self._running = False
        self._processed_count = 0
        self._error_count = 0

    async def _worker(self, worker_id: int) -> None:
        """Worker coroutine that processes files from the queue.

        Args:
            worker_id: Identifier for this worker (for logging)
        """
        logger.info(f"Worker {worker_id} started")

        while self._running:
            try:
                # Wait for a file with timeout (allows checking _running flag)
                try:
                    priority, file_path = await asyncio.wait_for(
                        self.queue.get(), timeout=1.0
                    )
                except asyncio.TimeoutError:
                    continue

                result = await self._process_file(worker_id, file_path)

                if result.success:
                    self._processed_count += 1
                else:
                    self._error_count += 1

                if self.on_complete:
                    try:
                        self.on_complete(result)
                    except Exception as e:
                        logger.error(f"Error in on_complete callback: {e}")

                self.queue.task_done()

            except asyncio.CancelledError:
                logger.info(f"Worker {worker_id} cancelled")
                break
            except Exception as e:
                logger.error(f"Worker {worker_id} error: {e}")

        logger.info(f"Worker {worker_id} stopped")

    async def _process_file(self, worker_id: int, file_path: str) -> ProcessingResult:
        """Process a single file.

        Args:
            worker_id: Worker identifier
            file_path: Path to the markdown file

        Returns:
            ProcessingResult with success status and details
        """
        start_time = time.time()
        path = Path(file_path)

        logger.info(f"[Worker {worker_id}] Processing: {file_path}")

        # Check if file exists
        if not path.exists():
            logger.warning(f"[Worker {worker_id}] File not found: {file_path}")
            return ProcessingResult(
                file_path=file_path,
                success=False,
                error="File not found",
                duration_ms=(time.time() - start_time) * 1000,
            )

        try:
            # Read content
            content = path.read_text(encoding="utf-8")

            # Check for existing frontmatter
            if self.skip_existing_frontmatter and has_frontmatter(content):
                logger.info(
                    f"[Worker {worker_id}] Skipping (has frontmatter): {file_path}"
                )
                return ProcessingResult(
                    file_path=file_path,
                    success=True,
                    error="Skipped (existing frontmatter)",
                    duration_ms=(time.time() - start_time) * 1000,
                )

            # Generate frontmatter using LLM
            logger.debug(f"[Worker {worker_id}] Calling LLM for: {file_path}")
            frontmatter = await generate_frontmatter(content, model=self.model)

            # Create complete document metadata
            # Get relative path from docs root
            try:
                docs_root = Path(
                    __file__
                ).parent.parent.parent  # .docgen/scripts -> docs/
                rel_path = path.relative_to(docs_root)
            except ValueError:
                rel_path = path

            doc_meta = DocumentMeta.from_file_path(rel_path, frontmatter)

            # Inject frontmatter into file
            await inject_frontmatter(file_path, doc_meta)

            duration_ms = (time.time() - start_time) * 1000
            logger.info(
                f"[Worker {worker_id}] ✓ Done ({duration_ms:.0f}ms): {file_path}"
            )

            return ProcessingResult(
                file_path=file_path,
                success=True,
                frontmatter=doc_meta,
                duration_ms=duration_ms,
            )

        except ModelNotFoundError as e:
            logger.error(f"[Worker {worker_id}] Model error: {e}")
            return ProcessingResult(
                file_path=file_path,
                success=False,
                error=str(e),
                duration_ms=(time.time() - start_time) * 1000,
            )

        except LLMError as e:
            logger.error(f"[Worker {worker_id}] LLM error: {e}")
            return ProcessingResult(
                file_path=file_path,
                success=False,
                error=str(e),
                duration_ms=(time.time() - start_time) * 1000,
            )

        except Exception as e:
            logger.error(f"[Worker {worker_id}] Unexpected error: {e}")
            return ProcessingResult(
                file_path=file_path,
                success=False,
                error=str(e),
                duration_ms=(time.time() - start_time) * 1000,
            )

    async def start(self) -> None:
        """Start the worker pool."""
        if self._running:
            logger.warning("Worker pool already running")
            return

        self._running = True
        self._workers = [
            asyncio.create_task(self._worker(i)) for i in range(self.num_workers)
        ]
        logger.info(f"Started {self.num_workers} workers")

    async def stop(self, timeout: float = 5.0) -> None:
        """Stop the worker pool gracefully.

        Args:
            timeout: Maximum time to wait for workers to finish
        """
        if not self._running:
            return

        self._running = False

        # Wait for queue to drain (with timeout)
        try:
            await asyncio.wait_for(self.queue.join(), timeout=timeout)
        except asyncio.TimeoutError:
            logger.warning(f"Queue did not drain within {timeout}s timeout")

        # Cancel workers
        for worker in self._workers:
            worker.cancel()

        # Wait for workers to finish
        await asyncio.gather(*self._workers, return_exceptions=True)
        self._workers = []

        logger.info(
            f"Worker pool stopped. Processed: {self._processed_count}, "
            f"Errors: {self._error_count}"
        )

    @property
    def stats(self) -> dict:
        """Get worker pool statistics."""
        return {
            "running": self._running,
            "num_workers": self.num_workers,
            "processed_count": self._processed_count,
            "error_count": self._error_count,
            "queue_size": self.queue.qsize(),
        }
