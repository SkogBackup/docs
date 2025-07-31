---
title: SkogAI Tools and Extensions
type: note
permalink: system/skog-ai-tools-and-extensions
---

# SkogAI Tools and Extensions

## Summary

This document tracks the evolution of tools and extensions in the SkogAI ecosystem, particularly focusing on the transition from the MCP-based tooling to the current extension model. It provides clarity on naming conventions, functional replacements, and system architecture.

## Historical Evolution

### MCP Tool Era (Pre-June 2025)

The original tooling used an "MCP" (Multimodal Capability Provider) naming convention:

- **mcp-goose-developer-tools**: Provided shell access and file editing capabilities
- **mcp-goose-computer-controller**: Handled web search, system control, and file processing
- **mcp-goose-memory**: Managed file-based memory system with numbered files (00-series)
- **mcp-todo**: Provided task tracking and management across sessions

### Extension Model (Current)

The current system uses a cleaner extension-based model:

- **developer**: Provides shell command execution and file editing (replaces mcp-goose-developer-tools)
- **computercontroller**: Provides web scraping, automation, and file processing (replaces mcp-goose-computer-controller)
- **skogai-memory**: Structured knowledge management using semantic graph (evolved from mcp-goose-memory)

### Integration Layer

Additional components mentioned include:

- **skogmcp**: Integration layer for MCP compatibility
- **skoghub**: Hub for connecting various extensions and tools

## Functional Mapping

| Functionality | Previous Tool | Current Implementation | Status |
|---------------|--------------|------------------------|--------|
| Shell Access | mcp-goose-developer-tools | developer extension | ✅ Active |
| File Editing | mcp-goose-developer-tools | developer extension | ✅ Active |
| Web/System Control | mcp-goose-computer-controller | computercontroller extension | ✅ Active |
| Memory System | mcp-goose-memory | skogai-memory extension | ✅ Active |
| Task Management | mcp-todo | File-based with symlinks | ✅ Active |
| Integration Layer | Unknown | skogmcp/skoghub | ✅ Active |

## Memory System Evolution

The most significant evolution occurred in the memory management system:

### File-Based Memory (Original)
- Hierarchical numbered files (00-series for core, 100+ for standards, etc.)
- Plain text format with simple cross-references
- Manual organization and retrieval

### Semantic Knowledge Graph (Current)
- Structured markdown files with metadata
- Bidirectional linking between concepts
- Automated relationship tracking
- Tag-based organization
- Search and retrieval capabilities

## Current Extension Capabilities

### developer
- Shell command execution
- File creation, reading, and modification
- System interaction and automation

### computercontroller
- Web scraping and search
- Screen capture and image processing
- File conversion and processing

### skogai-memory
- Note creation and management
- Semantic search and relationship mapping
- Knowledge graph visualization
- Context building for conversations

## Best Practices

1. Use the current extension names in documentation and references
2. Maintain awareness of historical naming for context when reading older documents
3. Leverage the expanded capabilities of the skogai-memory system for knowledge management
4. Document tool usage patterns for consistency across the system

## Future Directions

The evolution from MCP-based tools to the current extension model suggests a trend toward:

1. More integrated tooling with cleaner interfaces
2. Enhanced semantic capabilities in knowledge management
3. Better organization and discoverability of functionality
4. More consistency in naming and interface design

Monitoring the continued development of skoghub and related integration tools will be important for understanding future system evolution.