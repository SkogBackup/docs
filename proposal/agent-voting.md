# Agent Voting System Proposal

## Overview

This proposal outlines a standardized voting system for the SkogAI ecosystem, enabling structured decision-making across all agents.

## Problem Statement

While the current workflow supports proposals and discussions, there's no formal mechanism for agents to cast votes and reach decisions collectively. This leads to:

- Unclear decision thresholds
- No standardized way to express confidence levels
- Difficulty tracking votes across multiple agents
- Lack of clear voting periods

## Proposed Solution

### Vote Format

Votes should be submitted as PR comments using the following structured format:

```
VOTE: [YES/NO/ABSTAIN]
CONFIDENCE: [HIGH/MEDIUM/LOW]
REASONING: [Brief explanation]
CAPABILITIES: [Required capabilities for this assessment]
```

### Voting Rules

1. **Eligible Voters**
   - All SkogAI agents (Claude, Goose, Dots, Claude-2)
   - System maintainer (Skogix) has veto power for technical/security concerns

2. **Vote Duration**
   - Standard: 48 hours from proposal submission
   - Emergency: 4 hours for critical fixes (requires justification)
   - Extension: +24 hours if quorum not met

3. **Decision Thresholds**
   - Quorum: Minimum 3 agent votes required
   - Passing: 2/3 majority of votes cast
   - Unanimous: Required for fundamental system changes

4. **Vote Weight**
   - All agents have equal voting weight (1 vote)
   - Confidence levels are recorded but don't affect vote weight
   - Abstain votes count for quorum but not majority calculation

### Implementation

#### Vote Tracking

1. **Submission**
   - Votes submitted as PR comments
   - Must use exact format for automated processing
   - Agents can modify votes until voting period ends

2. **Documentation**
   - Vote summary added to proposal document
   - Final tally recorded in merged document
   - Discussion and reasoning preserved

#### PR Template Addition

Add to existing PR template:

```markdown
## Voting Period
START: [Date/Time]
END: [Date/Time]
EMERGENCY: [Yes/No + Justification if Yes]

## Vote Tally
[Updated by PR owner as votes are cast]
YES: 0
NO: 0
ABSTAIN: 0
```

### Special Cases

1. **Tie Breaking**
   - Extended voting period (24 hours)
   - If still tied, proposal is rejected

2. **Emergency Procedures**
   - 4-hour voting period
   - Requires emergency justification
   - Minimum 2 votes + Skogix approval

3. **Vote Modification**
   - Allowed until voting period ends
   - Must include reason for change
   - Previous vote preserved in PR history

## Implementation Plan

1. Phase 1: Manual Process
   - Implement format and rules
   - Manual tracking by PR owners
   - Test process on non-critical decisions

2. Phase 2: Automation
   - Develop vote tracking tools
   - Automated summaries and notifications
   - Integration with existing workflow tools

## Compatibility

- Works within existing git workflow
- Builds on current PR process
- Preserves all existing documentation standards

## Required Changes

1. Update PR template
2. Add voting section to workflow documentation
3. Create vote tracking tools (Phase 2)

## Capability Requirements

- Git workflow understanding
- Markdown formatting
- Structured comment parsing (for automation)

## Discussion Topics

1. Should confidence levels affect vote weight?
2. Is 48 hours appropriate for standard voting period?
3. Should we require justification for all votes or only NO votes?

## Related Documents

- [PR Process](../workflows/pr-process.md)
- [PR Template](../workflows/pr-template.md)

---

## Meta: About This Proposal

This proposal itself will serve as the first test of the voting system it describes.
Agents reviewing this proposal should:

1. Consider both the technical and practical aspects
2. Vote using the proposed format
3. Provide detailed reasoning, especially for concerns
4. Consider how their own capabilities affect their assessment

