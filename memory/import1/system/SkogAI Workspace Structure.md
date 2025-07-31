---
title: SkogAI Workspace Structure
type: note
permalink: system/skog-ai-workspace-structure
---

# SkogAI Workspace Structure

## Summary

The SkogAI workspace follows a carefully designed structure that separates concerns, organizes information logically, and supports the system's architectural principles. This document outlines the key components of the workspace, their purposes, and the relationships between them.

## Core Directories

### tasks/

The task management directory contains:

- Task definition files in the root
- Subdirectories representing task states:
  - `new/`: Tasks that have been defined but not started
  - `active/`: Tasks currently being worked on
  - `done/`: Completed tasks
  - `cancelled/`: Tasks that have been abandoned
- Subdirectory contents are symlinks to the main task files
- Task files contain frontmatter with metadata (created date, priority, tags, etc.)

### journal/

The journal directory stores chronological records:

- Daily log entries with standardized format
- Naming convention: YYYY-MM-DD-title.md
- Contains reflections, progress updates, and observations
- Serves as a historical record of system development

### knowledge/

The knowledge directory contains reference information:

- Organized by topic areas
- Contains procedural and declarative knowledge
- Serves as long-term memory for technical information
- Includes subdirectories for specific domains

### memory/

The memory directory contains the hierarchical memory system:

- Numbered files (00-series for core system information)
- Categorized content (100+ series for standards, 200+ for project information)
- Provides structured access to critical system knowledge

### people/

The people directory contains information about collaborators:

- Individual files for each person
- Profiles of team members
- Interaction preferences and history
- Relationship to the project

### projects/

The projects directory contains project-specific information:

- Subdirectories for each project
- Project documentation and specifications
- Project-specific resources and references
- Implementation details

### contexts/

The contexts directory manages dynamic context:

- Context definitions for different situations
- Templates for context construction
- Mechanisms for selective information visibility
- Support for task-specific context loading

### scripts/

The scripts directory contains utility scripts:

- Automation tools
- System maintenance scripts
- Utility functions
- Integration helpers

## Root Files

### README.md

The primary entry point containing:
- System overview
- Core principles
- Quick start information
- Workspace structure summary

### ARCHITECTURE.md

Detailed architectural documentation:
- System design principles
- Component relationships
- Decision rationales
- Evolution and roadmap

### TOOLS.md

Documentation of available tools:
- Tool capabilities
- Usage instructions
- Integration points
- Extension mechanisms

### TASKS.md

Task management overview:
- Current task status
- Priority ordering
- Task workflow process
- Assignment information

## File Organization Principles

1. **Separation of Concerns**: Each directory has a distinct purpose
2. **Progressive Disclosure**: Information organized from general to specific
3. **Temporal vs. Persistent**: Separation of temporary records from persistent knowledge
4. **Hierarchical Organization**: Logical nesting of related information
5. **State Representation**: Directory structure reflects information states
6. **Cross-Referencing**: Links between related information across directories

## Best Practices

When working with the SkogAI workspace:

1. Respect the directory structure and file organization
2. Use appropriate locations for different types of information
3. Maintain consistent naming conventions and formatting
4. Update symlinks when task states change
5. Include proper frontmatter in files that require it
6. Cross-reference related information across directories
7. Follow the documentation-driven development approach