# Hook Types Reference

Worktrunk hook types for automating worktree lifecycle.

## Hook Comparison

| Hook | When | Blocking? | Fail-Fast? | Use Case |
|------|------|-----------|------------|----------|
| `post-create` | After creating worktree | Yes | No | Dependencies, setup |
| `post-start` | When switching to worktree | No | No | Background builds |
| `pre-commit` | Before committing in merge | Yes | Yes | Lint, typecheck |
| `pre-merge` | Before merging to target | Yes | Yes | Tests, validation |
| `post-merge` | After successful merge | Yes | No | Deploy, notify |

## Template Variables

**All hooks:**
- `{{ repo }}` - Repository name
- `{{ branch }}` - Branch name
- `{{ worktree }}` - Worktree path
- `{{ repo_root }}` - Repository root path

**Merge hooks only:** (pre-commit, pre-merge, post-merge)
- `{{ target }}` - Target branch for merge

## Hook Details

### post-create

Runs after creating worktree, blocks until complete.

```toml
post-create = [
    "npm install",
    "npm run db:migrate",
    "git submodule update --init --recursive"
]
```

### post-start

Runs in background after creation, doesn't block.

```toml
post-start = [
    "npm run build",
    "docker-compose up -d"
]
```

### pre-commit

Runs before commit during merge. Fails fast.

```toml
pre-commit = ["npm run lint", "npm run typecheck"]
```

### pre-merge

Runs before merge to target. Fails fast.

```toml
pre-merge = ["npm test", "npm run build"]
```

### post-merge

Runs after successful merge.

```toml
post-merge = "npm run deploy"
```

## Format Options

**Single command:**
```toml
post-create = "npm install"
```

**Multiple commands (array):**
```toml
post-create = ["npm install", "npm run setup"]
```

**Named commands (table):**
```toml
[post-create]
dependencies = "npm install"
database = "npm run db:migrate"
```

## Merge Execution Order

1. Validate clean working tree
2. **pre-commit** (fail-fast)
3. Create commit
4. Switch to main worktree
5. Pull latest
6. **pre-merge** (fail-fast)
7. Merge branch
8. Push to remote
9. **post-merge** (best-effort)
10. Cleanup (delete branch, remove worktree)

## Common Patterns

### Dependencies + Background Build

```toml
post-create = "npm install"      # Blocking
post-start = "npm run build"     # Background
```

### Progressive Validation

```toml
pre-commit = ["npm run lint", "npm run typecheck"]  # Quick
pre-merge = ["npm test", "npm run build"]           # Thorough
```

### Target-Specific Deploy

```toml
post-merge = """
if [ "{{ target }}" = "main" ]; then
    npm run deploy:production
elif [ "{{ target }}" = "staging" ]; then
    npm run deploy:staging
fi
"""
```

### Submodule Lifecycle

```toml
post-create = "git submodule update --init --recursive"
pre-merge = "git submodule deinit --all"
```
