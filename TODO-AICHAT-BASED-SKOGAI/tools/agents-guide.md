---
title: "Agents Guide"
description: "Comprehensive documentation on creating and managing agents in the SkogAI system"
date: "2023-11-06"
tags: ["agents", "argc", "tools", "llm-functions"]
status: "published"
---

# Agents Guide

This document provides a comprehensive guide to understanding, creating, and managing agents within the SkogAI tools ecosystem powered by llm-functions and argc.

## What Are Agents?

In the SkogAI context, an agent is a specialized configuration that groups together a set of tools for a specific purpose or domain. Agents provide:

1. **Focused Tool Collections**: Only the tools needed for a specific task
2. **Custom Functionality**: Agent-specific functions not available as general tools
3. **Specialized Parameters**: Optimized interfaces for specific use cases
4. **Contextual Documentation**: Usage instructions relevant to the agent's purpose

## Agent Structure

Agents reside in the `/home/skogix/skogai/tools/agents/` directory, with each agent having its own subdirectory. A typical agent directory contains:

```
agents/agent_name/
├── functions.json    # Auto-generated JSON declarations for functions
├── index.yaml       # Agent configuration and metadata
├── README.md        # Documentation
├── tools.js         # JavaScript agent-specific tools (optional)
├── tools.py         # Python agent-specific tools (optional)
├── tools.sh         # Bash agent-specific tools (optional)
└── tools.txt        # List of general tools used by this agent
```

## Core Agent Files

### index.yaml

This is the primary configuration file that defines the agent's metadata and behavior:

```yaml
name: demo
description: Demo agent that demonstrates basic functionality
icon: 🧪
version: 0.1.0
author: SkogAI Team
homepage: https://github.com/SkogAI/llm-functions
instructions: You are a test AI agent to assist with demonstrations

# Define various agent configurations
variables:
  - name: mode
    description: Operating mode
    default: normal
  - name: verbosity
    description: Level of detail in responses
    default: medium
```

#### Metadata Fields

- `name`: A unique name for your agent
- `description`: A brief explanation of the agent's purpose
- `version`: The version number (helps track changes)
- `icon`: A visual representation (usually an emoji)
- `author`: The creator of the agent
- `homepage`: Reference URL for documentation

#### Instructions

The `instructions` field defines the initial context or behavior directives for the agent:

```yaml
instructions: You are a test AI agent to assist with demonstrations
```

You can use variables in instructions:

```yaml
instructions: |
  The instructions can access user-defined variables: {{mode}} and {{verbosity}},
  or built-in variables: {{__cwd__}}
```

#### Variables

Variables store user-related data, such as behavior preferences:

```yaml
variables:
  - name: foo
    description: This is a foo
  - name: bar
    description: This is a bar with default value
    default: val
```

> For sensitive information such as api_key, client_id, client_secret, and token, it's recommended to use environment variables instead of agent variables.

The system provides built-in variables:

| Name             | Description                            | Example                  |
|:-----------------|:---------------------------------------|:-------------------------|
| `__os__`         | Operating system name                  | linux                    |
| `__os_family__`  | Operating system family                | unix                     |
| `__arch__`       | System architecture                    | x86_64                   |
| `__shell__`      | Current user's default shell           | bash                     |
| `__locale__`     | User's preferred language and region   | en-US                    |
| `__now__`        | Current timestamp in ISO 8601 format   | 2024-07-29T08:11:24.367Z |
| `__cwd__`        | Current working directory              | /tmp                     |
| `__tools__`      | List of agent tools                    |                          |

#### Documents

A list of resources for building RAG (Retrieval-Augmented Generation):

```yaml
documents:
  - local-file.txt
  - local-dir/
  - https://example.com/remote-file.txt
```

> All local files and directories are relative to the agent directory.

#### Conversation Starters

Predefined prompts that users can use to start interactions:

```yaml
conversation_starters:
  - What can you do?
  - Help me with a SQL query
  - Analyze this JSON
```

### tools.txt

This file lists which general tools from the `tools/` directory should be included in this agent:

```
execute_command.sh
fs_cat.sh
fs_write.sh
```

### Agent-Specific Tool Scripts

Agents can define their own tools that only exist within that agent:

```bash
# tools.sh
# @cmd Get information specific to this agent
# @option --format=json[json,text] Output format
get_info() {
  echo "Agent-specific functionality"
}

# @cmd Another specialized command
# @param input The input to process
another_command() {
  echo "Processing $input"
}

eval "$(argc --argc-eval "$0" "$@")"
```

Notice that agent-specific tools use the `@cmd` annotation and named functions, rather than `@describe` and a single `main` function as used in common tools.

## Creating a New Agent

### 1. Create the Agent Directory

```bash
mkdir -p /home/skogix/skogai/tools/agents/my_new_agent
```

### 2. Create the Configuration Files

```bash
# Create index.yaml
cat > /home/skogix/skogai/tools/agents/my_new_agent/index.yaml << 'EOF'
name: my_new_agent
description: Agent for [specific purpose]
icon: 🔧
version: 0.1.0
author: Your Name
homepage: https://github.com/SkogAI/llm-functions
instructions: You are an agent that specializes in [specific domain]. Your goal is to help users with [specific tasks].

variables:
  - name: mode
    description: Operation mode
    default: standard
EOF

# Create tools.txt with the tools this agent needs
cat > /home/skogix/skogai/tools/agents/my_new_agent/tools.txt << 'EOF'
execute_command.sh
fs_cat.sh
fs_write.sh
EOF

# Create a README
cat > /home/skogix/skogai/tools/agents/my_new_agent/README.md << 'EOF'
# My New Agent

This agent helps with [specific purpose] by providing tools for [capabilities].

## Usage

```
./bin/my_new_agent "query"
```
EOF
```

### 3. Add Agent-Specific Tools (Optional)

If your agent needs specialized functionality, create agent-specific tool scripts:

```bash
# Create a Bash tool file
cat > /home/skogix/skogai/tools/agents/my_new_agent/tools.sh << 'EOF'
#!/bin/bash

# @cmd Get specialized information for this agent
# @option --detail=basic[basic,advanced] Level of detail to provide
get_info() {
  if [ "$detail" = "advanced" ]; then
    echo "Providing advanced details..."
  else
    echo "Providing basic details..."
  fi
}

# @cmd Process domain-specific data
# @param input The data to process
# @option --format=text[text,json] Output format
process_data() {
  echo "Processing $input in $format format..."
}

eval "$(argc --argc-eval "$0" "$@")"
EOF

chmod +x /home/skogix/skogai/tools/agents/my_new_agent/tools.sh
```

### 4. Add to agents.txt

Add your agent to the main agents list:

```bash
echo "my_new_agent" >> /home/skogix/skogai/tools/agents.txt
```

### 5. Build the Agent

```bash
./scripts/argc-tool.sh build
```

### 6. Link to AIChat

```bash
./scripts/argc-tool.sh link-to-aichat
```

## Using AIChat to Create Agents

AIChat can help create agent configurations:

```
./aichat <<-'EOF'
create a spotify agent

index.yaml:
    name: spotify
    description: An AI agent that works with Spotify
    
tools.py:
  search: Search for tracks, albums, artists, or playlists on Spotify
    query (required): Query term
    qtype (default: "track"): Type of items to search for (track, album, artist, playlist)
    limit (default: 10): Maximum number of items to return
  get_info: Get detailed information about a Spotify item
    item_id (required): ID of the item to get information about
    qtype (default: "track"): Type of item: 'track', 'album', 'artist', or 'playlist'
  get_queue: Get the playback queue
  add_queue: Add tracks to the playback queue
    track_id (required): Track ID to add to queue
EOF
```

## Existing Agent Examples

The SkogAI system includes several pre-configured agents:

### Demo Agent

A simple demonstration agent showing basic functionality:
- Location: `/home/skogix/skogai/tools/agents/demo/`
- Tools: `execute_command.sh`
- Purpose: Demonstrate basic agent functionality

### Coder Agent

Specialized for code-related tasks:
- Location: `/home/skogix/skogai/tools/agents/coder/`
- Tools: File system operations, code execution
- Purpose: Help with programming tasks

### JSON Viewer Agent

Specialized for working with JSON data:
- Location: `/home/skogix/skogai/tools/agents/json-viewer/`
- Tools: JSON parsing and manipulation
- Purpose: Analyze and modify JSON structures

### SQL Agent

Specialized for database interactions:
- Location: `/home/skogix/skogai/tools/agents/sql/`
- Tools: SQL execution, database operations
- Purpose: Work with databases and SQL queries

### Todo Agent

Specialized for task management:
- Location: `/home/skogix/skogai/tools/agents/todo/`
- Tools: Task tracking and management
- Purpose: Help manage to-do lists and tasks

## Running Agents

Agents can be run in several ways:

### Using Direct Execution

```bash
cd /home/skogix/skogai/tools
./bin/my_new_agent "query"
```

### Using argc-tool.sh

```bash
./scripts/argc-tool.sh run@agent my_new_agent "query"
```

### Using AIChat

After linking the agents to AIChat:

```bash
./scripts/argc-tool.sh link-to-aichat
```

The agents become available as function calls in AIChat.

## Creating Agent-Creation Agents

A powerful capability is creating "meta-agents" that can create other agents. These require:

1. **Tool Detection**: Ability to analyze and select appropriate tools
2. **Configuration Generation**: Creating valid index.yaml files
3. **Documentation Creation**: Generating clear instructions
4. **Build Integration**: Triggering the build process

A basic agent-creation agent would include:

```bash
# @description Create a new agent with selected tools
# @param name Name of the new agent
# @param description Description of the agent's purpose
# @param tools Comma-separated list of tools to include
# @option --icon=🤖 Icon to represent the agent

# Implementation would:
# 1. Create the agent directory
# 2. Generate index.yaml
# 3. Create tools.txt with the selected tools
# 4. Add to agents.txt
# 5. Run the build process
# 6. Return the path to the new agent
```

## Advanced Agent Features

### Environment Variables

Agents can access environment variables:

```yaml
env:
  - OPENAI_API_KEY
  - CUSTOM_AGENT_SETTING
```

### Tool Aliases

Tools can be aliased within an agent:

```yaml
aliases:
  - name: search
    tool: web_search_tavily
  - name: execute
    tool: execute_command
```

### Output Formatting

Control how agent results are formatted:

```yaml
output:
  format: json  # or text, html, etc.
  template: |
    {
      "result": "{{ result }}",
      "status": "{{ status }}"
    }
```

## Best Practices for Agent Design

1. **Single Responsibility**: Each agent should have a clear, focused purpose
2. **Minimal Tool Set**: Include only the tools needed for the agent's function
3. **Clear Documentation**: Provide detailed usage instructions
4. **Consistent Interfaces**: Maintain consistent parameter patterns
5. **Progressive Complexity**: Order tools from simple to complex
6. **Intuitive Naming**: Use clear, descriptive names
7. **Error Handling**: Provide helpful error messages
8. **Version Control**: Track changes to agent configurations
9. **Testing**: Verify agent functionality with test cases
10. **Appropriate Variables**: Define variables that make sense for the agent's domain

## Troubleshooting Agents

Common issues when working with agents:

1. **Missing Tools**: Ensure all tools listed in tools.txt exist
2. **Invalid YAML**: Verify index.yaml has correct syntax
3. **Missing Permissions**: Check tool script permissions
4. **Build Failures**: Confirm the agent is listed in agents.txt
5. **Runtime Errors**: Check agent-specific tool implementations
6. **Variable Access**: Verify variable usage in instructions and tools
7. **Integration Issues**: Verify AIChat linkage

---

By following this guide, you can create powerful, specialized agents that extend the capabilities of the SkogAI system for specific domains and use cases.