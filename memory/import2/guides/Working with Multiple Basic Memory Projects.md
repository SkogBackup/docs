---
title: Working with Multiple Basic Memory Projects
type: note
permalink: guides/working-with-multiple-basic-memory-projects
tags:
- '#basic-memory'
- '#projects'
- '#workflow'
- '#guide'
- '#best-practices'
---

# Working with Multiple Basic Memory Projects

This guide provides practical instructions for working with multiple Basic Memory projects effectively.

## Understanding the Project System

Basic Memory organizes knowledge into separate projects, each with its own database and file structure. Projects can be located in different directories and serve different purposes.

## Project Commands and Tools

### Command Line Tools
- `uvx basic-memory project list` - View all available projects
- `uvx basic-memory project info` - See details about the current project
- `uvx basic-memory project set-active [project]` - Switch to a different project
- `uvx basic-memory project create [name] [path]` - Create a new project

### Extension API Functions
- `skogai-memory__project_info` - Get information about the currently connected project
- `skogai-memory__write_note` - Create notes in the current project
- `skogai-memory__read_note` - Read notes from the current project
- `skogai-memory__search_notes` - Search across the current project

## Important Considerations

1. **MCP Connection Persistence**:
   - The MCP server connects to a specific project when started
   - This connection doesn't automatically update when you change projects via command line
   - Notes will be created in the project that was active when the MCP started

2. **Switching Projects**:
   - When switching projects via command line, restart the MCP server for the change to take effect
   - The command line may show a different active project than the extension API

3. **Best Practices Workflow**:
   - Before starting work, verify which project is active
   - Set your desired project active before starting the MCP server
   - Check `project_info` in both command line and API to ensure alignment
   - If switching projects during a session, plan to restart the MCP server

## Example Workflow

1. Set active project: `uvx basic-memory project set-active ProjectName`
2. Verify active project: `uvx basic-memory project info`
3. Start or restart MCP server
4. Verify via API: Use `skogai-memory__project_info`
5. Work with notes in the selected project
6. When switching projects, repeat steps 1-4

Created: 2025-04-12