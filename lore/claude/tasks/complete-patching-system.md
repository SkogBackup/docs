---
title: Complete the Patching System Implementation
state: new
priority: high
type: feature
created: "2025-06-05"
tags: [infrastructure, patching, system]
depends: []
---

# Complete the Patching System Implementation

## Context

Old Claude started implementing a patching system for the SkogAI ecosystem but it's incomplete. The system needs to handle two levels of patches:

1. **System patches**: gptme-base → skogai-base (infrastructure improvements)
2. **Agent patches**: skogai-base → individual agent workspaces

## Problem

The bootstrap challenge: The first system patch should be "the patch system itself" - we need to use the patch system to install the patch system.

## Current Structure

```
~/skogai/agent/
├── gptme-base/     # upstream gptme
├── skogai-base/    # SkogAI origin with system patches applied
├── claude/         # my workspace (agent patches applied)
└── [other agents]/ # other agent workspaces
```

## Requirements

### System Patches (gptme-base → skogai-base)
- [ ] Patch system infrastructure itself
- [ ] fork.sh functionality
- [ ] Core SkogAI improvements that benefit all agents
- [ ] Standardized run.sh implementations
- [ ] Context system enhancements

### Agent Patches (skogai-base → agents)
- [ ] Agent-specific customizations
- [ ] Individual context configurations
- [ ] Personality/workflow differences
- [ ] Agent-specific tools and scripts

## Technical Challenges

1. **Bootstrap Problem**: How to use the patch system to install itself
2. **Aider Integration**: Previous attempts with aider failed after 2+ hours
3. **Bidirectional Flow**: Agents should be able to contribute improvements back up
4. **Conflict Resolution**: How to handle merge conflicts in patches

## Success Criteria

- [ ] Can apply system patches from gptme-base to skogai-base automatically
- [ ] Can fork new agents from skogai-base with agent-specific patches
- [ ] Patch system is self-hosting (uses itself to update itself)
- [ ] Clear documentation for adding new patches
- [ ] Backward compatibility maintained

## Next Steps

1. Examine the current patch system implementation in claude/scripts/patch/
2. Identify what old Claude completed vs what's missing
3. Design the bootstrap solution for self-hosting patch system
4. Implement missing components
5. Test with a simple system patch
6. Document the complete workflow

## Notes

- This is foundational infrastructure - once working, it enables rapid agent ecosystem development
- The fork.sh functionality is part of this system
- Should integrate with the context system work we just completed
