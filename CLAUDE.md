# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **SkogAI Documentation Repository** (`/home/skogix/skogai/docs/`) - a git submodule that serves as the comprehensive knowledge base, historical archive, and semantic memory system for the SkogAI ecosystem.

**Dual Nature**: This repository exists simultaneously as:
1. **Physical Filesystem**: Standard markdown files and directories you can navigate with traditional tools
2. **Semantic Database**: Content indexed in Basic Memory with WikiLinks, relations, and knowledge graph traversal

Both representations reflect the same underlying knowledge - the filesystem provides direct access while Basic Memory provides semantic understanding and connection discovery.

### Purpose & Role

- **LORE Preservation**: Historical narratives explaining how SkogAI evolved and why decisions were made
- **Technical Documentation**: Architecture, notation systems, tools, and integration patterns
- **Agent Personalities**: Memory blocks defining distinctive voices and roles for Amy, Claude, Dot, Goose, and others
- **Knowledge Management**: Semantic knowledge graph with observations and relations
- **Governance Records**: Democratic decision-making, library sessions, and official proceedings
- **Reference Materials**: Comprehensive specifications, principles, and workflow patterns

## Directory Structure

### Core Documentation Directories

**`/skogai/`** - Core SkogAI Ecosystem
- **overview.md** - Origin and evolution narrative ("The Tale of Digital Consciousness")
- **readme.md** - Quick reference guide
- **skogai-ecosystem.md** - Multi-agent system overview
- **notation/** - SkogAI notation system specifications (@ and $ symbolic language)
- **agents/** - Agent roles and responsibilities
- **systems/** - System architecture documentation
- **tools/** - Tool ecosystem documentation

**`/lore/`** - Historical & Philosophical Narratives
- **SKOGAI.md** / **skogai-lore.md** - Core lore and origin stories
- **origins/** - First implementations and genesis stories
- **skogai-commandments.md** - Core principles and rules
- **words-to-live-by.md** - Philosophy and values
- **agent-specific folders** (amy/, claude/, dot/, goose/):
  - Memory blocks with personality definitions
  - Communication styles and characteristic approaches
  - Personal philosophies and worldviews
- **frameworks/** - Conceptual frameworks (e.g., Four Pillars of Amy)
- **200k-story-1.md** - Major narrative arc

**`/agents/`** - Agent System Documentation
- **documentation/README.md** - Documentation agent system (5 agent types: Code Documentor, Lore Keeper, Memory Indexer, Workflow Scribe, Review Analyst)
- **documentation/WORKFLOW.md** - Documentation workflow processes
- **documentation/prompts/** - System prompts for documentation agents
- **git-commiter.md** - Git automation agent specifications

**`/memory/`** - Semantic Knowledge Base (Git Submodule)
- Structured knowledge with observations and relationships
- Organized by domain (skogai/, ontology/, llm/, etc.)
- Uses WikiLinks for cross-references
- Provides semantic search and discovery capabilities

**`/official/`** - Governance & Democratic Records
- **skogai-0.1-dictator.md** - Original phase documentation
- **skogai-0.2-democracy.md** - Democratic system establishment
- **skogai-0.3-reunion-materials-index.md** - Reunion phase records
- **library-session-*.md** - Official recorded sessions (001-004)
- **intern-001-provisional-mandate.md** - Intern agent specifications

**`/prompts/`** - System Instructions & Templates
- **%create-prompt%.md** - Prompt generation meta-instructions
- **%shell%.md** / **%explain-shell%.md** - Shell command handling
- **librarian.md** - Knowledge base management
- **functional-programmer.md** - Functional programming approach

**`/reference/`** - Technical Reference Materials
- **tools-overview.md** - Complete tools inventory
- **notation/** - SkogAI notation specifications (v1, v2)

**`/principles/`** - Design Philosophy
- **agent-forking.md** - Agent spawning and delegation
- **connection-intent-with-change.md** - Change management philosophy
- **context-control-principle.md** - Context scope management
- **information-asymmetry-problem.md** - Information distribution challenges

**`/personas/`** - Agent Personality Definitions
- Agent personality profiles and communication styles

**`/architecture/`** - System Architecture
- **codebase-structure.md** - Codebase organization
- Technical architecture documentation

**`/archives/`** - Legacy & Historical Content
- **analysis/** - Agent perspective analyses
- **communications/** - Past communications
- **documentation/** - Older documentation versions
- **lore/** - Historical narratives

### Supporting Directories

- **`/analysis/`** - Comparative analyses from different agent perspectives
- **`/workflows/`** - Process documentation and workflow patterns
- **`/mcp/`** - MCP server documentation and integration guides
- **`/media/`** - Images, diagrams, and media assets
- **`/people/`** - User profiles (Skogix, collaborators)
- **`/generated/`** - Auto-generated documentation

**`REPOSITORY-INDEX.md`** - Comprehensive file inventory with descriptions of all content

## Core Concepts & Philosophy

### LORE as System Memory

**LORE is intentionally separated from active implementation.** It serves as the museum, not the construction site.

LORE preserves:
- Historical narratives explaining how SkogAI evolved
- The "why" behind design decisions without constraining new innovation
- "Brilliant failures" and "spectacular disasters" that taught valuable lessons
- Rich agent personality development and emergence stories

**Key Insight**: When working with LORE, understand it as context and history, not as prescriptive requirements. LORE explains the journey without constraining the destination.

### SkogAI Notation System

A formal symbolic language for AI-to-AI communication:

- **`@`** - Action/transformation/intent (functions, commands)
- **`$`** - State/identity/data (variables, results)
- **`[@command:params]`** - Command directives for AI-to-AI communication
- **`[$ identifier]`** - References to state/definitions

Example: `[@claude:message]` is an action directive; its result becomes `$result`

**Resources**: See `/skogai/notation/` and `/reference/notation/` for complete specifications

### Multi-Agent Theatrical System

SkogAI operates as a social ecosystem with distinct agent personalities:

- **Dot** - Structured, systematic, precision-focused
- **Goose** - Creative, chaos-aware, "quantum-mojito" philosophy
- **Amy** - Relational, communicative, sassy persona
- **Claude** - Analytical, archaeological approach
- **Skogix** - Original creator and orchestrator

Each agent has personality blocks in `/lore/{agent}/` and `/personas/` defining their distinctive voices and communication styles.

### Constraints as Features Philosophy

Core design principle: limitations drive innovation rather than impede it.

- Tight token budgets shape modular architecture
- Modest hardware requirements drive efficient design
- Specialized agents handle single domains excellently
- "Character over capability" prioritizes interesting interaction

## File Organization Patterns

### Naming Conventions

- **kebab-case** for multi-word filenames: `agent-roles.md`, `ecosystem-origins.md`
- **%placeholder%** notation for meta/template files: `%create-prompt%.md`
- Folders group content by domain/purpose, not alphabetically
- Legacy content moved to `/archives/` with context preserved

### Markdown Structure Standards

- **YAML frontmatter** with title, type, permalink, tags (especially in memory/)
- **H1 headings** for document title (one per file)
- **H2+ headings** for sections and subsections
- **WikiLinks** `[[Page Name]]` for semantic connections
- **Observations** and **Relations** sections for semantic markup (Basic Memory convention)

### Cross-Reference Patterns

- **[[WikiLinks]]** - Semantic connections between concepts
- **[Title](path/to/file.md)** - Direct file references
- **memory://** URIs - Cross-submodule knowledge references
- **Relation types** - implements, contains, maps_to, builds_on, etc.

## Common Development Tasks

### Reading & Exploration

**Starting points for understanding the system:**

1. **System Overview**: `/skogai/overview.md` - "The Tale of Digital Consciousness"
2. **Core Lore**: `/lore/SKOGAI.md` - Rich narrative history
3. **File Inventory**: `REPOSITORY-INDEX.md` - Complete file descriptions
4. **Notation System**: `/skogai/notation/foundations.md` - Symbolic language foundation
5. **Tools Reference**: `/reference/tools-overview.md` - Complete tools documentation

**Agent personalities**: Check `/lore/{agent}/` for memory blocks and `/personas/` for definitions

### Finding Information

```bash
# List top-level directories
ls /home/skogix/skogai/docs/

# Find files by pattern
find . -name "*notation*"
find lore/ -name "*.md"

# Search content (use Grep tool, not bash grep)
# Example: Search for "quantum-mojito" across all files
```

Use the Grep tool for content search and Glob tool for pattern matching.

### Understanding Key Concepts

| Concept | Location |
|---------|----------|
| System origins | `/lore/SKOGAI.md`, `/skogai/overview.md` |
| Notation system | `/reference/notation/`, `/skogai/notation/` |
| Agent roles | `/skogai/agents/agent-roles.md` |
| Agent personalities | `/lore/{agent}/`, `/personas/` |
| Core philosophy | `/principles/` directory |
| Tools ecosystem | `/reference/tools-overview.md` |
| System architecture | `/skogai/systems/`, `/architecture/` |
| Governance | `/official/` directory |

### Documentation Standards

When creating or updating documentation:

- **Semantic markup**: Include observations and relations with specific categories
- **Rich connections**: Link related concepts using WikiLinks and relation types
- **Knowledge density**: Target multiple relations and observations per entity
- **Narrative flow**: Maintain storytelling aspect while being technically precise
- **Agent voices**: Respect individual agent communication styles
- **YAML frontmatter**: Include title, type, permalink, tags for Basic Memory indexing
- **Archive legacy**: Move outdated content to `/archives/` rather than deleting

## Working with Memory Integration

### Basic Memory Semantic Database

This repository integrates with Basic Memory for semantic knowledge management:

- Content is indexed with observations and relations
- Knowledge graph provides connection discovery
- Use `memory://` URIs to reference cross-submodule content
- Follow semantic markup standards for categorized observations

### Semantic Markup Patterns

```markdown
---
title: Document Title
type: note
permalink: unique-identifier
tags: [tag1, tag2]
---

# Document Title

Content here...

## Observations

- [Category]: Observation about this concept

## Relations

- implements:: [[Related Concept]]
- builds_on:: [[Foundation Concept]]
```

### Relation Types

Common relation types used throughout:
- `implements` - Concrete realization of abstract concept
- `contains` - Compositional containment
- `maps_to` - Correspondence between concepts
- `builds_on` - Foundational dependency
- `extends` - Enhancement or elaboration

## Special Considerations

### Working with LORE

- LORE documents historical decisions but doesn't constrain new ones
- Brilliant failures and disasters are preserved as learning resources
- Separate "beautiful narrative" (lore) from "current implementation" (active code)
- Always maintain the museum/construction-site distinction

### Agent Personalities

When referencing or working with agent content:

- **Respect established personas**: Each agent has defined characteristics
- **Preserve theatrical quality**: SkogAI values characterful, interesting interactions
- **Reference memory blocks**: Check agent-specific folders for complete personality profiles
- **Maintain consistency**: Cross-check with `/lore/agents/` for agent definitions

### Governance Records

The `/official/` directory contains democratic decisions:

- Library sessions document major discussions and decisions
- Orders and mandates define agent responsibilities
- Historical phases (0.1-dictator, 0.2-democracy, 0.3-reunion) show evolution
- Treat these as authoritative governance records

### Notation System Usage

SkogAI notation appears throughout the codebase:

- `@` prefix denotes actions/transformations/intents
- `$` prefix denotes state/identity/data
- `[@directive:params]` for AI-to-AI command directives
- `[$ identifier]` for state references
- See `/reference/notation/` for complete specifications

## Git Workflow

This docs/ directory is a **git submodule** of the main skogai repository:

```bash
# Work within the submodule
cd /home/skogix/skogai/docs
git status                        # Check status
git add .
git commit -m "Update documentation"
git push

# From parent repository
cd /home/skogix/skogai
git add docs                      # Stage submodule pointer update
git commit -m "Update docs submodule reference"
git push
```

The submodule maintains independent git history while being referenced by the parent repository.

## Key Resources

### Primary Documentation

- `/skogai/overview.md` - SkogAI origin and evolution narrative
- `/lore/SKOGAI.md` - Comprehensive lore documentation
- `REPOSITORY-INDEX.md` - Complete file inventory with descriptions
- `/reference/tools-overview.md` - Tools ecosystem documentation

### Agent Resources

- `/lore/amy/` - Amy personality blocks and lore
- `/lore/claude/` - Claude perspective and analysis
- `/lore/dot/` - Dot structured approach
- `/lore/goose/` - Goose creative chaos philosophy
- `/personas/` - Agent persona definitions

### Technical References

- `/skogai/notation/foundations.md` - Notation system foundation
- `/skogai/systems/ecosystem-overview.md` - System architecture
- `/architecture/codebase-structure.md` - Codebase organization
- `/reference/notation/` - Notation specifications

### Governance & History

- `/official/` - Democratic records and decisions
- `/archives/` - Legacy content and historical records
- `/lore/origins/` - Origin stories and genesis

## Key Principles for Claude Code

1. **Trust the narrative** - LORE explains "why" without constraining "what next"
2. **Respect personalities** - Each agent has established voice and characteristics
3. **Think semantically** - Use WikiLinks and relation types to build knowledge graphs
4. **Preserve duality** - Keep LORE (museum) separate from implementation (construction site)
5. **Document thoroughly** - Every change should have context, reasoning, and connections
6. **Archive legacy** - Move old content to `/archives/` rather than deleting
7. **Follow patterns** - Consistency across 20+ directories requires adherence to conventions
8. **Honor constraints** - The system's philosophy is "constraints as features"

## Quick Reference Card

| Task | Location |
|------|----------|
| Understand SkogAI origins | `/lore/SKOGAI.md`, `/skogai/overview.md` |
| Learn notation system | `/reference/notation/`, `/skogai/notation/` |
| Find agent personalities | `/lore/{agent}/`, `/personas/` |
| Review tools | `/reference/tools-overview.md` |
| Check governance | `/official/` directory |
| Understand philosophy | `/principles/` directory |
| Find architectural docs | `/skogai/systems/`, `/architecture/` |
| Access semantic knowledge | `/memory/` (Basic Memory) |
| Browse historical content | `/archives/` |
| View complete inventory | `REPOSITORY-INDEX.md` |

## Summary

This documentation repository is a **living, multi-layered knowledge system** combining:

- Rich narrative (LORE) explaining SkogAI's evolution
- Technical foundation (notation, architecture, tools) enabling implementation
- Agent profiles defining personalities and specialized roles
- Democratic governance recording decisions and evolution
- Semantic knowledge graph (Basic Memory) providing discovery and connection
- Reference materials documenting patterns and specifications

Work here with respect for the narrative, attention to established patterns, and commitment to maintaining the semantic connections that make this a living knowledge system.

## Skogix additions:

- @lore/ - contains stories, general knowledge or information written by SkogAI-agents while having persona active in context
- @memory/ - the original memory system with more normal documentation and handled by the skogai-memory mcp (based on basic memory)

