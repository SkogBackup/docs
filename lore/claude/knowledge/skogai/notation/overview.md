# SkogAI Notation System Overview

## Purpose

The SkogAI ecosystem uses a consistent notation system for knowledge representation, command processing, and cross-agent communication. Understanding this notation is essential for working within the ecosystem.

## Core Notation Elements

### Type Notation: `$type`
Type references and definitions for precise, implementation-agnostic specifications.

See: [type-notation.md](./type-notation.md)

Examples:
- `$string`, `$int`, `$message`
- `$coordinate = $int * $int` (product type)
- `$message_type = |user|assistant|system|tool|` (sum type)

### Content Block Notation: `[tag]...[/tag]`
Content blocks with special meaning for semantic markup and selective processing.

See: [content-block-notation.md](./content-block-notation.md)

Examples:
- `[example]...[/example]` - Illustrative examples
- `[rewrite:...]...[/rewrite]` - Content transformation directives
- `[note]...[/note]` - Important information

### Command Directive Notation: `[@command:param1:param2]`
Command directives that execute and replace themselves with output.

See: [command-directive-notation.md](./command-directive-notation.md)

Examples:
- `[@fetch:data.json]` - Retrieve data
- `[@agent:message]` - Agent communication
- `[@format:[@fetch:data]:pretty]` - Nested commands (inside-out processing)

### Property Notation: `entity.property`
Relationship notation expressing "have" or "part of" connections.

See: [property-notation.md](./property-notation.md)

Examples:
- `message.id` - A message has an identifier
- `task.state` - A task has a state
- `project.timeline` - A timeline is part of a project

## Practical Applications

### Dynamic Content Generation
Command directives enable live data and computed content:
```
Current status: [@agent:get-status]
```

### Type-Safe Definitions
Algebraic types provide precise contracts:
```
$task = {
  id: $string * $unique,
  state: |new|active|blocked|completed|cancelled|,
  priority: |low|medium|high|
}
```

### Clean Restarts
The notation enables precise control over what information is included in different contexts, supporting the "clean restart" pattern where AI agents can start fresh without irrelevant conversation history.

### Cross-Agent Communication
Universal notation allows different AI agents to communicate reliably:
```
[@agent:amy:review-task:task-123]
```

## Design Principles

1. **Human-Readable**: Notation is clear and understandable
2. **Machine-Processable**: Can be parsed and executed programmatically
3. **Composable**: Elements combine to create complex operations
4. **Declarative**: Focus on *what*, not *how*
5. **Universal**: Works across different tools and agents in the ecosystem

## Related Documentation

- **Command Processing**: How directives are recursively evaluated
- **Type System**: Algebraic data types in detail
- **Agent Communication**: Using notation for multi-agent interaction
- **Clean Restart Pattern**: Context control for fresh starts
