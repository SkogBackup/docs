# Documentation Repository Migration Plan

## Target Structure

```
docs/
├── agents/
│   ├── amy/
│   ├── claude/
│   ├── dot/
│   ├── goose/
│   ├── intern/
│   └── automation/
├── lore/
│   ├── origin/
│   ├── events/
│   ├── philosophy/
│   └── skogix/
├── governance/
│   ├── sessions/
│   └── orders/
├── technical/
│   ├── architecture/
│   ├── memory-system/
│   ├── notation/
│   ├── ansible/
│   └── cloudflare/
├── prompts/
│   ├── system/
│   ├── agents/
│   └── tools/
├── guides/
├── media/
├── historical/
│   ├── important-moments/
│   └── archived/
└── _workspace/
    ├── drafts/
    ├── review/
    └── logs/
```

---

## Phase 1: Consolidate Agents

### agents/amy/
```bash
# Profile
mv archives/profiles/amy.md agents/amy/profile.md

# Memory blocks
mv lore/amy/*.md agents/amy/memory-blocks/

# Related content
mv lore/personas/Amy\ Character\ Profile\ Summary.md agents/amy/
mv archives/lore/amy_lore_mandate.md agents/amy/
```

### agents/claude/
```bash
# Profile
mv archives/profiles/claude.md agents/claude/profile.md

# Memory blocks
mv lore/claude/*.md agents/claude/memory-blocks/

# Prompts (consolidate from memory)
mv memory/agent/claude/prompts/ agents/claude/prompts/

# Other claude-specific
mv memory/agent/claude/*.md agents/claude/memory/
```

### agents/dot/
```bash
mv archives/profiles/dot.md agents/dot/profile.md
mv lore/dot/*.md agents/dot/memory-blocks/
mv lore/personas/Dot\ Character\ Profile\ Summary.md agents/dot/
```

### agents/goose/
```bash
mv lore/goose/*.md agents/goose/memory-blocks/
mv lore/personas/Goose\ Character\ Profile\ Summary.md agents/goose/
```

### agents/intern/
```bash
mv profiles/intern.md agents/intern/profile.md
mv profiles/intern/ agents/intern/
mv official/intern-001-provisional-mandate.md agents/intern/mandate.md
```

### agents/automation/
```bash
mv agents/documentation/ agents/automation/documentation/
mv agents/git-commiter.md agents/automation/
mv archives/profiles/agents/coder.md agents/automation/coder-profile.md
```

---

## Phase 2: Reorganize Lore

### lore/origin/
```bash
mv lore/SKOGAI.md lore/origin/
mv lore/base-origin-story.md lore/origin/
mv lore/skogai-lore.md lore/origin/
mv lore/skogai-lore-master-knowledge.md lore/origin/
mv lore/skogai-lore-backup.md lore/origin/
mv lore/original-skogai-character-card-*.md lore/origin/
mv lore/original-skogix-cyberpunk-character-card-*.md lore/origin/
```

### lore/events/
```bash
mv lore/events/*.md lore/events/  # already there
mv lore/200k-story-1.md lore/events/
mv lore/first-monkey-brain-2025-03-14.md lore/events/
```

### lore/philosophy/
```bash
mv lore/skogai-commandments.md lore/philosophy/
mv lore/words-to-live-by.md lore/philosophy/
mv lore/concepts/ lore/philosophy/concepts/
mv lore/frameworks/ lore/philosophy/frameworks/
mv lore/treaties/ lore/philosophy/
```

### lore/skogix/
```bash
# Keep existing lore/skogix/ structure
# Move additional skogix content
mv lore/skogix-notation.md lore/skogix/
mv lore/skogix-poet.md lore/skogix/
mv archives/profiles/skogix.md lore/skogix/profile.md
```

### lore/ root cleanup
```bash
# Move Amy-specific to agents
mv lore/amy_ravenwolf_blog.md agents/amy/
mv lore/amy1.yml agents/amy/

# Move system-related
mv lore/systems/ technical/systems/

# Archive old experiments
mv lore/old/ historical/archived/lore-old/
mv lore/dot-amy-roleplay.md historical/archived/
```

---

## Phase 3: Create Governance Section

```bash
mkdir -p governance/sessions governance/orders

# Official documents
mv official/skogai-0.1-dictator.md governance/0.1-dictator.md
mv official/skogai-0.2-democracy.md governance/0.2-democracy.md
mv official/library-session-*.md governance/sessions/

# Orders
mv lore/ORDER-01-2025-03-14.md governance/orders/
mv lore/first-executive-order.md governance/orders/

# Tracking/proposals
mv archives/tracking/proposal-summaries.md governance/
mv archives/system/voting-system.md governance/
```

---

## Phase 4: Consolidate Technical Docs

### technical/architecture/
```bash
mv memory/architecture/ technical/architecture/
mv curated/home/skogix/skogai/data/architecture/ technical/architecture/skogchat/
```

### technical/memory-system/
```bash
mv memory/README.md technical/memory-system/
mv memory/.skogai/ technical/memory-system/config/
mv memory/concepts/ technical/memory-system/concepts/
mv memory/guides/ technical/memory-system/guides/
mv memory/llm/ technical/memory-system/llm/
mv memory/meta/ technical/memory-system/meta/
mv archives/system/rag-system.md technical/memory-system/
```

### technical/notation/
```bash
mv memory/ontology/ technical/notation/
```

### technical/ansible/
```bash
mv memory/ansible/ technical/ansible/
```

### technical/cloudflare/
```bash
mv memory/inventory/ technical/cloudflare/
mv memory/guides/Cloudflare\ MCP\ Setup\ Guide*.md technical/cloudflare/
```

### technical/dev/
```bash
mv memory/dev/ technical/dev/
```

---

## Phase 5: Centralize Prompts

```bash
# Main prompts directory - keep structure but organize
# Move agent-specific prompts to agents/ (done in Phase 1)

# Organize remaining prompts
mkdir -p prompts/system prompts/tools prompts/meta

# System prompts
mv prompts/claude.md prompts/system/
mv prompts/librarian.md prompts/system/
mv prompts/documentation-manager.md prompts/system/
mv prompts/skogai-xml.md prompts/system/

# Tool prompts
mv prompts/%*.md prompts/tools/
mv prompts/argc-creator.md prompts/tools/
mv prompts/tool-*.md prompts/tools/
mv prompts/neovim-manager.md prompts/tools/

# Meta prompts
mv prompts/metaprompt*.md prompts/meta/
mv prompts/prompt-creator.md prompts/meta/
mv prompts/skogai-prompt-creator.md prompts/meta/
mv prompts/character-*.md prompts/meta/

# Notation/conversion
mv prompts/convert-to-skogai-*.md prompts/tools/
mv prompts/skogai-notation.md prompts/tools/
```

---

## Phase 6: Historical & Archives

### historical/important-moments/
```bash
mv important-moments/ historical/important-moments/
```

### historical/archived/
```bash
# Old lore experiments (moved in Phase 2)
# Analysis documents
mv analysis/ historical/analysis/

# Old archives content
mv archives/notes/ historical/archived/notes/
mv archives/logs/ historical/archived/logs/
mv archives/reports/ historical/archived/reports/
```

---

## Phase 7: Workspace & Cleanup

### _workspace/
```bash
mkdir -p _workspace/drafts _workspace/review _workspace/logs

mv archives/drafts/ _workspace/drafts/
mv to-be-looked-over/ _workspace/review/
mv logs/ _workspace/logs/
```

### Delete/Remove
```bash
# Duplicate mirrors
rm -rf curated/home/skogix/skogai/docs/
rm -rf curated/home/skogix/skogai/data/node_modules/

# Empty directories after moves
rm -rf archives/profiles/
rm -rf archives/system/
rm -rf archives/lore/
rm -rf archives/tracking/  # after moving relevant files
rm -rf official/  # after moving all content
rm -rf profiles/  # after moving to agents/

# Session data (consider gitignoring instead)
# .claude/data/sessions/ - may want to keep but gitignore
# .aichat-sessions/ - may want to keep but gitignore
```

### Keep as-is
```bash
# These are fine where they are
media/
generated/
curated/test/
curated/todo/
.github/
```

---

## Phase 8: Final Cleanup

### Update references
- Search for broken internal links
- Update any hardcoded paths in scripts
- Update README files

### Create new READMEs
- `agents/README.md` - Overview of all agents
- `technical/README.md` - Technical documentation index
- `governance/README.md` - Governance history
- `lore/README.md` - Updated lore index

### Gitignore updates
```gitignore
# Add to .gitignore
_workspace/logs/
.claude/data/sessions/
.aichat-sessions/
```

---

## Migration Order (Recommended)

1. **Phase 1: Agents** - Biggest impact, consolidates scattered content
2. **Phase 7: Workspace** - Clears out review/draft noise
3. **Phase 4: Technical** - Organizes reference documentation
4. **Phase 2: Lore** - Cleans up the largest directory
5. **Phase 5: Prompts** - Quick win, single directory
6. **Phase 3: Governance** - Small, focused
7. **Phase 6: Historical** - Archive old content
8. **Phase 8: Cleanup** - Final polish

---

## Verification Checklist

- [ ] All agent content consolidated under agents/
- [ ] No duplicate files between curated/ and main directories
- [ ] All prompts in one location (or agent-specific)
- [ ] Lore contains only narratives/philosophy
- [ ] Technical docs separated from lore
- [ ] Workspace contains only in-progress items
- [ ] Old/archived content clearly separated
- [ ] READMEs updated
- [ ] No broken internal links
