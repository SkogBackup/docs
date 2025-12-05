---
title: questions-review-session
type: note
permalink: agent/claude/questions-review-session
---

# Questions Review Session - August 9, 2025

## Outstanding Questions to Address

### Architecture Questions for System We're Building
1. What should the $SKOGAI_DOT_CONTEXT/update script contain?
2. How should it generate $SKOGAI_PWD/tmp/context files?
3. What argc commands/options should skogcontext provide?
4. How does the modular split work (agent-context vs agent-git-flow)?
5. How should the modular pieces interact?
6. What are the actual requirements for the agent-context tool?
7. How does the SKOGAI_DOT_FOLDER mechanism work?
8. How does the wrapper pattern (agent-git -> Argcfile.sh) function?

### Context System Questions
1. How is the context data structured and generated?
2. What are all the different context sections and their purposes?
3. How does the timestamp and dynamic updating work?
4. How does the system detect and reflect changes?
5. What other context sources exist beyond git?
6. What are these remaining environment variables for:
   - `$LLM_OUTPUT` - Where does LLM output get written?
   - `$SKOGAI_PWD` - Working directory context?
   - `$ARGC_PWD` - Working directory for argc operations?
   - `$SKOGAI_DOT_CONTEXT` - Current context folder in use?

### Modular argc System Design Questions
1. **Static vs Agent Balance**: Which context generation tasks should be static tools vs agent-specific?
2. **Module Auto-Discovery**: Should `./.context/modules/` be scanned automatically or explicitly configured?
3. **Environment Variable Patterns**: Should `SKOGAI_MODULE_*` variables point to directories or individual scripts?
4. **Context Formatting**: Should section names always default to script basename?
5. **Error Handling Strategy**: Let individual argc module errors bubble up?

### From run.md
- Should there be a `./run` script or `./Argcfile.sh`?
- What argc commands should skogcontext provide?
- How should it integrate with the context generation system?
- What relationship should it have with `./update`?

## Ready to Start Next Phase
These questions need answers before proceeding with implementation.
