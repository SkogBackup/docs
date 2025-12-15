# SkogAI Command Directive Notation

## Overview

Command directives use the `[@command:param1:param2]` syntax to create dynamic, executable content that gets replaced with its output during processing.

## Syntax

```
[@command:parameter1:parameter2:...]
```

## Processing Model

Command directives are processed **recursively from inside out**:

```
[@format:[@fetch:data.json]:pretty]
```

Processing steps:
1. `[@fetch:data.json]` executes first, retrieving data
2. This directive is replaced with its output
3. `[@format:<output>:pretty]` processes the fetched data
4. The entire directive is replaced with the final formatted result

## Common Command Patterns

### Data Fetching
```
[@fetch:path/to/file]
```

### Agent Communication
```
[@agent:query or message]
```

Runs operations and replaces itself with the agent's response.

### Formatting
```
[@format:content:format-type]
```

### Composition
Commands can be nested to create complex transformations:

```
[@transform:[@filter:[@fetch:data]:criteria]:output-format]
```

## Benefits

1. **Dynamic Content**: Content is generated at processing time
2. **Tool Integration**: Seamlessly integrates external tools and scripts
3. **Clean Separation**: Implementation details hidden behind directive syntax
4. **Composability**: Commands can be combined for complex operations

## Use Cases

- Dynamic script execution
- Cross-agent communication
- Data transformation pipelines
- Context generation for AI prompts
- Template expansion with live data
