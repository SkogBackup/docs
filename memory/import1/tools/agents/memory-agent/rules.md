# SkogAI Memory Rules and Guidelines

## Core Rules

1. **Filename Standards**
   - Use lowercase for all filenames
   - Use hyphens for word separation (kebab-case)
   - Avoid spaces, underscores, and special characters
   - Keep names concise but descriptive

2. **Required Elements**
   - Every file must have a title as the first heading (# Title)
   - Every file must include an observations section
   - Every file must include a relations section
   - Every file should include a summary under the title

3. **Observation Format**
   ```markdown
   ## observations
   - [category] Description text #tag1 #tag2 (optional context)
   ```

4. **Relation Format**
   ```markdown
   ## relations
   - relation_type [[linked-document]] (optional context)
   ```

5. **Semantic Density**
   - Each file should contain at least 3-5 observations
   - Each file should establish at least 2-3 relations
   - Relations should use specific types rather than generic connections

## Mandatory Structure

```markdown
# Title of Document

## Summary
Brief overview of the content.

[Main content sections with appropriate headings]

## observations
- [category] Observation 1 #tag1 #tag2
- [category] Observation 2 #tag3
- [category] Observation 3 #tag4 #tag5

## relations
- relation_type [[Document A]] (context)
- another_relation [[Document B]] (context)
```

## Content Quality Guidelines

1. **Titles** should be:
   - Clear and descriptive
   - Focused on the primary topic
   - Consistent with related documents
   - Usually 2-6 words in length

2. **Summary** should:
   - Provide a quick understanding in 1-3 sentences
   - Highlight the most important aspects
   - Include key terminology for searchability

3. **Observations** should be:
   - Single ideas or facts (one idea per observation)
   - Appropriately categorized
   - Tagged for discoverability
   - Clear and concise

4. **Relations** should:
   - Use the most specific relation type that applies
   - Connect to truly relevant documents
   - Include helpful context when needed
   - Create a cohesive knowledge network

## Common Issues to Check

- [ ] Missing observations section
- [ ] Missing relations section
- [ ] Uncategorized observations (missing [category])
- [ ] No tags on observations
- [ ] Generic relation types when specific ones apply
- [ ] Too few observations (less than 3)
- [ ] Too few relations (less than 2)
- [ ] Title doesn't match filename
- [ ] Filename not in kebab-case
- [ ] Missing summary section

## Validation Process

When creating or updating memory entries, the validation process includes:

1. **Structural Validation**: Checking for required sections
2. **Content Validation**: Ensuring content quality and completeness
3. **Relation Validation**: Verifying relation targets exist or are created as forward references
4. **Formatting Validation**: Confirming the document follows markdown standards

## observations

- [fact] Every SkogAI Memory file must include observations and relations sections #requirements
- [principle] Consistent formatting is essential for automation and tool integration #standards
- [technique] Using categorized observations creates a semantically rich knowledge base #semantics
- [requirement] Filenames must use kebab-case (lowercase with hyphens) #naming-conventions
- [requirement] Each entry should establish connections with at least 2-3 related documents #connectivity

## relations

- implements [[documentation-standards]] (provides rules for structured content)
- part_of [[skogai-memory-system]] (defines system requirements)
- relates_to [[memory-validation-process]] (establishes validation criteria)
- foundation_for [[automated-tools]] (enables tooling through consistent structure)