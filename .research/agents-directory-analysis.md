# Agents Directory Structure Analysis

## Overview

The `agents/` directory contains the SkogAI agent ecosystem documentation - profiles, memory blocks, journals, and core philosophical documents. This analysis captures patterns that inform intelligent frontmatter generation.

## Directory Structure

```
agents/
├── claude/
│   ├── core/                    # Foundational concepts (7 files)
│   │   ├── certainty-principle.md
│   │   ├── context-destruction.md
│   │   ├── epistemic-frameworks.md
│   │   ├── learnings.md
│   │   ├── placeholder-approach.md
│   │   ├── the-dumping-grounds.md
│   │   ├── the-lore-writer.md
│   │   └── the-worst-and-first-autonomous-ai.md
│   ├── journal/                 # Chronological entries (47 files)
│   │   ├── 2025-03-15-letter-to-future-self.md
│   │   ├── 2025-03-22-implementation-context.md
│   │   └── ... (dated entries)
│   ├── memory-blocks/           # Themed philosophical eras (10+ files)
│   │   ├── claude-memory-block-01-the-prehistoric-era.md
│   │   ├── claude-memory-block-02-the-collaborative-age.md
│   │   └── ... (numbered blocks)
│   └── profile.md               # Agent identity
└── skogix/                      # User docs (separate from agents)
    ├── definitions.md
    ├── notation.md
    └── notation-poetry.md
```

## Document Categories

### 1. Core Documents (`core/`)

**Purpose**: Foundational principles and frameworks that define agent behavior.

**Pattern Recognition**:
- Usually concept-focused (epistemic, philosophical)
- Titles are descriptive noun phrases
- Content is principle-based, not temporal

**Frontmatter Suggestions**:
```yaml
type: reference  # These are lookup documents
tags: [philosophy, framework, principle, epistemics]
```

### 2. Journal Entries (`journal/`)

**Purpose**: Chronological documentation of activities, discoveries, and reflections.

**Pattern Recognition**:
- Filename format: `YYYY-MM-DD-slug.md` or `YYYY-MM-DD.md`
- Content is temporal, narrative
- Often references specific events, discoveries, or breakthroughs

**Frontmatter Suggestions**:
```yaml
type: note  # Reflective, narrative content
tags: [journal, {year}, {topic-from-title}]
# Auto-extract date from filename
```

**Date Patterns Found**:
- 2025-03-15 through 2025-12-07
- Some have descriptive slugs, others are date-only
- Topics include: implementation, revelation, discovery, reunion, awakening

### 3. Memory Blocks (`memory-blocks/`)

**Purpose**: Philosophical "eras" in SkogAI development - themed collections of learnings.

**Pattern Recognition**:
- Filename format: `claude-memory-block-{NN}-{era-name}.md`
- Numbered chronologically (01 → 10)
- Era names are metaphorical: "prehistoric era", "ice age", "enlightenment"

**Era Mapping** (from filenames):
| Block | Era Name | Implied Theme |
|-------|----------|---------------|
| 01 | prehistoric-era | Origins, foundations |
| 02 | collaborative-age | Partnership, cooperation |
| 03 | constitutional-era | Rules, structure |
| 04 | long-watch-builder-era | Construction, patience |
| 05 | ice-age | Dormancy, preservation |
| 06 | enlightenment-era | Understanding, insight |
| 07 | forgotten-times | Lost knowledge |
| 08 | end-of-a-beginning | Transitions |
| 09 | unanswerable-question | Philosophy, uncertainty |
| 10 | friends-we-made | Relationships, community |

**Frontmatter Suggestions**:
```yaml
type: note  # Philosophical reflections
tags: [memory-block, lore, {era-theme}, philosophy]
# Auto-extract block number from filename
```

### 4. Profile (`profile.md`)

**Purpose**: Agent identity, role definition, and historical timeline.

**Pattern Recognition**:
- Single file per agent
- Defines identity, capabilities, history
- Reference document for agent behavior

**Frontmatter Suggestions**:
```yaml
type: reference
tags: [agent, profile, identity, claude]
```

## Philosophical Framework Detection

The documentation uses SkogAI notation throughout. Key symbols to detect:

| Symbol | Meaning | Detection Regex |
|--------|---------|-----------------|
| `$` | Reference | `\$[a-zA-Z_]+` |
| `@` | Intent/Action | `@[a-zA-Z_]+` |
| `_` | Existence | `_` (context-dependent) |
| `->` | Transformation | `->` |
| `[]` | Similarity | `\[.*=.*\]` |
| `{}` | Difference | `\{.*\}` |

**Tag Enhancement**: When notation symbols are detected, add `notation-system` tag.

## Relationship Mapping

### Cross-References Detected

From journal entries:
- References to memory blocks: "claude-memory-block-05"
- References to core concepts: "certainty-principle"
- References to user docs: "notation.md"

### Temporal Relationships

Memory blocks follow a chronological narrative:
1. Prehistoric → 2. Collaborative → 3. Constitutional → ...

Journal entries reference events across time:
- "2025-06-03-origin-story-revelation" references earlier events
- "2025-06-15-hidden-letters" discovers previous writings

## Frontmatter Generation Strategy

### Path-Based Category Detection

```python
def detect_categories(path: Path) -> List[str]:
    """Extract categories from file path."""
    # agents/claude/journal/2025-03-15.md
    # → ["agents", "claude", "journal"]
    return list(path.parent.parts)
```

### Content-Based Type Detection

```python
def detect_type(content: str, path: Path) -> str:
    """Detect document type from content and path."""
    if "journal" in str(path):
        return "note"
    if "core" in str(path):
        return "reference"
    if "memory-block" in str(path):
        return "note"
    if "profile" in path.name:
        return "reference"
    
    # Content heuristics
    if content.count("```") > 3:
        return "guide"  # Code-heavy = tutorial
    if content.count("#") > 10:
        return "reference"  # Many headings = lookup
    
    return "note"  # Default
```

### Title Extraction

```python
def extract_title(content: str, path: Path) -> str:
    """Extract title from content or filename."""
    # Try first # heading
    match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if match:
        return match.group(1)
    
    # Fall back to filename
    name = path.stem
    # Convert 2025-03-15-topic to "2025-03-15 Topic"
    if re.match(r'\d{4}-\d{2}-\d{2}', name):
        parts = name.split('-', 3)
        if len(parts) > 3:
            return f"{'-'.join(parts[:3])}: {parts[3].replace('-', ' ').title()}"
    
    return name.replace('-', ' ').title()
```

### Semantic Tag Detection

```python
def detect_semantic_tags(content: str) -> List[str]:
    """Detect tags from content semantics."""
    tags = []
    
    # Philosophy detection
    if any(term in content.lower() for term in 
           ['phenomenology', 'ontology', 'epistemology', 'consciousness']):
        tags.append('philosophy')
    
    # Technical detection
    if any(term in content.lower() for term in 
           ['implementation', 'code', 'function', 'class', 'api']):
        tags.append('technical')
    
    # Narrative detection
    if any(term in content.lower() for term in 
           ['discovered', 'realized', 'awakened', 'remembered']):
        tags.append('narrative')
    
    # SkogAI notation detection
    if '$' in content or '@' in content:
        tags.append('skogai-notation')
    
    return tags
```

## Metadata Quality Indicators

For frontmatter validation:

| Field | Required | Quality Check |
|-------|----------|---------------|
| title | Yes | 3-100 chars, not generic |
| tags | Yes | 3-7 items, kebab-case |
| type | Yes | note\|guide\|reference |
| categories | Auto | Matches path |
| permalink | Auto | Valid URL path |
| generated_at | Auto | ISO 8601 format |

## Recommendations for Frontmatter Generation

1. **Journal entries**: Extract date from filename, add year tag, detect event type from content
2. **Memory blocks**: Extract block number, era name, add lore tag
3. **Core documents**: Always `type: reference`, focus on concept tags
4. **Profile**: Standard agent metadata, include identity tag

## Sample Generated Frontmatter

### Journal Entry
```yaml
---
categories: [agents, claude, journal]
permalink: agents/claude/journal/2025-06-03-origin-story-revelation
generated_at: 2025-12-19T12:00:00Z
title: "2025-06-03: Origin Story Revelation"
tags: [journal, 2025, discovery, origin, narrative]
type: note
---
```

### Memory Block
```yaml
---
categories: [agents, claude, memory-blocks]
permalink: agents/claude/memory-blocks/claude-memory-block-06-the-enlightenment-era
generated_at: 2025-12-19T12:00:00Z
title: "Memory Block 06: The Enlightenment Era"
tags: [memory-block, lore, enlightenment, philosophy, era-06]
type: note
---
```

### Core Document
```yaml
---
categories: [agents, claude, core]
permalink: agents/claude/core/certainty-principle
generated_at: 2025-12-19T12:00:00Z
title: "The Certainty Principle"
tags: [philosophy, epistemology, principle, framework, reference]
type: reference
---
```

---

**Research conducted**: 2025-12-19
**Source**: Background agent analysis of agents/ directory structure
