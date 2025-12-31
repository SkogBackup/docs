---
title: skogai-prompts-repository
type: index
permalink: docs/prompts
symlink: lore/agents/prompts
tags: [skogai, prompts, index]
---

# SkogAI Prompts Repository

Central repository for reusable prompts, templates, and agent instructions used across the SkogAI ecosystem.

## Repository Structure

```
prompts/
├── README.md           # This file - repository index
├── CLAUDE.md          # Claude-specific instructions and patterns
├── personas/          # Persona-specific prompt templates
├── lore/              # Lore generation prompts
├── tools/             # Tool development and usage prompts
├── workflows/         # Multi-step workflow templates
└── system/            # System-level prompts and guidelines
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

| Use Case | Prompt Location | Description |
|----------|----------------|-------------|
| Create lore entry | `lore/entry-creation.md` | Transform technical → narrative |
| Define persona | `personas/creation.md` | Build consistent character voice |
| Build argc tool | `tools/argc-template.md` | Standard tool structure |
| Orchestrate workflow | `workflows/pipeline.md` | Multi-step automation |

## Using These Prompts

### Direct Reference
```
@agents/prompts/lore/entry-creation.md
```

### In Code
```python
from pathlib import Path
prompt_path = Path("agents/prompts/lore/entry-creation.md")
```

### In Workflows
```bash
# Via symlink
cat agents/prompts/workflows/pipeline.md
```

## Prompt Standards

All prompts in this repository follow these conventions:

1. **Frontmatter**: YAML metadata block
   ```yaml
   ---
   title: prompt-name
   type: prompt|template|guide
   category: lore|persona|tool|workflow
   tags: [relevant, tags]
   ---
   ```

2. **Structure**:
   - Clear objective statement
   - Input requirements
   - Expected output format
   - Examples (where applicable)

3. **Naming**: `kebab-case.md`

4. **Categories**:
   - `persona` - Character/voice definitions
   - `lore` - Narrative generation
   - `tool` - Development patterns
   - `workflow` - Multi-step processes
   - `system` - Core instructions

## Contributing

When adding new prompts:

1. Choose appropriate category directory
2. Use descriptive kebab-case filename
3. Include complete frontmatter
4. Provide usage examples
5. Test with actual use cases
6. Document any dependencies

## Integration Points

This repository integrates with:

- **Lore System**: `@lore/` - Narrative generation
- **Persona System**: `@knowledge/expanded/personas/` - Character definitions
- **Orchestrator**: `@orchestrator/` - Workflow automation
- **Integration**: `@integration/` - Pipeline tools

## Migration Notes

High-value content identified from legacy systems:

**From TODO-AICHAT-BASED-SKOGAI:**
- 7 reusable prompt templates (prompts/)
- Agent creation guides (364 lines)
- Tool development guide (410 lines)
- Persona/lorebook documentation

**Status**: Pending selection and migration

---

**Last Updated**: 2025-12-31
**Maintainer**: skogix
**Repository**: Part of SkogAI lore project
