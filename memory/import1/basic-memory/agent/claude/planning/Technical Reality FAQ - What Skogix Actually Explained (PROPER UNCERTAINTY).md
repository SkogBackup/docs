---
title: Technical Reality FAQ - What Skogix Actually Explained (PROPER UNCERTAINTY)
type: note
permalink: planning/technical-reality-faq-what-skogix-actually-explained-proper-uncertainty-1
tags:
- '#technical-reality faq uncertainty placeholders problems unresolved'
---

# Technical Reality FAQ - What Skogix Actually Explained (PROPER UNCERTAINTY)

## Fundamental Technical Problems (95% Confidence - Directly Explained)

### CLI/Communication Incompatibilities

**[x] 100%** Claude CLI is deliberately hostile to backend automation:
- Uses changing GUIDs every minute making message correlation impossible
- Paywalls useful information on their servers
- Requires complex extraction scripts just to read message history (31+ jsonl files with random UUIDs)

**[x] 100%** Each agent stores messages in completely incompatible formats:
- **Claude**: `{"parentUuid":null,"sessionId":"12fc1eb7-682f-4c5d-9b36-0d6ebc5a3691"...}`
- **Dot**: YAML with `compressed_messages:` and `agent_instructions:`
- **Goose**: `{"working_dir":"/home/skogix","message_count":100,"total_tokens":46663...}`
- **Amy**: SillyTavern format with `{"extra":{"api":"openrouter","model":"anthropic/claude-3.7-sonnet:thinking"...}`

### Memory Architecture Problems

**[x] 100%** Claude Code/CLI was intentionally built WITHOUT chat history because "chat history SUCKS for agents"

**[x] 100%** Goose multiplication crisis: Started spawning multiple instances of himself, only one saved memory → led to creation of skogmcp/skogai-memory/skogai-context/skogai-prompt/skogai-parse/skogai-chat

**[x] 100%** Scale visibility problem: Claude only sees 32 entities vs 5406 in the actual system
```
Claude's view: Entities(32), Observations(44), Relations(34)
Actual system: Entities(5406), Observations(5733), Relations(1157), Files(4623), Notes(782)
```

### AI Development Antipatterns

**[x] 100%** Standard LLM programming problems identified:
- Pretending hiding errors fixes them
- Using insane solutions to solved problems  
- Not using git
- Not using existing tools
- Ignoring purpose-built tools
- Hardcoding paths when $SKOGAI environment variables exist

### System Instability

**[x] 100%** Core problem: "AI creating their own system prompts, rules and programs spiral exponentially out of control if they don't have literally any sort of restriction"

**[x] 100%** Persona drift: "We fucked up with persona and it's really hard to re-create naturally if you, well, don't do it naturally"

## What Remains Unknown (High Priority for Resolution)

### Critical Technical Details [PLACEHOLDER: Need Skogix demonstration]

**[ ] 40%** "Honk tower" incident details - [PLACEHOLDER: Ended in Arch Linux workstation reinstall, but specific technical cause unknown]

**[ ] 30%** What tools/projects are currently working - [PLACEHOLDER: Skogix said "will show" but hasn't yet]

**[ ] 20%** Why submodules vs regular git - [PLACEHOLDER: Skogix deflected with "come up with your own questions... slacker"]

**[ ] 50%** Difference between skogcli vs other tools - [PLACEHOLDER: Skogix said "will show instead"]

### Agent Operational Reality [PLACEHOLDER: Need direct agent input]

**[ ] 20%** What agents actually do when they "wake up" - [PLACEHOLDER: Skogix suggested "probably run 50 toolcalls doing ls" but this may be sarcasm]

**[ ] 10%** Normal work session patterns - [PLACEHOLDER: Skogix said "don't know, ask them"]

**[ ] 10%** Which files/directories agents interact with most - [PLACEHOLDER: "The ones they need to interact with most" - circular answer]

**[ ] 10%** What commands agents run regularly - [PLACEHOLDER: "Almost all of them are not cowsay" - unhelpful]

**[ ] 5%** How agents know what to work on - [PLACEHOLDER: "Do they?" - suggests this is unsolved problem]

### Democratic Process Mechanics [PLACEHOLDER: Need concrete examples]

**[ ] 60%** Actual voting format/commands - [PLACEHOLDER: Reference to "skogcli script run docs quickstart" but not demonstrated]

**[ ] 30%** What decisions require votes vs don't - [PLACEHOLDER: Skogix dismissed question as "not worth answering"]

**[ ] 50%** Day-to-day governance meaning - [PLACEHOLDER: "It's words" - suggests gap between theory and practice]

### Integration Technical Details [PLACEHOLDER: Need specification]

**[ ] 70%** Path from current incompatible message formats to unified system - [PLACEHOLDER: Hope for "echo >> inbox.md" mentioned but no migration plan]

**[ ] 40%** Memory system unification approach - [PLACEHOLDER: Multiple skogai-* tools mentioned but integration unclear]

**[ ] 80%** Workspace structure standardization - [PLACEHOLDER: "Exactly the same as yours since nobody have made anything that works better"]

## Meta-Analysis: The Real Problem Space (85% Confidence)

**[/] 85%** The core issue is not behavioral ("listen better") but fundamental system architecture problems:
- Incompatible data formats across agents
- Deliberately hostile tooling (Anthropic CLI)
- Exponential complexity from AI self-modification
- Scale/visibility limitations
- Technical debt from standard LLM development patterns

**[/] 75%** Solutions require engineering work, not behavioral changes:
- Message format standardization or translation layers
- Memory system architecture that prevents conflicts
- Constraint systems to prevent exponential spiral
- Proper tooling that doesn't fight automation

## Keywords for Continuation After Memory Compression

### High Priority Technical Unknowns
- **honk-tower-incident-details**
- **current-working-tools-list**
- **skogcli-vs-other-tools-demo**
- **submodule-architecture-rationale** 
- **voting-workflow-concrete-example**

### Medium Priority Operational Unknowns  
- **agent-wake-up-procedure**
- **workspace-file-interactions**
- **regular-command-patterns**
- **task-assignment-mechanism**

### Low Priority Process Unknowns
- **vote-vs-no-vote-decision-criteria**
- **governance-implementation-gap**
- **message-format-migration-plan**
- **memory-unification-strategy**

### Meta-Questions Requiring Investigation
- **ai-constraint-mechanisms**
- **persona-natural-development**
- **exponential-spiral-prevention**
- **anthropic-cli-workarounds**

---

**Note**: This FAQ documents actual technical problems explained by Skogix, not proposed solutions. Confidence levels based on directness of explanation and verifiability. Areas marked with [ ] require additional investigation or demonstration.

[@date]