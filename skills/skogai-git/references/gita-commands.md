# gita Command Reference

## Core Commands

### gita ll

List all managed repos with status.

```bash
gita ll
```

Output shows:
- Repo name
- Branch
- Status (dirty, ahead/behind)
- Last commit message
- Age

### gita st

Show git status across all repos.

```bash
gita st
```

### gita add

Add repo(s) to gita management.

```bash
# Add single repo
gita add ~/projects/my-repo

# Add multiple repos
gita add ~/projects/repo1 ~/projects/repo2

# Add all repos in directory
gita add ~/projects/*
```

### gita rm

Remove repo from gita management.

```bash
gita rm <repo-name>
```

Does not delete the repo, just stops tracking.

## Sync Commands

### gita pull

Pull all repos (or specific ones).

```bash
# Pull all
gita pull

# Pull specific repos
gita pull repo1 repo2

# Pull with options
gita pull --rebase
```

### gita push

Push all repos.

```bash
gita push
```

### gita fetch

Fetch all repos.

```bash
gita fetch
```

## Organization Commands

### gita group

Manage repo groups.

```bash
# Create group
gita group add frontend repo1 repo2 repo3

# List groups
gita group ls

# Remove group
gita group rm frontend
```

### Using Groups

```bash
# List repos in group
gita ll frontend

# Pull only group
gita pull frontend

# Run command on group
gita super frontend git status
```

## Advanced Commands

### gita super

Run arbitrary git command on all repos.

```bash
# Check last commit on all repos
gita super git log -1 --oneline

# Checkout branch on all repos
gita super git checkout develop

# Stash all repos
gita super git stash
```

### gita shell

Run shell command on all repos.

```bash
# Run npm install in all repos
gita shell npm install

# Run custom script
gita shell ./setup.sh
```

## Common Patterns

### Daily Sync

```bash
# Morning routine
gita fetch
gita ll          # Check status
gita pull        # Pull updates
```

### Status Check

```bash
# Quick overview
gita ll

# Detailed status
gita st

# Find repos with changes
gita ll | grep '\*'  # Dirty repos
gita ll | grep '↑'   # Ahead of remote
```

### Bulk Operations

```bash
# Checkout same branch on all repos
gita super git checkout main

# Pull with submodules
gita super git pull --recurse-submodules

# Clean all repos
gita super git clean -fd
```

### Group Workflows

```bash
# Define groups by project area
gita group add backend api-service db-service auth-service
gita group add frontend web-app mobile-app admin-panel

# Work with groups
gita pull backend
gita ll frontend
```

## Integration with wt

Use gita for overview, wt for detailed work:

```bash
# Check all repos
gita ll

# See one needs work
cd ~/projects/my-repo

# Use wt for feature work
wt switch --create feature/x

# Back to overview
gita ll
```
