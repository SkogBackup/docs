---
name: skogai-project-lifecycle
description: Navigate SkogAI's dual workflow system - explosive creative phase using skogix personal plugin setup and the controlled and production-ready phase skogai/claude where all of SkogAI's experience comes into play with long term goals and strategies. Use when starting new features, deciding when to migrate work, planning a workflow or tooling setup or understanding the pruning process that is core to SkogAI's philosophy.
---

<objective>
Guide navigation between SkogAI's two development workflows: explosive creative experimentation and production-ready implementation.
</objective>

<essential_principles>

## The Dual System

**`.skogai/skogix/` - Explosive Phase**

- Try everything, fail fast, MVP focus
- "Spew tokens all over the place" - half won't work, that's fine
- No constraints, rapid iteration
- Prove it works first

**`.skogai/claude/` - Production Phase**

- Tested, pruned, well-oiled
- Functional-first (F#), high test coverage
- Anti-bloat principles enforced
- Make it perfect after proving it works

## The Flow

```
explosive → test/validate → prune → polish → production
```

Each phase has different tools, constraints, and success criteria.

</essential_principles>

<intake>
Where are you in the lifecycle?

1. Starting new feature/idea (explosive phase)
2. Have working MVP, need to prune/polish (transition)
3. Migrating to production (.skogai/claude/)
4. Understanding the philosophy/when to use which

**Wait for response before routing.**
</intake>

<routing>
| Response | Workflow | Purpose |
|----------|----------|---------|
| 1, "start", "new", "explosive" | workflows/starting-explosive.md | How to work in .skogai/skogix/ |
| 2, "prune", "polish", "transition" | workflows/pruning-to-production.md | How to clean up working code |
| 3, "migrate", "production", "claude" | workflows/migration-path.md | Moving to .skogai/claude/ |
| 4, "philosophy", "when", "understand" | references/workflow-philosophy.md | Decision criteria |

**After routing, follow the workflow exactly.**
</routing>

<current_examples>

## Real Examples from This Repo

[@todo:skogix: add real examples from both sides of the lifecycle to illustrate the concepts as well as actually adding the skogai-pruning-theory as a part of the flow]
**Explosive phase** (`.skogai/skogix/src/`):

- Personal projects
- Beta testing
- Rapid prototyping
- `@.skogai/skogix/src/agents/document-writer.md`

**Production phase** (`.skogai/claude/`):

- `@.skogai/claude/agents/code-simplicity-reviewer.md` - only core agent
- `@.skogai/claude/skills/skogai-argc/` - proven argc patterns
- `@.skogai/claude/workflows/` - 4 core workflows (plan, work, review, compound)
- `@.skogai/claude/hooks/post-tool-use.sh` - battle-tested automation

## Migration Examples

[@todo:skogix:add actual implementation-examples]
Skills that graduated from temporary to core:

- `skogai-argc` - started explosive, now core
- `skogai-docs` - started explosive, now core
- `skogai-jq` - started explosive, now core
- `skogai-todos` - started explosive, now core
- `skogai-worktrunk` - started explosive, now core

Skills still in temporary:

- `skogai-developing-for-claude-code` - being validated
- `skogai-skill-creator` - being validated
- `skogai-git-worktree` - being validated

</current_examples>

<success_criteria>
You understand:

- [ ] When the additive nature of LLMs are to your advantage or disadvantage
- [ ] How to guide your workflow back to the structured production phase
- [ ] What "pruning" means in practice and why SkogAI talks about "what the agent do not know is the _only_ thing we should care about"
- [ ] Have milestones set up for when to transition between phases
      </success_criteria>
