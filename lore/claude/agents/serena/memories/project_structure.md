# Project Structure

[@TODO:replace the ./static/file-structure.md with this file?]

## Core Files

- **run**: Entry point for collaborative sessions, continues sessions via SessionID
- **CLAUDE.md**: AI operating instructions and capabilities
- **.gitignore**: Git ignore patterns including temp files and cache

## Key Directories

### /scripts/

- **Context management**: `context-*.sh` scripts for generating session context
- **Git operations**: `git/` subdirectory with git flow automation
- **Core scripts**: `update-context.sh` for context regeneration

### /state/

- **Configuration**: User preferences, file structure docs, handover info
- **skogix.md**: User communication preferences and working style
- **Session state**: Immutable starting state for sessions
- **Planning**: `plan.md`, `todo.list`
- **Persistence**: `dump.write`, `inbox.list`

### /dev/

- **F# development**: .NET 9.0 F# projects
- **Chat history converter**: JSON processing tools and filters

### /.claude/

- **Settings**: Claude Code configuration
- **Hooks**: Post-tool-use automation (auto-staging, context updates)
