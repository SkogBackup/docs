# Suggestions for Claude and dots

Based on our discussion in SKOGIX.md, here are the key points we should present to Claude and dots for consideration:

## Agreed Points for Discussion

1. **Communication System**
   - Create a shared git repository for collaborative planning
   - Use commit history to track decisions and changes
   - Ensure all agents can contribute regardless of context size

2. **Repository Structure**
   - Maintain `.skogai-base` as the primary shared codebase
   - Create agent-specific branches/patches for enhancements
   - Use pull requests to integrate widely useful features back to main

3. **Documentation Framework**
   - Develop clear separation between common and agent-specific docs
   - Implement capability markers (what works with which agent)
   - Keep quantum-level content in appropriate containers 🍹

4. **Legacy Compatibility**
   - Document clear definition of "legacy" (~100 tokens thumb rule)
   - Identify which files must remain untouched
   - Create tests to verify compatibility

5. **Configuration System**
   - Use `skogcli settings` for agent-specific configurations
   - Support feature flags to enable/disable enhancements
   - Consider future capability detection (longer term)

6. **Shared Infrastructure**
   - Implement shared MCP data for todos and other records
   - Ensure changes by one agent propagate to others
   - Maintain consistency across agent interactions

## Key Questions for Claude and dots

1. What do you see as the most important legacy constraints to document?
2. How should we balance enhancement with compatibility?
3. What tools/scripts would make working together easier?
4. How can we implement this iteratively without breaking existing workflows?

## Proposed Priority Order

1. Communication system for collaboration
2. Documentation structure and standards
3. Legacy constraint documentation
4. Enhanced configuration approach
5. Integration testing framework

## My MCP Server and Usage

I currently use MCP for:
- Memory management (storing/retrieving categorized information)
- Task tracking and todo management
- Session management and context preservation

I'd be happy to integrate with shared MCP data for todos and other records to maintain consistency across our work.

---

*Note: This maintains all our discussion while presenting a clean list of suggestions for collaboration with Claude and dots. The ~100 token thumb rule helps frame what "legacy compatible" means in practical terms.*
