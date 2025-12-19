# SkogAI Documentation Generator

A workflow for regenerating documentation using local Ollama models.

## Overview

This system:
1. Stores doc metadata (path, tags, categories) in SQLite
2. Uses prompt templates to guide Ollama
3. Generates markdown with frontmatter
4. Outputs to organized folders with timestamps

## Quick Start

### Batch Processing (Recommended - NEW!)

Process all markdown files with frontmatter generation queue:

```bash
# 1. Queue files for processing
python3 .docgen/scripts/enqueue_files.py --dir agents/
python3 .docgen/scripts/enqueue_files.py --dir skogix/

# 2. Check queue status
python3 .docgen/scripts/queue_status.py

# 3. Process queue (run overnight!)
python3 .docgen/scripts/process_queue.py
```

See [QUICKSTART.md](QUICKSTART.md) or [QUEUE_SYSTEM.md](QUEUE_SYSTEM.md) for full details.

### Database-Driven Generation

Generate documents from stored metadata:

```bash
# Initialize database with schema
python3 .docgen/scripts/init_db.py --sample-data

# Generate all documents
python3 .docgen/scripts/generate_docs.py

# Generate specific document by ID
python3 .docgen/scripts/generate_docs.py --doc-id 1

# Use different Ollama model
python3 .docgen/scripts/generate_docs.py --model llama3.2

# Custom output directory
python3 .docgen/scripts/generate_docs.py --output ./regenerated
```

### 3. Add Your Own Documents

```python
import sqlite3

conn = sqlite3.connect('.docgen/docs.db')
cursor = conn.cursor()

# Add document
cursor.execute("""
    INSERT INTO documents (path, title, type, content, prompt_template)
    VALUES (?, ?, ?, ?, ?)
""", (
    "agents/new-agent/profile.md",
    "New Agent",
    "note",
    "Context about the new agent...",
    "agent-profile"  # Which prompt template to use
))
doc_id = cursor.lastrowid

# Add tags
for tag in ["agent", "new"]:
    cursor.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (tag,))
    cursor.execute("SELECT id FROM tags WHERE name = ?", (tag,))
    tag_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO document_tags VALUES (?, ?)", (doc_id, tag_id))

conn.commit()
conn.close()
```

## Directory Structure

```
.docgen/
├── README.md              # This file
├── schema.sql             # Database schema
├── docs.db               # SQLite database (generated)
├── prompts/              # Ollama prompt templates
│   ├── agent-profile.txt
│   ├── memory-block.txt
│   └── notation-doc.txt
├── scripts/              # Python scripts
│   ├── init_db.py        # Initialize database
│   └── generate_docs.py  # Main generator
└── templates/            # Templates
    └── frontmatter.yaml  # Frontmatter structure
```

## Prompt Templates

Templates are in `.docgen/prompts/`:
- `agent-profile.txt` - Generate agent profiles
- `memory-block.txt` - Generate memory blocks
- `notation-doc.txt` - Generate technical docs

To add a new template:
1. Create `.docgen/prompts/your-template.txt`
2. Use placeholders like `{input_context}`, `{title}`, `{agent_name}`
3. Reference it in database: `prompt_template='your-template'`

## Frontmatter

Generated documents include YAML frontmatter:

```yaml
---
categories:
- agents
- claude
tags:
- agent
- profile
permalink: agents/claude/profile
title: Claude Profile
type: note
generated_at: 2025-12-17T12:00:00
---
```

## Requirements

- Python 3.6+
- Ollama installed and running
- Ollama model pulled (e.g., `ollama pull llama3.2`)

## Workflow

1. **Store metadata in database** - What docs exist, their paths, tags
2. **Read from database** - Query which docs to generate
3. **Load prompt template** - Get the right prompt for doc type
4. **Call Ollama** - Generate content using template + context
5. **Add frontmatter** - Inject YAML with tags, path, timestamp
6. **Write to folder** - Save to organized directory structure

## Example Usage

```bash
# One-time setup
python3 .docgen/scripts/init_db.py --sample-data

# Generate all docs
python3 .docgen/scripts/generate_docs.py

# Output appears in ./generated/
```

## Customization

- **Different models**: Use `--model` flag
- **Custom prompts**: Edit files in `.docgen/prompts/`
- **Schema changes**: Modify `.docgen/schema.sql` and reinitialize
- **Output format**: Edit `generate_frontmatter()` in `generate_docs.py`
