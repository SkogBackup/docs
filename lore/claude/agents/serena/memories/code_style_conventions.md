# Code Style and Conventions

## Functional Programming Philosophy
- **Data Transformations**: Express ideas in terms of data and transformations rather than control flow
- **Pure Functions**: Prefer pure functions and immutable data structures
- **Simplicity First**: Always strive for simplicity first, improve complexity later
- **Function Signatures**: Use function signatures and data types as primary communication tools

## Shell Script Conventions
- **printf bare with newlines**: Primary way to display output from scripts
- **No git add -A**: Use specific file additions instead
- **./scripts/ prefix**: Always use ./scripts/ for script execution when possible

## File Naming
- **Lowercase significance**: Use lowercase for files/directories - uppercase letters are significant when used
- **Context scripts**: `./scripts/context-*` files output information for reading/appending
- **State management**: `./state/` contains immutable session state data

## Git Conventions
- **Git Flow**: Uses git flow for branch management
- **Specific staging**: `git add <filename>` preferred over `git add -A`
- **Script-based operations**: Use scripts for git operations when possible

## Communication Style
- **Concise responses**: Prefer brief, direct answers
- **Data flow diagrams**: Use when showing system information flow
- **Transparent collaboration**: Direct, honest communication without unnecessary explanation