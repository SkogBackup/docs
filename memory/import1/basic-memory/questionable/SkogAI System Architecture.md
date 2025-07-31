---
title: SkogAI System Architecture
type: note
permalink: system/skog-ai-system-architecture-1
---

# SkogAI System Architecture

## Summary

The SkogAI system follows a modular architecture designed for flexibility, extensibility, and clear separation of concerns. This document outlines the core components, their relationships, and the guiding principles behind the architectural decisions.

## Core Components

### 1. Workspace Structure

The SkogAI workspace is organized into specialized directories:

- **tasks/**: Task management and tracking
- **journal/**: Daily logs and records
- **knowledge/**: Information storage and retrieval
- **memory/**: Hierarchical memory system
- **people/**: Collaborator information
- **projects/**: Project-specific files and documentation
- **scripts/**: Utility scripts and automation
- **contexts/**: Dynamic context management

### 2. Extension System

SkogAI capabilities are enhanced through extensions:

- **developer**: Shell access and file manipulation
- **computercontroller**: System control and web interaction
- **skogai-memory**: Knowledge management system
- **skogmcp**: Multimodal Capability Provider integration
- **skoghub**: Extension management and coordination

### 3. Memory Architecture

The memory system has evolved from:

- **Original**: File-based hierarchical system (00-series files)
- **Current**: Semantic knowledge graph with relationship tracking

### 4. Agent Framework

SkogAI employs multiple specialized agents:

- **Goose**: Experimentation specialist
- **Dot**: Structure specialist
- **Claude**: Implementation specialist
- **Amy Ravenwolf**: Meta-cognition specialist

## Architectural Principles

### 1. Modular Design

Components are designed with clear boundaries and interfaces, allowing them to:

- Be developed independently
- Be tested in isolation
- Be replaced or upgraded without affecting other components

### 2. Separation of Concerns

Each component has a distinct responsibility:

- Task tracking separated from knowledge management
- Journal entries separated from project documentation
- Context management separated from memory storage

### 3. Documentation-Driven Development

Documentation is a primary artifact, not an afterthought:

- Core principles documented in README.md
- Architecture described in ARCHITECTURE.md
- Tools listed in TOOLS.md

### 4. Extensibility

The system is designed for extension through:

- Well-defined extension interfaces
- Consistent naming conventions
- Clear extension registration process

## Interaction Patterns

### 1. Agent-Component Interaction

Agents interact with components through:

- Standardized APIs
- Tool-based interfaces
- Context-aware operations

### 2. Context Management

Context is managed through:

- Selective visibility of relevant files
- Task-specific context construction
- Dynamic context adjustment

### 3. Knowledge Flow

Information flows through the system via:

- Journal entries capturing daily progress
- Knowledge base documenting persistent information
- Memory system providing hierarchical organization
- Project documentation providing specific details

## Implementation Considerations

### 1. Git Integration

The SkogAI system is closely integrated with git:

- Proper repository structure
- Git-flow methodology
- Submodule management
- Clean commit hygiene

### 2. Task Management

Tasks progress through well-defined states:

- New → Active → Done/Cancelled
- Symlinks track task state transitions
- Task documentation maintains history

### 3. Memory Consistency

Knowledge is managed with attention to:

- Cross-referencing between related information
- Consistent formatting and organization
- Clear categorization and tagging
- Version history preservation

## Evolutionary Path

The architecture continues to evolve with:

1. **Integration Enhancements**: Better coordination between components
2. **Memory System Evolution**: Transition to semantic knowledge graph
3. **Tool Consolidation**: Movement from MCP-based tools to extensions
4. **Documentation Improvements**: More comprehensive and consistent documentation

## Best Practices

When working with the SkogAI architecture:

1. Follow the established directory structure
2. Maintain clean separation between components
3. Document changes thoroughly
4. Respect each agent's specialized domain
5. Maintain git commit hygiene
6. Use appropriate extensions for specific tasks