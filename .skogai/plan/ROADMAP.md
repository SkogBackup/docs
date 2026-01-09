# Docs Repository Roadmap

## v0.0.1 - skogai-old-school back-to-basics

**Goal:** Return to the solid documentation foundations from the legacy `todo/CLAUDE.md` structure. Incorporate the question-based format, comprehensive tool ecosystem docs, and clear interface guides into the current repository.

**Reference:** The old `todo/CLAUDE.md` has excellent patterns worth preserving:
- Question-based structure (what am i working on, who am i working with, how should i work, etc.)
- Detailed tool ecosystem documentation
- Interface documentation (AIChat, Goose)
- Clear workflow guides

### Phase 1: Foundation Structure
**Status:** Not Started

Establish the core documentation structure following the legacy patterns.

Tasks:
- [ ] Rewrite root `CLAUDE.md` using question-based format from `todo/CLAUDE.md`
- [ ] Create directory overview structure matching legacy approach
- [ ] Add "what are the commands?" section with actual available scripts
- [ ] Add "what are the rules?" section for conventions

### Phase 2: Directory READMEs
**Status:** Not Started

Address the 11 directories identified as missing READMEs in CONCERNS.md.

Tasks:
- [ ] `agents/README.md` - Multi-agent ecosystem overview
- [ ] `agents/claude/README.md` - Claude agent profile index
- [ ] `agents/dot/README.md` - Dot agent profile index
- [ ] `agents/goose/README.md` - Goose agent profile index
- [ ] `governance/README.md` - Governance structure docs
- [ ] `skogix/README.md` - Notation system index
- [ ] `tools/README.md` - Tools ecosystem overview
- [ ] `prompts/guides/README.md` - Guides index
- [ ] `prompts/lore/README.md` - Lore prompts index
- [ ] `prompts/personas/README.md` - Persona prompts index

### Phase 3: Tech Debt Cleanup
**Status:** Not Started

Address high-priority issues from CONCERNS.md.

Tasks:
- [ ] Fix `todo/intefaces/` typo - merge into `todo/interfaces/`
- [ ] Complete empty `tools/argc/examples.md`
- [ ] Decide on claude-mem CLAUDE.md file tracking (.gitignore or commit)
- [ ] Consolidate duplicate trait-generation prompts

### Phase 4: Content Migration
**Status:** Not Started

Migrate valuable content from legacy `todo/` structure into current organization.

Tasks:
- [ ] Evaluate `todo/tools/` docs for migration
- [ ] Evaluate `todo/interfaces/` docs for migration
- [ ] Evaluate `todo/git/` workflow docs for migration
- [ ] Update cross-references after migration

---

## Future Milestones (Planned)

### v0.0.2 - prompts-pipeline
Automated frontmatter generation and prompt management pipeline.

### v0.0.3 - lore-integration
Connect lore system with agent profiles and documentation.

---

*Roadmap created: 2026-01-09*
