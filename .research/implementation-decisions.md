# Implementation Decisions & Rationale

## Overview

This document captures the key technical decisions made during the frontmatter automation system design, with rationale and alternatives considered.

---

## Decision 1: Python watchdog over inotify-tools

### Chosen: Python `watchdog` library
### Alternative: Linux `inotifywait` (inotify-tools)

### Rationale

| Factor | watchdog | inotify-tools |
|--------|----------|---------------|
| **Cross-platform** | ✅ Linux/macOS/Windows | ❌ Linux only |
| **Pattern matching** | ✅ Built-in glob patterns | ❌ Manual filtering |
| **Debouncing** | ✅ Easy with Python | ⚠️ Requires shell scripting |
| **Async integration** | ✅ Easy with asyncio | ❌ Subprocess only |
| **Error handling** | ✅ Python exceptions | ⚠️ Exit codes |
| **Resource usage** | ⚠️ Slightly higher | ✅ Kernel-level, minimal |

### Key Code Pattern

```python
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

class MarkdownHandler(PatternMatchingEventHandler):
    def __init__(self):
        super().__init__(
            patterns=["**/*.md"],
            ignore_patterns=["**/.git/**", "**/node_modules/**"],
            ignore_directories=True
        )
```

### Alternative Implementation (inotify)

```bash
inotifywait -m -r -e create,modify --format '%w%f' ./docs \
  | while read file; do
      if [[ "$file" == *.md ]]; then
        process_file "$file"
      fi
    done
```

### Verdict

watchdog wins for:
1. Easier integration with existing Python scripts in `.docgen/`
2. Built-in pattern matching reduces boilerplate
3. Future-proofing for potential macOS users

---

## Decision 2: Pydantic Structured Output over Regex Parsing

### Chosen: Pydantic models with Ollama `format` parameter
### Alternative: Regex extraction of `<output>` tags (existing approach)

### Rationale

| Factor | Pydantic + format | Regex extraction |
|--------|-------------------|------------------|
| **Reliability** | ✅ 100% valid JSON | ⚠️ Can fail on malformed output |
| **Type safety** | ✅ Validated at parse time | ❌ String manipulation |
| **Error messages** | ✅ Clear validation errors | ❌ Generic parse failures |
| **Flexibility** | ✅ Easy schema changes | ⚠️ Regex updates needed |
| **Model compatibility** | ⚠️ Requires Ollama 0.4+ | ✅ Works with any output |

### Key Code Pattern

```python
from pydantic import BaseModel, Field
from typing import List, Literal
import ollama

class Frontmatter(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    tags: List[str] = Field(..., min_length=3, max_length=7)
    type: Literal["note", "guide", "reference"] = "note"

# Ollama with structured output
response = await client.chat(
    model='qwen3:4b',
    messages=[...],
    format=Frontmatter.model_json_schema(),  # Enforces structure
    options={'temperature': 0}
)

# Guaranteed valid
frontmatter = Frontmatter.model_validate_json(response.message.content)
```

### Existing Pattern (to replace)

```python
def extract_output_tags(text):
    """Extract content between <output> tags"""
    match = re.search(r'<output>(.*?)</output>', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()  # Fallback - often malformed
```

### Verdict

Pydantic wins for:
1. **Guaranteed structure** - LLM uses constrained decoding
2. **Better debugging** - Validation errors show exactly what's wrong
3. **Type hints** - IDE support and documentation

---

## Decision 3: qwen3:4b as Default Model

### Chosen: `qwen3:4b`
### Alternatives: `llama3.1:8b`, `tinyllama:1.1b`, `gemma3:9b`

### Benchmark (from librarian research)

| Model | Params | Speed (tok/s) | Memory | Quality | Best For |
|-------|--------|---------------|--------|---------|----------|
| tinyllama:1.1b | 1.1B | ~50 | ~2GB | Basic | Speed priority |
| **qwen3:4b** | 4B | ~30 | ~4GB | Excellent | **General use** |
| llama3.1:8b | 8B | ~20 | ~8GB | Superior | Complex docs |
| gemma3:9b | 9B | ~15 | ~10GB | Superior | Analysis |

### Rationale

For frontmatter generation (short, structured output):
1. **Speed matters more than depth** - 4B is fast enough
2. **Qwen excels at structured output** - Better JSON/YAML than Llama
3. **Memory footprint** - 4GB allows running 24/7 on modest hardware
4. **Quality is sufficient** - Frontmatter is metadata, not prose

### Configuration

```bash
# Pull the model
ollama pull qwen3:4b

# Keep loaded for instant response
export OLLAMA_KEEP_ALIVE="24h"
```

---

## Decision 4: Async Worker Pool over Sequential Processing

### Chosen: `asyncio.Queue` with 2-4 workers
### Alternative: Sequential file processing

### Rationale

| Factor | Async Pool | Sequential |
|--------|------------|------------|
| **Throughput** | ✅ 2-4x faster | ❌ One at a time |
| **Latency** | ✅ Queue absorbs bursts | ⚠️ Backlog builds up |
| **Complexity** | ⚠️ More code | ✅ Simple loop |
| **Resource usage** | ⚠️ Multiple concurrent LLM calls | ✅ One at a time |

### Key Code Pattern

```python
class WorkerPool:
    def __init__(self, num_workers: int = 2):
        self.queue = asyncio.PriorityQueue()
        self.num_workers = num_workers
    
    async def worker(self, worker_id: int):
        while True:
            priority, file_path = await self.queue.get()
            await self._process_file(file_path)
            self.queue.task_done()
    
    async def start(self):
        self._workers = [
            asyncio.create_task(self.worker(i))
            for i in range(self.num_workers)
        ]
```

### Why 2 Workers Default

- **Ollama's default**: `OLLAMA_NUM_PARALLEL=1`
- **Safe default**: 2 workers with sequential model access
- **Configurable**: `--workers 4` for multi-GPU setups

---

## Decision 5: Debouncing with 500ms Delay

### Chosen: 0.5 second debounce
### Alternatives: No debounce, 2s debounce

### The Problem

Editors often trigger multiple events per save:
1. `modified` - Content written
2. `modified` - File attributes updated
3. `modified` - Sync completed

Without debouncing, one "save" triggers 3 LLM calls.

### Solution

```python
def _schedule_processing(self, file_path: str, priority: int):
    # Cancel existing timer for this file
    if file_path in self._pending:
        self._pending[file_path].cancel()
    
    # Schedule new timer
    handle = self.loop.call_later(
        0.5,  # 500ms debounce
        lambda: self.queue.put_nowait((priority, file_path))
    )
    self._pending[file_path] = handle
```

### Why 500ms

| Delay | Behavior |
|-------|----------|
| 0ms (none) | Multiple duplicate LLM calls |
| 100ms | May catch editor mid-write |
| **500ms** | Covers most save sequences |
| 2000ms | Feels sluggish |

### Verdict

500ms balances responsiveness with deduplication.

---

## Decision 6: systemd User Service over Root Service

### Chosen: `~/.config/systemd/user/docgen-watcher.service`
### Alternative: `/etc/systemd/system/docgen-watcher.service`

### Rationale

| Factor | User Service | System Service |
|--------|--------------|----------------|
| **Permissions** | ✅ Runs as user | ⚠️ Needs file access setup |
| **Installation** | ✅ No sudo required | ❌ Requires root |
| **Startup** | ✅ On user login | ⚠️ On boot (may precede Ollama) |
| **Logs** | ✅ User's journal | ⚠️ System journal |

### Key Configuration

```ini
[Unit]
Description=SkogAI Documentation Frontmatter Generator
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/skogix/docs
ExecStart=/home/skogix/docs/.venv/bin/python -m .docgen.scripts.frontmatter-daemon
Restart=always
RestartSec=10

[Install]
WantedBy=default.target
```

### Usage

```bash
# Enable and start
systemctl --user enable docgen-watcher
systemctl --user start docgen-watcher

# View logs
journalctl --user -u docgen-watcher -f
```

---

## Decision 7: Backup Before Write

### Chosen: Create `.bak` file before modifying
### Alternative: No backup / Git-only backup

### Rationale

```python
async def inject_frontmatter(file_path, doc_meta, backup=True):
    if backup:
        backup_path = path.with_suffix(path.suffix + '.bak')
        shutil.copy2(path, backup_path)
    
    # Now safe to modify
    async with aiofiles.open(path, 'w') as f:
        await f.write(new_content)
```

### Why

1. **LLM can fail** - Malformed output shouldn't corrupt files
2. **Git may not be available** - Backup is immediate
3. **Easy recovery** - Just rename `.md.bak` → `.md`
4. **Negligible cost** - One extra file copy

---

## Decision 8: Skip Files with Existing Frontmatter

### Chosen: Skip files starting with `---`
### Alternative: Regenerate all frontmatter

### Rationale

```python
def has_frontmatter(content: str) -> bool:
    return content.strip().startswith('---')
```

| Approach | Behavior |
|----------|----------|
| **Skip existing** | Respects manual edits, faster |
| Regenerate | Always fresh, loses custom edits |

### Override

```bash
# Force regeneration
python -m .docgen.scripts.frontmatter-daemon --force-regenerate
```

---

## Summary of Key Decisions

| Decision | Choice | Key Reason |
|----------|--------|------------|
| File watcher | watchdog | Cross-platform, pattern matching |
| Output parsing | Pydantic schemas | Guaranteed valid structure |
| Default model | qwen3:4b | Speed/quality balance |
| Processing | Async pool (2 workers) | Throughput without overload |
| Debounce | 500ms | Covers editor save sequences |
| Service | systemd user | No root required |
| Safety | Backup before write | Protects against LLM failures |
| Idempotency | Skip existing frontmatter | Respects manual edits |

---

**Document created**: 2025-12-19
**Purpose**: Capture technical decisions for future reference and onboarding
