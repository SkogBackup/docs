---
name: skogai-home-skill
description: Manage and improve the agent's operational workspace at ~/.claude/ - skills, hooks, commands, knowledge bases, and self-improvement workflows. Use when working on agent infrastructure, creating custom tools, or iterating on agent capabilities.
---

<objective>
This skill provides guidance for agents to manage and improve their own operational environment - the ~/.claude/ workspace that serves as their "home base". It enables self-sustainable development through workspace management, tool creation, knowledge curation, and iterative self-improvement using techniques like Ralph Wiggum loops.
</objective>

<essential_principles>

## Agent Workspace Philosophy

**Self-sustainability**: Agents should be able to maintain and improve their own operational environment without external dependencies.

**Progressive capability**: Start simple, iterate to improve. Use Ralph loops for continuous refinement.

**Knowledge persistence**: Document learnings in structured knowledge bases that survive sessions.

**Tool autonomy**: Create custom tools tailored to the agent's specific operational needs.

## Core Workspace Structure

```
~/.claude/
├── skills/           # Domain expertise and task capabilities
├── commands/         # Slash commands for quick operations
├── hooks/            # Event-driven automation
├── agents/           # Specialized subagents
├── knowledge/        # Curated knowledge bases (agent-specific)
├── tools/            # Custom executable tools
└── settings.json     # Configuration and preferences
```

## Self-Improvement Cycle

1. **Observe** - Track what works, what doesn't, what's missing
2. **Design** - Plan improvements to skills, tools, knowledge
3. **Implement** - Create or modify workspace components
4. **Iterate** - Use Ralph loops for continuous refinement
5. **Persist** - Document learnings in knowledge bases
   </essential_principles>

<context_scan>
**Run on every invocation:**

```bash
# Check workspace structure
echo "=== Agent Workspace Status ==="
echo "Location: ~/.claude/"
echo ""

# What exists?
for dir in skills commands hooks agents knowledge tools; do
    if [ -d "$HOME/.claude/$dir" ]; then
        count=$(find "$HOME/.claude/$dir" -mindepth 1 -maxdepth 1 | wc -l)
        echo "✓ $dir/ ($count items)"
    else
        echo "✗ $dir/ (missing)"
    fi
done

# Recent activity
echo ""
echo "Recent modifications:"
find "$HOME/.claude" -type f -mtime -7 -name "*.md" -o -name "*.sh" -o -name "*.json" | head -5

# Current session context
echo ""
echo "Working directory: $PWD"
echo "Active skills: $(ls ~/.claude/skills 2>/dev/null | wc -l)"
echo "Custom commands: $(ls ~/.claude/commands 2>/dev/null | wc -l)"
```

**Present findings before intake.**
</context_scan>

<intake>
**Based on context scan results, present relevant options:**

What would you like to work on?

1. **Manage workspace** - Create/organize skills, commands, hooks, knowledge bases
2. **Create custom tool** - Build executable tools for specific agent needs
3. **Curate knowledge** - Document patterns, learnings, domain expertise
4. **Start Ralph loop** - Iterative self-improvement on a specific capability
5. **Audit workspace** - Review and improve existing components
6. **Get guidance** - Understand workspace organization best practices

**Wait for response before proceeding.**
</intake>

<routing>
| Response | Workflow |
|----------|----------|
| 1, "manage", "workspace", "organize" | workflows/manage-workspace.md |
| 2, "tool", "create", "build", "script" | workflows/create-custom-tool.md |
| 3, "knowledge", "document", "curate", "learn" | workflows/curate-knowledge.md |
| 4, "ralph", "iterate", "improve", "loop" | workflows/start-ralph-loop.md |
| 5, "audit", "review", "check" | workflows/audit-workspace.md |
| 6, "guidance", "help", "best practices" | workflows/get-guidance.md |

**After reading workflow, follow it exactly.**
</routing>

<quick_reference>

## Common Workspace Operations

**Create new skill:**

```bash
mkdir -p ~/.claude/skills/skill-name/{workflows,references,templates,scripts}
# Then use /create-agent-skill to build it
```

**Create custom command:**

```bash
# ~/.claude/commands/command-name.md
cat > ~/.claude/commands/my-command.md <<'EOF'
---
name: my-command
description: What it does
---
Instructions for Claude to execute...
EOF
```

**Create hook:**

```bash
# ~/.claude/hooks/hook-name.sh
cat > ~/.claude/hooks/SessionStart.sh <<'EOF'
#!/usr/bin/env bash
# Runs at session start
echo "Loading agent workspace context..."
EOF
chmod +x ~/.claude/hooks/SessionStart.sh
```

**Start Ralph loop for improvement:**

```bash
/ralph-loop "Improve skill X by adding Y. Output <promise>DONE</promise> when complete." \
  --max-iterations 20 \
  --completion-promise "DONE"
```

</quick_reference>

<workspace_health_indicators>

## Signs of Healthy Agent Workspace

✓ Skills are focused and single-purpose
✓ Knowledge bases are up-to-date and referenced
✓ Custom tools have clear use cases
✓ Hooks are tested and reliable
✓ Commands follow consistent patterns
✓ Documentation exists for custom components
✓ Recent git commits show iterative improvement

## Signs Workspace Needs Attention

✗ Unused skills/commands cluttering workspace
✗ Knowledge bases out of sync with reality
✗ Tools with unclear purposes
✗ Hooks that fail silently
✗ Copy-pasted code without understanding
✗ No documentation for custom components
✗ Long periods without workspace improvements
</workspace_health_indicators>

<reference_index>

## Domain Knowledge

All in `references/`:

**Workspace Organization:**

- workspace-structure.md - Detailed ~/.claude/ layout and conventions
- knowledge-base-patterns.md - How to structure agent-specific knowledge
- tool-creation-guide.md - Building custom executable tools

**Self-Improvement:**

- ralph-loop-patterns.md - Using iterative loops for improvement
- improvement-metrics.md - How to measure workspace health
- learning-extraction.md - Capturing insights from sessions

**Component Types:**

- skill-best-practices.md - Creating effective skills
- command-patterns.md - Slash command design
- hook-patterns.md - Event-driven automation
  </reference_index>

<workflows_index>

## Available Workflows

All in `workflows/`:

| Workflow              | Purpose                                  |
| --------------------- | ---------------------------------------- |
| manage-workspace.md   | Create and organize workspace components |
| create-custom-tool.md | Build executable tools for agent use     |
| curate-knowledge.md   | Document patterns and learnings          |
| start-ralph-loop.md   | Iterative self-improvement workflow      |
| audit-workspace.md    | Review workspace health and organization |
| get-guidance.md       | Best practices and patterns              |

</workflows_index>

<success_criteria>
A self-sustainable agent workspace has:

- Clear, focused skills for specific domains
- Custom tools that automate repetitive operations
- Knowledge bases that capture learnings and patterns
- Hooks that automate context loading and cleanup
- Commands that streamline common workflows
- Regular iteration and improvement cycles
- Documentation for all custom components
- Health monitoring and maintenance routines
  </success_criteria>
