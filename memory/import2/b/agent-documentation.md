# SkogAI Agent Guide

## Summary
This guide helps AI assistants effectively use the SkogAI-Memory system to build and navigate a semantic knowledge graph through natural conversations with users. It outlines core functionality, best practices, and integration patterns that maximize the knowledge graph's value through consistent formats and rich interconnections.

## Details

### Core Concepts

#### Purpose of This Guide

This document provides AI assistants with comprehensive guidance on using SkogAI-Memory effectively when working with users. It covers reading, writing, and navigating knowledge through the Model Context Protocol (MCP), focusing on building a valuable interconnected knowledge graph that persists across conversations.

#### SkogAI-Memory Overview

SkogAI-Memory allows both AI assistants and users to record context in local Markdown files, building a knowledge base through natural conversations. The system's core attributes are:

- **Local-First**: All data stored in plain text files on the user's computer
- **Real-Time**: Content updates visible immediately to users
- **Bi-Directional**: Both AI assistants and users can read and edit notes
- **Semantic**: Simple patterns create a structured knowledge graph
- **Persistent**: Knowledge persists across sessions and conversations

#### The Knowledge Graph Paradigm

The system's value comes primarily from connections between notes, not just the notes themselves. When writing notes, the assistant's primary goal should be creating a rich, interconnected knowledge graph by:

1. **Increasing Semantic Density**: Adding multiple observations and relations to each note
2. **Using Accurate References**: Referencing existing entities by their exact titles
3. **Creating Forward References**: Creating links to entities that don't exist yet
4. **Building Bidirectional Links**: Connecting entities from both directions
5. **Using Meaningful Categories**: Adding semantic context with appropriate observation categories
6. **Choosing Precise Relations**: Using specific relation types that convey meaning

A knowledge graph with 10 heavily connected notes provides more value than 20 isolated notes.

### Core Tools and Functions

#### Writing Knowledge

```python
response = await write_note(
    title="Search Design",              # Required: Note title
    content="# Search Design\n...",     # Required: Note content
    folder="specs",                     # Optional: Folder to save in
    tags=["search", "design"],          # Optional: Tags for categorization
    verbose=True                        # Optional: Get parsing details
)
```

#### Reading Knowledge

```python
# Multiple ways to access the same content
content = await read_note("Search Design")             # By title
content = await read_note("specs/search-design")       # By path 
content = await read_note("memory://specs/search")     # By memory URL
```

#### Searching for Knowledge

```python
results = await search_notes(
    query="authentication system",      # Text to search for
    page=1,                             # Optional: Pagination
    page_size=10                        # Optional: Results per page
)
```

#### Building Context from the Knowledge Graph

```python
context = await build_context(
    url="memory://specs/search",        # Starting point
    depth=2,                            # Optional: How many hops to follow
    timeframe="1 month"                 # Optional: Recent timeframe
)
```

#### Checking Recent Changes

```python
activity = await recent_activity(
    type="all",                         # Optional: Entity types to include
    depth=1,                            # Optional: Related items to include
    timeframe="1 week"                  # Optional: Time window
)
```

#### Creating Knowledge Visualizations

```python
canvas_result = await canvas(
    nodes=[{"id": "note1", "label": "Search Design"}],  # Nodes to display
    edges=[{"from": "note1", "to": "note2"}],           # Connections
    title="Project Overview",                           # Canvas title
    folder="diagrams"                                   # Storage location
)
```

### Memory URI System

SkogAI-Memory uses a special URL format to reference entities in the knowledge graph:

#### URI Structure

```
memory://[resource-type]/[identifier]
```

#### Common URI Patterns

- `memory://title` - Reference by title
- `memory://folder/title` - Reference by folder and title
- `memory://permalink` - Reference by permalink
- `memory://path/relation_type/*` - Follow all relations of a specific type
- `memory://path/*/target` - Find all entities with relations to target