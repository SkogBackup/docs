# Plan: Automated Frontmatter Generation System

## Overview

Create a real-time documentation automation system that monitors the docs repository for new/modified markdown files and automatically generates frontmatter using local LLM (Ollama).

## Goals

1. **Real-time detection** - Instant awareness of new/modified `.md` files
2. **Intelligent frontmatter** - LLM-generated title, tags, type based on content
3. **24/7 operation** - Reliable background service with multiple Ollama instances
4. **Quality output** - Structured, validated frontmatter using Pydantic schemas
5. **Seamless integration** - Build on existing `.docgen/` infrastructure

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    docs/ repository                             │
│  agents/ │ skogix/ │ tools/ │ .docgen/                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ File events (create/modify)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Watcher Service                               │
│  - Python watchdog library                                      │
│  - PatternMatchingEventHandler for *.md                         │
│  - Debouncing (500ms delay)                                     │
│  - Ignore: .git, node_modules, .docgen/input                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Debounced events
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Event Queue                                   │
│  - asyncio.Queue for event batching                             │
│  - Deduplication by file path                                   │
│  - Priority: new files > modified files                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Concurrent processing
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   LLM Worker Pool                               │
│  - 2-4 async workers                                            │
│  - ollama AsyncClient                                           │
│  - Structured output via Pydantic schema                        │
│  - Retry with exponential backoff                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Validated frontmatter
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   File Writer                                   │
│  - Inject frontmatter preserving content                        │
│  - Update SQLite metadata                                       │
│  - Logging and metrics                                          │
└─────────────────────────────────────────────────────────────────┘
```

---

## Implementation Phases

### Phase 1: Core Infrastructure (Day 1-2)

#### 1.1 Pydantic Schema for Frontmatter

```python
# .docgen/scripts/models.py
from pydantic import BaseModel, Field
from typing import List, Literal
from datetime import datetime

class Frontmatter(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    tags: List[str] = Field(..., min_items=3, max_items=7)
    type: Literal["note", "guide", "reference"] = "note"
    
class DocumentMeta(BaseModel):
    categories: List[str]  # Auto-generated from path
    permalink: str         # Auto-generated
    generated_at: datetime # Auto-generated
    frontmatter: Frontmatter  # LLM-generated
```

#### 1.2 Ollama Client Wrapper

```python
# .docgen/scripts/llm.py
import ollama
from tenacity import retry, stop_after_attempt, wait_exponential
from .models import Frontmatter

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)
async def generate_frontmatter(content: str, model: str = "qwen3:4b") -> Frontmatter:
    """Generate structured frontmatter using Ollama."""
    client = ollama.AsyncClient()
    
    response = await client.chat(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Generate frontmatter:\n\n{content[:1000]}"}
        ],
        format=Frontmatter.model_json_schema(),
        options={"temperature": 0}
    )
    
    return Frontmatter.model_validate_json(response.message.content)
```

#### 1.3 Dependencies

```txt
# .docgen/requirements.txt
watchdog>=4.0.0
ollama>=0.4.0
pydantic>=2.0.0
tenacity>=8.0.0
aiosqlite>=0.19.0
```

---

### Phase 2: File Watcher Service (Day 2-3)

#### 2.1 Watcher Implementation

```python
# .docgen/scripts/watcher.py
import asyncio
from pathlib import Path
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from .llm import generate_frontmatter
from .writer import inject_frontmatter

class MarkdownHandler(PatternMatchingEventHandler):
    def __init__(self, queue: asyncio.Queue, loop: asyncio.AbstractEventLoop):
        super().__init__(
            patterns=["**/*.md"],
            ignore_patterns=[
                "**/.git/**",
                "**/.docgen/input/**",
                "**/node_modules/**"
            ],
            ignore_directories=True
        )
        self.queue = queue
        self.loop = loop
        self.pending = {}
        self.debounce_delay = 0.5
    
    def on_created(self, event):
        self._queue_file(event.src_path, priority=1)
    
    def on_modified(self, event):
        self._queue_file(event.src_path, priority=2)
    
    def _queue_file(self, file_path: str, priority: int):
        """Queue file with debouncing."""
        if file_path in self.pending:
            self.pending[file_path].cancel()
        
        timer = self.loop.call_later(
            self.debounce_delay,
            lambda: self.loop.call_soon_threadsafe(
                self.queue.put_nowait,
                (priority, file_path)
            )
        )
        self.pending[file_path] = timer
```

#### 2.2 Async Worker Pool

```python
# .docgen/scripts/workers.py
import asyncio
from pathlib import Path
from .llm import generate_frontmatter
from .writer import inject_frontmatter

async def process_worker(queue: asyncio.Queue, worker_id: int):
    """Process files from queue."""
    while True:
        priority, file_path = await queue.get()
        
        try:
            print(f"[Worker {worker_id}] Processing: {file_path}")
            
            content = Path(file_path).read_text()
            
            # Skip if already has frontmatter (optional)
            if content.startswith("---"):
                print(f"[Worker {worker_id}] Skipping (has frontmatter)")
                continue
            
            frontmatter = await generate_frontmatter(content)
            await inject_frontmatter(file_path, frontmatter)
            
            print(f"[Worker {worker_id}] ✓ Done: {file_path}")
            
        except Exception as e:
            print(f"[Worker {worker_id}] ✗ Error: {e}")
        
        finally:
            queue.task_done()
```

---

### Phase 3: Service Management (Day 3-4)

#### 3.1 Main Entry Point

```python
#!/usr/bin/env python3
# .docgen/scripts/frontmatter-daemon.py

import asyncio
import signal
from pathlib import Path
from watchdog.observers import Observer
from .watcher import MarkdownHandler
from .workers import process_worker

WATCH_DIRS = [
    "./agents",
    "./skogix", 
    "./tools"
]
NUM_WORKERS = 2

async def main():
    loop = asyncio.get_event_loop()
    queue = asyncio.PriorityQueue()
    
    # Start workers
    workers = [
        asyncio.create_task(process_worker(queue, i))
        for i in range(NUM_WORKERS)
    ]
    
    # Start watcher
    handler = MarkdownHandler(queue, loop)
    observer = Observer()
    
    for watch_dir in WATCH_DIRS:
        if Path(watch_dir).exists():
            observer.schedule(handler, watch_dir, recursive=True)
            print(f"Watching: {watch_dir}")
    
    observer.start()
    print(f"Started {NUM_WORKERS} workers. Press Ctrl+C to stop.")
    
    # Handle shutdown
    stop_event = asyncio.Event()
    
    def shutdown():
        print("\nShutting down...")
        stop_event.set()
    
    loop.add_signal_handler(signal.SIGINT, shutdown)
    loop.add_signal_handler(signal.SIGTERM, shutdown)
    
    await stop_event.wait()
    
    observer.stop()
    observer.join()
    
    for worker in workers:
        worker.cancel()

if __name__ == "__main__":
    asyncio.run(main())
```

#### 3.2 systemd Service

```ini
# ~/.config/systemd/user/docgen-watcher.service
[Unit]
Description=Documentation Frontmatter Auto-Generator
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/skogix/docs
ExecStart=/home/skogix/docs/.venv/bin/python -m .docgen.scripts.frontmatter-daemon
Restart=always
RestartSec=10
Environment=OLLAMA_HOST=http://localhost:11434
Environment=OLLAMA_KEEP_ALIVE=24h

[Install]
WantedBy=default.target
```

#### 3.3 Service Management

```bash
# Install and enable
systemctl --user daemon-reload
systemctl --user enable docgen-watcher
systemctl --user start docgen-watcher

# Check status
systemctl --user status docgen-watcher

# View logs
journalctl --user -u docgen-watcher -f
```

---

### Phase 4: Ollama Configuration (Day 4)

#### 4.1 Model Setup

```bash
# Pull recommended model
ollama pull qwen3:4b

# Verify
ollama list
```

#### 4.2 Environment Tuning

```bash
# Add to ~/.bashrc or systemd environment
export OLLAMA_KEEP_ALIVE="24h"      # Keep model loaded
export OLLAMA_NUM_PARALLEL=2         # Concurrent requests
```

#### 4.3 Multiple Instances (Optional, for high throughput)

```bash
# Instance 1 (default port)
ollama serve

# Instance 2 (custom port)
OLLAMA_HOST=0.0.0.0:11435 ollama serve
```

---

### Phase 5: Testing & Validation (Day 5)

#### 5.1 Unit Tests

```python
# .docgen/tests/test_frontmatter.py
import pytest
from ..scripts.models import Frontmatter
from ..scripts.llm import generate_frontmatter

def test_frontmatter_validation():
    fm = Frontmatter(
        title="Test Document",
        tags=["test", "validation", "pytest"],
        type="note"
    )
    assert fm.title == "Test Document"
    assert len(fm.tags) == 3

@pytest.mark.asyncio
async def test_generate_frontmatter():
    content = "# Git Hooks\n\nHow to use pre-commit hooks..."
    fm = await generate_frontmatter(content)
    
    assert fm.title
    assert len(fm.tags) >= 3
    assert fm.type in ("note", "guide", "reference")
```

#### 5.2 Integration Test

```bash
# Create test file
echo "# Test Document\n\nThis is a test." > ./agents/test-doc.md

# Check if processed (watch logs)
journalctl --user -u docgen-watcher -f

# Verify frontmatter
head -20 ./agents/test-doc.md

# Cleanup
rm ./agents/test-doc.md
```

---

## File Structure After Implementation

```
.docgen/
├── README.md
├── requirements.txt          # NEW: Python dependencies
├── schema.sql
├── docs.db
├── input/                    # Existing queue directory
├── output/                   # Existing output directory
├── prompts/
│   ├── create-frontmatter.txt
│   └── ...
├── scripts/
│   ├── models.py             # NEW: Pydantic schemas
│   ├── llm.py                # NEW: Ollama client wrapper
│   ├── watcher.py            # NEW: File watcher
│   ├── workers.py            # NEW: Async worker pool
│   ├── writer.py             # NEW: Frontmatter injector
│   ├── frontmatter-daemon.py # NEW: Main entry point
│   ├── generate-frontmatter.py  # Existing
│   ├── process-queue.sh         # Existing
│   └── ...
├── templates/
│   └── frontmatter.yaml
└── tests/                    # NEW: Test suite
    ├── __init__.py
    ├── test_frontmatter.py
    └── test_watcher.py
```

---

## Task Checklist

### Phase 1: Core Infrastructure
- [ ] Create `models.py` with Pydantic schemas
- [ ] Create `llm.py` with Ollama wrapper
- [ ] Add `requirements.txt`
- [ ] Test structured output generation

### Phase 2: File Watcher
- [ ] Create `watcher.py` with debouncing
- [ ] Create `workers.py` with async pool
- [ ] Create `writer.py` for frontmatter injection
- [ ] Test file detection and processing

### Phase 3: Service
- [ ] Create `frontmatter-daemon.py` main script
- [ ] Create systemd service file
- [ ] Test service start/stop/restart
- [ ] Test graceful shutdown

### Phase 4: Ollama
- [ ] Pull `qwen3:4b` model
- [ ] Configure environment variables
- [ ] Test model performance
- [ ] (Optional) Set up multiple instances

### Phase 5: Testing
- [ ] Write unit tests
- [ ] Write integration tests
- [ ] Document usage
- [ ] Monitor for first week

---

## Success Criteria

1. ✅ New `.md` files get frontmatter within 5 seconds
2. ✅ Service runs continuously for 24+ hours without intervention
3. ✅ Generated frontmatter passes Pydantic validation 100%
4. ✅ No duplicate processing of the same file
5. ✅ Graceful handling of Ollama unavailability (retry, queue)

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Ollama crashes | systemd auto-restart, health checks |
| Model OOM | Use smaller model (qwen3:4b), memory limits |
| File permission errors | Run as user, not root |
| Infinite loops | Ignore `.docgen/` directory |
| Corrupt frontmatter | Pydantic validation, backup before write |

---

## Future Enhancements

1. **Web UI** - Dashboard showing processing status
2. **Relationship detection** - Cross-reference related documents
3. **Quality scoring** - Rate frontmatter quality
4. **Git integration** - Commit frontmatter changes automatically
5. **Multi-model routing** - Different models for different doc types
