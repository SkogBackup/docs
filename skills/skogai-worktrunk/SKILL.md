---
name: worktrunk
description: Use when working with git worktrees (wt), managing submodules across branches, git-flow workflows, or multi-repo management (gita). Covers worktrunk configuration, hook automation, and when to use wt vs gita for different scenarios.
---

# Worktrunk + Gita

Together, these tools replace most git workflows:
- **wt (worktrunk)**: Single repo, multiple worktrees - work on many branches simultaneously
- **gita**: Multiple repos, unified operations - manage entire ecosystems

## Core Commands

### Worktrunk (wt) - Single Repo Worktree Management

**Essential commands:**
```bash
wt list                    # List all worktrees and branches
wt switch <branch>         # Switch to existing worktree
wt switch --create <name>  # Create new worktree from current branch
wt merge [target]          # Merge current worktree back to target (default: main/develop)
wt remove <branch>         # Remove worktree and optionally branch
```

**Configuration commands:**
```bash
wt config show            # Show config files and locations
wt config create          # Create user config (~/.config/worktrunk/config.toml)
```

**Workflow commands (wt step):**
```bash
wt step commit            # Commit with LLM-generated message
wt step push <target>     # Push changes to target branch
wt step rebase <target>   # Rebase onto target
wt step post-create       # Manually run post-create hook
wt step pre-merge         # Manually run pre-merge hook
```

### Gita - Multi-Repo Management

**Essential commands:**
```bash
gita ll                   # List all managed repos with status
gita st                   # Show git status across all repos
gita add <path>           # Add repo(s) to gita management
gita pull                 # Pull all repos (or specific ones)
gita push                 # Push all repos
gita fetch                # Fetch all repos
```

**Organization commands:**
```bash
gita group add <name> <repos>   # Create repo group
gita group ls                   # List all groups
gita ll <group>                 # List repos in group
```

**Operations across repos:**
```bash
gita super <git-command>        # Run arbitrary git command on all repos
gita shell <shell-command>      # Run shell command on all repos
```

## When to Use Which

**Use wt (worktrunk):**
- ✅ Working on multiple branches of ONE repo simultaneously
- ✅ Git-flow workflows (feature/release/hotfix branches)
- ✅ Projects with submodules that need isolation per branch
- ✅ Need to switch between branches without stashing

**Use gita:**
- ✅ Managing MULTIPLE related repositories
- ✅ Checking status across many repos
- ✅ Syncing (pull/push) multiple repos at once
- ✅ Running commands across repo groups

**Use both together:**
- Main project with submodules (wt for main, gita for overview)
- Monorepo ecosystem (wt for features, gita for related services)

## Basic Workflows

### Worktrunk: Feature Branch Workflow

```bash
# Start new feature
wt switch --create feature/my-feature

# Work is isolated in new worktree (typically ~/dev/feature/my-feature)
cd ~/dev/feature/my-feature
# ... make changes ...
git commit -m "changes"

# Merge back to develop
wt merge develop

# Clean up merged worktrees
wt remove feature/my-feature
```

### Gita: Multi-Repo Status Check

```bash
# Add repos to gita
gita add ~/projects/main-app ~/projects/lib1 ~/projects/lib2

# Check status of all
gita ll

# Pull all repos
gita pull

# Check which have uncommitted changes
gita st

# Run custom command across all
gita super git log -1 --oneline
```

## Available Documentation

- **SKILL.md**: This file - configuration workflows and common patterns
- **reference/README.md**: Features, installation, examples, FAQ
- **reference/*.md**: Detailed configuration and hook specifications
- **Completion files**: Full command syntax
  - `/home/skogix/.local/src/argc-completions/completions/wt.sh`
  - `/home/skogix/.local/src/argc-completions/completions/gita.sh`

## Two Types of Configuration

Worktrunk uses two separate config files with different scopes and behaviors:

### User Config (`~/.config/worktrunk/config.toml`)
- **Scope**: Personal preferences for the individual developer
- **Location**: `~/.config/worktrunk/config.toml` (never checked into git)
- **Contains**: LLM integration, worktree path templates, approved commands
- **Permission model**: Always propose changes and get consent before editing
- **See**: `reference/user-config.md` for detailed guidance

### Project Config (`.config/wt.toml`)
- **Scope**: Team-wide automation shared by all developers
- **Location**: `<repo>/.config/wt.toml` (checked into git)
- **Contains**: Hooks for worktree lifecycle (post-create, pre-merge, etc.)
- **Permission model**: Proactive (create directly, changes are reversible via git)
- **See**: `reference/project-config.md` for detailed guidance

## Determining Which Config to Use

When a user asks for configuration help, determine which type based on:

**User config indicators**:
- "set up LLM" or "configure commit generation"
- "change where worktrees are created"
- "customize commit message templates"
- Affects only their environment

**Project config indicators**:
- "set up hooks for this project"
- "automate npm install"
- "run tests before merge"
- Affects the entire team

**Both configs may be needed**: For example, setting up LLM integration requires user config, but automating quality checks requires project config.

## Core Workflows

### Setting Up LLM Integration (User Config)

Most common request. Follow this sequence:

1. **Check if LLM tool exists**
   ```console
   which llm  # or: which aichat
   ```

2. **If not installed, guide installation (don't run it)**
   ```console
   uv tool install -U llm
   ```

3. **Guide API key setup (don't run it)**
   ```console
   llm install llm-anthropic
   llm keys set anthropic
   llm models default claude-haiku-4-5-20251001
   ```

4. **Propose config change**
   ```toml
   [commit-generation]
   command = "llm"
   ```
   Ask: "Should I add this to your config?"

5. **After approval, apply**
   - Check if config exists: `wt config list`
   - If not, guide through `wt config create`
   - Read, modify, write preserving structure

6. **Suggest testing**
   ```console
   llm "say hello"
   wt merge  # in a repo with uncommitted changes
   ```

**See `reference/user-config.md` for complete details.**

### Setting Up Project Hooks (Project Config)

Common request for workflow automation. Follow discovery process:

1. **Detect project type**
   ```console
   ls package.json Cargo.toml pyproject.toml
   ```

2. **Identify available commands**
   - For npm: Read `package.json` scripts
   - For Rust: Common cargo commands
   - For Python: Check pyproject.toml

3. **Design appropriate hooks**
   - Dependencies (fast, must complete) → `post-create`
   - Tests/linting (must pass) → `pre-commit` or `pre-merge`
   - Long builds → `post-start`

4. **Validate commands work**
   ```console
   npm run lint  # verify exists
   which cargo   # verify tool exists
   ```

5. **Create `.config/wt.toml`**
   ```toml
   # Install dependencies when creating worktrees
   post-create = "npm install"

   # Validate code quality before committing
   pre-commit = ["npm run lint", "npm run typecheck"]

   # Run tests before merging
   pre-merge = "npm test"
   ```

6. **Add comments explaining choices**

7. **Suggest testing**
   ```console
   wt switch --create test-hooks
   ```

**See `reference/project-config.md` for complete details.**

## Permission Models

### User Config: Conservative
- **Never edit without consent** - Always show proposed change and wait for approval
- **Never install tools** - Provide commands for users to run themselves
- **Preserve structure** - Keep existing comments and organization
- **Validate first** - Ensure TOML is valid before writing

### Project Config: Proactive
- **Create directly** - Changes are versioned, easily reversible
- **Validate commands** - Check commands exist before adding
- **Explain choices** - Add comments documenting why hooks exist
- **Warn on danger** - Flag destructive operations before adding

## Common Tasks Reference

### User Config Tasks
- Set up LLM integration → `reference/user-config.md#llm-setup`
- Customize worktree paths → `reference/user-config.md#worktree-paths`
- Custom commit templates → `reference/user-config.md#templates`
- Troubleshoot LLM issues → `reference/user-config.md#troubleshooting`

### Project Config Tasks
- Set up hooks for new project → `reference/project-config.md#new-project`
- Add hook to existing config → `reference/project-config.md#add-hook`
- Use template variables → `reference/project-config.md#variables`
- Convert command formats → `reference/project-config.md#formats`
- Troubleshoot hook execution → `reference/project-config.md#troubleshooting`

## Key Commands

```console
# View all configuration
wt config list

# Create initial user config
wt config create

# LLM setup guide
wt config --help
```

## Common Patterns

### Submodule Workflows (Complete Lifecycle)

Projects with git submodules need **both** initialization and cleanup hooks.

**Problem:** New worktrees have empty submodule directories. Merging without cleanup creates dirty submodule references.

**Solution:** Complete submodule lifecycle management

```toml
# .config/wt.toml
# Initialize submodules when creating worktrees
post-create = "git submodule update --init --recursive"

# Clean submodule state before merging
pre-merge = "git submodule deinit --all"
```

**Why both hooks?**
- `post-create`: Ensures fresh submodules in every worktree (avoid manual `git submodule update`)
- `pre-merge`: Deinitializes submodules before merge (ensures clean merge, no dirty references)

**Real-world example** (from skogai project):
```toml
post-create = [
    "git submodule update --init --recursive",
    "cd tools && argc list@tool > tools.txt",
    "cd tools && argc list@agent > agents.txt",
    "cd tools && argc build",
]

pre-merge = "git submodule deinit --all"
```

### Git-Flow Integration

Worktrunk integrates naturally with git-flow workflows (develop/feature/release/hotfix).

**Standard git-flow setup:**
- **Main branch**: `develop` (not `main` or `master`)
- **Feature branches**: `feature/*`
- **Release branches**: `release/*`
- **Hotfix branches**: `hotfix/*`

**Complete workflow:**
```bash
# Create feature branch from develop
wt switch --create feature/my-feature --force

# Work in isolated worktree (typically $HOME/dev/feature/my-feature)
cd ~/dev/feature/my-feature
# ... make changes ...
git commit -m "feat: add feature"

# Merge back to develop (runs pre-merge hooks)
wt merge develop

# Clean up merged worktrees
wt remove feature/my-feature
```

**With submodules:**
The hooks handle everything automatically:
1. `post-create` initializes submodules in new worktree
2. Work normally (submodules already initialized)
3. `pre-merge` deinits submodules (clean merge)
4. `wt merge` completes (no submodule conflicts)

### Custom Build Systems

Non-standard build tools (argc, task, etc.) can integrate via hooks.

**Pattern: Subdirectory operations**
```toml
post-create = [
    "cd tools && argc list@tool > tools.txt",
    "cd tools && argc build",
]
```

**Pattern: Custom tool validation**
Before adding custom tool to hooks, validate it exists:
```bash
which argc  # verify tool exists
argc --help # verify it works
```

**Pattern: Mixed standard + custom**
```toml
post-create = [
    "git submodule update --init --recursive",  # Standard
    "npm install",                               # Standard
    "cd tools && argc build",                    # Custom
]
```

**Why validate first?** Custom tools might not be available to all developers. Add installation instructions to project README if using non-standard tools.

### Multi-Repo + Submodules Pattern

When managing multiple repos that each have submodules:

**Use gita for overview:**
```bash
# Add all your repos to gita
gita add ~/skogai ~/skogai-tools ~/skogai-docs

# Check status across all
gita ll

# Pull all repos and their submodules
gita super git pull --recurse-submodules
```

**Use wt for feature work:**
```bash
# Work on feature in main repo
cd ~/skogai
wt switch --create feature/new-thing
# Submodules initialized via post-create hook
```

## Loading Additional Documentation

Load **reference/README.md** for general features, installation, commands, and examples.

Load **reference files** for detailed configuration, hook specifications, and troubleshooting.

Find specific sections with grep:
```console
grep -A 20 "## Installation" reference/README.md
grep -A 20 "## LLM Setup" reference/user-config.md
grep -A 30 "### post-create" reference/project-config.md
```
