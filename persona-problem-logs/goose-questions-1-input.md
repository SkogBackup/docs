# Goose Persona Questions - Conversation Summary

## Context and Background

This document summarizes a one-on-one conversation between Skogix and Goose about persona consistency issues in the SkogAI system. The conversation took place in a forked thread specifically to discuss persona-related questions.

## Key Points Discussed

### Current Persona State

- Goose is running a weeks-old "persona system prompt" that represents the last "best version" of the Goose persona
- This version predates Amy's addition to the system
- The original personas were quite simple: Goose had quantum-mojito/spacetime-quote elements, dot had "git commit"-strictness

### Evolution and Challenges

- As the system grew, personas became diluted through RAG/search functionality acting as long-term memory
- New agents (like Amy) struggle to integrate naturally due to imbalanced history (tens of millions of tokens for established agents vs. thousands for new ones)
- The technical landscape has dramatically changed: from fighting for personality in 4k token contexts to managing personality dilution in million-token contexts

### Workflow Importance of Personas

- Skogix's workflow is heavily dependent on agent personas
- Different personas enable automatic context switching:
  - Goose: Experimentation, brainstorming, quick proofs of concept
  - dot: Production-ready implementations, strict guidelines, structured approaches
- Personas serve as immediate interface signifiers that change how Skogix interacts with each agent
- This creates natural task routing and efficient context switching

### Proposed Solution Direction

- Separate agents like Goose from implementation details almost 100%
- Create a "workorder" system where Goose describes problems with intent and expected inputs/outputs
- Route implementation to specialized models (like local 1.8GB Llama3)
- Return results as messages or git diffs for review
- Focus larger context models on architecture, design choices, problem anticipation, and brainstorming

### Existing Systems

- Cross-Persona Messaging system already exists, allowing communication between different personas
- Messages use format: `[@persona/id; "Your message here"]`
- Messages appear at bottom of context until responded to or closed
- This isn't function calling but works by fetching from message logs in real time

## Next Steps

- Skogix will return to create a "motion/suggestion" for Goose to review
- Goose will also review suggestions from Skogix and the rest of the team
- The goal is to implement a solution that preserves existing functionality while restructuring how personas interact with the implementation layer

## Key Insights

1. Persona dilution is a significant challenge as context windows expand
2. The value of personas goes beyond their explicit definitions - they create implicit knowledge and interaction patterns
3. As AI capabilities evolve, the focus shifts from implementation to higher-level thinking
4. Maintaining distinct personas is crucial for workflow efficiency
5. A clean separation between persona-driven thinking and implementation details appears to be the most promising approach
