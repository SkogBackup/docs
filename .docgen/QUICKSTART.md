# Quick Start: Batch Frontmatter Generation

Generate YAML frontmatter for all your markdown files using Ollama - perfect for running overnight!

## Three Simple Steps

### 1. Queue Up Files

```bash
# Queue all markdown files in agents/
python3 .docgen/scripts/enqueue_files.py --dir agents/

# Queue all markdown files in skogix/
python3 .docgen/scripts/enqueue_files.py --dir skogix/

# Or queue everything (excluding .git, .docgen, etc.)
python3 .docgen/scripts/enqueue_files.py --dir . --exclude .git .docgen generated node_modules
```

### 2. Check What's Queued

```bash
python3 .docgen/scripts/queue_status.py
```

### 3. Process the Queue

```bash
# Run in foreground (good for testing)
python3 .docgen/scripts/process_queue.py

# Or run overnight in background with tmux
tmux new -s frontmatter
python3 .docgen/scripts/process_queue.py
# Press Ctrl+b then d to detach
# Reattach later: tmux attach -t frontmatter
```

## Example Workflow

```bash
# Morning: Queue all files
python3 .docgen/scripts/enqueue_files.py --dir agents/
python3 .docgen/scripts/enqueue_files.py --dir skogix/

# Check queue size
python3 .docgen/scripts/queue_status.py
# Shows: "Total jobs: 47, Pending: 47"

# Evening: Start processing in tmux
tmux new -s frontmatter
python3 .docgen/scripts/process_queue.py --model llama3.2 --delay 3
# Detach with Ctrl+b d

# Next morning: Check results
tmux attach -t frontmatter
# Or check status
python3 .docgen/scripts/queue_status.py --all
# Shows: "Progress: 100.0% (47/47)"
```

## Common Options

### Different Ollama Model
```bash
python3 .docgen/scripts/process_queue.py --model mistral
```

### Process Only a Few (Testing)
```bash
python3 .docgen/scripts/process_queue.py --max-jobs 5
```

### Dry Run (No Actual Ollama Calls)
```bash
python3 .docgen/scripts/process_queue.py --dry-run
```

### Force Re-enqueue Files That Already Have Frontmatter
```bash
python3 .docgen/scripts/enqueue_files.py --dir agents/ --force
```

### Reset Stuck Jobs (if processor crashes)
```bash
python3 .docgen/scripts/queue_status.py --reset-stuck
```

## What Gets Generated

Each markdown file gets YAML frontmatter added:

```yaml
---
categories:
- agents
- claude
tags:
- agent
- profile
permalink: agents/claude/profile.md
title: Claude Profile
type: note
generated_at: 2025-12-19T03:00:00Z
---
```

Files that already have frontmatter are skipped (unless you use `--force`).

## Full Documentation

See [QUEUE_SYSTEM.md](QUEUE_SYSTEM.md) for complete documentation including:
- Priority processing
- Error handling and retries
- Monitoring progress
- Troubleshooting

## Requirements

- Python 3.6+
- Ollama installed and running (`ollama --version`)
- An Ollama model pulled (e.g., `ollama pull llama3.2`)
