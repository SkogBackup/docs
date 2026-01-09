# Codebase Concerns

**Analysis Date:** 2026-01-09

## Tech Debt

**Directory Typo:**
- Issue: `todo/intefaces/` misspelled as "intefaces" instead of "interfaces"
- Files: `todo/intefaces/aichat/` (parallel to correct `todo/interfaces/aichat/`)
- Why: Likely typo during directory creation
- Impact: Confusion, duplicate content across both directories
- Fix approach: Merge contents into `todo/interfaces/`, delete misspelled directory

**Duplicate Prompt Templates:**
- Issue: Two versions of trait-generation prompt exist
- Files: `prompts/personas/trait-generation.md`, `prompts/personas/trait-generation-skogai-version.md`
- Why: Iterating on prompt design
- Impact: Unclear which to use, maintenance burden
- Fix approach: Consolidate to single file or clearly document differences

**Auto-Generated CLAUDE.md Files:**
- Issue: Multiple CLAUDE.md files with only claude-mem context, untracked
- Files: `prompts/lore/CLAUDE.md`, `prompts/personas/CLAUDE.md`, `skogix/CLAUDE.md`, `.research/CLAUDE.md`
- Why: claude-mem auto-generates tracking sections
- Impact: Untracked files, unclear if ephemeral or important
- Fix approach: Either track in git or add to .gitignore

## Known Bugs

**Broken Reference Paths:**
- Symptoms: @-notation paths reference non-existent directories
- Trigger: Following documentation cross-references
- Files affected: `lore/README.md`, `prompts/README.md`
- Workaround: Treat as external system references, not local paths
- Root cause: Documentation written for different repository structure

## Missing Documentation

**Directories Without README:**
- `agents/` - No root agent documentation
- `agents/claude/` - No Claude overview
- `agents/dot/` - No Dot overview
- `agents/goose/` - No Goose overview
- `governance/` - No governance structure docs
- `skogix/` - No notation system index
- `tools/` - No tools ecosystem overview
- `prompts/guides/` - Completely undocumented
- `prompts/lore/` - No lore prompt index
- `prompts/personas/` - No persona prompt index

**Impact:** Navigation difficulty for new users, unclear directory purposes

## Incomplete Content

**Empty/Stub Files:**
- `tools/argc/examples.md` - Only YAML frontmatter, no content (214 bytes)
- Fix: Add actual argc examples or remove file

**Placeholder Values:**
- `lore/README.md` line 389: `other-author=persona_XXXXX` placeholder
- Fix: Replace with real value or document as example

**Unfinished TODO:**
- `lore/README.md` line 641: "TODO: Connect pipeline - ingest git diff → call existing tools → link to session"
- Fix: Complete implementation or remove TODO

## Broken References

**@-notation Paths (external system references):**
- `@knowledge/core/lore/schema.json` - Does not exist locally
- `@knowledge/core/book-schema.json` - Does not exist locally
- `@knowledge/core/persona/schema.json` - Does not exist locally
- `@context/templates/` - Does not exist locally
- `@context/current/` - Does not exist locally
- `@context/archive/` - Does not exist locally

**Script References:**
- `tools/argc/index.md` references `./scripts/docs-cli` - Does not exist
- `tools/argc/index.md` references `./scripts/docs-context` - Does not exist

**Symlink Reference:**
- `prompts/README.md` - `symlink: lore/agents/prompts` - Path likely invalid

## Deprecated Content

**Files with Deprecation Markers:**
- `todo/tools/agents-guide.md` line 303: `[$DEPRECATED:skogix:TODO:must check this still is valid before use]`
- `todo/intefaces/aichat/agents-guide.md` line 303: Same deprecated marker
- `prompts/todo/skogai-agents-aichat.md` line 303: Same deprecated marker
- Impact: Multiple copies of deprecated content
- Fix: Consolidate or remove deprecated files

## Inconsistencies

**Frontmatter Variations:**
- Some prompts use `use_tools: fs` field, others don't
- `category` vs `categories` used inconsistently
- Some files missing frontmatter entirely

**Work-in-Progress Markers:**
- `prompts/personas/trait-generation-skogai-version.md` line 8: Contains unresolved `[$instructions-structure]` placeholder

## Pending Migrations

**From prompts/README.md:**
- "Status: Pending selection and migration"
- Source: TODO-AICHAT-BASED-SKOGAI
- Content: 7 reusable prompt templates, Agent creation guides (364 lines), Tool development guide (410 lines)

---

## Priority Summary

### High Priority
1. Fix `todo/intefaces/` typo - merge into `todo/interfaces/`
2. Add missing README files to key directories
3. Complete empty `tools/argc/examples.md`
4. Decide on claude-mem CLAUDE.md file tracking

### Medium Priority
5. Consolidate duplicate trait-generation prompts
6. Fix broken @-notation references or document as external
7. Remove or update deprecated content
8. Complete placeholder values in lore/README.md

### Low Priority
9. Standardize frontmatter across all files
10. Complete pending migration from legacy system
11. Add missing prompt sections where needed

---

*Concerns audit: 2026-01-09*
*Update as issues are fixed or new ones discovered*
