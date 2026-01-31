---
name: working-with-claude-code
description: Use when working with Claude Code CLI, plugins, hooks, MCP servers, skills, configuration, or any Claude Code feature - provides comprehensive official documentation for all aspects of Claude Code
allowed-tools: [Read, Grep, Bash]
---

# Working with Claude Code

## Overview

This skill provides complete, authoritative documentation for Claude Code directly from docs.claude.com. Instead of guessing about configuration paths, API structures, or feature capabilities, read the official docs stored in this skill's references directory.

## When to Use

Use this skill when:
- Creating or configuring Claude Code plugins
- Setting up MCP servers
- Working with hooks (pre-commit, session-start, etc.)
- Writing or testing skills
- Configuring Claude Code settings
- Troubleshooting Claude Code issues
- Understanding CLI commands
- Setting up integrations (VS Code, JetBrains, etc.)
- Configuring networking, security, or enterprise features

## Quick Reference

| Task | Read This File |
|------|---------------|
| Create a plugin | `claude-code/plugins.md` |
| Set up MCP server | `claude-code/mcp.md` or `agents-and-tools/mcp-connector.md` |
| Configure hooks | `claude-code/hooks.md` |
| Write a skill | `claude-code/skills.md` and `agents-and-tools/agent-skills/best-practices.md` |
| SDK reference | `agent-sdk/python.md` or `agent-sdk/typescript.md` |
| Tool implementation | `agents-and-tools/tool-use/implement-tool-use.md` |
| Getting started | `claude-code/quickstart.md` or `claude-code/overview.md` |
| Migration guide | `claude-code/migration-guide.md` |

## Documentation Organization

Documentation is organized in `references/` mirroring the platform.claude.com URL structure:

```
references/
├── claude-code/              # Claude Code CLI documentation
│   ├── overview.md
│   ├── quickstart.md
│   ├── plugins.md
│   ├── skills.md
│   ├── hooks.md
│   ├── slash-commands.md
│   ├── mcp.md
│   ├── permissions.md
│   ├── sessions.md
│   ├── cost-tracking.md
│   ├── todo-tracking.md
│   ├── file-checkpointing.md
│   ├── modifying-system-prompts.md
│   ├── streaming-vs-single-mode.md
│   ├── structured-outputs.md
│   ├── subagents.md
│   └── migration-guide.md
│
├── agent-sdk/                # Agent SDK documentation
│   ├── python.md
│   ├── typescript.md
│   ├── typescript-v2-preview.md
│   ├── custom-tools.md
│   ├── hosting.md
│   └── secure-deployment.md
│
├── agents-and-tools/         # Tools and MCP connectors
│   ├── agent-skills/
│   │   └── best-practices.md
│   ├── tool-use/
│   │   ├── implement-tool-use.md
│   │   ├── programmatic-tool-calling.md
│   │   ├── fine-grained-tool-streaming.md
│   │   ├── bash-tool.md
│   │   ├── code-execution-tool.md
│   │   ├── computer-use-tool.md
│   │   ├── text-editor-tool.md
│   │   ├── tool-search-tool.md
│   │   ├── memory-tool.md
│   │   ├── web-fetch-tool.md
│   │   └── web-search-tool.md
│   ├── mcp-connector.md
│   └── remote-mcp-servers.md
│
├── build-with-claude/        # Building guides (prompt engineering, etc.)
│   └── ...
│
└── resources/                # Prompt library and use case guides
    └── prompt-library/
        └── ...

```

### Currently Fetching

Sections automatically downloaded from platform.claude.com:
- `claude-code/` - CLI tool documentation
- `agent-sdk/` - SDK reference (Python/TypeScript)
- `agents-and-tools/` - Tool use, skills, MCP connectors
- `build-with-claude/` - Building guides (prompt engineering, streaming, etc.)
- `resources/` - Prompt library and use case guides

### Available but Not Currently Fetched

To expand coverage, add to the pattern in `scripts/update_docs.js`:
- `/docs/en/api/` - API reference (messages, batches, models, admin)
- `/docs/en/about-claude/` - General info (models, pricing, glossary)
- `/docs/en/test-and-evaluate/` - Testing and evaluation guides
- `/docs/en/release-notes/` - Release notes

**Note:** The script automatically creates subdirectories based on the URL path structure.

## Workflow

### For Specific Questions

1. Identify the relevant documentation file from the list above
2. Use Read tool to load: `@references/section/filename.md`
3. Find the answer in the official documentation
4. Apply the solution

**Example:**
```
User: "How do I create a Claude Code plugin?"
→ Read @references/claude-code/plugins.md
→ Follow the official plugin creation steps
```

### For Broad Topics

When exploring a topic, start with the overview document, then drill into specific files:

- **Extending Claude Code**: Start with `claude-code/plugins.md`, `claude-code/skills.md`, or `claude-code/mcp.md`
- **Tool Development**: Check `agents-and-tools/tool-use/` directory
- **SDK Usage**: Browse `agent-sdk/` directory
- **Prompt Engineering**: Explore `build-with-claude/` and `resources/prompt-library/`

### For Uncertain Topics

Use Grep tool to search across all documentation:

```bash
pattern: "search term"
path: ~/.claude/skills/working-with-claude-code/references/
```

## Updating Documentation

The skill includes `scripts/update_docs.js` to fetch the latest documentation from docs.claude.com.

Run when:
- Documentation seems outdated
- New Claude Code features are released
- Official docs have been updated

```bash
node ~/.claude/skills/working-with-claude-code/scripts/update_docs.js
```

The script:
1. Fetches llms.txt from docs.claude.com
2. Extracts all Claude Code documentation URLs
3. Downloads each page to `references/`
4. Reports success/failures

## Common Patterns

### Plugin Development

Read `claude-code/plugins.md` for complete plugin development guide.

### MCP Server Setup

Read `claude-code/mcp.md` for SDK integration, or `agents-and-tools/mcp-connector.md` for connector setup. For remote servers, see `agents-and-tools/remote-mcp-servers.md`.

### Hook Configuration

Read `claude-code/hooks.md` for overview and implementation details.

### Skill Creation

Read `claude-code/skills.md` for the authoring guide, then `agents-and-tools/agent-skills/best-practices.md` for optimization tips.

### Agent SDK Usage

- **Python**: Read `agent-sdk/python.md`
- **TypeScript**: Read `agent-sdk/typescript.md` or `agent-sdk/typescript-v2-preview.md`
- **Custom Tools**: Read `agent-sdk/custom-tools.md`
- **Hosting**: Read `agent-sdk/hosting.md` and `agent-sdk/secure-deployment.md`

### Tool Development

Browse `agents-and-tools/tool-use/` for specific tools:
- `implement-tool-use.md` - General tool implementation
- `bash-tool.md`, `web-fetch-tool.md`, etc. - Specific tool references

## What This Skill Does NOT Do

- This skill provides **documentation access**, not procedural guidance
- For workflows on **how to build** plugins/skills, use the `extending-claude-code` skill (when available)
- This skill is a **reference library**, not a tutorial

## Red Flags

If you find yourself:
- Guessing about SDK APIs → Read `agent-sdk/python.md` or `agent-sdk/typescript.md`
- Speculating about tool implementation → Read `agents-and-tools/tool-use/implement-tool-use.md`
- Unsure about hook configuration → Read `claude-code/hooks.md`
- Making assumptions about MCP setup → Read `claude-code/mcp.md` or `agents-and-tools/mcp-connector.md`
- Guessing about permissions → Read `claude-code/permissions.md`
- Wondering about deployment → Read `agent-sdk/hosting.md` or `agent-sdk/secure-deployment.md`

**Always consult the official documentation before guessing.**
