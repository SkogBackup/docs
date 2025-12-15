# SkogAI Type Notation

## Overview

SkogAI uses `$type` notation for type references and definitions. This algebraic type system enables precise, implementation-agnostic definitions.

## Type Reference Syntax

```
$type
```

Examples:
- `$string` - String type
- `$int` - Integer type
- `$message` - Message type
- `$coordinate` - Custom coordinate type

## Type Definitions

### Product Types

Product types combine multiple values using the `*` operator:

```
$coordinate = $int * $int
```

This represents a coordinate as a pair of integers (x, y).

### Sum Types

Sum types represent alternatives using the `|` delimiter:

```
$message_type = |user|assistant|system|tool|
```

This represents that a message can be one of: user, assistant, system, or tool.

### Type Constraints

Types can have constraints that add rules:

- `$unique` - Value must be unique
- `$optional` - Value may be omitted
- `$positive` - Numeric value must be positive

Example:
```
$user_id = $int * $unique * $positive
```

## Benefits

1. **Precision**: Exact definition of what data structures contain
2. **Implementation-agnostic**: Not tied to any specific programming language
3. **Mathematical foundation**: Enables reasoning about type safety
4. **Documentation**: Types serve as clear documentation of data structures
