# Technology Stack

**Analysis Date:** 2026-01-09

## Document Formats

**Primary:**
- Markdown (.md) - All documentation content
- YAML frontmatter - Document metadata embedded in markdown

**Secondary:**
- JSON - Configuration files, schema definitions
- YAML - Agent orchestration configs (`todo/interfaces/goose/memory/*.yaml`)

## Runtime

**Environment:**
- Documentation repository - no runtime execution
- Git-based version control

**Dependencies:**
- None required for documentation access
- Optional: `skogcli` for environment config export (`.envrc`)

## Frameworks

**Documentation:**
- Static markdown with YAML frontmatter
- No build system required

**Tooling:**
- argc - CLI framework (documented in `tools/argc/`)
- gh - GitHub CLI (documented in `tools/gh/`)

## Key Dependencies

**External Tool Symlinks:**
- `tools/argc/src/argc` → `/home/skogix/.local/src/argc`
- `tools/argc/src/argc-completions` → `/home/skogix/.local/src/argc-completions`

**Environment Variables:**
- `SKOGAI_HOME=/home/skogix/skogai` (symlink to `/mnt/extra/skogai`)
- `skogcli config export-env --namespace skogai` (via `.envrc`)

## Configuration

**Environment:**
- `.envrc` - direnv configuration for environment setup
- `.gitignore` - ignores `.aider*`, `.docgen/scripts/__pycache__`

**Frontmatter Schema:**
- `title` - Document title (required)
- `type` - prompt|note|user|index|research|guide
- `permalink` - Cross-reference path
- `tags` - Array of categorization tags
- `category` - lore|persona|tool|workflow|system

## Platform Requirements

**Development:**
- Any platform with git and text editor
- Optional: direnv for automatic environment loading

**Integration:**
- LLM API keys for prompt execution:
  - `OPENROUTER_API_KEY` (referenced in `lore/README.md`)
  - `OPENAI_API_KEY` (referenced in tool docs)

---

*Stack analysis: 2026-01-09*
*Update after major dependency changes*
