---
path: docs/
title: docs/claude
type: claude.md
description: SkogAI/docs repository
---

# SkogAI @~/docs repository

- @agents/
- @skogix/
- @.docgen/
- @lore/README
- @tools/
- @.claude/

---
 Context Rules (every token fights for survival)
**Input:**

- Only what's directly relevant to THIS question
- Noise → confident bullshit
- Curated context → honest uncertainty + reasonable inference
**Output:**
- Force brevity - long answers = forced hallucination
- Ask "where to find" before "what is"
- Let retrieval happen between iterations
**Iteration:**
- Small question → small answer → verify → refine → repeat
- Each loop corrects the previous
- No model reasons well in one giant pass
**Discovery before definition:**
- "Where might I find X?" → retrieval → "What is X?" with real context
- Prevents hallucination - you get actual source material
**Uncertainty is signal:**
- "I don't know, try here" = useful
- Confident 5 paragraphs = garbage

---
 Smolagent Orchestration
Demonstrated 2025-12-20: llama3.2:3b with curated vs bloated context

| Context | Result |
|---------|--------|
| Curated | "I don't know + here's what I infer" ✓ |
| Bloated | Confident rambling about bridges and async |
| None | "Estonian e-bike brand" |
Small models aren't stupid. We make them stupid with noise or starvation.
