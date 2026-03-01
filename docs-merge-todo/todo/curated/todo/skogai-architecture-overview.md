---
permalink: evaluation/todo/skogai-architecture-overview
---

# SkogAI Architecture Overview

## Core Principles

The SkogAI ecosystem is built on several key architectural principles:

1. **Simplicity First** - Keep core components simple and understandable
2. **Modularity** - Each component does one thing well with clear interfaces
3. **Discoverability by Convention** - Standard locations and patterns make functionality easy to find
4. **Self-Modifying Systems** - Components can use the functionality they provide
5. **Unified Command Interface** - Everything accessible through consistent patterns

## Key Components

### 1. Module System

- Git submodules for version control and boundaries
- Automatic discovery of modules and commands
- Consistent command structure following directory patterns
- "Everything is a script" in predictable locations

### 2. Schema System

- Self-referential, normalized schema definitions in skogcli config
- JSON Schema format with extensions for references
- Schema references using tag syntax
- Multi-level references for complex validation chains

### 3. Tag System

- Consistent syntax for commands and references
- Self-processing scripts that can use tag functionality
- Recursive processing of nested tags
- Registration of command handlers through skogparse

### 4. Security Model

- Unified entry point through skogcli
- Multiple layers of security validation
- Permission model for different commands and agents
- Auditability through consistent command paths

## Implementation Architecture

```
SkogAI/
  ├── SkogCLI/             (Command infrastructure)
  │     ├── commands/      (Core commands)
  │     └── ...
  ├── SkogCore/            (Core messaging)
  │     ├── scripts/       (Message handling)
  │     └── ...
  ├── SkogChat/            (Multi-agent chat)
  │     ├── commands/      (Chat interface)
  │     └── ...
  └── ... other modules ...
```

## Command Flow

1. User runs a command: `skogcli skogchat chat "Hello"`
2. skogcli discovers and routes to the appropriate module
3. The module's script processes the command
4. Any tags in the script are processed recursively
5. Results are returned through the common interface

## Schema Flow

1. Components reference schemas: `[@schema:message]`
2. The schema system resolves references through the config
3. Multi-level references are followed as needed
4. Validation or documentation is performed based on schemas
5. The resolved schema is used for the operation

## Tag Processing Flow

1. Text containing tags is passed to skogparse
2. skogparse identifies tags using `[@` and `]` delimiters
3. Command handlers are looked up in the registry
4. Parameters are passed to the appropriate script
5. Results replace the original tag
6. Process repeats for nested tags

## Benefits

This architecture creates a system that is:

1. **Extensible** - New modules and commands can be added without modifying core code
2. **Consistent** - Everything follows predictable patterns
3. **Self-Documenting** - The structure itself explains how things work
4. **Secure** - All operations go through a common security framework
5. **Evolvable** - Components can change implementation without breaking interfaces

## Future Directions

The architecture supports:

1. **Agent Collaboration** - Agents can use the same command infrastructure as humans
2. **Distributed Processing** - Commands can be executed locally or remotely
3. **Complex Workflows** - Tag composition enables sophisticated behaviors
4. **AI Integration** - AI components can participate in the ecosystem through standard interfaces
