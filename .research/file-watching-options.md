# File Watching Options Research

## Executive Summary

Two primary approaches for monitoring markdown file changes:
1. **inotify-tools (Shell)** - Kernel-level, lightweight, Linux-native
2. **Python watchdog** - Cross-platform, feature-rich, better batching

**Recommendation**: Use **Python watchdog** for flexibility and integration with existing Python scripts, with inotifywait as backup for simple use cases.

---

## Option 1: inotify-tools (inotifywait)

### Overview
Linux kernel-level file system notification system. Zero-polling, instant detection.

### Installation
```bash
sudo apt install inotify-tools  # Debian/Ubuntu
sudo pacman -S inotify-tools     # Arch
```

### Basic Usage
```bash
# Watch for new/modified markdown files
inotifywait -m -r -e create,modify --format '%w%f' ./docs \
  | while read file; do
      if [[ "$file" == *.md ]]; then
        echo "Processing: $file"
        cp "$file" .docgen/input/
      fi
    done
```

### Pros
- Kernel-level: no polling, instant detection
- Minimal resource usage
- Simple shell integration
- Already available on Linux

### Cons
- Linux-only (no macOS/Windows)
- Limited batching/debouncing
- No pattern matching built-in
- Harder to integrate with Python async

### Best For
- Simple daemon scripts
- Low-overhead monitoring
- Pure shell automation

---

## Option 2: Python watchdog

### Overview
Cross-platform file system monitoring with rich event handling and pattern matching.

### Installation
```bash
pip install watchdog
```

### Basic Usage
```python
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

class MarkdownHandler(PatternMatchingEventHandler):
    def __init__(self):
        super().__init__(
            patterns=["**/*.md"],
            ignore_patterns=["**/node_modules/**", "**/.git/**"],
            ignore_directories=True
        )
    
    def on_created(self, event):
        print(f"New file: {event.src_path}")
        self.process_file(event.src_path)
    
    def on_modified(self, event):
        print(f"Modified: {event.src_path}")
        self.process_file(event.src_path)
    
    def process_file(self, file_path):
        # Queue for frontmatter generation
        import shutil
        shutil.copy(file_path, ".docgen/input/")

observer = Observer()
observer.schedule(MarkdownHandler(), "./docs", recursive=True)
observer.start()
```

### Debouncing Pattern

Watchdog can fire multiple events per file modification. Solution:

```python
import time
from threading import Timer

class DebouncedHandler(PatternMatchingEventHandler):
    def __init__(self, debounce_seconds=0.5):
        super().__init__(patterns=["**/*.md"])
        self.debounce_seconds = debounce_seconds
        self.timers = {}
    
    def on_any_event(self, event):
        if event.is_directory:
            return
        
        # Cancel existing timer for this file
        if event.src_path in self.timers:
            self.timers[event.src_path].cancel()
        
        # Schedule new timer
        timer = Timer(
            self.debounce_seconds,
            self.process_file,
            [event.src_path]
        )
        self.timers[event.src_path] = timer
        timer.start()
    
    def process_file(self, file_path):
        del self.timers[file_path]
        print(f"Processing (debounced): {file_path}")
```

### Async Integration

Bridge watchdog's threading with asyncio:

```python
import asyncio
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class AsyncEventHandler(FileSystemEventHandler):
    def __init__(self, queue: asyncio.Queue, loop: asyncio.AbstractEventLoop):
        self.queue = queue
        self.loop = loop
    
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.md'):
            self.loop.call_soon_threadsafe(
                self.queue.put_nowait,
                ('created', event.src_path)
            )

async def main():
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()
    
    handler = AsyncEventHandler(queue, loop)
    observer = Observer()
    observer.schedule(handler, "./docs", recursive=True)
    observer.start()
    
    while True:
        event_type, file_path = await queue.get()
        print(f"Async processing: {event_type} - {file_path}")
        # Process file here

asyncio.run(main())
```

### Pros
- Cross-platform (Linux/macOS/Windows)
- Pattern matching built-in
- Easy debouncing/batching
- Python async integration
- Rich event types

### Cons
- Python dependency
- Slightly higher resource usage than inotify
- Requires daemon process

### Best For
- Complex automation pipelines
- Cross-platform requirements
- Integration with Python tools
- Async processing

---

## Option 3: Git Hooks

### Overview
Trigger on git commit events rather than file system changes.

### Implementation
```bash
# .git/hooks/post-commit
#!/bin/bash

# Get list of changed markdown files
changed_files=$(git diff-tree --no-commit-id --name-only -r HEAD | grep '\.md$')

for file in $changed_files; do
    if [ -f "$file" ]; then
        cp "$file" .docgen/input/
        echo "Queued: $file"
    fi
done

# Trigger queue processing
.docgen/scripts/process-queue.sh
```

### Pros
- Integrates with version control workflow
- Only processes committed files
- No daemon required

### Cons
- Misses uncommitted changes
- Delayed processing (commit-time only)
- Requires git discipline

### Best For
- CI/CD integration
- Production-ready docs only
- Commit-triggered workflows

---

## Comparison Matrix

| Feature | inotify | watchdog | Git Hooks |
|---------|---------|----------|-----------|
| Platform | Linux only | Cross-platform | Cross-platform |
| Detection | Instant | Instant | On commit |
| Batching | Manual | Built-in | Automatic |
| Async | Hard | Easy | N/A |
| Resources | Minimal | Low | None |
| Pattern matching | Manual | Built-in | Manual |
| Python integration | Subprocess | Native | Subprocess |

---

## Recommended Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    File System                              │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              Python Watchdog (Primary)                      │
│  - PatternMatchingEventHandler for *.md                     │
│  - Debouncing (0.5s delay)                                  │
│  - Ignore patterns (.git, node_modules)                     │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  Async Queue                                │
│  - asyncio.Queue for event batching                         │
│  - FIFO processing                                          │
│  - Concurrent LLM calls (limited)                           │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│               LLM Processing (Ollama)                       │
│  - Structured output with Pydantic schema                   │
│  - Retry with exponential backoff                           │
│  - Validation before write                                  │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  File Writer                                │
│  - Inject frontmatter                                       │
│  - Preserve original content                                │
│  - Update database metadata                                 │
└─────────────────────────────────────────────────────────────┘
```

---

## systemd Service Template

For 24/7 operation:

```ini
# /etc/systemd/user/docgen-watcher.service
[Unit]
Description=Documentation Frontmatter Auto-Generator
After=network.target ollama.service

[Service]
Type=simple
WorkingDirectory=/home/skogix/docs
ExecStart=/home/skogix/docs/.docgen/scripts/watcher.py
Restart=always
RestartSec=10
Environment=OLLAMA_HOST=http://localhost:11434

[Install]
WantedBy=default.target
```

Enable with:
```bash
systemctl --user enable docgen-watcher
systemctl --user start docgen-watcher
```
