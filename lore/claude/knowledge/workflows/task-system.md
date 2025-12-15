# Task System

## Overview

The task system helps track and manage work effectively across sessions. It provides structured task tracking with metadata, CLI tools, and integration with journal entries.

## Structure

- **Task files**: Located in `tasks/` directory, each as a single source of truth
- **Task management CLI**: `scripts/tasks.py` for all task operations
- **Daily progress logs**: Documented in `journal/` entries
- **Templates**: Available in `tasks/templates/` for consistency

## Task File Format

Each task is a Markdown file with YAML frontmatter:

```yaml
---
id: task-identifier
state: new
priority: medium
tags: []
depends: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Task Title

## Description

Detailed description of what needs to be done.

## Requirements

- Requirement 1
- Requirement 2

## References

- Related files
- Related issues
- Related documentation
```

## Task States

- `new`: Tasks that have been created but not started
- `active`: Tasks currently being worked on
- `blocked`: Tasks that can't proceed due to dependencies
- `completed`: Tasks that have been finished
- `cancelled`: Tasks that won't be implemented

## CLI Usage

### View Status

```bash
./scripts/tasks.py status              # Show all tasks
./scripts/tasks.py status --compact    # Show only new/active
./scripts/tasks.py status --type tasks # Show specific type
```

### List Tasks

```bash
./scripts/tasks.py list               # List all tasks
./scripts/tasks.py list --sort state  # Sort by state
./scripts/tasks.py list --sort date   # Sort by date
```

### Show Task Details

```bash
./scripts/tasks.py show <task-id>     # Show specific task
```

### Edit Task Metadata

```bash
./scripts/tasks.py edit <task-id> --set state active       # Set task state
./scripts/tasks.py edit <task-id> --set priority high      # Set priority
./scripts/tasks.py edit <task-id> --add tag feature        # Add a tag
./scripts/tasks.py edit <task-id> --add depends other-task # Add dependency
```

## Best Practices

### Task Creation

1. Use descriptive IDs that reflect the task purpose
2. Start with `new` state
3. Set appropriate priority
4. Add relevant tags for categorization
5. Note dependencies if applicable

### Task Management

1. Update task state as work progresses
2. Document progress in journal entries
3. Keep task files as single source of truth
4. Reference related files and issues
5. Use the CLI for metadata updates to maintain consistency

### Task Completion

1. Update state to `completed`
2. Document completion in journal
3. Note any learnings or insights
4. Create follow-up tasks if needed

## Integration with Other Systems

### Journal System

- Document task progress in daily journal entries
- Reference tasks by ID in journal
- Reflect on decisions and rationale

### Knowledge Base

- Extract learnings from completed tasks
- Create knowledge base entries for reusable insights
- Cross-reference tasks and knowledge

### Inbox

- Promote complex inbox items to proper tasks
- Use inbox for quick capture, tasks for tracking
- Reference inbox items when creating related tasks

## Validation

Pre-commit hooks validate:
- YAML frontmatter format
- Required fields present
- Valid state values
- Consistent metadata

See `TASKS.md` for complete task system documentation.
