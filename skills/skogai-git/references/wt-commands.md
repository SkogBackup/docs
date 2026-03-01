# wt (Worktrunk) Command Reference

## Core Commands

### wt list

List all worktrees and branches with status.

```bash
wt list
```

Output shows:
- Branch name
- Status indicators (dirty, ahead/behind)
- Path to worktree
- Remote tracking info
- Last commit

### wt switch

Switch to existing worktree or create new one.

```bash
# Switch to existing
wt switch <branch>

# Create new worktree from current branch
wt switch --create <name>

# Create from specific base
wt switch --create <name> --base <base-branch>
```

**Shortcuts:**
- `^` - default branch (main/master)
- `-` - previous branch
- `@` - current branch

**Options:**
- `-c, --create` - Create new branch
- `-b, --base <BASE>` - Base branch (default: main)
- `-x, --execute <CMD>` - Run command after switch

### wt merge

Merge current worktree back to target branch.

```bash
# Merge to default target
wt merge

# Merge to specific branch
wt merge <target>
```

Runs `pre-merge` hooks before merging.

### wt remove

Remove worktree and optionally delete branch.

```bash
# Remove worktree, delete branch if merged
wt remove <branch>

# Keep branch after removal
wt remove <branch> --no-delete-branch

# Force delete unmerged branch
wt remove <branch> --force-delete
```

## Configuration Commands

### wt config

Manage configuration files.

```bash
# Show config files and locations
wt config show

# Create user config
wt config create

# List all config
wt config list
```

## Workflow Commands (wt step)

### wt step commit

Commit with LLM-generated message.

```bash
wt step commit
```

Requires LLM configured in user config.

### wt step push

Push changes to target branch.

```bash
wt step push <target>
```

### wt step rebase

Rebase onto target branch.

```bash
wt step rebase <target>
```

### Hook Commands

Manually run hooks:

```bash
wt step post-create    # Run post-create hook
wt step pre-merge      # Run pre-merge hook
```

## Configuration Files

### User Config

Location: `~/.config/worktrunk/config.toml`

```toml
[commit-generation]
command = "llm"

[worktree]
path-template = "~/dev/{branch}"
```

### Project Config

Location: `<repo>/.config/wt.toml`

```toml
# Hooks
post-create = "npm install"
pre-merge = ["npm run lint", "npm test"]

# Named hooks
[hooks.project]
post-create = "npm install"
pre-commit = "npm run lint"
pre-merge = "npm test"
```

## Common Patterns

### Feature Branch Workflow

```bash
# Start feature
wt switch --create feature/my-feature

# Work in worktree
cd ~/dev/feature/my-feature
# ... make changes ...
git commit -m "feat: add feature"

# Merge back
wt merge develop

# Cleanup
wt remove feature/my-feature
```

### Submodule Workflow

```bash
# Config in .config/wt.toml
post-create = "git submodule update --init --recursive"
pre-merge = "git submodule deinit --all"
```

### Git-Flow Integration

```bash
wt switch --create feature/x    # From develop
wt switch --create release/1.0  # From develop
wt switch --create hotfix/urgent # From main
```
