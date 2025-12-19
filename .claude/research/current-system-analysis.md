# Current System Analysis: .docgen Infrastructure

## Overview

The `.docgen/` directory contains a sophisticated documentation generation pipeline with SQLite metadata tracking and LLM integration. Currently operates in batch mode with manual script execution.

## Architecture Components

### 1. Database Layer (`schema.sql`)

SQLite database with relational structure:

```sql
-- Core entities
documents (id, path, title, type, content, prompt_template, created_at, updated_at)
categories (id, name)
tags (id, name)

-- Many-to-many relationships
document_categories (document_id, category_id)
document_tags (document_id, tag_id)
```

**Key Features:**
- Automatic `updated_at` trigger on document modifications
- Indexes on `path`, `type`, and `updated_at` for efficient querying
- Supports tagging/categorization for organization

### 2. LLM Integration Methods

The system uses **three different Ollama calling methods**:

#### Method A: curl + JSON API (`generate-frontmatter.py`)
```python
result = subprocess.run(
    ["curl", "-s", "http://localhost:11434/api/generate",
     "-d", json.dumps(payload)],
    capture_output=True, text=True
)
```

#### Method B: aichat wrapper (`process-queue.sh`)
```bash
aichat --model openrouter:qwen/qwen-2.5-coder-32b-instruct --file /tmp/prompt.txt
```

#### Method C: Shell + ollama CLI (`ollama.sh` - presumed)
Direct ollama CLI invocation

### 3. Processing Patterns

#### Queue-based Processing (`process-queue.sh`)
1. Scan `.docgen/input/` for markdown files
2. Generate prompt via `make-prompt.sh`
3. Call LLM via aichat
4. Extract output between `<output>` tags
5. Inject auto-generated fields (categories, permalink, timestamp)
6. Combine frontmatter + body
7. Remove from queue

#### Direct File Processing (`generate-frontmatter.py`)
1. Accept file paths as CLI arguments
2. Read content, extract body (strip existing frontmatter)
3. Build prompt with file context
4. Call Ollama API
5. Parse response, extract frontmatter
6. Write back to file in-place

### 4. Prompt Template System

Templates stored in `.docgen/prompts/`:
- `create-frontmatter.txt` - Main frontmatter generation prompt
- `agent-profile.txt` - Agent-specific generation
- `memory-block.txt` - Memory block generation
- `notation-doc.txt` - Technical notation docs

**Template Features:**
- XML-like tags for structured input/output (`<output>`, `<task>`, `<example>`)
- Clear field guidelines (tags, title, type)
- Placeholder injection (`{path}`, `{title}`, `{timestamp}`)

### 5. Frontmatter Structure

```yaml
---
categories: [tools, path]  # Auto-generated from path
permalink: tools/path/what-we-currently-know  # Auto-generated
generated_at: 2025-12-19T00:50:00Z  # Auto-generated
tags: [git, hooks, validation]  # LLM-generated
title: Document Title  # LLM-generated
type: note  # LLM-generated (note|guide|reference)
---
```

## Identified Gaps

### 1. No Real-Time File Watching
- All processing is manual/batch
- No automatic detection of new files
- Requires explicit script invocation

### 2. No Event-Driven Pipeline
- No queue monitoring daemon
- No webhook/trigger system
- No file system event handling

### 3. Limited Error Recovery
- No retry mechanisms in current scripts
- No validation of LLM output
- No rollback on failure

### 4. No Structured Output Enforcement
- Relies on regex extraction of `<output>` tags
- No JSON schema validation
- Potential for malformed frontmatter

### 5. Mixed LLM Backend Strategy
- Uses both local ollama and remote openrouter
- No unified interface
- No model selection strategy

## Extension Opportunities

1. **File Watching Layer**: Add `watchdog` or `inotifywait` to monitor directories
2. **Event Queue**: Extend `process-queue.sh` to run continuously
3. **Structured Output**: Use Ollama's `format` parameter for JSON schema enforcement
4. **Retry Logic**: Implement exponential backoff with `tenacity`
5. **Validation**: Add Pydantic models for frontmatter structure
6. **Unified API**: Standardize on ollama Python library

## Files Summary

| File | Purpose | Status |
|------|---------|--------|
| `schema.sql` | Database schema | ✅ Complete |
| `scripts/generate-frontmatter.py` | Direct file processing | ✅ Working |
| `scripts/process-queue.sh` | Queue-based batch processing | ✅ Working |
| `scripts/add_frontmatter_tools.py` | Tool docs specific | ✅ Working |
| `scripts/add_frontmatter_journals.py` | Journal specific | ✅ Working |
| `prompts/create-frontmatter.txt` | Main prompt template | ✅ Complete |
| `templates/frontmatter.yaml` | Structure template | ✅ Complete |
