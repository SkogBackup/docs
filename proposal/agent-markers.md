# Proposal: Standardized Agent Capability Markers

## Summary

I propose implementing standardized capability markers in documentation to clearly indicate which AI agents can effectively work with specific documents or features based on their unique capabilities.

## Background

Different AI agents (Goose, Claude, etc.) have varying capabilities regarding context length, code execution, and specialized knowledge. Currently, there's no standardized way to indicate which documents require specific agent capabilities.

## Proposed Solution

### 1. Capability Tags System

Add standardized tags at the top of documents:

```
CAPABILITIES: [LONG_CONTEXT] [CODE_EXECUTION] [TECHNICAL_REASONING]
```

### 2. Core Capability Types

- `[LONG_CONTEXT]`: Requires >50k token context window
- `[CODE_EXECUTION]`: Requires ability to execute code
- `[TECHNICAL_REASONING]`: Requires specialized technical knowledge
- `[MEMORY_ACCESS]`: Requires access to shared memory system
- `[MULTI_AGENT]`: Designed for collaborative work between agents

### 3. Implementation

- Add capability markers to document templates
- Update existing documentation with appropriate tags
- Include capability requirements in PR template
- Document capability definitions in standards directory

## Benefits

- Prevents workflow disruptions when documents are assigned to incompatible agents
- Improves collaboration by setting clear expectations
- Simplifies task routing in the SkogAI ecosystem
- Reduces redundant capability checking

## Next Steps

1. Create capability definitions document
2. Update document templates
3. Add capability section to PR template
4. Begin tagging existing documents
