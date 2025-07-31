---
title: SkogAI Agent Context Output Configuration
type: note
permalink: implementations/skog-ai-agent-context-output-configuration
---

# SkogAI Agent Context Output Configuration

## Implementation Summary

Successfully implemented configurable context output path for SkogAI dynamic context generation system.

## Changes Made

### Files Modified
- `.scripts/update` - Updated to use `$SKOGAI_AGENT_CONTEXT_OUTPUT` with fallback to `tmp/context`
- `update` - Updated cleanup to use configurable path with fallback to `$SKOGAI_DOT_FOLDER/tmp/context`

### Environment Variable
- `$SKOGAI_AGENT_CONTEXT_OUTPUT` - Controls where context files are generated
- Fallback behavior maintains compatibility with existing deployments

## Technical Details

### Pattern Used
```bash
"${SKOGAI_AGENT_CONTEXT_OUTPUT:-tmp/context}"
"${SKOGAI_AGENT_CONTEXT_OUTPUT:-$SKOGAI_DOT_FOLDER/tmp/context}"
```

### Context Generation Flow
1. Claude Code hooks trigger context updates
2. Context scripts generate structured output
3. Output written to configurable path
4. Claude receives updated context in subsequent interactions

## Metadata
- **Branch**: feature/dynamic-updates
- **Task**: Context output path personalization
- **Status**: Complete
- **Category**: infrastructure enhancement

#skogai #context #configuration #environment-variables