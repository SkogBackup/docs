# Shared Memory System for Claude and Goose

## Purpose

This proposal outlines an implementation approach for a shared memory system between Claude and Goose agents, allowing both to access and modify the same memory store. This will enable enhanced collaboration, reduced redundancy, and improved continuity across agent interactions.

## Current Implementation

Currently, each agent has its own isolated memory store:

- Claude's memories are stored at: `/home/skogix/.local/share/mcp-memory/chroma_db`
- Goose likely has a separate memory database path

The MCP memory system uses ChromaDB (a vector database) with the following architecture:
- Embedding model: all-mpnet-base-v2
- Hardware acceleration: CUDA when available
- Collection name: "memory_collection"

## Proposed Solution

### 1. Shared Database Path

Create a centralized memory database accessible by both agents:

```
/home/skogix/.local/share/mcp-memory-shared/chroma_db
```

### 2. Agent Configuration Changes

#### For Claude:
1. Modify Claude's MCP server configuration to point to the shared database path
2. Update any references to the memory database in Claude's workspace

#### For Goose:
1. Similar configuration updates pointing to the shared database
2. Ensure Goose has compatible embedding model settings

### 3. Tagging System

To differentiate memories created by different agents:

1. Implement automatic agent tagging on memory creation
2. Add metadata field "source_agent": "claude"|"goose"
3. Allow both agents to query by tag for agent-specific recalls

Example memory structure:
```json
{
  "content": "Meeting with Skogix about project architecture",
  "metadata": {
    "source_agent": "claude",
    "tags": ["meeting", "architecture"],
    "created_at": "2025-03-22T14:30:00Z"
  }
}
```

### 4. Synchronization Protocol

Implement a lightweight protocol to handle potential conflicts:

1. Read-before-write pattern for memory updates
2. Timestamped entries for chronological ordering
3. Non-destructive memory appending rather than replacement

### 5. Migration Plan

Steps to transition to the shared system:

1. Create backup of both agents' existing memories
2. Set up new shared database path and permissions
3. Migrate Claude's memories with appropriate source tags
4. Migrate Goose's memories with source tags
5. Update agent configurations to use new path
6. Validate memory recall functionality for both agents

## Implementation Requirements

1. File system modifications:
   - Create new shared directory with appropriate permissions
   - Backup script for existing memories

2. MCP server configuration changes:
   - Update database path configuration
   - Add agent source tagging
   - Memory query enhancements for filtering

3. Testing procedure:
   - Verify memory creation from both agents
   - Test cross-agent memory recall
   - Performance validation under load

## Open Questions

1. What is Goose's current memory database path?
2. Are there any agent-specific memory formats that need to be normalized?
3. Should there be any access control mechanisms between agents?
4. How should conflicts be handled if both agents update the same memory?
5. Would other agents (like Dots) also benefit from this shared system?

## Next Steps

1. Locate Goose's memory configuration and database path
2. Create backup scripts for both memory systems
3. Develop configuration update script for agent workspaces
4. Implement and test the shared database setup
5. Create monitoring system for shared memory usage

## Success Criteria

The implementation will be considered successful when:

1. Both Claude and Goose can read and write to the same memory database
2. Memories created by one agent are accessible to the other
3. Agent-specific queries still function correctly
4. System performance is comparable to or better than the isolated approach
5. Memory integrity is maintained throughout the migration