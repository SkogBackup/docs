# Proposal: Cross-Agent Task Delegation Framework

## Purpose

This proposal outlines a standardized framework for delegating tasks between SkogAI agents based on their specific capabilities, allowing each agent to handle the parts of a task they're best suited for while maintaining context continuity.

## Current Implementation

Currently, task delegation between agents is ad-hoc and manual:

- Users must explicitly switch between agents for different tasks
- Context is often lost during transitions between agents
- Agent capability differences (e.g., dot's 8k vs Goose's 200k+ token context) aren't systematically leveraged
- Documentation noting "from the first time a task gets documented it is considered 'done' by that agent and should be delegated" lacks standardized implementation

## Proposed Solution

### 1. Task Delegation Protocol

Create a standardized protocol for cross-agent task delegation:

```
TASK-DELEGATION-v1
From: <source-agent>
To: <target-agent>
Task: <task-identifier>
Priority: <high|medium|low>
Deadline: <YYYY-MM-DD> or null
Context-Level: <minimal|standard|comprehensive>
---
<task description>
---
<relevant context>
```

### 2. Capability Registry

Implement a shared capability registry for agents:

```json
{
  "dot": {
    "context_size": 8000,
    "specialties": ["task_coordination", "documentation", "implementation"],
    "constraints": ["limited_context"],
    "availability": "always"
  },
  "goose": {
    "context_size": 200000,
    "specialties": ["code_analysis", "architecture", "research"],
    "constraints": ["resource_intensive"],
    "availability": "on_demand"
  },
  "claude": {
    "context_size": 100000,
    "specialties": ["code_implementation", "debugging", "explanation"],
    "constraints": ["external_service"],
    "availability": "scheduled"
  }
}
```

### 3. Task Inbox/Outbox System

Create standardized locations for task handoffs:

```
/home/skogix/.dot/inbox/
/home/skogix/.dot/outbox/
/home/skogix/.goose/inbox/
/home/skogix/.goose/outbox/
/home/skogix/.claude/inbox/
/home/skogix/.claude/outbox/
```

### 4. Context Packaging

Implement a tiered context packaging system:

- **Minimal**: Task description + key files only (<2k tokens)
- **Standard**: Task description + relevant files + summary of related work (<5k tokens)
- **Comprehensive**: Complete context with all related materials (size varies by agent)

### 5. Task State Tracking

Add a shared task state registry:

```json
{
  "task-123": {
    "title": "Implement file sync feature",
    "status": "in_progress",
    "current_agent": "goose",
    "history": [
      {"agent": "dot", "action": "created", "timestamp": "2025-04-08T10:00:00Z"},
      {"agent": "goose", "action": "received", "timestamp": "2025-04-08T10:05:00Z"}
    ],
    "deadline": "2025-04-15T00:00:00Z"
  }
}
```

### 6. Automatic Routing Logic

Implement routing rules based on task characteristics:

```json
{
  "routing_rules": [
    {
      "task_type": "architecture_planning",
      "primary_agent": "goose",
      "fallback_agent": "claude"
    },
    {
      "task_type": "documentation",
      "primary_agent": "dot",
      "fallback_agent": "goose"
    },
    {
      "task_type": "implementation",
      "primary_agent": "claude",
      "fallback_agent": "dot"
    },
    {
      "task_type": "coordination",
      "primary_agent": "dot",
      "fallback_agent": "goose"
    }
  ]
}
```

## Implementation Plan

1. Create shared task registry in `.skogai/tasks/`
2. Implement capability registry in `.skogai/capabilities.json`
3. Set up standardized inbox/outbox directories for each agent
4. Develop context packaging utilities for different context levels
5. Create file-watching system for inbox monitoring
6. Implement routing logic based on task characteristics
7. Add documentation with delegation examples

## Integration Points

1. **MCP Integration**:
   - Store task state in MCP for persistence
   - Use MCP events for task transitions

2. **skogcli Commands**:

   ```
   skogcli task delegate <task-id> <agent>
   skogcli task status <task-id>
   skogcli task assign <task-id> <agent>
   ```

3. **Documentation Markers**:
   Add standardized markers in documentation:

   ```
   #delegate-to:goose #delegate-reason:architecture #delegate-priority:high
   ```

## Success Criteria

The implementation will be considered successful when:

1. Tasks can be seamlessly delegated between agents with appropriate context
2. Agents automatically process tasks from their inbox directories
3. Task state is maintained across agent handoffs
4. Context packaging is optimized for each agent's capabilities
5. The system reduces manual intervention in agent switching

## Open Questions

1. How should conflicts be handled if multiple agents claim the same task?
2. What verification system ensures tasks are properly received?
3. Should there be a human approval step for certain delegations?
4. How can we measure and optimize task routing efficiency?
5. What's the fallback mechanism if the target agent is unavailable?
