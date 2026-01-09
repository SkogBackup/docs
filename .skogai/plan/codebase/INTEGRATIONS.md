# External Integrations

**Analysis Date:** 2026-01-09

## APIs & External Services

**LLM Providers:**
- OpenRouter - Primary LLM gateway
  - Auth: `OPENROUTER_API_KEY` env var
  - Usage: Lore generation, prompt execution
  - Docs: `lore/README.md`

- OpenAI - Alternative provider
  - Auth: `OPENAI_API_KEY` env var
  - Usage: Referenced in tool guides
  - Docs: `prompts/todo/skogai-agents-aichat.md`

**Local LLM:**
- Ollama - Local model execution
  - Integration planned: `.research/ollama-integration.md`
  - Status: Research phase

## Data Storage

**File System:**
- Markdown documents - Primary storage
- JSON configs - Schema definitions, status files
- YAML - Agent orchestration configs

**Monitoring:**
- `todo/memory/.basic-memory/watch-status.json` - File watcher status
  - Tracks: PID, start time, error count, sync status
  - Last known state: Running with 1 synced file

## Tool Integrations

**argc Framework:**
- Purpose: CLI authoring and task automation
- Location: `tools/argc/`
- Source: Symlinked to `/home/skogix/.local/src/argc`
- Docs: 10+ documentation files (README.md, SKILL.md, reference.md, etc.)

**GitHub CLI (gh):**
- Purpose: GitHub operations
- Location: `tools/gh/`
- Docs: filtering.md, json.md, release.md

**skogcli:**
- Purpose: Environment configuration management
- Integration: `.envrc` calls `skogcli config export-env`
- Namespace: `skogai`

## Cross-Repository References

**@-notation Paths (documented but external):**
- `@lore/` - Narrative generation system
- `@knowledge/` - Knowledge base (external)
- `@orchestrator/` - Workflow automation (external)
- `@integration/` - Pipeline tools (external)
- `@context/` - Session state management (external)

**Symlink Targets:**
- `lore/agents/prompts` - Referenced in `prompts/README.md`
- `/mnt/extra/skogai` - Extended data storage via `SKOGAI_HOME`

## Agent Communication

**AIChat Integration:**
- Documentation: `todo/interfaces/aichat/`
- Guides: agents-guide.md, tools.md, function-calls.md
- Migration: agents/migration-guide.md

**Goose Orchestration:**
- Configs: `todo/interfaces/goose/memory/*.yaml`
- Files: goose-orchestrator.yaml, goose-process-design-specialist.yaml

**Memory System:**
- claude-mem - Auto-generated context tracking
- Pattern: `<claude-mem-context>` blocks in CLAUDE.md files
- Locations: `prompts/lore/`, `prompts/personas/`, `skogix/`, `.research/`

---

*Integration audit: 2026-01-09*
*Update when adding/removing external services*
