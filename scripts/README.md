# SkogAI/Docs Utility Scripts

This directory contains utility scripts that simplify common git operations for the SkogAI/Docs repository.

## Available Scripts

### `docs-cli`

A command-line utility that condenses multiple git commands into simple operations.

```bash
./scripts/docs-cli COMMAND [ARGUMENTS]
```

#### Commands:

- `status` - Show git status
- `last` - Show last commit
- `branches` - List all branches
- `branch` - Show current branch
- `checkout BRANCH` - Checkout a branch
- `history [N]` - Show last N commits (default: 5)
- `diff [FILE]` - Show changes in file or repo
- `view FILE` - View a file's contents
- `ls [DIR]` - List files in directory
- `create-proposal NAME` - Create new proposal branch
- `create-draft NAME` - Create new draft branch
- `summarize` - Show repository overview
- `help` - Show available commands

#### Examples:

```bash
# Show last commit
./scripts/docs-cli last

# View a specific file
./scripts/docs-cli view workflows/pr-process.md

# Create a new proposal branch
./scripts/docs-cli create-proposal context-system

# Get a complete repository summary
./scripts/docs-cli summarize
```

### `docs-context`

Generates a markdown summary of the repository's current state.

```bash
# Output to terminal
./scripts/docs-context

# Save to a file
./scripts/docs-context > context.md
```

The context includes:
- Current branch information
- Recent commits
- Repository structure
- Active proposals
- Key documentation content

## Purpose

These scripts replace multiple git commands that were previously needed to check repository status. They provide consistent formatting and simplified syntax for common operations in the SkogAI documentation workflow.