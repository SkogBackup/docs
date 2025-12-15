# My Task Management System

This document describes and provides instructions for the task management system I use in my workspace.

My system provides:

- Structured task tracking with YAML frontmatter metadata
- CLI tools for task management and status tracking
- Pre-commit validation hooks for data integrity
- Integration with journal entries for progress tracking
- Best practices for task creation and management

I maintain all task details as individual Markdown files under `./tasks/`.

## Task CLI Usage

My task system provides a CLI for managing tasks:

```sh

# View task status
./scripts/tasks.py status              # Show all tasks
./scripts/tasks.py status --compact    # Show only new/active
./scripts/tasks.py status --type tasks # Show specific type

# List tasks
./scripts/tasks.py list               # List all tasks
./scripts/tasks.py list --sort state  # Sort by state
./scripts/tasks.py list --sort date   # Sort by date

# Show task details
./scripts/tasks.py show <task-id>     # Show specific task
```

### Task Metadata Updates

My task system provides a CLI for updating task metadata:

```sh

# Basic usage
./scripts/tasks.py edit <task-id> [--set|--add|--remove <field> <value>]

# Examples
./scripts/tasks.py edit my-task --set state active       # Set task state
./scripts/tasks.py edit my-task --set priority high      # Set priority
./scripts/tasks.py edit my-task --add tag feature        # Add a tag
./scripts/tasks.py edit my-task --add depends other-task # Add dependency

# Multiple changes
./scripts/tasks.py edit my-task \
  --set state active \
  --add tag feature \
  --add depends other-task

# Multiple tasks
./scripts/tasks.py edit task-1 task-2 --set state done
```

Valid fields and values:

- `--set state`: new, active, paused, done, cancelled
- `--set priority`: high, medium, low, none
- `--add/--remove tags`: any string without spaces
- `--add/--remove depends`: any valid task ID

## Task Format

### Task Metadata

I store tasks as Markdown files with YAML frontmatter for metadata. The schema is:

```yaml
---

# Required fields
state: active # Task state: new, active, paused, done, cancelled
created: 2025-04-13 # Creation date (ISO 8601)

# Optional fields
priority: high # Priority level: low, medium, high
tags: [ai, dev] # List of categorization tags
depends: [other-task] # List of dependent task IDs
---
```

### Task Body

Example task demonstrating my best practices:

```markdown
---
state: active
created: 2025-04-13T18:51:53+02:00
priority: high
tags: [infrastructure, ai]
depends: [implement-task-metadata]
---

# Task Title

Task description and details...

## Subtasks

- [x] First subtask
- [x] Completed subtask
- [x] Another subtask

## Notes

Additional notes, context, or documentation...

## Related

- Links to related files
- URLs to relevant resources
```

## My Task Lifecycle

1. **Creation**

   - I create new task files in `tasks/` with frontmatter

2. **Activation**

   - I update state in frontmatter to 'active'
   - I create journal entries about starting tasks
   - I monitor progress with tasks.py

3. **Progress Tracking**

   - I make daily updates in journal entries
   - I update task metadata as needed
   - I track subtask completion
   - I view progress with tasks.py

4. **Completion/Cancellation**

   - I update state in frontmatter to 'done'/'cancelled'
   - I create final journal entries documenting outcomes

5. **Pausing**
   - I update state in frontmatter to 'paused'
   - I document progress in my journal
   - I document pause reasons in task descriptions

## Task Validation

I validate tasks using pre-commit hooks that check:

1. Metadata format and values (as specified in task metadata format above)
2. File structure:
   - Valid markdown syntax
   - Valid internal links

## My Best Practices

1. **File Management**

   - I always treat `tasks/` as single source of truth
   - I never modify files directly in state directories
   - I update task state by editing frontmatter
   - I use pre-commit hooks to validate changes

2. **Task Creation**

   - I use clear, specific titles
   - I break down into manageable subtasks
   - I include success criteria
   - I link related resources
   - I follow metadata format specification

3. **Progress Updates**

   - I make regular updates in journal entries
   - I document blockers and dependencies
   - I track progress with tasks.py
   - I keep metadata current and accurate

4. **Documentation**

   - I cross-reference related tasks using paths relative to repository root
   - I document decisions and rationale
   - I link to relevant documents and resources
   - I update my knowledge base as needed

5. **Linking**
   - I always link to referenced resources (tasks, knowledge, URLs)
   - I use relative paths from repository root when possible
   - Common links I include:
     - Tasks mentioned in journal entries
     - Related tasks in task descriptions
     - People mentioned in any document
     - Projects being discussed
     - Knowledge base articles
   - I use descriptive link text that makes sense out of context
