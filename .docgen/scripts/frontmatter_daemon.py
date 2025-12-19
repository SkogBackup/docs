#!/usr/bin/env python3
"""
Frontmatter generation daemon.

Monitors directories for new/modified markdown files and automatically
generates frontmatter using a local LLM via Ollama.

Usage:
    cd /home/skogix/docs/.docgen
    uv run python -m scripts.frontmatter_daemon

Or directly:
    uv run --directory .docgen python scripts/frontmatter_daemon.py

Configuration via environment variables:
    DOCGEN_MODEL: Ollama model to use (default: qwen3:4b)
    DOCGEN_WORKERS: Number of concurrent workers (default: 2)
    DOCGEN_DEBOUNCE: Debounce delay in seconds (default: 0.5)
    DOCGEN_DIRS: Comma-separated list of directories to watch
"""

import argparse
import asyncio
import logging
import os
import signal
import sys
from pathlib import Path
from typing import List, Optional

# Handle imports for both module and direct execution
if __name__ == "__main__":
    # Running directly - add scripts directory to path
    sys.path.insert(0, str(Path(__file__).parent))
    from watcher import DirectoryWatcher, scan_existing_files
    from workers import WorkerPool
    from llm import check_ollama_health, pull_model_if_needed, DEFAULT_MODEL
    from models import ProcessingResult
else:
    # Running as module
    from .watcher import DirectoryWatcher, scan_existing_files
    from .workers import WorkerPool
    from .llm import check_ollama_health, pull_model_if_needed, DEFAULT_MODEL
    from .models import ProcessingResult

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)

# Default configuration
# Paths relative to parent docs/ directory (daemon runs from .docgen/)
DEFAULT_WATCH_DIRS = [
    "../agents",
    "../skogix",
    "../tools",
]
DEFAULT_NUM_WORKERS = 2
DEFAULT_DEBOUNCE_DELAY = 0.5


class FrontmatterDaemon:
    """Main daemon class for frontmatter generation."""

    def __init__(
        self,
        watch_dirs: List[str],
        model: str = DEFAULT_MODEL,
        num_workers: int = DEFAULT_NUM_WORKERS,
        debounce_delay: float = DEFAULT_DEBOUNCE_DELAY,
        scan_existing: bool = False,
    ):
        """Initialize the daemon.

        Args:
            watch_dirs: List of directories to watch
            model: Ollama model to use
            num_workers: Number of concurrent workers
            debounce_delay: Debounce delay in seconds
            scan_existing: Whether to scan and process existing files on startup
        """
        self.watch_dirs = watch_dirs
        self.model = model
        self.num_workers = num_workers
        self.debounce_delay = debounce_delay
        self.scan_existing = scan_existing

        self._queue: Optional[asyncio.PriorityQueue] = None
        self._watcher: Optional[DirectoryWatcher] = None
        self._worker_pool: Optional[WorkerPool] = None
        self._stop_event: Optional[asyncio.Event] = None
        self._running = False

    def _on_file_processed(self, result: ProcessingResult) -> None:
        """Callback for processed files."""
        if result.success and result.frontmatter:
            logger.info(
                f"Generated frontmatter for: {result.file_path} "
                f"(title: {result.frontmatter.title})"
            )
        elif result.error and "Skipped" not in result.error:
            logger.error(f"Failed to process {result.file_path}: {result.error}")

    async def start(self) -> None:
        """Start the daemon."""
        if self._running:
            logger.warning("Daemon already running")
            return

        logger.info("=" * 60)
        logger.info("Starting Frontmatter Generation Daemon")
        logger.info("=" * 60)
        logger.info(f"Model: {self.model}")
        logger.info(f"Workers: {self.num_workers}")
        logger.info(f"Debounce: {self.debounce_delay}s")
        logger.info(f"Directories: {self.watch_dirs}")
        logger.info("=" * 60)

        # Check Ollama health
        logger.info("Checking Ollama health...")
        if not await check_ollama_health(self.model):
            logger.warning(f"Model '{self.model}' not available, attempting to pull...")
            if not await pull_model_if_needed(self.model):
                logger.error("Failed to pull model. Exiting.")
                return

        logger.info("Ollama health check passed")

        # Initialize components
        loop = asyncio.get_event_loop()
        self._queue = asyncio.PriorityQueue()
        self._stop_event = asyncio.Event()

        # Start worker pool
        self._worker_pool = WorkerPool(
            queue=self._queue,
            num_workers=self.num_workers,
            model=self.model,
            on_complete=self._on_file_processed,
        )
        await self._worker_pool.start()

        # Start file watcher
        self._watcher = DirectoryWatcher(
            directories=self.watch_dirs,
            queue=self._queue,
            loop=loop,
            debounce_delay=self.debounce_delay,
        )
        self._watcher.start()

        self._running = True

        # Scan existing files if requested
        if self.scan_existing:
            logger.info("Scanning for existing files without frontmatter...")
            count = await scan_existing_files(
                directories=self.watch_dirs,
                queue=self._queue,
                skip_with_frontmatter=True,
            )
            if count > 0:
                logger.info(f"Queued {count} existing files for processing")

        logger.info("Daemon started successfully. Press Ctrl+C to stop.")

        # Wait for stop signal
        await self._stop_event.wait()

    async def stop(self) -> None:
        """Stop the daemon gracefully."""
        if not self._running:
            return

        logger.info("Stopping daemon...")

        # Stop watcher first (no new files)
        if self._watcher:
            self._watcher.stop()

        # Stop worker pool (finish current work)
        if self._worker_pool:
            await self._worker_pool.stop(timeout=10.0)
            stats = self._worker_pool.stats
            logger.info(
                f"Final stats - Processed: {stats['processed_count']}, "
                f"Errors: {stats['error_count']}"
            )

        self._running = False

        if self._stop_event:
            self._stop_event.set()

        logger.info("Daemon stopped")

    def request_stop(self) -> None:
        """Request the daemon to stop (from signal handler)."""
        if self._stop_event:
            self._stop_event.set()


async def run_daemon(args: argparse.Namespace) -> None:
    """Run the daemon with given arguments."""
    # Parse watch directories
    if args.dirs:
        watch_dirs = [d.strip() for d in args.dirs.split(",")]
    else:
        watch_dirs = os.environ.get("DOCGEN_DIRS", "").split(",")
        watch_dirs = [d.strip() for d in watch_dirs if d.strip()] or DEFAULT_WATCH_DIRS

    # Get configuration from args or environment
    model = args.model or os.environ.get("DOCGEN_MODEL", DEFAULT_MODEL)
    num_workers = args.workers or int(
        os.environ.get("DOCGEN_WORKERS", DEFAULT_NUM_WORKERS)
    )
    debounce = args.debounce or float(
        os.environ.get("DOCGEN_DEBOUNCE", DEFAULT_DEBOUNCE_DELAY)
    )

    # Create daemon
    daemon = FrontmatterDaemon(
        watch_dirs=watch_dirs,
        model=model,
        num_workers=num_workers,
        debounce_delay=debounce,
        scan_existing=args.scan_existing,
    )

    # Setup signal handlers
    loop = asyncio.get_event_loop()

    def signal_handler():
        logger.info("\nReceived shutdown signal...")
        daemon.request_stop()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, signal_handler)

    try:
        await daemon.start()
    finally:
        await daemon.stop()


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Frontmatter Generation Daemon",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Start with defaults
    python frontmatter-daemon.py
    
    # Watch specific directories
    python frontmatter-daemon.py --dirs "./agents,./skogix"
    
    # Use different model with more workers
    python frontmatter-daemon.py --model llama3.1:8b --workers 4
    
    # Process existing files on startup
    python frontmatter-daemon.py --scan-existing
        """,
    )

    parser.add_argument(
        "--dirs",
        "-d",
        type=str,
        help="Comma-separated list of directories to watch",
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        help=f"Ollama model to use (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--workers",
        "-w",
        type=int,
        help=f"Number of concurrent workers (default: {DEFAULT_NUM_WORKERS})",
    )
    parser.add_argument(
        "--debounce",
        type=float,
        help=f"Debounce delay in seconds (default: {DEFAULT_DEBOUNCE_DELAY})",
    )
    parser.add_argument(
        "--scan-existing",
        action="store_true",
        help="Scan and process existing files without frontmatter on startup",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging",
    )

    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        asyncio.run(run_daemon(args))
    except KeyboardInterrupt:
        pass  # Handled by signal handler


if __name__ == "__main__":
    main()
