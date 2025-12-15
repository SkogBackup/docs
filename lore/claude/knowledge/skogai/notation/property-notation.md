# SkogAI Property Notation

## Overview

Property notation uses dot syntax to express relationships between entities: `entity.property`

## Syntax

```
entity.property
```

## Interpretation

The comment in CLAUDE.md suggests: "this should be explained as 'have or be a part of' - property is a loaded word with meaning."

### "Have" Relationship
```
message.id
```
A message **has** an identifier.

### "Part Of" Relationship
```
user.name
```
A name is **part of** a user's identity.

## Why Not Just "Property"?

The word "property" can imply:
- Ownership (problematic for relationships)
- Static attributes (ignoring dynamic relationships)
- Implementation details (focusing on storage rather than meaning)

Instead, thinking in terms of "have" and "part of" emphasizes:
- **Relationships**: How entities relate to each other
- **Composition**: How complex entities are built from simpler ones
- **Meaning**: What the relationship signifies conceptually

## Examples

```
task.state        # A task has a state
journal.date      # A date is part of a journal entry
person.skills     # Skills are part of a person's profile
project.timeline  # A timeline is part of a project
```

## Integration with Type System

Property notation works with the type system:

```
$message = {
  id: $string * $unique,
  content: $string,
  timestamp: $datetime
}
```

Then `message.id` refers to the unique string identifier that a message has.

## Benefits

1. **Clarity**: Expresses relationships clearly
2. **Flexibility**: Works for various relationship types
3. **Consistency**: Familiar dot notation with richer meaning
4. **Composition**: Supports nested relationships (e.g., `project.team.members`)
