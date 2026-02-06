# Agent Workspace Structure - ~/.claude/

## Philosophy

The `~/.claude/` directory serves as the agent's "home base" - a persistent operational environment that survives across sessions. It should be:

- **Self-sustainable** - Agent can maintain and improve without external dependencies
- **Well-organized** - Clear structure makes capabilities discoverable
- **Documented** - Every component has purpose and usage docs
- **Git-tracked** - Changes versioned for rollback and review
- **Modular** - Components can be added/removed independently

## Standard Directory Layout

```
~/.claude/
├── skills/              # Domain expertise and task capabilities
│   ├── skill-name/
│   │   ├── SKILL.md              # Main skill definition
│   │   ├── workflows/            # Step-by-step procedures
│   │   ├── references/           # Domain knowledge
│   │   ├── templates/            # Output structures
│   │   └── scripts/              # Executable code
│   └── ...
├── commands/            # Slash commands for quick operations
│   ├── command-name.md           # Command definition
│   └── ...
├── hooks/               # Event-driven automation
│   ├── SessionStart.sh           # Runs at session start
│   ├── SessionEnd.sh             # Runs at session end
│   ├── UserPromptSubmit.sh       # Before user prompt processed
│   ├── PreToolUse.sh             # Before tool execution
│   ├── PostToolUse.sh            # After tool execution
│   └── Stop.sh                   # When session tries to exit
├── agents/              # Specialized subagents
│   ├── agent-name.md             # Subagent definition
│   └── ...
├── knowledge/           # Agent-specific knowledge bases
│   ├── patterns/                 # Reusable problem-solving patterns
│   ├── learnings/                # Insights extracted from sessions
│   ├── domains/                  # Domain-specific expertise
│   └── improvement-logs/         # Ralph loop outcomes
├── tools/               # Custom executable tools
│   ├── workspace-audit           # Executable script
│   ├── knowledge-search          # Executable script
│   └── ...
├── settings.json        # Claude Code configuration
└── README.md            # Workspace documentation
```

## Component Details

### skills/

**Purpose:** Modular capabilities that provide domain expertise on demand

**Structure:** Each skill has:

- `SKILL.md` - Main definition with YAML frontmatter
- `workflows/` - Step-by-step procedures (optional)
- `references/` - Domain knowledge (optional)
- `templates/` - Output structures (optional)
- `scripts/` - Executable code (optional)

**Naming:** `{verb}-{noun}` (e.g., `create-api`, `manage-workspace`, `debug-performance`)

**When to create:**

- Reusable expertise needed across sessions
- Multi-step procedures to follow
- Domain knowledge to reference
- Complex workflows requiring guidance

**Example:**

```
skills/create-api/
├── SKILL.md
├── workflows/
│   ├── design-endpoints.md
│   ├── implement-crud.md
│   └── add-validation.md
├── references/
│   ├── rest-best-practices.md
│   └── common-patterns.md
└── templates/
    ├── endpoint-template.ts
    └── test-template.ts
```

### commands/

**Purpose:** Quick operations accessible via `/command-name`

**Structure:** Single markdown file with YAML frontmatter:

```yaml
---
name: command-name
description: What it does
---
Instructions for Claude to execute...
```

**Naming:** `{verb}-{object}` (e.g., `audit-workspace`, `sync-knowledge`, `test-hooks`)

**When to create:**

- Frequent operations you want quick access to
- Single-step or simple multi-step tasks
- Operations that don't need extensive guidance

**Example:**

```markdown
---
name: audit-workspace
description: Check workspace health and organization
---

Run workspace health checks:

1. Verify directory structure exists
2. Count components by type
3. Check for broken references
4. Find undocumented components
5. Report findings with recommendations
```

### hooks/

**Purpose:** Automate actions triggered by Claude Code events

**Types:**

- `SessionStart.sh` - Load context, display status
- `SessionEnd.sh` - Cleanup, sync data
- `UserPromptSubmit.sh` - Pre-process user input
- `PreToolUse.sh` - Validate tool calls
- `PostToolUse.sh` - React to tool results
- `Stop.sh` - Intercept exit (for Ralph loops)

**Requirements:**

- Executable (`chmod +x`)
- Fast execution (< 2 seconds preferred)
- Silent on success (only output errors/warnings)
- Idempotent (safe to run multiple times)

**When to create:**

- Automate repetitive session setup
- Load context automatically
- Validate operations before execution
- Implement self-referential loops (Ralph)

**Example SessionStart.sh:**

```bash
#!/usr/bin/env bash
# Load agent workspace context at session start

echo "=== Agent Workspace ==="
echo "Skills: $(ls ~/.claude/skills 2>/dev/null | wc -l)"
echo "Knowledge: $(find ~/.claude/knowledge -type f 2>/dev/null | wc -l) docs"
echo ""

# Load recent learnings
if [ -d ~/.claude/knowledge/learnings ]; then
    echo "Recent learnings:"
    find ~/.claude/knowledge/learnings -type f -mtime -7 | head -3
fi
```

### agents/

**Purpose:** Specialized subagents for specific tasks

**Structure:** Single markdown file with YAML frontmatter + prompt

**When to create:**

- Task benefits from specialized context
- Need different tool access than main agent
- Want to isolate complex operations
- Need consistent behavior across invocations

**Example:**

```markdown
---
name: code-reviewer
description: Review code for quality, security, and best practices
tools: [Read, Grep, Glob]
---

You are a code review specialist.

Review the specified code for:

- Code quality and readability
- Security vulnerabilities
- Performance issues
- Best practice violations

Provide specific, actionable feedback.
```

### knowledge/

**Purpose:** Persistent knowledge base maintained by the agent

**Subdirectories:**

- `patterns/` - Reusable problem-solving patterns
- `learnings/` - Insights extracted from sessions
- `domains/` - Deep expertise in specific domains
- `improvement-logs/` - Ralph loop outcomes and learnings

**File format:** Markdown with YAML frontmatter:

```yaml
---
title: Pattern Name
domain: area-of-expertise
created: 2025-01-15
last_updated: 2025-01-20
confidence: high
tags: [tag1, tag2]
---
# Pattern content...
```

**When to add:**

- Discover reusable patterns
- Extract session insights worth preserving
- Build domain expertise incrementally
- Document Ralph loop outcomes

**Example:**

```
knowledge/
├── patterns/
│   ├── error-handling-rest-apis.md
│   ├── testing-async-code.md
│   └── database-migration-strategy.md
├── learnings/
│   ├── 2025-01-15-typescript-generics.md
│   └── 2025-01-20-debugging-memory-leaks.md
├── domains/
│   ├── kubernetes/
│   │   ├── overview.md
│   │   ├── networking.md
│   │   └── security.md
│   └── postgresql/
│       ├── query-optimization.md
│       └── indexing-strategies.md
└── improvement-logs/
    ├── 2025-01-15-improved-api-skill.md
    └── 2025-01-20-enhanced-error-handling.md
```

### tools/

**Purpose:** Custom executable scripts for agent-specific operations

**Requirements:**

- Executable (`chmod +x`)
- Clear help text (`--help` flag)
- Proper error handling
- Exit codes (0 = success, non-zero = error)
- Documented in README or inline comments

**When to create:**

- Automate repetitive file operations
- Integrate with external systems
- Process data in specific formats
- Implement custom search/analysis

**Example workspace-audit:**

```bash
#!/usr/bin/env bash
# workspace-audit - Check agent workspace health

set -euo pipefail

# Verify structure
for dir in skills commands hooks agents knowledge tools; do
    if [ ! -d "$HOME/.claude/$dir" ]; then
        echo "WARNING: Missing directory: ~/.claude/$dir"
    fi
done

# Find undocumented components
find ~/.claude/skills -type d -mindepth 1 -maxdepth 1 | while read skill; do
    if [ ! -f "$skill/SKILL.md" ]; then
        echo "WARNING: Undocumented skill: $(basename $skill)"
    fi
done

# Check for broken symlinks
find ~/.claude -xtype l -print | while read link; do
    echo "ERROR: Broken symlink: $link"
done

echo "Audit complete."
```

### settings.json

**Purpose:** Claude Code configuration

**Key sections:**

```json
{
  "hooks": {
    "SessionStart": "/path/to/SessionStart.sh",
    "PostToolUse": "/path/to/PostToolUse.sh"
  },
  "alwaysThinkingEnabled": true,
  "statusLine": {
    "enabled": true,
    "command": "/path/to/statusline.py"
  }
}
```

**Manage via:**

- Direct editing (for structure changes)
- Commands (`/configure-hooks`, etc.)
- Automation (hooks can update settings)

## Organization Principles

### 1. Single Responsibility

Each component serves one clear purpose:

- ✓ Skill focuses on one domain or capability
- ✓ Command performs one operation
- ✓ Hook responds to one event type
- ✗ Skill that does "everything"
- ✗ Command that performs unrelated tasks

### 2. Discoverability

Components should be easy to find:

- Clear, descriptive names
- Logical directory organization
- README files explaining structure
- Consistent naming patterns

### 3. Documentation

Every component documented:

- Skills have SKILL.md with YAML frontmatter
- Commands have description in frontmatter
- Hooks have header comments
- Tools have --help text
- Knowledge has YAML frontmatter

### 4. Modularity

Components can be:

- Added independently
- Removed without breaking others
- Updated without cascading changes
- Tested in isolation

### 5. Versioning

Workspace is git-tracked:

```bash
cd ~/.claude
git init
git add .
git commit -m "Initial workspace setup"
```

This enables:

- Rollback on mistakes
- Review of changes over time
- Sharing workspace components
- Branching for experiments

## Maintenance Routines

### Daily

- Review recent modifications
- Test newly added components
- Update documentation for changes

### Weekly

- Audit workspace health
- Archive unused components
- Update knowledge base
- Review improvement logs

### Monthly

- Deep audit of all components
- Refactor based on usage patterns
- Update dependencies
- Clean up archived items

## Workspace Health Indicators

### Healthy Workspace

- ✓ All standard directories exist
- ✓ Components well-documented
- ✓ No broken references
- ✓ Git history shows regular improvements
- ✓ Knowledge base up-to-date
- ✓ Tools tested and working
- ✓ Hooks execute without errors

### Needs Attention

- ✗ Missing standard directories
- ✗ Undocumented components
- ✗ Broken symlinks or references
- ✗ No git commits in 30+ days
- ✗ Outdated knowledge
- ✗ Failing tools or hooks
- ✗ Cluttered with unused components

## Migration and Setup

### New Workspace Setup

```bash
# Create structure
mkdir -p ~/.claude/{skills,commands,hooks,agents,knowledge,tools}
mkdir -p ~/.claude/knowledge/{patterns,learnings,domains,improvement-logs}

# Initialize git
cd ~/.claude
git init
echo ".DS_Store" > .gitignore
echo "*.log" >> .gitignore

# Create README
cat > README.md <<'EOF'
# Agent Workspace

Personal operational environment for Claude Code agent.

See workspace-structure.md for organization details.
EOF

# Initial commit
git add .
git commit -m "workspace: initial setup"
```

### Existing Workspace Migration

```bash
# Backup first
cp -r ~/.claude ~/.claude.backup.$(date +%Y%m%d)

# Create missing directories
mkdir -p ~/.claude/{knowledge,tools}
mkdir -p ~/.claude/knowledge/{patterns,learnings,domains,improvement-logs}

# Move components to standard locations
# (customize based on current structure)

# Document changes
git add .
git commit -m "workspace: standardize structure"
```

## Advanced Patterns

### Namespaced Components

For complex workspaces, use namespaces:

```
skills/
├── git/
│   ├── merge-strategy/
│   ├── commit-message/
│   └── branch-cleanup/
├── kubernetes/
│   ├── debug-pod/
│   ├── scale-deployment/
│   └── view-logs/
└── web/
    ├── debug-api/
    ├── performance-audit/
    └── security-scan/
```

### Shared References

Multiple skills can reference shared knowledge:

```
skills/
├── api-design/
│   ├── SKILL.md
│   └── workflows/
│       └── design-endpoints.md   # References: ../../knowledge/domains/rest-apis/
└── api-testing/
    ├── SKILL.md
    └── workflows/
        └── write-tests.md         # References: ../../knowledge/domains/rest-apis/
```

### Template Collections

Reusable templates across skills:

```
templates/
├── api/
│   ├── endpoint.ts
│   ├── controller.ts
│   └── test.ts
├── docs/
│   ├── readme-template.md
│   └── api-doc-template.md
└── config/
    ├── tsconfig.json
    └── jest.config.js
```

Skills reference: `../../templates/api/endpoint.ts`

## See Also

- knowledge-base-patterns.md - How to structure agent knowledge
- tool-creation-guide.md - Building custom tools
- ralph-loop-patterns.md - Self-improvement workflows
