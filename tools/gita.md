# Gita - Multi-Repository Git Management

## Overview

Gita is a tool for managing multiple git repositories with two core functionalities:

1. **Display status** of multiple repos side by side
2. **Delegate git commands** from any working directory to all or specific repos

## Core Concepts

### Power Features

- **`gita shell <command>`** - Run ANY shell command across all repos
  - Example: `gita shell pwd` shows paths of all repos
  - Example: `gita shell git status -sb` shows status in each repo
  - This is the foundation for creating simple, powerful wrapper scripts

- **`gita super <repo> <git-command>`** - Run git command on specific repo from anywhere

### Status Display

- `gita ll` shows compact status with symbols:
  - `[]` - clean
  - `[*]` - uncommitted changes
  - `[+]` - staged changes
  - `[?]` - untracked files
  - `[∅]` - detached HEAD / not on branch
  - `[↑]` - ahead of remote
  - `[$]` - submodule changes

## Command Safety Categories

### ✅ 100% Safe - Read-Only Commands

These commands never modify your repos and are always safe to script:

```bash
gita ll          # Status overview (compact with symbols)
gita ls          # List repos/paths
gita st          # Detailed status for all repos
gita br          # Show local branches across repos
gita diff        # Show differences
gita log         # Show full logs
gita lo          # Show one-line log for latest 7 commits
gita last        # Show log information of HEAD
gita remote      # Show remote settings
gita info        # Show gita configuration
gita stat        # Show edit statistics
gita show        # Show detailed commit information
gita reflog      # Show ref logs
gita tag         # Show tags
```

**Available Wrapper Scripts:**
- `git-show-all-paths.sh` → `gita shell pwd`
- `git-show-all-status.sh` → `gita st`
- `git-show-all-branches.sh` → `gita br`
- `git-show-all-remotes.sh` → `gita remote -v`
- `git-show-recent-commits.sh` → `gita lo`
- `git-show-dirty-repos.sh` → `gita super git diff --quiet` (uses exit codes, not text parsing)

### ⚠️ Safe - Fail-Graceful Commands

These commands are safe for scripting because they **fail gracefully** rather than forcing destructive operations:

```bash
gita fetch       # Download updates, never touches working tree
gita pull        # Fails if uncommitted changes exist
gita push        # Fails if not synced or no upstream tracking
```

**Key Insight:** These commands refuse to run when there's a conflict, making them safe for batch operations.

Example of `gita pull` failing gracefully:
```
gemini-cli: error: cannot pull with rebase: Your index contains uncommitted changes.
gemini-cli: error: Please commit or stash them.
```

### 🛠️ Administrative - Safe (Gita Config Only)

These modify gita's configuration, not your repositories:

```bash
gita add <path>  # Add repo to gita tracking
gita rm <name>   # Remove repo from gita tracking
gita freeze      # Export all repo information
gita clone       # Clone repos from freeze file
gita rename      # Rename a repo in gita
gita group       # Manage repo groups
gita context     # Set working context
gita flags       # Configure git flags
gita color       # Color configuration
```

### 🚨 Dangerous - Require User Confirmation

**NEVER script these without explicit user approval** - they can destroy work:

```bash
gita clean       # DELETES all untracked files/folders (destructive!)
gita reset       # Can discard commits (very destructive!)
gita stash       # Hides changes (reversible but confusing)
gita merge       # Modifies history
gita rebase      # Rewrites history
gita mergetool   # Interactive merge resolution
gita difftool    # Interactive diff tool
gita patch       # Create patches
gita clear       # Removes ALL groups and repositories from gita
```

### 💪 Power User Commands

```bash
gita super <repo> <git-cmd>  # Run specific git command on one repo
gita shell <shell-cmd>       # Run any shell command in all repos
```

These are as safe or dangerous as the command you pass to them.

## Recommended Everyday Scripts

Based on safety analysis, these wrapper scripts are available in `@scripts/`:

```bash
# Read-only wrappers (always safe)
git-show-all-paths.sh       # gita shell pwd
git-show-all-status.sh      # gita st
git-show-all-branches.sh    # gita br
git-show-all-remotes.sh     # gita remote -v
git-show-recent-commits.sh  # gita lo

# Safe operations (fail gracefully)
git-fetch-all.sh            # gita fetch
git-pull-all.sh             # gita pull (fails on dirty repos)

# Filtered views (using gita super with exit codes)
git-show-dirty-repos.sh     # gita super git diff --quiet
```

**Why `gita super` with exit codes?**
Instead of fragile text parsing with grep/sed/awk, use `gita super` with git commands that have meaningful exit codes. For example, `git diff --quiet` exits non-zero when there are changes, and gita prints only those repo paths. This is robust and uses the tool as designed.

## Patterns for Agents

When working with multi-repo operations:

1. **Always use read-only commands first** to assess state
2. **Use fail-graceful commands** (`fetch`, `pull`, `push`) for bulk operations
3. **Never automate destructive commands** without explicit user approval
4. **Prefer wrapper scripts** over raw gita commands for consistency
5. **Check `gita ll` output** to understand repo states before operations

## Integration with Other Tools

- **Worktrunk (`wt`)**: Use for branch-specific worktree management
- **Gita**: Use for cross-repo status checks and bulk operations
- **Git submodules**: Gita tracks them as separate repos

## Repository Groups

Repos are organized into logical groups for easier management:

### Group Structure

```bash
src              # /home/skogix/.local/src - Build tools
  - argc, gptme, goose, aichat, gemini-cli, etc.
  - Tools we build from source

letta            # Letta framework ecosystem
  - letta-1, letta-code, agent-file, ai-memory-sdk, etc.
  - All Letta-related projects

skogai-core      # /home/skogix/skogai - Main project
  - skogai, docs, tools
  - Core SkogAI infrastructure

skogai-agents    # /home/skogix/skogai - Agent submodules
  - claude, amy, dot, skogai/goose
  - Individual agent workspaces

dev              # /home/skogix/dev - Active development
  - dev/skills, dev/worktrunk, conductor, supabase, etc.
  - Development worktrees and experiments

archives         # Backup/historical repos
  - archive-2025-*, lore-archive, skog-claude
  - Old versions preserved for reference

projects         # Top-level projects
  - lore, PLUGINS, worktrunk, mcp-proxy, etc.
  - Standalone projects
```

### Working with Groups

```bash
# View all groups
gita group ll

# Check status of a specific group
gita ll src
gita ll skogai-core

# Run commands on a group (using context)
gita context src
gita fetch            # Only fetches src group
gita context none     # Reset to all repos

# Add repos to a group
gita group add -n group-name repo1 repo2
```

## Common Workflows

### Morning Sync (Safe)
```bash
gita fetch              # Download all updates
gita ll                 # Check status
gita pull               # Pull clean repos (fails gracefully on dirty)
```

### Group-Specific Operations
```bash
gita ll dev             # Check dev worktree status
gita ll skogai-core     # Check core project status
./scripts/git-show-dirty-repos.sh  # Find all dirty repos
```

### Status Check
```bash
./scripts/git-show-all-paths.sh    # See where everything is
gita group ll                       # See all groups
gita ll                             # See what needs attention
gita br                             # See all branches
```

## Configuration Management

Gita configuration is stored in **@/home/skogix/.dotfiles/config/gita/** (version-controlled in dotfiles):

```
~/.dotfiles/config/gita/
├── repos.csv    # Repository paths and names
└── groups.csv   # Group definitions
```

### Configuration Format

**repos.csv** - One repo per line:
```csv
/full/path/to/repo,repo-name,,
```

**groups.csv** - Group definitions with optional path:
```csv
group_name:repo1 repo2 repo3:optional-path
```

### Backup and Restore

```bash
# Export current configuration
gita freeze > gita-backup.txt

# Restore on new machine (symlink gita config to dotfiles location)
gita clone < gita-backup.txt
```

### Cross-Machine Setup

Since gita config lives in dotfiles:
1. Clone your dotfiles repo on new machine
2. Symlink gita config: `ln -s ~/.dotfiles/config/gita ~/.config/gita`
3. Run `gita clone` or manually clone repos
4. Groups and repo tracking automatically available

**Why dotfiles?**
- ✅ Version controlled across machines
- ✅ Easy backup and restore
- ✅ Consistent repo organization everywhere
- ✅ Simple CSV format for manual editing if needed

## References

- Gita GitHub: https://github.com/nosarthur/gita
- Bash completion: https://github.com/nosarthur/gita/blob/master/.gita-completion.bash
- Configuration: @/home/skogix/.dotfiles/config/gita/

## Notes for AI Agents

- **Prefer wrapper scripts** in `@scripts/` over raw gita commands
- **Always check safety category** before running commands
- **Use `gita shell`** as the primitive for creating new wrappers
- **Document new wrappers** by updating this file
- This document should be referenced when working with multi-repo operations
