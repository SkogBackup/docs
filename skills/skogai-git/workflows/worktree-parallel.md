# Worktree Parallel Work

Create and manage worktrees for parallel development on multiple branches.

<required_reading>
- references/wt-commands.md (if unfamiliar with wt)
- references/hook-types.md (if setting up automation)
</required_reading>

<process>

## 1. Check Current State

```bash
wt list
```

Shows all branches, worktrees, and status.

## 2. Create New Worktree

```bash
# From default branch (main/master)
wt switch --create feature/my-feature

# From specific base
wt switch --create feature/my-feature --base develop
```

This:
- Creates new branch
- Creates worktree in configured path (default: `~/.worktrees/<branch>`)
- Runs `post-create` hooks (npm install, etc.)
- Switches to new worktree

## 3. Work in Worktree

```bash
# You're now in the worktree
pwd  # ~/.worktrees/feature/my-feature

# Work normally
git status
git add .
git commit -m "feat: add feature"
```

Each worktree is fully independent.

## 4. Switch Between Worktrees

```bash
# Switch to another worktree
wt switch feature/other-feature

# Switch to main
wt switch main
# Or shortcut:
wt switch ^
```

## 5. Merge When Done

```bash
# Merge current worktree to default target
wt merge

# Or to specific target
wt merge develop
```

This:
- Runs `pre-commit` hooks
- Creates commit
- Switches to target branch
- Runs `pre-merge` hooks (tests)
- Merges
- Pushes
- Runs `post-merge` hooks
- Cleans up worktree

## 6. Manual Cleanup (if needed)

```bash
# Remove worktree, delete branch if merged
wt remove feature/my-feature

# Force delete unmerged branch
wt remove feature/abandoned --force-delete

# Keep branch, just remove worktree
wt remove feature/my-feature --no-delete-branch
```

</process>

<common_patterns>

## Git-Flow Feature

```bash
wt switch --create feature/login --base develop
# ... work ...
wt merge develop
```

## Hotfix

```bash
wt switch --create hotfix/critical --base main
# ... fix ...
wt merge main
```

## Multiple Features in Parallel

```bash
# Start first feature
wt switch --create feature/auth

# Start second feature (in new terminal)
wt switch --create feature/payments

# Switch between them
wt switch feature/auth
wt switch feature/payments

# Merge each when ready
wt switch feature/auth
wt merge
wt switch feature/payments
wt merge
```

## PR Review Isolation

```bash
wt switch --create review/pr-123
gh pr checkout 123
# ... review ...
wt remove review/pr-123 --force-delete
```

</common_patterns>

<success_criteria>
- Worktree created and hooks ran
- Can switch between worktrees freely
- Changes merged cleanly
- Worktree cleaned up after merge
</success_criteria>
