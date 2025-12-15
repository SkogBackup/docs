---
id: consolidate-task-management
title: Consolidate task management into structured system
state: new
priority: high
created: "2025-11-28"
tags:
  - task-management
  - system-improvement
  - consolidation
---

# Consolidate Task Management into Structured System

## Objective

Migrate all task tracking to the structured tasks/ directory system, deprecating TO-DOS.md in favor of YAML frontmatter tasks managed by scripts/tasks.py.

## Context

Currently have dual systems:
- TO-DOS.md: Simple markdown list for quick capture
- tasks/: Structured YAML frontmatter with metadata, managed by scripts/tasks.py CLI

The structured system provides:
- State tracking (new, active, paused, done, cancelled)
- Priority levels
- Tags and categorization
- Progress tracking with subtasks
- Dependency management
- Rich CLI for status, filtering, editing

## Requirements

1. Convert existing TO-DOS.md item to task
2. Decide on quick capture workflow (if needed)
3. Update documentation to reference tasks/ only
4. Remove or repurpose TO-DOS.md
5. Document task creation best practices

## Progress

- [ ] Convert TO-DOS.md item to structured task
- [ ] Decide if quick capture needs different workflow
- [ ] Update CLAUDE.md to reference tasks/ system
- [ ] Update workflow documentation
- [ ] Remove or archive TO-DOS.md
- [ ] Document task creation patterns

## Acceptance Criteria

- [ ] All tasks in structured format under tasks/
- [ ] Clear workflow for task creation
- [ ] Documentation updated
- [ ] No duplicate task management systems
- [ ] scripts/tasks.py is authoritative tool

## Related

- See: `scripts/tasks.py` for CLI capabilities
- See: `TASKS.md` for system documentation
- See: `knowledge/workflows/task-system.md`
- File: `TO-DOS.md` (to be migrated/removed)
