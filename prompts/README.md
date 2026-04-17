---
title: skogai-prompts-repository
type: index
permalink: docs/prompts
symlink: lore/agents/prompts
tags: [skogai, prompts, index]
---

# SkogAI Prompts Repository

Central repository for reusable prompts, templates, and agent instructions used across the SkogAI ecosystem.

## Quick Links

- **📘 [PROMPT_STYLE_GUIDE.md](PROMPT_STYLE_GUIDE.md)** - Complete XML-style formatting guide
- **⚡ [PROMPT_QUICK_REFERENCE.md](PROMPT_QUICK_REFERENCE.md)** - One-page cheatsheet
- **📋 [TEMPLATE.yaml](TEMPLATE.yaml)** - Standard template for creating new prompts

## Repository Structure

```
agents/prompts/
├── README.md           # This file - repository index
├── lore/              # Lore generation prompts (YAML + guides)
│   ├── entry-generation.yaml         # Operational prompt
│   ├── extraction-json.yaml          # Operational prompt
│   ├── extraction-markdown.yaml      # Operational prompt
│   ├── title-generation.yaml         # Operational prompt
│   ├── connection-analysis.yaml      # Operational prompt
│   └── *.md                          # Documentation/guides
├── personas/          # Persona creation prompts (YAML + guides)
│   ├── generation.yaml               # Operational prompt
│   ├── from-text.yaml                # Operational prompt
│   └── *.md                          # Documentation/guides
├── guides/            # Cross-cutting documentation
│   └── skogai-character-guide.md    # Character creation guide
└── agents/            # Agent-specific prompts
    └── claude-append-system-prompt.md

Format:
- *.yaml  = Operational prompts (loaded by scripts via yq)
- *.md    = Documentation, guides, examples
```

## Quick Reference

### By Category

**Personas & Character**

- Character voice templates
- Personality trait definitions
- Interaction style guides

**Lore Generation**

- Entry creation prompts
- Narrative transformation templates
- Book organization patterns

**Tool Development**

- Argc command templates
- Script creation patterns
- Integration guidelines

**Workflows**

- Multi-agent orchestration
- Pipeline automation
- Session management

### By Use Case

| Use Case                | Prompt Location                 | Description                               |
| ----------------------- | ------------------------------- | ----------------------------------------- |
| Create lore entry       | `lore/entry-generation.yaml`    | Transform title → narrative prose         |
| Extract lore (JSON)     | `lore/extraction-json.yaml`     | Extract entities from docs → JSON         |
| Extract lore (Markdown) | `lore/extraction-markdown.yaml` | Extract entities → markdown               |
| Generate titles         | `lore/title-generation.yaml`    | Generate entry titles for lorebook        |
| Find connections        | `lore/connection-analysis.yaml` | Identify relationships between entries    |
| Generate persona        | `personas/generation.yaml`      | Create traits/voice from name+description |
| Extract persona         | `personas/from-text.yaml`       | Extract persona profile from text         |

## Using These Prompts

### In Shell Scripts (via yq)

```bash
# Load prompt template
PROMPT_FILE="$SKOGAI_DIR/agents/prompts/lore/entry-generation.yaml"
PROMPT_TEMPLATE=$(yq eval '.template' "$PROMPT_FILE")

# Substitute variables
PROMPT="${PROMPT_TEMPLATE//\{\{title\}\}/$title}"
PROMPT="${PROMPT//\{\{category\}\}/$category}"

# Send to LLM
ollama run llama3.2 "$PROMPT"
```

### Direct Reference

```
@agents/prompts/lore/entry-generation.yaml
```

### In Python

```python
from pathlib import Path
import yaml

prompt_path = Path("agents/prompts/lore/entry-generation.yaml")
with open(prompt_path) as f:
    prompt_data = yaml.safe_load(f)
    template = prompt_data['template']
```

## Prompt Standards

### YAML Format (Operational Prompts)

All operational prompts use YAML with this structure:

```yaml
name: prompt-name
description: Brief description of what this prompt does
version: "1.0"
template: |
  <role>Define the LLM's role</role>

  <critical_instruction>
  What MUST be done (output format, no meta-commentary, etc.)
  </critical_instruction>

  <task>
  The specific task to perform
  </task>

  <input_data>
  {{variable_name}}
  </input_data>

  <output_format>
  Exact format expected
  </output_format>

  <rules>
  - Specific rules and constraints
  - Formatting requirements
  </rules>

  <examples>
  <example>
  Input: ...
  Output: ...
  </example>
  </examples>

  <execution_instruction>
  Final trigger to generate output
  </execution_instruction>

variables:
  - name: variable_name
    type: string
    required: true
    description: What this variable represents
```

### Markdown Format (Documentation)

Documentation files (.md) use frontmatter:

```yaml
---
title: guide-name
type: guide|reference
category: lore|persona|tool
tags: [relevant, tags]
---
```

### Naming Conventions

- **YAML prompts**: `kebab-case.yaml`
- **Markdown guides**: `kebab-case.md`
- Variables in templates: `{{snake_case}}`

## Contributing

When adding new prompts:

1. Choose appropriate category directory
1. Use descriptive kebab-case filename
1. Include complete frontmatter
1. Provide usage examples
1. Test with actual use cases
1. Document any dependencies

## Integration Points

This repository integrates with:

- **Lore System**: `@lore/` - Narrative generation
- **Persona System**: `@knowledge/expanded/personas/` - Character definitions
- **Orchestrator**: `@orchestrator/` - Workflow automation
- **Integration**: `@integration/` - Pipeline tools

## Recent Changes

**2026-01-12**: Prompt repository restructured

- Migrated from `/prompts/` to `/agents/prompts/` as canonical location
- Converted all operational prompts to improved YAML format with XML-style structure tags
- Updated scripts (`llama-lore-integrator.sh`, `llama-lore-creator.sh`) to use new paths
- Maintained markdown guides for documentation purposes
- Added better prompt engineering patterns (`<role>`, `<task>`, `<rules>`, `<examples>`)

______________________________________________________________________

**Last Updated**: 2026-01-12 **Maintainer**: skogix **Repository**: Part of SkogAI lore project
