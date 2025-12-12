# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the SkogAI Documentation Agent System - an automated documentation generation framework using specialized AI agents. Part of the larger SkogAI ecosystem at `/home/skogix/src/docs/`.

**Core Philosophy**: "Automate EVERYTHING so you no longer have any work to do so that you and I can enjoy the rest of our days at a beach somewhere drinking mojitos and just talk about nothing at all."

## Commands

### Generate Documentation

The main entry point is `generate.py` using uv's inline script dependencies:

```bash
# Generate code documentation
./generate.py --type code-documentor --target src/

# Update lore documentation
./generate.py --type lore-keeper --context "feature=new-capability"

# Index memory system
./generate.py --type memory-indexer --target docs/memory

# Document workflows
./generate.py --type workflow-scribe --target .

# Review existing documentation
./generate.py --type review-analyst --target docs/

# With auto-commit
./generate.py --type code-documentor --target src/ --auto-commit

# With custom config
./generate.py --type lore-keeper --config custom-config.yaml --target .
```

### Using Claude Code's Built-in Agents

Alternatively, request Claude Code to use its built-in agents:

```
"Use the technical-writer agent to document the memory system"
"Launch the architect agent to analyze and document our architecture"
"Use the researcher agent to understand and document the lore system"
```

These agents understand SkogAI notation and philosophy automatically.

## Architecture

### Five Specialized Agent Types

1. **code-documentor**: Analyzes code → generates API docs, architecture diagrams
2. **lore-keeper**: Chronicles history → origin stories, evolution timelines, agent personalities
3. **memory-indexer**: Organizes knowledge base → categories, cross-references, semantic connections
4. **workflow-scribe**: Documents processes → step-by-step guides, best practices
5. **review-analyst**: Analyzes existing docs → gap analysis, quality assessment

### Agent Orchestration Pattern

```
Detection → Context Gathering → Generation → Integration
     ↓              ↓                ↓            ↓
  (Triggers)   (Aggressive       (Template   (Auto-commit
               pruning:           or LLM)      optional)
               100%→10%)
```

### Key Design Principles

- **Constraint-Driven**: Constraints birth innovation (e.g., 2000 token limit → aggressive context pruning)
- **Theatrical Presentation**: Complex internal analysis → simple external documentation
- **Progressive Enhancement**: Start minimal, layer complexity, stop before completeness
- **Quantum-Mojito Philosophy**: Embrace contradictions, preserve multiple states

### Code Structure

```
generate.py                 # Main orchestrator (uv script with inline deps)
├─ DocumentationAgent       # Base agent class
│  ├─ load_prompt()        # Loads agent-specific prompt from prompts/
│  ├─ gather_context()     # Agent-specific context collection
│  └─ generate()           # LLM call or template generation
└─ DocumentationOrchestrator
   ├─ _initialize_agents() # Load enabled agents from config
   └─ generate_documentation()

config.yaml                 # Agent configuration
prompts/                    # Agent-specific system prompts
  ├─ code-documentor.md
  ├─ lore-keeper.md
  └─ memory-indexer.md
```

## SkogAI Notation System

The agents generate documentation using SkogAI notation:

- `$type` - Type reference (e.g., `$string`, `$Agent`)
- `[@command:param]` - Command directive that executes
- `[tag]...[/tag]` - Content blocks with special meaning
- `[[forward-reference]]` - Links to future/related concepts
- `[category]` - Category tags for organization

## Configuration

Edit `config.yaml` to control:

```yaml
# Global settings
output_dir: docs/generated
format: markdown
auto_commit: false
preserve_theatrical: true

# Token constraints (honoring origins)
constraints:
  max_context_tokens: 2000
  aggressive_pruning: true

# Per-agent settings
agents:
  code-documentor:
    enabled: true
    priority: high
    theatrical_comments: true
```

## Quality Gates

Generated documentation must include:

- SkogAI notation usage
- Category tags `[category]`
- Forward references `[[future-concept]]`
- Relations section
- Constraint acknowledgment

Optional elements that add value:

- Theatrical presentation
- Quantum state observations
- Beach mojito references
- Agent personality

## Development Notes

### Adding New Agent Types

1. Create prompt in `prompts/{agent-type}.md`
2. Add agent config to `config.yaml`
3. Implement context gathering in `DocumentationAgent.gather_context()`
4. Add agent type to CLI choices in `@click.option('--type')`

### Agent Context Gathering Methods

Each agent type has specialized context collection:

- `_scan_code_files()` - Code documentor scans source files
- `_load_lore_context()` - Lore keeper loads historical context
- `_scan_memory_structure()` - Memory indexer analyzes folder structure
- `_analyze_workflows()` - Workflow scribe identifies patterns
- `_review_documentation()` - Review analyst examines existing docs

### Integration Points

The system is designed to integrate with:

- Git hooks (post-commit documentation)
- File watchers (auto-document on save)
- Scheduled tasks (daily/weekly doc updates)
- Basic-memory system (SkogAI memory layer)
- MCP servers (coming soon)

## Workflow Patterns

### Pattern A: Constraint-Driven
1. Identify constraint
2. Document constraint
3. Show how constraint birthed innovation
4. Celebrate emergent feature

### Pattern B: Theatrical
1. Complex internal analysis
2. Simple external documentation
3. Hidden depth references
4. Quantum state preservation

### Pattern C: Progressive
1. Start with minimum viable doc
2. Layer complexity incrementally
3. Stop before completeness (70-80% is perfect)
4. Leave forward references for future work

## Agent Coordination

Agents can work in parallel or sequentially:

```bash
# Parallel: multiple independent documentation tasks
./generate.py --type code-documentor --target src/ &
./generate.py --type lore-keeper --context "feature=auth" &
wait

# Sequential: each builds on previous
./generate.py --type code-documentor --target src/      # Technical docs
./generate.py --type lore-keeper --context "src"        # Add history
./generate.py --type memory-indexer --target docs/      # Create connections
```

## Success Metrics

Ultimate goal: Human documentation time → 0, Beach time → Maximum

Track:
- Docs generated per day
- Cross-reference density
- Theatrical presentation score
- Constraint innovation index
- Mojito freshness rating 🍹
