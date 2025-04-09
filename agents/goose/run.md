# Run.sh Documentation

## Overview

`run.sh` is a modular context generation script for the SkogAI Goose assistant. It enables users to create customized context for the assistant by combining different information sources like workspace structure, journal entries, tasks, and file contents.

The script follows SkogAI's principles of additive parameters, modularity, and explicit documentation of uncertainty. It's designed to be simple to use while remaining highly extensible.

## Basic Usage

```bash
./run.sh [options]
```

### Core Options

| Option | Description |
|--------|-------------|
| `--interactive` | Run Goose interactively with generated context |
| `--workspace` | Include workspace structure in context |
| `--journal` | Include journal entries in context |
| `--todo` | Include task list in context |
| `--memory <num>` | Include memory files with numbers less than `<num>` from `/home/skogix/.goose/memory` |
| `--path <file>` | Include file contents in context (can be used multiple times) |
| `--debug` | Show verbose debugging information |
| `--help`, `-h` | Display help message |

### Examples

```bash

# Return empty context
./run.sh

# Launch Goose in interactive mode with empty context
./run.sh --interactive

# Return context with workspace and journal info
./run.sh --workspace --journal

# Run Goose with workspace context
./run.sh --workspace --interactive

# Return task list context
./run.sh --todo

# Include single file contents in context
./run.sh --path ./run.sh

# Include multiple files in context
./run.sh --path ./run.sh --path ./scripts/context-path.sh

# Run Goose with debugging enabled
./run.sh --debug --interactive
```

## Key Features

1. **Modular Context Generation**: Each context type is handled by a separate script in ./scripts/
2. **Additive Parameters**: Each flag adds additional context rather than setting exclusive modes
3. **Multiple File Support**: Include multiple file contents using repeated `--path` options
4. **Debugging Support**: Verbose logging with `--debug` flag
5. **Interactive or Output Mode**: Either launch Goose or return generated context as output

## Context Scripts

The script relies on separate context generation scripts located in the `./scripts/` directory:

1. **context-workspace.sh**: Provides directory structure and file listings
2. **context-journal.sh**: Includes recent journal entries
3. **context-todo.sh**: Shows active tasks from tasks/ directory and TASKS.md
4. **context-path.sh**: Formats file contents with syntax highlighting
5. **context-memory.sh**: Loads memory files with numbers less than the specified value from `/home/skogix/.goose/memory`
6. **context-claude-enhanced.sh**: [PLACEHOLDER: Comprehensive context including identity, tasks, journals, memories, knowledge base, and workspace status - see scripts/context-claude-enhanced.sh for details]
7. **context-enhanced.sh**: [PLACEHOLDER: Wrapper around context-claude-enhanced.sh with headers, footers and token usage calculation - see scripts/context-enhanced.sh for details]

## Generated Context

The generated context follows a standard Markdown format:

1. **Header**: Title and generation timestamp
2. **Content Sections**: Each requested context type in order of specification
3. **Footer**: End marker and generation timestamp

All generated contexts are saved in the `tmp/` directory:
- Full combined context: `tmp/context.md`
- Individual context components: `tmp/context-[type].md`

## Extending Run.sh

### Adding New Context Types

1. Create a new script in `./scripts/` (e.g., `context-newtype.sh`)
2. The script should output formatted Markdown to stdout
3. Add a new flag in the argument processing section of `run.sh`
4. Add a corresponding variable (e.g., `SHOW_NEWTYPE`)
5. Add a section to include the new context when the flag is set

### Best Practices

1. **Module Independence**: Each script should function independently
2. **Error Handling**: Scripts should use `set -e` to break on any error
3. **Markdown Formatting**: All output should use proper Markdown formatting
4. **Consistent Headers**: Use consistent header levels (`#`, `##`, etc.)
5. **Debug Logging**: Use `debug_log()` for debugging information
6. **Documentation Comments**: Document script purpose and parameters thoroughly
7. **Explicit Uncertainty**: Use the placeholder approach when documenting uncertain elements

### Placeholder Approach

When documenting elements you're uncertain about, follow the SkogAI placeholder approach:

1. Create complete structural frameworks
2. Explicitly mark unknown elements with placeholders: `[PLACEHOLDER: description and reasoning]`
3. Include reasoning about what elements might do
4. Preserve clear distinction between knowledge and conjecture

## Future Development Directions

The script is designed to be extended with:

1. **Token Size Management**: Adding level parameters to each context script
2. **Additional Context Types**: People, knowledge, etc.
3. **Persistent Context**: Continuing previous sessions
4. **Enhanced Filtering**: More granular control over what's included

## Troubleshooting

### Common Issues

1. **Script Permission Errors**: Ensure context scripts are executable (`chmod +x scripts/context-*.sh`)
2. **Missing Components**: Verify all required script files exist in ./scripts/
3. **Path Errors**: Use absolute paths or relative paths from the script directory
4. **File Not Found**: Check that files specified with --path exist and are readable

### Debugging

Enable debugging mode with `--debug` to see:
- Which context components are being included
- Where files are being saved
- Potential error sources

## Summary

Run.sh provides a flexible way to generate context for Goose that's tailored to your needs. By combining different context types, you can provide the assistant with exactly the information needed for your task.

For a typical session, consider running:
```bash
./run.sh --workspace --memory 10 --path /path/to/relevant/file --interactive
```

This will provide Goose with workspace structure, memory files (numbered 00-09), and specific file contents, giving it the context needed to assist effectively with your tasks.
