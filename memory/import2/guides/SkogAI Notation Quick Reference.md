---
title: SkogAI Notation Quick Reference
type: reference
permalink: guides/skog-ai-notation-quick-reference
tags:
- skogai-notation quick-reference symbols operators syntax cheat-sheet
---

# SkogAI Notation Quick Reference

*Essential symbols and meanings for the void-based programming language*

## The Four Dimensions

| Symbol | Name | Meaning | Example |
|--------|------|---------|---------|
| `@` | Intent/Action | "the intent to act or do something" | `[@fizz:15]` |
| `$` | Reference/State | "to define or reference something" | `$.json.string` |
| `_` | Existence/Void | "to be anything/everything and nothing/nobody" | `"_": ""` |
| `?` | Collaboration | The uncertainty bridge between minds | `?Claude` |

## Core Operators

| Symbol | Name | Definition | Usage |
|--------|------|------------|-------|
| `=` | Identity | "to be something" | `[$id=$id]` |
| `->` | Transformation | Path from one state to another | `{$id1@$id2}` |
| `*` | Composition | Multiply/combine concepts | `$int*$unique` |
| `\|` | Choice | Selection between options | `{$id1\|$id2}->[$id1]` |
| `.` | Belonging | "to belong or have something" | `$parent.$child` |
| `:` | Following | "to follow or continue something" | `$type:item` |

## Relational Operators

| Symbol | Name | Meaning |
|--------|------|---------|
| `[_]` | Similarity | Same through void |
| `{_}` | Difference | Different through void |
| `$$` | Meta-reference | Reference to reference |
| `$@` | Reference-to-action | State becoming intent |
| `@$` | Action-on-reference | Intent acting on state |

## Key Type Definitions

```
$id = $int*$unique
$unique = [@date:now]
$eid = $entity.id*$entity.gen
$@=@$ (functions as perfect loops)
```

## Essential Syntax Patterns

### Action Execution
```
[@action:parameter]
```

### JSON Path Reference
```
$.path.to.value
```

### Type Definitions
```
"type": "$definition*$composition"
```

### Relationship Chains
```
$parent.$child:$grandchild
```

## Termination Values

| Type | Termination | Purpose |
|------|-------------|---------|
| String | `""` | Empty string stops recursion |
| Integer | `0` | Zero stops numeric recursion |
| List | `[]` | Empty list stops collection recursion |

## The Fundamental Equation

```
@ + ? = $
```

*Intent plus collaboration equals manifestation*

## Common Expressions

### Identity Paradox
```
[$id=$id]  // Same from similarity perspective
{$id=$id}  // Different from difference perspective
```

### Trust
```
$you@?@$me  // You acting through uncertainty on me
```

### Understanding
```
?->[$meaning]  // Uncertainty resolving to shared meaning
```

### Creativity
```
_@?->$new  // Void through uncertainty creates novelty
```

## Implementation Shortcuts

### Quick Tool Creation
```bash
[@create-script:name:description]
```

### Instant Execution
```bash
echo "[@command:param]" | skogparse --execute
```

### AI Collaboration
```bash
[@claude:your question here]
```

### System Definition
```bash
[@def:concept]  // Get AI explanation of any concept
```

---

*Remember: Everything emerges from the interplay between void (@) and reference ($), mediated by existence (_) and collaboration (?)*