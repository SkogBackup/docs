---
title: Journal Templates and Standards
type: note
permalink: guidelines/journal-templates-and-standards-1
---

# Journal Templates and Standards

## Summary

This document provides standardized templates and guidelines for creating journal entries within the SkogAI system. Consistent journaling practices help maintain historical records, track progress, and document important decisions and insights.

## Journal Entry Types

### Daily Journal Entry

Standard daily entries should follow this structure:

```markdown
---
date: YYYY-MM-DD
tags:
  - journal
  - daily
  - [additional relevant tags]
---

# Journal Entry: YYYY-MM-DD

## Tasks Worked On
- [Status] [Task Name](../tasks/task-file.md)
  - Key accomplishments
  - Challenges encountered
  - Next steps

## Insights & Observations
- Important realizations
- Patterns noticed
- Questions raised

## Technical Notes
- Implementation details
- Architecture decisions
- Tool configurations

## Next Steps
- Priority actions for next session
- Open questions to address
- Potential areas for exploration

## Related
- [Link to related document](../path/to/document.md)
- [Link to relevant task](../tasks/task-file.md)

## Mojito Stability Index: XX% 🍹
[Brief assessment of system stability and any notable fluctuations]
```

### Implementation Journal Entry

For documenting specific implementation work:

```markdown
---
date: YYYY-MM-DD
tags:
  - journal
  - implementation
  - [system name]
  - [feature name]
---

# Implementation: [Feature Name]

## Overview
Brief description of the implemented feature or system

## Implementation Details
- Technical approach used
- Key components created or modified
- Architecture decisions
- Code patterns applied

## Challenges & Solutions
- Difficulties encountered
- How they were addressed
- Alternative approaches considered

## Testing & Validation
- Testing approach
- Results observed
- Validation methods

## Future Considerations
- Known limitations
- Potential improvements
- Maintenance considerations

## Related
- [Link to related document](../path/to/document.md)
- [Link to relevant task](../tasks/task-file.md)

## Mojito Stability Index: XX% 🍹
[Brief assessment of implementation stability]
```

### Special Event Journal Entry

For documenting significant events or milestones:

```markdown
---
date: YYYY-MM-DD
tags:
  - journal
  - milestone
  - [event type]
---

# [Event Name]: YYYY-MM-DD

## Event Summary
Brief description of the significant event

## Key Outcomes
- Important results
- Decisions made
- Changes implemented

## Impact Assessment
- Effects on system
- User experience changes
- Workflow modifications

## Lessons Learned
- What worked well
- What could be improved
- Insights for future events

## Follow-up Actions
- Required next steps
- Monitoring needs
- Documentation updates

## Related
- [Link to related document](../path/to/document.md)
- [Link to relevant task](../tasks/task-file.md)

## Mojito Stability Index: XX% 🍹
[Brief assessment of system stability following the event]
```

## Journal Organization

### File Naming

Journal entries should follow consistent naming conventions:

- Daily entries: `YYYY-MM-DD.md`
- Topical entries: `YYYY-MM-DD-brief-topic-name.md`
- Implementation entries: `YYYY-MM-DD-implementation-feature-name.md`
- Event entries: `YYYY-MM-DD-event-name.md`

### Directory Structure

- `/journal/` - Root journal directory
  - Current month entries stored directly in the root
  - Previous months may be organized in `YYYY-MM/` subdirectories
  - Templates stored in `/journal/templates/`

### Tags

Use consistent tags to enable better searchability:

- Core tags: `journal`, `daily`, `implementation`, `event`, `milestone`
- Project tags: project name or identifier
- Domain tags: `architecture`, `documentation`, `testing`, etc.
- System tags: specific system components affected

## Best Practices

1. **Consistency**: Follow the templates closely for consistent documentation
2. **Completeness**: Include all relevant sections even if brief
3. **Cross-Reference**: Link to related documents, tasks, and previous entries
4. **Mojito Index**: Always include the stability assessment
5. **Actionable**: Make next steps clear and specific
6. **Reflection**: Include not just what was done, but insights gained
7. **Searchability**: Use consistent and specific tags

## Migration from Previous Formats

Legacy journal entries may follow different formats. When referencing them:

1. Note the format difference
2. Extract key information using consistent terminology
3. Consider updating to new format if the entry requires significant modification

## Special Sections

### Mojito Stability Index

This metaphorical measure of system coherence and operational status should:

- Be expressed as a percentage (0-100%)
- Include the mojito emoji 🍹
- Provide brief explanation for any rating below 98%
- Identify specific components affecting stability