# Gita - Multi-Repository Git Management

## Overview

Gita is a tool for managing multiple git repositories with two core functionalities:

1. **Display status** of multiple repos side by side
2. **Delegate git commands** from any working directory to all or specific repos

## Quick Start - Setting Up Gita

### Initial Setup (From Scratch)

**Key insight:** The `-r` (recursive) flag can hang on large repository trees. Use individual `gita add` commands instead.

**Step 1:** Add first repo with `--group-path` to set the group's base directory:

```bash
gita add -g core --group-path /home/skogix/skogai /home/skogix/skogai
```

**Step 2:** Add remaining repos to the same group:

```bash
gita add -g core /home/skogix/skogai/docs
gita add -g core /home/skogix/skogai/tools
gita add -g core /home/skogix/skogai/amy
# ... etc
```

Or batch them in a single command:

```bash
gita add -g core /home/skogix/skogai/docs /home/skogix/skogai/tools /home/skogix/skogai/amy
```

**Step 3:** Verify with `gita ll` and `gita group ll`

**Current Configuration:**

```bash
core: /home/skogix/skogai (9 repos)
  - skogai (parent), docs, tools, .plugin
  - amy, claude, dot, goose, letta

src: /home/skogix/.local/src (12 repos)
  - argc, argc-completions, aichat, cli
  - gptme, gptme-agent-template, gptme-rag, gptme-webui
  - gemini-cli, claude-memory, mcp-proxy, skogparse
```

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

## Command Quirks and Workarounds

### Commands That Need Repo Arguments

Some commands require specific repo names and cannot operate on all repos:

```bash
# ❌ These DON'T work on all repos:
gita br          # Error: requires repo argument
gita remote      # Error: requires repo argument
gita ls core     # Error: ls takes repo names, not group names

# ✅ Use these workarounds instead:
gita shell git branch --show-current    # Show current branch for all repos
gita shell git remote get-url origin    # Show remotes for all repos
gita group ll                           # List groups (not `gita ls <group>`)
```

### Context Switching for Group Operations

Use `gita context <group>` to filter ALL gita commands to a specific group:

```bash
gita context src     # Set context to src group
gita ll              # Now shows only src repos
gita fetch           # Only fetches src repos
gita context none    # Reset to all repos
```

### Diff and Log Commands

```bash
# For individual repos:
gita super <repo> log --oneline -5     # Works great
gita super <repo> diff                 # Shows diff for specific repo

# For all repos:
gita shell git diff --stat             # Show diff stats across repos
gita shell git log --oneline -5        # Show recent commits for all
```

## Patterns for Agents

When working with multi-repo operations:

1. **Always use read-only commands first** to assess state
2. **Use fail-graceful commands** (`fetch`, `pull`, `push`) for bulk operations
3. **Never automate destructive commands** without explicit user approval
4. **Prefer wrapper scripts** over raw gita commands for consistency
5. **Check `gita ll` output** to understand repo states before operations
6. **Use `gita shell`** as the workhorse for cross-repo operations
7. **Use `gita context`** to temporarily filter to a specific group
8. **Use `gita super`** to target specific repos from anywhere

## Integration with Other Tools

- **Worktrunk (`wt`)**: Use for branch-specific worktree management
- **Gita**: Use for cross-repo status checks and bulk operations
- **Git submodules**: Gita tracks them as separate repos

## Repository Groups

Repos are organized into logical groups for easier management:

### Group Structure

**Currently Active Groups:**

```bash
core             # /home/skogix/skogai - Main project
  - skogai (parent repo)
  - docs, tools, .plugin
  - amy, claude, dot, goose, letta (agent submodules)

src              # /home/skogix/.local/src - Build from source
  - argc, argc-completions, cli
  - gptme, gptme-agent-template, gptme-rag, gptme-webui
  - aichat, gemini-cli, claude-memory
  - mcp-proxy, skogparse
```

**Potential Future Groups:**

```bash
dev              # /home/skogix/dev - Active development
  - Development worktrees and experiments

archives         # Backup/historical repos
  - Old versions preserved for reference

projects         # Standalone top-level projects
  - Independent project repos
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
gita shell git branch --show-current # See current branch for all repos
```

## Useful Command Patterns

### Quick Repo Inventory

```bash
gita ls | wc -w                    # Count tracked repos
gita group ll                      # Show all groups and their repos
gita freeze                        # Export full configuration (backup)
gita ll | grep -E "\[\*|\[\+|\[?" # Show only repos with changes
```

### Cross-Repo Information Gathering

```bash
gita shell pwd                              # Show all repo paths
gita shell git branch --show-current        # Show current branch for each
gita shell git remote get-url origin        # Show all remote URLs
gita shell git log --oneline -5             # Recent commits for all repos
gita shell git diff --stat                  # Diff stats for all repos
```

### Targeting Specific Repos

```bash
gita super <repo> status -sb               # Quick status from anywhere
gita super <repo> log --oneline -5         # Recent log from anywhere
gita super <repo> diff                     # Show diff from anywhere
gita ll <repo>                             # Status for specific repo
```

### Color Scheme Reference

Check with `gita color ll`:
- **red** = diverged (local and remote have different commits)
- **green** = in_sync (clean and synced with remote)
- **purple** = local_ahead (ahead of remote, ready to push)
- **yellow** = remote_ahead (behind remote, need to pull)
- **white** = no_remote (no remote tracking configured)

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

### Setup Guidelines
- **Never use `-r` (recursive)** - it hangs on large trees; add repos individually instead
- **Use `--group-path`** with the first add to set a group's base directory
- **Batch individual adds** - multiple paths in one `gita add -g <group> <path1> <path2>...` command works great
- **Test with `-n` (dry-run)** before actual adds to verify behavior

### Command Usage Patterns
- **Prefer `gita shell`** as the workhorse for cross-repo operations
- **Use `gita context`** to filter operations to a specific group temporarily
- **Use `gita super`** to target specific repos from anywhere
- **Always check safety category** before running commands
- **Document new wrappers** by updating this file

### Command Gotchas
- `gita ls` takes REPO names, not group names (use `gita group ll` for groups)
- `gita br`, `gita remote` require specific repo arguments (use `gita shell` for cross-repo)
- `gita diff <repo>` only shows path (use `gita super <repo> diff` or `gita shell git diff`)
- Context switching affects ALL gita commands until reset with `gita context none`

### This Document
- Reference when working with multi-repo operations
- Update with new patterns discovered during actual usage
- Maintain "what we actually did" sections alongside theory
