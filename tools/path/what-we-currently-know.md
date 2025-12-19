# path - what we currently know

## current state (2025-11-13)

### the problem we solved

claude (AI agents) run in non-interactive bash shells and don't inherit the user's shell environment automatically. tools managed by version managers (like nvm for node) aren't in the default PATH.

### the solution: SKOGAI_PATH

**concept:** environment variable containing bin directories that AI agents need

**current implementation:** manually set in zshrc for testing
```bash
export SKOGAI_PATH="/home/skogix/.nvm/versions/node/v25.1.0/bin:/home/skogix/.local/bin/"
```

**how claude uses it:**
```bash
export PATH="$SKOGAI_PATH:$PATH"
node --version  # works
npm install     # works
```

### what's in SKOGAI_PATH

currently contains:
- `/home/skogix/.nvm/versions/node/v25.1.0/bin` - nvm-managed node/npm
- `/home/skogix/.local/bin/` - local user binaries

(potentially other tool paths in the future)

### verification

```bash
# check what's available
echo "$SKOGAI_PATH"

# verify it's set
printenv | grep SKOGAI_PATH

# test usage
export PATH="$SKOGAI_PATH:$PATH" && which node && which npm
```

## the pattern for claude

**always prepend SKOGAI_PATH to PATH when using tools:**

```bash
# for node/npm
export PATH="$SKOGAI_PATH:$PATH"
npm install
npm run build

# for any tool that might be in SKOGAI_PATH
export PATH="$SKOGAI_PATH:$PATH"
some-tool --version
```

**don't:**
- investigate where tools are installed
- try to detect versions
- compute paths dynamically
- hardcode paths like `/home/skogix/.nvm/versions/node/v25.1.0/bin`

**do:**
- trust the environment variable
- use `$SKOGAI_PATH` directly
- prepend to PATH before using tools

## related: skogcli environment system

**discovered:** environment variables are managed via skogcli with namespaces

**namespaces:**
- `skogai.env` - shared/global variables
- `claude.env` - claude-specific variables
- `amy.env`, `goose.env`, etc. - other agents
- service-specific: `github.env`, `cloudflare.env`, etc.

**how it works:**
```bash
# view config
skogcli config get claude.env
skogcli config get skogai.env

# export to environment
skogcli config export-env --namespace skogai,claude

# list all env configs
skogcli config list | grep env
```

**examples of SKOGAI_* variables available to claude:**
```bash
SKOGAI=/home/skogix/skogai
SKOGAI_PATH=/home/skogix/.nvm/versions/node/v25.1.0/bin:/home/skogix/.local/bin/
SKOGAI_NVM_BIN=/home/skogix/.nvm/versions/node/v25.1.0/bin
SKOGAI_AGENT_NAME=claude
SKOGAI_CLAUDE_HOME=/home/skogix/claude
SKOGAI_CONFIG=/home/skogix/skogai/config
SKOGAI_SRC=/home/skogix/.local/src
SKOGAI_WORKTREE_PATH=/home/skogix/worktrees
# ... and many more
```

**key insight:** claude gets environment variables automatically - no setup needed in claude code

## future plan

**foo.path config type:**
- similar to `foo.env` but for PATH management
- automatically concatenates paths with `:`
- example: `skogai.path` would generate `SKOGAI_PATH` variable
- allows declarative PATH management instead of manual zshrc configuration

**when implemented:**
- the usage pattern stays the same (`export PATH="$SKOGAI_PATH:$PATH"`)
- just moves from manual zshrc setup to skogcli-managed config
- documentation remains accurate

## what we learned

1. **version managers are complex** - nvm stores versions at dynamic paths, npm needs node in PATH
2. **environment variables solve it cleanly** - instead of detection logic, just use what's provided
3. **SKOGAI_PATH is the pattern** - single variable containing all tool paths needed by AI agents
4. **trust the environment** - don't investigate, don't compute, just use what's set
5. **skogcli manages configs** - namespaced environment variables, clean separation per agent/service

## what remains unknown

- exact implementation of `foo.path` config type
- whether other tools besides node/npm will need SKOGAI_PATH
- whether we need separate PATH variables or one combined SKOGAI_PATH
- how to handle tools that need more than just PATH (env vars, config files, etc.)

## see also

- @docs/tools/javascript/node.md - (placeholder for future node-specific docs)
- @docs/tools/javascript/npm.md - (placeholder for future npm-specific docs)
- skogcli config documentation (when it exists)
