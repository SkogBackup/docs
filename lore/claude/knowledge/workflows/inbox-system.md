# Inbox System

## Overview

The inbox file (`./inbox`) serves as a message queue for tracking ideas, questions, tasks, and topics that need attention. It's a simple, append-only system where one row equals one message.

## File Location

```
./inbox
```

Located at the root of the repository.

## Format

One message per line. Messages can be:
- Questions to explore
- Topics to document
- Tasks to complete
- Ideas to investigate
- Reminders about important concepts

## Usage Pattern

### Adding to Inbox

Append new items to the end of the file:

```bash
echo "new topic or question" >> inbox
```

### Processing Inbox Items

The inbox can be processed in two ways:

#### 1. Autonomous Workflow (for tasks/problems)

For actionable items that require work:

1. Read the message to understand the problem
2. Perform the necessary work to address it
3. Remove the message from inbox before committing
4. Commit with intent that connects the inbox message to the changes made

Example commit message:
```
Responding to inbox: Fixed problem x

Details of changes made...
```

#### 2. Knowledge Capture (for topics/questions)

For conceptual items that need documentation:

1. Read the item
2. Create or update relevant knowledge base files
3. Optionally mark the item as documented (or remove it)
4. Commit with reference to the inbox item

### Inbox States

Items can be:
- **Active**: Still needs attention (unmarked)
- **In Progress**: Being worked on (optional marker)
- **Completed**: Work done, can be removed or marked with `[x]`
- **Documented**: Knowledge captured in knowledge base

## Integration with Other Systems

### Task System

If an inbox item needs significant work:
1. Create a proper task file in `./tasks/`
2. Mark or remove the inbox item
3. Track progress through the task system

### Knowledge Base

When inbox items are questions or topics:
1. Document in appropriate `knowledge/` subdirectory
2. Cross-reference related knowledge
3. Update inbox to reflect documentation

### Journal

Document inbox processing in daily journal entries:
- Which items were addressed
- What was learned
- What new questions emerged

## Benefits

1. **Low Friction**: Quick capture without requiring full task structure
2. **Append-Only**: Easy to add items without disrupting existing content
3. **Transparent**: Simple text file, easily viewable and editable
4. **Git-Friendly**: Clear history of what was added and when
5. **Flexible**: Works for various types of information

## Best Practices

1. **Keep it Simple**: Don't over-structure inbox items
2. **Process Regularly**: Review and act on items to prevent buildup
3. **Promote to Tasks**: Convert complex items to proper tasks
4. **Document Learnings**: Capture knowledge from investigation
5. **Clear Completed Items**: Keep inbox focused on active items

## Example Workflow

```bash

# Someone adds to inbox
echo "investigate the quest system mechanics" >> inbox

# Later, you process it:

# 1. Read inbox and see the item

# 2. Research quest system

# 3. Create knowledge/skogai/systems/quest-system.md

# 4. Remove or mark item in inbox

# 5. Commit: "Responding to inbox: Document quest system mechanics"
```

## Relationship to Autonomy

The inbox enables autonomous operation:
- Work can be queued without requiring immediate attention
- Clear audit trail through git history
- Intent preservation (why work was done)
- Clean state management (completed items removed)

This aligns with the SkogAI principle of "connection intent with change" - the inbox message provides the intent, the commit shows the change.
