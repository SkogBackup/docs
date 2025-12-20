# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is the documentation repository for the SkogAI ecosystem. It contains:
- Agent profiles and lore (`agents/`)
- User documentation and notation systems (`skogix/`)
- Automated frontmatter generation system (`.docgen/`)

## Directory Structure

```
docs/
├── agents/               # Agent profiles, memory blocks, and journals
├── skogix/              # User docs, notation system, definitions  
├── tools/               # External tool documentation
├── governance/          # Library sessions and project phases
└── .docgen/             # Python automation system for documentation
    ├── scripts/         # Core Python modules
    ├── prompts/         # LLM prompt templates
    └── docs.db          # SQLite metadata database
```

## Automated Documentation System

The `.docgen/` system is **production-ready** with modern Python architecture:

### Core Components (✅ Complete)
- **LLM Integration**: Uses Python `ollama` library with structured output (Pydantic schemas)
- **Async Workers**: Concurrent processing with retry logic and exponential backoff
- **File Watching**: Real-time markdown file detection with debouncing
- **Queue System**: Priority-based batch processing with status tracking
- **Error Handling**: Custom exceptions (`LLMError`, `ModelNotFoundError`, `ConnectionError`)

### Quick Commands
```bash
# Real-time daemon (watches for new/modified .md files)
uv run python .docgen/scripts/frontmatter_daemon.py

# Batch processing
uv run python .docgen/scripts/enqueue_files.py --dir agents/
uv run python .docgen/scripts/process_queue.py

# Generate specific documents
uv run python .docgen/scripts/generate_docs.py --model qwen3:8b
```

## SkogAI Notation

The repository documents a formal notation system used throughout SkogAI:
- `@` = intent/action (void, side-effect)
- `$` = reference (null pointer)  
- `_` = existence
- `=` = being
- `|` = choice
- `[]` = similarity
- `{}` = difference
- `.` = belonging
- `:` = continuation
- `->` = directional intent

**Core equation**: `@ + ? = $` (intent + bridge = reality)

## Development Guidelines

See `AGENTS.md` for complete coding standards including:
- Python naming conventions (snake_case/PascalCase)
- Type hints and async patterns
- Import organization and error handling
- Testing with pytest and uv dependency management

## System Status

**Ollama Integration**: ✅ **Production Ready**
- Modern async Python implementation with structured output
- Retry logic and error recovery
- File watching daemon operational
- Queue-based batch processing functional

**Ready for**: New feature development, content creation, or system expansion
