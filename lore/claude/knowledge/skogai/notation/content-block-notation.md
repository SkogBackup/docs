# SkogAI Content Block Notation

## Overview

Content blocks use `[tag]...[/tag]` syntax to mark sections with special meaning or processing requirements.

## Syntax

```
[tag]
content goes here
[/tag]
```

## Common Tags

### Examples
```
[example]
This demonstrates how something works
[/example]
```

Used to provide illustrative examples that help explain concepts.

### Rewrite Directives
```
[rewrite:instructions]
content to be rewritten
[/rewrite]
```

Marks content that should be transformed or relocated according to the instructions.

### Code Blocks
```
[code]
function example() {
  return "hello";
}
[/code]
```

### Notes and Comments
```
[note]
Important information to remember
[/note]
```

## Processing

Content blocks can be:
- Preserved as-is for documentation
- Processed by specific tools that understand the tag
- Extracted for special handling (e.g., examples for testing)
- Used to control inclusion in different contexts

## Benefits

1. **Semantic Markup**: Content has clear meaning and purpose
2. **Selective Processing**: Different tools can handle different tags
3. **Documentation**: Self-documenting structure
4. **Context Control**: Control what appears in different processing contexts

## Relationship to Command Directives

Content blocks are declarative (marking what something *is*), while command directives are imperative (specifying what to *do*). They complement each other in the SkogAI notation system.
