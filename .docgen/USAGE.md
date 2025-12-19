# Usage Guide: SkogAI Documentation Generator

## Overview

This system provides **automatic frontmatter generation** for markdown documentation files using local LLM via Ollama. It supports both:

1. **Real-time automation** - Watch directories for new/modified files and generate frontmatter automatically
2. **Batch processing** - Process existing files manually

## Quick Start (Real-Time Mode)

```bash
# 1. Install dependencies
cd /home/skogix/docs
python3 -m venv .venv
source .venv/bin/activate
pip install -r .docgen/requirements.txt

# 2. Pull the recommended model
ollama pull qwen3:4b

# 3. Start the daemon
python -m .docgen.scripts.frontmatter-daemon

# Files added to ./agents, ./skogix, or ./tools will get frontmatter automatically!
```

---

## Method 1: Real-Time Automation (Recommended)

### How It Works

```
┌──────────────────────────────────────────────────────────────────┐
│                    docs/ repository                              │
│    agents/ │ skogix/ │ tools/                                   │
└──────────────────────────────────────────────────────────────────┘
                           │
                           │ File events (create/modify)
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                   File Watcher (watchdog)                        │
│    - Monitors for *.md files                                     │
│    - Debounces rapid saves (500ms)                              │
│    - Ignores .git, .docgen/input, node_modules                  │
└──────────────────────────────────────────────────────────────────┘
                           │
                           │ Queued file paths
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                   LLM Worker Pool (2-4 workers)                  │
│    - Async processing                                            │
│    - Retry with exponential backoff                             │
│    - Structured output via Pydantic                             │
└──────────────────────────────────────────────────────────────────┘
                           │
                           │ Generated frontmatter
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                   File Writer                                    │
│    - Injects frontmatter                                         │
│    - Preserves content                                          │
│    - Creates .bak backup                                        │
└──────────────────────────────────────────────────────────────────┘
```

### Setup

```bash
# Run the automated setup script
.docgen/scripts/setup.sh

# Or manually:
python3 -m venv .venv
source .venv/bin/activate
pip install -r .docgen/requirements.txt
ollama pull qwen3:4b
```

### Running the Daemon

**Manual run:**
```bash
source .venv/bin/activate
python -m .docgen.scripts.frontmatter-daemon

# With options:
python -m .docgen.scripts.frontmatter-daemon \
  --dirs "./agents,./skogix,./tools" \
  --model qwen3:4b \
  --workers 2 \
  --scan-existing
```

**As a systemd service (24/7 operation):**
```bash
# Enable and start
systemctl --user enable docgen-watcher
systemctl --user start docgen-watcher

# Check status
systemctl --user status docgen-watcher

# View logs
journalctl --user -u docgen-watcher -f

# Stop
systemctl --user stop docgen-watcher
```

### Daemon Options

| Option | Description | Default |
|--------|-------------|---------|
| `--dirs`, `-d` | Comma-separated directories to watch | `./agents,./skogix,./tools` |
| `--model`, `-m` | Ollama model to use | `qwen3:4b` |
| `--workers`, `-w` | Number of concurrent workers | `2` |
| `--debounce` | Debounce delay in seconds | `0.5` |
| `--scan-existing` | Process existing files on startup | `false` |
| `--debug` | Enable debug logging | `false` |

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DOCGEN_MODEL` | Ollama model | `qwen3:4b` |
| `DOCGEN_WORKERS` | Worker count | `2` |
| `DOCGEN_DEBOUNCE` | Debounce delay | `0.5` |
| `DOCGEN_DIRS` | Directories to watch | `./agents,./skogix,./tools` |
| `OLLAMA_HOST` | Ollama API endpoint | `http://localhost:11434` |

---

## Method 2: Manual/Batch Processing

For processing files on-demand rather than real-time.

### Single File Processing

```bash
python3 .docgen/scripts/generate-frontmatter.py agents/claude/profile.md
```

### Queue-Based Processing

```bash
# Add files to queue
cp new-doc.md .docgen/input/

# Process queue
.docgen/scripts/process-queue.sh
```

### Database-Driven Generation

```bash
# Import markdown to database
python3 .docgen/scripts/import_markdown.py \
  --file input/my-doc.md \
  --output agents/my-agent/profile.md \
  --template agent-profile

# Generate from database
python3 .docgen/scripts/generate_docs.py --model llama3.2
```

---

## Frontmatter Structure

Generated frontmatter includes:

```yaml
---
categories: [agents, claude]      # Auto-generated from path
permalink: agents/claude/profile  # Auto-generated from path
generated_at: 2025-12-19T12:00:00Z # Auto-generated timestamp
title: Claude Agent Profile       # LLM-generated
tags: [agent, profile, skogai]    # LLM-generated (3-7)
type: note                        # LLM-generated (note|guide|reference)
---
```

### Field Types

| Field | Source | Description |
|-------|--------|-------------|
| `categories` | Auto | Derived from file path directories |
| `permalink` | Auto | File path without extension |
| `generated_at` | Auto | UTC timestamp of generation |
| `title` | LLM | Concise document title (3-8 words) |
| `tags` | LLM | Content keywords (3-7, kebab-case) |
| `type` | LLM | Classification: note, guide, or reference |

---

## Model Selection

### Recommended Models

| Model | Size | Speed | Use Case |
|-------|------|-------|----------|
| `qwen3:4b` | 4B | Fast | **Recommended** - Best balance |
| `llama3.1:8b` | 8B | Medium | Higher quality for complex docs |
| `tinyllama:1.1b` | 1.1B | Very Fast | Minimal resources |

### Changing Models

```bash
# Pull new model
ollama pull llama3.1:8b

# Use in daemon
python -m .docgen.scripts.frontmatter-daemon --model llama3.1:8b

# Or set environment variable
export DOCGEN_MODEL=llama3.1:8b
```

---

## Troubleshooting

### Ollama Connection Issues

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Start Ollama if needed
ollama serve

# Check model availability
ollama list
```

### Service Not Starting

```bash
# Check logs
journalctl --user -u docgen-watcher -n 50

# Verify paths in service file
cat ~/.config/systemd/user/docgen-watcher.service

# Reload after changes
systemctl --user daemon-reload
systemctl --user restart docgen-watcher
```

### Files Not Being Processed

1. Check if file is in a watched directory (`agents/`, `skogix/`, `tools/`)
2. Ensure file has `.md` extension
3. Check if file already has frontmatter (skipped by default)
4. Look for errors in daemon output

### Performance Tuning

```bash
# More workers for faster processing
--workers 4

# Shorter debounce for quicker response
--debounce 0.2

# Keep model loaded (in systemd service)
Environment=OLLAMA_KEEP_ALIVE=24h
```

---

## Directory Structure

```
.docgen/
├── docs.db               # SQLite metadata database
├── requirements.txt      # Python dependencies
├── schema.sql           # Database schema
├── README.md            # System overview
├── USAGE.md             # This file
├── input/               # Queue for manual processing
├── output/              # Generated output
├── prompts/             # LLM prompt templates
│   ├── create-frontmatter.txt
│   ├── agent-profile.txt
│   └── memory-block.txt
├── scripts/
│   ├── __init__.py      # Package init
│   ├── models.py        # Pydantic schemas
│   ├── llm.py           # Ollama client
│   ├── watcher.py       # File watcher
│   ├── workers.py       # Async workers
│   ├── writer.py        # Frontmatter injector
│   ├── frontmatter-daemon.py  # Main daemon
│   ├── setup.sh         # Setup script
│   ├── generate-frontmatter.py  # Manual processing
│   └── process-queue.sh  # Queue processor
└── templates/
    └── frontmatter.yaml  # Structure template
```

---

## Examples

### Example 1: Process existing documentation

```bash
# Start daemon with scan-existing flag
python -m .docgen.scripts.frontmatter-daemon --scan-existing

# This will:
# 1. Start watching directories
# 2. Queue all existing .md files without frontmatter
# 3. Process them through the LLM
```

### Example 2: Watch only specific directory

```bash
python -m .docgen.scripts.frontmatter-daemon --dirs "./agents/claude"
```

### Example 3: High-throughput processing

```bash
# Use more workers and faster model
python -m .docgen.scripts.frontmatter-daemon \
  --model qwen3:4b \
  --workers 4 \
  --debounce 0.2 \
  --scan-existing
```

---

## Integration with Other Tools

### Git Pre-commit Hook

```bash
# .git/hooks/pre-commit
#!/bin/bash
# Ensure frontmatter exists on committed markdown files
for file in $(git diff --cached --name-only | grep '\.md$'); do
    if ! head -1 "$file" | grep -q "^---$"; then
        echo "Warning: $file has no frontmatter"
    fi
done
```

### CI/CD Integration

```yaml
# .github/workflows/docs.yml
- name: Generate Frontmatter
  run: |
    pip install -r .docgen/requirements.txt
    python -m .docgen.scripts.frontmatter-daemon --scan-existing --no-watch
```
