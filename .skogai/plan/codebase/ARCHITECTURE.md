# Architecture

**Analysis Date:** 2026-01-09

## Pattern Overview

**Overall:** Multi-layered Documentation Ecosystem

**Key Characteristics:**
- Three-layer organization (Foundation → Agents → Knowledge Systems)
- Agent-centric knowledge management
- Prompt templates for LLM-driven generation
- Cross-reference system using @-notation

## Layers

**Foundation Layer:**
- Purpose: Core philosophy and user context
- Contains: `CLAUDE.md`, `skogix/` directory
- Location: Repository root + `skogix/`
- Depends on: Nothing (base layer)
- Used by: All other layers

**Agent Layer:**
- Purpose: AI personality profiles, journals, memory blocks
- Contains: Agent profiles, episodic memory, decision history
- Location: `agents/{claude,dot,goose}/`
- Depends on: Foundation layer for context
- Used by: Knowledge systems for prompt execution

**Knowledge Systems Layer:**
- Purpose: Reusable components, templates, tools
- Contains: Prompts, lore system, tool documentation, governance
- Location: `prompts/`, `lore/`, `tools/`, `governance/`
- Depends on: Foundation + Agent layers
- Used by: External systems, LLM workflows

## Data Flow

**Documentation Creation:**
1. User defines intent in `skogix/user.md`
2. Agent context loaded from `agents/*/profile.md`
3. Prompt template selected from `prompts/`
4. LLM generates content using template + context
5. Output stored in appropriate directory

**Cross-Reference Resolution:**
- `@path/notation` references external systems
- Permalinks in frontmatter enable internal linking
- Symlinks connect to external source directories

**State Management:**
- File-based: All state in markdown/JSON files
- No persistent runtime state
- Git provides version history

## Key Abstractions

**Agent:**
- Purpose: AI personality with persistent identity
- Examples: `agents/claude/profile.md`, `agents/dot/profile.md`, `agents/goose/profile.md`
- Pattern: Profile + memory-blocks + journal

**Prompt Template:**
- Purpose: Reusable LLM instruction format
- Examples: `prompts/lore/entry-generation.md`, `prompts/personas/trait-generation.md`
- Pattern: Frontmatter → Objective → Inputs → Expected Output → Prompt

**Memory Block:**
- Purpose: Episodic agent memory storage
- Examples: `agents/claude/memory-blocks/claude-memory-block-01-*.md`
- Pattern: Numbered files (01-13) with narrative content

## Entry Points

**Primary:**
- `/CLAUDE.md` - Core project instructions
- Purpose: Define context rules, philosophy
- Responsibilities: Set token efficiency expectations, discovery patterns

**Secondary:**
- `/prompts/README.md` - Prompt template index
- `/lore/README.md` - Lore system documentation
- `/agents/*/profile.md` - Agent identities

## Error Handling

**Strategy:** N/A (documentation repository)

**Validation:**
- YAML frontmatter must be valid
- Cross-references may be broken (see CONCERNS.md)

## Cross-Cutting Concerns

**Context Management:**
- "Every token fights for survival" philosophy
- Discovery before definition approach
- Iterative refinement pattern

**Documentation Standards:**
- YAML frontmatter required
- kebab-case filenames
- Consistent prompt structure

**Agent Philosophy:**
- Quantum-Mojito: Multiple interpretations in superposition
- 99.9999% Paradox: Explicit uncertainty over false confidence
- Constraints as creative forces

---

*Architecture analysis: 2026-01-09*
*Update when major patterns change*
