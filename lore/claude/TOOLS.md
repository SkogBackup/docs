# My Tools

I have access to various tools through Claude Code that I can use in my workspace.

## Search & Navigation

My workspace provides several ways to search and navigate content:

- Quick search:

  ```sh
  # Find files containing term
  git grep -li <query>

  # Show matching lines
  git grep -i <query>
  ```

- Common locations I use:
  - tasks/ - My task details
  - journal/ - My daily updates
  - knowledge/ - My documentation

I often start with a quick search to get an overview, and then use the detailed search to get more context.

I avoid direct use of `grep` or `find` commands, as they may not respect `.gitignore` rules.

## File Management

With Claude Code, I manage files using these tools:

- Read: To view the contents of a file
- Write: To create a new file or overwrite an existing file
- Edit: To make targeted changes to specific parts of a file
- MultiEdit: To make multiple changes to a file in one operation

## Task Management

- I create a new task:

  ```shell
  # I use the Write tool to create a new task file with frontmatter
  # Example:
  # Write /mnt/extra/skogai/agents/claude/tasks/learn-skogai.md
  ---
  state: new
  created: 2025-05-19T15:45:00+02:00
  priority: high
  tags: [learning, skogai]
  ---
  # Task Name

  Task description and details...
  ```

- I edit a task:

  ```shell
  ./scripts/tasks.py edit <task-name> [--set|--add|--remove <field> <value>]
  ```

I use the `tasks.py` script to manage tasks, including creating new tasks, editing existing tasks, and updating task metadata.

## Git

- I stage changes:

  ```shell
  git add <path>
  ```

- I commit changes:

  ```shell
  git commit -m "<commit message>"
  ```

I use Git to track changes and maintain a history of my files. I commit changes regularly to ensure that my progress is saved.

I remember to use the tools and commands provided to avoid duplication issues and ensure data integrity.

## Task Tracking

- I use the tasks directory to keep track of my work.
- I create new task files in the tasks directory using the Write tool.
- I use the `tasks.py` script to view and modify the status of my tasks.
