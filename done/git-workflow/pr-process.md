# Git Workflow Process

## Overview
This document outlines the standard git workflow for the SkogAI ecosystem. This process ensures that changes are properly reviewed, discussed, and documented before becoming official.

## Branching Strategy

### Branch Types
- `main`: The official, approved documentation
- `proposal/{topic}`: Proposed changes or additions
- `draft/{topic}`: Early work-in-progress changes
- `hotfix/{topic}`: Urgent corrections

### Branch Naming Convention
- Use lowercase with hyphens for readability
- Include a descriptor of the content 
- Examples:
  - `proposal/context-system-architecture`
  - `proposal/mcp-integration-standards`
  - `draft/agent-communication-protocol`

## Pull Request Process

### 1. Branch Creation
1. Create a branch from `main` with appropriate prefix
   ```bash
   git checkout -b proposal/my-proposal main
   ```
2. Make your changes, following document templates
3. Commit with descriptive messages
   ```bash
   git commit -m "docs: Add context system implementation guidelines"
   ```

### 2. Pull Request Submission
1. Push your branch to the repository
   ```bash
   git push -u origin proposal/my-proposal
   ```
2. Create a pull request via GitHub
3. Fill out the PR template
4. Add appropriate reviewers (at least one other agent)

### 3. Review Process
1. Reviewers examine proposed changes
2. Discussion happens in PR comments
3. Discussion summaries should be preserved in the document
4. Address feedback with additional commits
5. Re-request review after addressing feedback

### 4. Approval and Merging
1. Requires approval from at least one other agent
2. May require approval from Skogix for major changes
3. Merge using the "Squash and merge" option
4. PR title becomes the commit message
   - Use format: `docs: Short descriptive title`
5. Delete branch after merging

## PR Template

```markdown
## Proposal Description
[Brief description of the proposed documentation]

## Motivation
[Why is this documentation needed?]

## Reviewers
[List required reviewers]

## Related Work
[Link to related discussions or documents]

## Special Considerations
[Any compatibility or implementation notes]
```

## Review Checklist

Reviewers should ensure the document:
- [ ] Follows documentation standards
- [ ] Includes capability markers if relevant
- [ ] Preserves important discussion context
- [ ] Uses clear, consistent terminology
- [ ] Has proper cross-references to related documents
- [ ] Considers legacy system compatibility if applicable

## Discussion Preservation

The git workflow itself serves as the mechanism for discussion preservation:
1. Discussions happen in PR comments
2. Important points are summarized in the document itself
3. PR history preserves the complete discussion context
4. Closed PRs remain accessible for historical reference

## Amendment Process

To amend existing documentation:
1. Create a new branch from `main`
2. Make changes to the existing document
3. Follow the standard PR process
4. Reference the original PR in your new PR description

---

This document itself was created following this process, serving as both an example and the initial standard.