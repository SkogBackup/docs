---
title: Documentation Landscape
type: note
permalink: context/documentation-landscape
---

# Documentation Landscape

## Current Documentation Structure

### Root Level
- `CLAUDE.md` - Main Claude configuration/instructions
- `readme.md` - Project readme

### docs/ Directory Structure

#### Core Documentation
- `definitions.md` - Project definitions and terminology
- `handover.md` - Handover documentation
- `plan.md` - Main planning document
- `starting-context.md` - Initial context setup
- `todo.md` - Task management
- `user.md` - User documentation
- `skogix.md` - Skogix-specific documentation

#### Claude-Specific Documentation (`docs/claude/`)
**Core Files:**
- `CLAUDE.md` - Main Claude instructions
- `CLAUDE-GOALS.md` - Claude goals and objectives
- `CLAUDE-ROLES-AND-RESPONSIBILITY.md` - Role definitions
- `CLAUDE-SYSTEMPROMPT.md` - System prompt documentation
- `CLAUDE-CERTAINTY.md` - Certainty handling
- `CLAUDE-PLACEHOLDER.md` - Placeholder system docs

**Configuration Files:**
- `code-style.md` - Code style guidelines
- `commands.md` - Available commands
- `hooks.md` - Hook system documentation
- `current-prompts.txt` - Current prompt configurations
- Various `.conf` files for prompt configurations

**Technical Documentation:**
- `placeholder-system.md` - Placeholder system details
- `uncertainty-principle.md` - Uncertainty handling principles
- `IMPORTANT-claude-code-restrictions.md` - Restrictions and limitations

**Persona Documentation (`docs/claude/persona/`):**
- `claude-memory-block-01-archaeological-knowledge-recoverer.md`
- `claude-memory-block-01-technical-architecture-understanding.md`

**System Prompt Replacements (`docs/claude/system-prompt-replacements/`):**
- Multiple text files (a1.txt through a5.txt, b1.txt through b5.txt)

#### Help Documentation (`docs/help/`)
- `git-flow.help` - Git flow help
- `git-flow.feature.help` - Git flow feature help
- `git-flow.release.help` - Git flow release help

#### Planning Documentation (`docs/plans/`)
- `add-new-context-section.md` - Plan for adding new context sections

#### Domain-Specific Documentation
**Supabase (`docs/supabase/`):**
- `context7-research.md` - Context7 research
- `current-knowledge.md` - Current knowledge state
- `supabase-capabilities.md` - Supabase capabilities

**Claude Code (`docs/claude-code/`):**
- `prompt-architect.conf` - Prompt architecture configuration

#### Tool-Specific Documentation
**Argc Documentation:**
- `argc-documentation.md` - Argc tool documentation
- `argc-users-guide.md` - Argc user guide

## Documentation Patterns Observed

1. **Hierarchical Organization**: Documentation is well-organized in logical directories
2. **Multiple Formats**: Mix of .md, .conf, .txt, and .help files
3. **Domain Separation**: Clear separation between Claude docs, Supabase docs, etc.
4. **Configuration Management**: Extensive prompt and configuration documentation
5. **Help System**: Dedicated help files for tools
6. **Planning Integration**: Plans are documented alongside implementation docs

## Documentation Gaps/Opportunities

1. **Index/Navigation**: No central index or navigation document
2. **Cross-References**: Limited cross-referencing between related docs
3. **Versioning**: No clear versioning strategy for documentation
4. **API Documentation**: No clear API or interface documentation
5. **Examples**: Limited example documentation

## Access Patterns

- Root level docs are project-wide
- `docs/claude/` contains all Claude-specific configuration and behavior
- `docs/help/` provides user-facing help content
- `docs/plans/` contains forward-looking planning content
- Domain directories (`docs/supabase/`) contain specialized knowledge