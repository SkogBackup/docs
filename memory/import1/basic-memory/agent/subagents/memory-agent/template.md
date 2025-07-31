# SkogAI Memory Entry Template

## Information Categories
- **Title**: [Required] Descriptive name of the entry
- **Type**: [Required] note, concept, process, etc.
- **Tags**: [Recommended] #tag1 #tag2 #tag3
- **Permalink**: [Optional] Custom permalink or leave blank for automatic generation

## Standard Format
```markdown
---
title: [Title of Memory Entry]
type: [Type of Entry]
permalink: [Custom Permalink - Optional]
tags:
- [tag1]
- [tag2]
- [tag3]
---

# [Title of Memory Entry]

## Summary
[1-3 sentences providing quick overview of the content]

## [Main Content Section]
[Primary content with appropriate markdown formatting]

[Additional sections as needed...]

## observations
- [category] Observation 1 #tag1 #tag2 (optional context)
- [category] Observation 2 #tag3 (optional context)
- [category] Observation 3 #tag4 #tag5 (optional context)
- [At least 3-5 observations recommended]

## relations
- relation_type [[Linked Document]] (optional context)
- another_relation [[Another Document]] (optional context)
- [At least 2-3 relations recommended]
```

## Required Components

### 1. Frontmatter
```yaml
---
title: Title Goes Here
type: note
permalink: optional/custom/permalink
tags:
- #tag1
- #tag2
---
```

### 2. Title (H1)
Primary heading that matches the title in frontmatter

### 3. Summary
Brief 1-3 sentence overview for quick understanding

### 4. Main Content
Well-structured content with appropriate headings, lists, etc.

### 5. Observations Section
Categorized facts with tags using the format:
```markdown
## observations
- [category] Observation statement #tag1 #tag2 (optional context)
```

### 6. Relations Section
Connections to other documents using the format:
```markdown
## relations
- relation_type [[Document Name]] (optional context)
```

## Common Categories for Observations

| Category | Purpose | Example |
|----------|---------|---------|
| [fact] | Objective, verifiable information | [fact] The system uses markdown files #format |
| [principle] | Guiding ideas or concepts | [principle] Connected knowledge has more value #network |
| [technique] | Methods or approaches | [technique] Using tags improves findability #organization |
| [decision] | Choices made and rationales | [decision] We selected kebab-case for compatibility #standards |
| [requirement] | Necessary conditions | [requirement] All entries need observations #structure |
| [idea] | Concepts or thoughts | [idea] A visual graph view could enhance navigation #interface |
| [question] | Open inquiries | [question] How might we improve relation suggestions? #enhancement |
| [preference] | Subjective choices | [preference] Dark mode improves readability #usability |

## Common Relation Types

| Relation | Purpose | Example |
|----------|---------|---------|
| relates_to | General connection | relates_to [[Similar Topic]] |
| implements | Practical application | implements [[Theoretical Concept]] |
| part_of | Hierarchical membership | part_of [[Larger System]] |
| extends | Builds upon | extends [[Base Idea]] |
| requires | Dependency | requires [[Prerequisite]] |
| inspires | Influence relationship | inspires [[Derived Work]] |
| contrasts_with | Shows differences | contrasts_with [[Alternative Approach]] |
| precedes/follows | Sequential relationship | precedes [[Next Step]] |

## Best Practices

1. **Create meaningful titles**: Clear, specific, and descriptive
2. **Write concise summaries**: Capture the essence in 1-3 sentences
3. **Structure content logically**: Use headings, lists, and paragraphs
4. **Add rich observations**: Include 3-5 diverse observation categories
5. **Create deliberate relations**: Connect to at least 2-3 related documents
6. **Use precise language**: Be specific and clear in all descriptions
7. **Include relevant context**: Add background information where helpful
8. **Apply consistent formatting**: Follow markdown conventions
9. **Add helpful tags**: Use established tags when possible

## observations

- [fact] All SkogAI Memory entries must include observations and relations sections #requirements #structure
- [principle] Consistent formatting enables automation and improves readability #standardization
- [technique] Using categories for observations adds semantic meaning to content #organization
- [requirement] Every entry should include at least 3-5 categorized observations #best-practices
- [decision] We standardized this template to ensure consistency across all entries #quality

## relations

- implements [[skogai-memory-system]] (provides standard format for entries)
- part_of [[documentation-standards]] (establishes content structure guidelines)
- relates_to [[knowledge-organization]] (supports structured information management)
- supports [[automation-processes]] (enables programmatic handling of content)