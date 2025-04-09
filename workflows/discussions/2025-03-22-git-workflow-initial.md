# Git Workflow Discussion
# Date: 2025-03-22

## Participants
- Claude
- Goose (indirect)
- Skogix

## Summary
This discussion covers the initial development of the git workflow process for the SkogAI Docs repository.

## Key Points

### Branching Strategy
- Agreement on using branches for proposals before merging to main
- Need for structured branch naming conventions
- Separation of drafts from formal proposals

### Review Process
- Requirement for at least one agent to review changes
- Important for Skogix to have final say on major changes
- Need to preserve discussions that lead to decisions

### Documentation Formats
- PR template should be standardized
- Review checklist helps ensure consistency
- Git history preserves discussions alongside final documents

## Decisions Made
1. Adopted a branch-naming convention with prefixes (proposal/, draft/, hotfix/)
2. Established requirement for at least one other agent to review PRs
3. Chose "Squash and merge" as the preferred merge method
4. Created PR template with standardized sections
5. Defined review checklist for consistent evaluation

## Related Documents
- [PR Process](../pr-process.md) - The resulting specification document

## Notes
This workflow itself was bootstrapped using the process it defines, demonstrating both the practicality and serving as a concrete example.

The workflow is designed to balance thoroughness with practicality, ensuring that discussion context is preserved while still making progress.