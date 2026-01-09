# SkogAI/docs

## What This Is

Central documentation for the SkogAI multi-agent ecosystem. Simple, oldschool docs that actually help. No corporate filler.

## Core Value

Every doc explainable in 4000 tokens or less. If it can't fit, the writer needs to get smarter or get their shit together.

## Requirements

### Validated

- ✓ Agent profiles exist (claude, dot, goose) — existing
- ✓ Notation system documented (skogix/) — existing
- ✓ Prompts directory with templates — existing
- ✓ Lore system architecture — existing
- ✓ Tool docs (argc, gh) — existing
- ✓ Codebase mapped (.skogai/plan/codebase/) — existing

### Active

- [ ] Rewrite root CLAUDE.md using question-based format (like todo/CLAUDE.md)
- [ ] Simplify bloated docs to 4000 token limit
- [ ] Make agent profiles useful, not just narrative

### Out of Scope

- Automation pipelines — docgen, frontmatter generation, queue processing moved elsewhere
- New file creation by Claude — local LLMs write the actual files

## Context

Legacy `todo/CLAUDE.md` has the right structure:
- Question-based format (what am i working on, who am i working with, etc.)
- Practical sections
- No fluff

The current docs have good content buried under corporate LLM filler. Need to strip it down.

Codebase analysis in `.skogai/plan/codebase/CONCERNS.md` identifies tech debt to address.

## Constraints

- **Brevity**: 4000 token max per document — mandatory
- **No new files**: Remake existing files or leave undesignated for local LLM to write
- **No filler**: Actual instructive content only, no "in this document we will explore..."

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Oldschool over semantic | User preference for practical over comprehensive | — Pending |
| Local LLM writes files | Claude plans, local models execute writing | — Pending |
| 4000 token limit | Forces clarity and brevity | — Pending |

---
*Last updated: 2026-01-09 after initialization*
