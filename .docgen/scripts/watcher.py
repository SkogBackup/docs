"""
File system watcher for automatic frontmatter generation.

Uses watchdog to monitor directories for new/modified markdown files
and queues them for processing with debouncing.
"""

import asyncio
import logging
from pathlib import Path
from typing import Callable, Dict, Optional, Set

from watchdog.events import FileSystemEvent, PatternMatchingEventHandler
from watchdog.observers import Observer

logger = logging.getLogger(__name__)

# Default patterns
DEFAULT_PATTERNS = ["**/*.md", "**/*.markdown"]
DEFAULT_IGNORE_PATTERNS = [
    "**/.git/**",
    "**/.docgen/input/**",
    "**/.docgen/output/**",
    "**/node_modules/**",
    "**/.venv/**",
    "**/__pycache__/**",
]


class DebouncedMarkdownHandler(PatternMatchingEventHandler):
    """Event handler with debouncing for markdown files.

    Debouncing prevents duplicate processing when editors save files
    multiple times in quick succession.
    """

    def __init__(
        self,
        queue: asyncio.Queue,
        loop: asyncio.AbstractEventLoop,
        debounce_delay: float = 0.5,
        patterns: Optional[list] = None,
        ignore_patterns: Optional[list] = None,
    ):
        """Initialize the handler.

        Args:
            queue: Async queue to push file paths to
            loop: Asyncio event loop for thread-safe queue operations
            debounce_delay: Delay in seconds before processing (default: 0.5s)
            patterns: File patterns to watch (default: *.md, *.markdown)
            ignore_patterns: Patterns to ignore (default: .git, node_modules, etc.)
        """
        super().__init__(
            patterns=patterns or DEFAULT_PATTERNS,
            ignore_patterns=ignore_patterns or DEFAULT_IGNORE_PATTERNS,
            ignore_directories=True,
            case_sensitive=False,
        )
        self.queue = queue
        self.loop = loop
        self.debounce_delay = debounce_delay
        self._pending: Dict[str, asyncio.TimerHandle] = {}
        self._processed: Set[str] = set()

    def on_created(self, event: FileSystemEvent) -> None:
        """Handle file creation events."""
        if not event.is_directory:
            logger.debug(f"File created: {event.src_path}")
            self._schedule_processing(event.src_path, priority=1)

    def on_modified(self, event: FileSystemEvent) -> None:
        """Handle file modification events."""
        if not event.is_directory:
            logger.debug(f"File modified: {event.src_path}")
            self._schedule_processing(event.src_path, priority=2)

    def on_moved(self, event: FileSystemEvent) -> None:
        """Handle file move/rename events."""
        if not event.is_directory and hasattr(event, "dest_path"):
            # Check if destination matches our patterns
            dest = Path(event.dest_path)
            if dest.suffix.lower() in (".md", ".markdown"):
                logger.debug(f"File moved to: {event.dest_path}")
                self._schedule_processing(event.dest_path, priority=1)

    def _schedule_processing(self, file_path: str, priority: int) -> None:
        """Schedule file for processing with debouncing.

        If a file is already scheduled, cancel the previous timer and
        reschedule. This handles rapid successive saves.

        Args:
            file_path: Path to the file
            priority: Processing priority (1=high/new, 2=lower/modified)
        """
        # Cancel existing timer for this file
        if file_path in self._pending:
            self._pending[file_path].cancel()
            del self._pending[file_path]

        # Schedule new processing after debounce delay
        def queue_file():
            if file_path in self._pending:
                del self._pending[file_path]

            # Thread-safe queue operation
            self.loop.call_soon_threadsafe(self.queue.put_nowait, (priority, file_path))
            logger.info(f"Queued for processing: {file_path}")

        # Use loop.call_later for debouncing
        handle = self.loop.call_later(self.debounce_delay, queue_file)
        self._pending[file_path] = handle

    def cancel_pending(self) -> int:
        """Cancel all pending timers.

        Returns:
            Number of cancelled timers
        """
        count = len(self._pending)
        for handle in self._pending.values():
            handle.cancel()
        self._pending.clear()
        return count


class DirectoryWatcher:
    """Manages watchdog observers for multiple directories."""

    def __init__(
        self,
        directories: list,
        queue: asyncio.Queue,
        loop: asyncio.AbstractEventLoop,
        debounce_delay: float = 0.5,
        patterns: Optional[list] = None,
        ignore_patterns: Optional[list] = None,
    ):
        """Initialize the watcher.

        Args:
            directories: List of directories to watch
            queue: Async queue to push file paths to
            loop: Asyncio event loop
            debounce_delay: Debounce delay in seconds
            patterns: File patterns to watch
            ignore_patterns: Patterns to ignore
        """
        self.directories = [Path(d) for d in directories]
        self.queue = queue
        self.loop = loop
        self.debounce_delay = debounce_delay
        self.patterns = patterns
        self.ignore_patterns = ignore_patterns

        self._observer: Optional[Observer] = None
        self._handler: Optional[DebouncedMarkdownHandler] = None

    def start(self) -> None:
        """Start watching directories."""
        self._handler = DebouncedMarkdownHandler(
            queue=self.queue,
            loop=self.loop,
            debounce_delay=self.debounce_delay,
            patterns=self.patterns,
            ignore_patterns=self.ignore_patterns,
        )

        self._observer = Observer()

        for directory in self.directories:
            if directory.exists():
                self._observer.schedule(
                    self._handler,
                    str(directory),
                    recursive=True,
                )
                logger.info(f"Watching directory: {directory}")
            else:
                logger.warning(f"Directory does not exist: {directory}")

        self._observer.start()
        logger.info("File watcher started")

    def stop(self) -> None:
        """Stop watching directories."""
        if self._handler:
            cancelled = self._handler.cancel_pending()
            if cancelled:
                logger.info(f"Cancelled {cancelled} pending operations")

        if self._observer:
            self._observer.stop()
            self._observer.join(timeout=5.0)
            logger.info("File watcher stopped")

    @property
    def is_running(self) -> bool:
        """Check if the watcher is running."""
        return self._observer is not None and self._observer.is_alive()


async def scan_existing_files(
    directories: list,
    queue: asyncio.Queue,
    skip_with_frontmatter: bool = True,
) -> int:
    """Scan directories for existing markdown files without frontmatter.

    Useful for initial processing of existing files.

    Args:
        directories: Directories to scan
        queue: Queue to add files to
        skip_with_frontmatter: Skip files that already have frontmatter

    Returns:
        Number of files queued
    """
    count = 0

    for directory in directories:
        path = Path(directory)
        if not path.exists():
            continue

        for md_file in path.rglob("*.md"):
            # Skip ignored directories
            if any(part.startswith(".") for part in md_file.parts):
                continue
            if "node_modules" in md_file.parts:
                continue

            # Check for existing frontmatter
            if skip_with_frontmatter:
                try:
                    content = md_file.read_text(encoding="utf-8")
                    if content.strip().startswith("---"):
                        logger.debug(f"Skipping (has frontmatter): {md_file}")
                        continue
                except Exception as e:
                    logger.warning(f"Could not read {md_file}: {e}")
                    continue

            await queue.put((2, str(md_file)))  # Priority 2 (lower than new files)
            count += 1
            logger.debug(f"Queued existing file: {md_file}")

    logger.info(f"Queued {count} existing files for processing")
    return count
