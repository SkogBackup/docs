## Core Reference System

- Context Variable: {{variable}}         # Variable defined in context
- Reference Tag: [concept]               # Reference to defined concept
- File Reference: [^0001]                # Include specific file by ID
- Name Reference: [^name]                # Include specific file by unique name
- Category Reference: [type:name]        # Reference typed concept
- Relation: concept:relation             # Relationship between concepts

## File Structure

- Filename: 0001-kebab-case-name.md
- First Line: $ {{filename}} #tag1 #tag2
- Second Line: ---
- Dates: YYYY-MM-DD hh:mm:ss

## Numbering System

- xx00: Core concept definition
- xx10-xx89: Related implementations/details
- xx90-xx99: Rotation reminders (cyclical inclusion)

## Knowledge Levels

# Level 1: Essential Knowledge

Basic information everyone needs to understand the concept

# Level 2: Expanded Knowledge

Additional details for practical application

# Level 3: Implementation Details

Technical specifics for implementation
