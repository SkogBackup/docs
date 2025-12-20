---
path: docs/
title: docs/claude
type: claude.md
description: SkogAI/docs repository
---

# SkogAI @~/docs repository

- @agents/ - AI agent profiles, journals, memory blocks (claude, dot, goose)
- @skogix/ - human/user, notation system, definitions
- @.docgen/ - frontmatter automation, queue processing, ollama integration
- @lore/README - lore system architecture, orchestration patterns, reference implementation
- @tools/ - external tool docs (argc, gh)
- @.claude/ - research, plans, decisions for this repo

---
 Context Rules (every token fights for survival)
**Input:**

- Only what's directly relevant to THIS question
- Noise → confident hallucination
- Curated context → honest uncertainty + reasonable inference
**Output:**
- Required length beyond available knowledge forces fabrication
- Discovery questions ("where to find") before definition questions ("what is")
- Retrieval between iterations, not assumptions
**Iteration:**
- Small question → small answer → verify → refine → repeat
- Each iteration corrects the previous
- Single-pass reasoning degrades with complexity
**Discovery before definition:**
- "Where might I find X?" → retrieval → "What is X?" with real context
- Source material prevents fabrication
**Uncertainty is signal:**
- Acknowledged uncertainty with direction = valuable output
- Confidence without knowledge correlation = fabrication indicator

---
 Smolagent Orchestration
Demonstrated 2025-12-20: llama3.2:3b with curated vs bloated context

| Context | Result |
|---------|--------|
| Curated | "I don't know + here's what I infer" ✓ |
| Bloated | Confident rambling about bridges and async |
| None | "Estonian e-bike brand" |

Output quality correlates with context quality, not model size alone.
