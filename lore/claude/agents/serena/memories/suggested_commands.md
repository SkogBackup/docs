# Suggested Commands

## Session Management

- `./run` - skogix entry point for either a new or existing session
- `./scripts/update-context.sh` - Regenerate context for current session

## Git Operations (via Git Flow)

- `./scripts/git/feature-.sh` - Features
- `./scripts/git/release-.sh` - Releases
- `./scripts/git/feature-checkout.sh <name>` - Switch to feature branch
- `./scripts/git/current-feature.sh` - Show current feature branch
- `./scripts/git/stage.sh <file>` - Stage specific file
- `./scripts/git/*-start.sh <name>` - Start a git flow operation
- `./scripts/git/*-finish.sh` - Finish a git flow operation
- `./scripts/context-*.sh` - Output various context information which are used to build context files

## File Operations

- Files in `/state/` should be treated as immutable session state
- Use `./scripts/` prefix for all script operations
- Context updates happen automatically via Claude hooks

