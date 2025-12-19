# Queue-Based Frontmatter Generation System

A batch processing system for generating YAML frontmatter on markdown files using local Ollama models.

## Overview

This system allows you to:
1. **Queue up** files that need frontmatter
2. **Run overnight** to let Ollama process them one by one
3. **Resume** automatically if interrupted
4. **Monitor** progress and handle failures

## Quick Start

### 1. Enqueue Files

Add files to the processing queue:

```bash
# Enqueue a single file
python3 .docgen/scripts/enqueue_files.py --file agents/claude/profile.md

# Enqueue an entire directory
python3 .docgen/scripts/enqueue_files.py --dir agents/

# Enqueue with high priority (process first)
python3 .docgen/scripts/enqueue_files.py --dir skogix/ --priority 10

# Force re-enqueue files that already have frontmatter
python3 .docgen/scripts/enqueue_files.py --dir agents/ --force
```

### 2. Check Queue Status

See what's in the queue:

```bash
# Quick summary
python3 .docgen/scripts/queue_status.py

# Detailed view of all jobs
python3 .docgen/scripts/queue_status.py --all

# See only pending jobs
python3 .docgen/scripts/queue_status.py --pending

# See failed jobs
python3 .docgen/scripts/queue_status.py --failed
```

### 3. Process the Queue

Run the worker to process all jobs:

```bash
# Process entire queue
python3 .docgen/scripts/process_queue.py

# Use a different Ollama model
python3 .docgen/scripts/process_queue.py --model mistral

# Process only 5 jobs (for testing)
python3 .docgen/scripts/process_queue.py --max-jobs 5

# Dry run (simulate without calling Ollama)
python3 .docgen/scripts/process_queue.py --dry-run

# Adjust delay between jobs (default 2 seconds)
python3 .docgen/scripts/process_queue.py --delay 5
```

## Complete Workflow Example

```bash
# Step 1: Enqueue all markdown files in docs
python3 .docgen/scripts/enqueue_files.py --dir agents/
python3 .docgen/scripts/enqueue_files.py --dir skogix/

# Step 2: Check what was queued
python3 .docgen/scripts/queue_status.py

# Step 3: Run overnight (or in tmux/screen session)
python3 .docgen/scripts/process_queue.py --model llama3.2 --delay 3

# Step 4: Check results in the morning
python3 .docgen/scripts/queue_status.py --all
```

## Run Overnight in Background

### Using tmux (recommended)

```bash
# Start a tmux session
tmux new -s frontmatter

# Inside tmux, run the processor
python3 .docgen/scripts/process_queue.py

# Detach from tmux: Ctrl+b then d
# Reattach later: tmux attach -t frontmatter
```

### Using nohup

```bash
# Run in background with output log
nohup python3 .docgen/scripts/process_queue.py > queue_process.log 2>&1 &

# Check progress
tail -f queue_process.log

# Check if still running
ps aux | grep process_queue
```

## Queue Management

### Reset Stuck Jobs

If the processor crashes, jobs may be stuck in "processing" status:

```bash
python3 .docgen/scripts/queue_status.py --reset-stuck
```

### Clear Completed Jobs

Clean up the queue after successful processing:

```bash
python3 .docgen/scripts/queue_status.py --clear-completed
```

### Check Failed Jobs

See what failed and why:

```bash
python3 .docgen/scripts/queue_status.py --failed
```

## How It Works

### 1. Enqueue Phase

- Scans directories for `.md` files
- Checks if file already has frontmatter (skips unless `--force`)
- Generates an Ollama prompt for each file
- Stores in SQLite queue with status='pending'

### 2. Processing Phase

- Pulls next job from queue (ordered by priority, then time)
- Marks job as 'processing'
- Calls Ollama with the prompt
- Parses YAML frontmatter from response
- Updates the markdown file with new frontmatter
- Marks job as 'completed'

### 3. Error Handling

- If Ollama fails, job is retried (default: 3 times)
- After max retries, job is marked as 'failed'
- Failed jobs can be manually reset to retry

## Database Schema

Queue table structure:

```sql
processing_queue (
    id              INTEGER PRIMARY KEY,
    file_path       TEXT NOT NULL,
    prompt          TEXT NOT NULL,
    status          TEXT (pending|processing|completed|failed),
    priority        INTEGER (higher = processed first),
    retries         INTEGER (current retry count),
    max_retries     INTEGER (default: 3),
    error_message   TEXT,
    created_at      TIMESTAMP,
    started_at      TIMESTAMP,
    completed_at    TIMESTAMP
)
```

## Customization

### Change Ollama Model

```bash
# Use a different model
python3 .docgen/scripts/process_queue.py --model llama3.2:latest
python3 .docgen/scripts/process_queue.py --model mistral
```

### Adjust Processing Delay

```bash
# Faster (1 second between jobs)
python3 .docgen/scripts/process_queue.py --delay 1

# Slower (10 seconds between jobs)
python3 .docgen/scripts/process_queue.py --delay 10
```

### Custom Prompt Template

Edit `.docgen/prompts/create-frontmatter.txt` to change how Ollama is prompted.

### Exclude Directories

```bash
# Exclude specific directories when enqueueing
python3 .docgen/scripts/enqueue_files.py --dir . --exclude node_modules .git build dist
```

## Monitoring Progress

Real-time progress check:

```bash
# In one terminal, run the processor
python3 .docgen/scripts/process_queue.py

# In another terminal, watch progress
watch -n 5 'python3 .docgen/scripts/queue_status.py'
```

## Troubleshooting

### "Ollama not found"
- Make sure Ollama is installed: `ollama --version`
- Check it's in your PATH

### Jobs stuck in "processing"
- Use `--reset-stuck` to reset them:
  ```bash
  python3 .docgen/scripts/queue_status.py --reset-stuck
  ```

### All jobs failing
- Check a failed job's error message:
  ```bash
  python3 .docgen/scripts/queue_status.py --failed
  ```
- Try a dry run first:
  ```bash
  python3 .docgen/scripts/process_queue.py --dry-run --max-jobs 1
  ```

### Need to stop processing
- Use Ctrl+C to gracefully stop
- Current job will be marked as failed and can be retried
- Remaining jobs stay in queue

## Examples

### Process high-priority agent docs first, then everything else

```bash
# Queue agents with high priority
python3 .docgen/scripts/enqueue_files.py --dir agents/ --priority 10

# Queue other docs with normal priority
python3 .docgen/scripts/enqueue_files.py --dir skogix/ --priority 0

# Process (agents will go first)
python3 .docgen/scripts/process_queue.py
```

### Re-generate frontmatter for all files

```bash
# Force re-enqueue everything
python3 .docgen/scripts/enqueue_files.py --dir . --force --exclude .git .docgen generated

# Process
python3 .docgen/scripts/process_queue.py
```

### Test on a few files first

```bash
# Enqueue
python3 .docgen/scripts/enqueue_files.py --dir agents/claude/

# Test with max 3 jobs
python3 .docgen/scripts/process_queue.py --max-jobs 3

# Check results
python3 .docgen/scripts/queue_status.py --all
```

## File Locations

```
.docgen/
├── scripts/
│   ├── enqueue_files.py     # Add files to queue
│   ├── process_queue.py     # Process queue (worker)
│   └── queue_status.py      # Check queue status
├── prompts/
│   └── create-frontmatter.txt  # Ollama prompt template
├── docs.db                  # SQLite database (includes queue)
└── QUEUE_SYSTEM.md          # This file
```

## Next Steps

After frontmatter is generated, you may want to:
- Commit the changes: `git add -A && git commit -m "Add frontmatter"`
- Review failed jobs and fix manually
- Adjust prompt template for better results
- Clear completed jobs from queue
