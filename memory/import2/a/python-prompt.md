# SkogAI Memory System

A semantic knowledge management system for structured information and connected thoughts.

## Table of Contents

- [Overview](#overview)
- [Core Concepts](#core-concepts)
- [Getting Started](#getting-started)
- [File Structure](#file-structure)
- [Creating Memories](#creating-memories)
- [Memory URI System](#memory-uri-system)
- [Observations [@file:README.md] Relations](#observations--relations)
- [Best Practices](#best-practices)
- [Automation [@file:README.md] Enforcement](#automation--enforcement)
- [Troubleshooting](#troubleshooting)
- [Examples](#examples)
- [Related Resources](#related-resources)

## Overview

SkogAI Memory is a knowledge management system that transforms information into an interconnected knowledge graph using simple markdown files. The system enables both humans and AI assistants to store, retrieve, and navigate knowledge efficiently, creating a living network of information that grows in value over time.

Key benefits of using this system:

- **Simplicity**: Plain text markdown files that can be edited with any editor
- **Portability**: No specialized software needed beyond basic text editing
- **Structure**: Clear patterns for organizing knowledge
- **Connectivity**: Built-in mechanisms for relating pieces of information
- **Discoverability**: Easy to find related information through semantic connections
- **Automation**: Structure enables tooling for maintenance and enhancement

The system is designed around the principle that *connected knowledge provides more value than isolated information*.

### Knowledge Graph Visualization

```
                                       +-----------------+
                                       |                 |
                                       |  Document A     |
                                       |  # Title        |
                                       |  Content...     |
                                       |  ## observations|
                                       |  ## relations   |
                                       |                 |
                                       +-----------------+
                                        /      |       \n                                       /       |        \n                                      /        |         \n          +-----------------+   implements    |     relates_to    +-----------------+
          |                 |                 |                   |                 |
          |  Document B     | <---------------+                   |  Document D     |
          |  # Title        |                 |                   |  # Title        |
          |  Content...     |                part_of             |  Content...     |
          |  ## observations|                 |                   |  ## observations|
          |  ## relations   |                 |                   |  ## relations   |
          |                 |                 |                   |                 |
          +-----------------+                 v                   +-----------------+
                  |                  +-----------------+                  ^
                  |                  |                 |                  |
                  |                  |  Document C     |                  |
                  |                  |  # Title        |                  |
                  |                  |  Content...     |                  |
                  +----------------->|  ## observations|------------------+
                      extends        |  ## relations   |    references
                                     |                 |
                                     +-----------------+
```

## Core Concepts

### Markdown Files

All knowledge in the system is stored in simple markdown (.md) files, which are:
- Human-readable and easily edited
- Version control friendly
- Structured enough for machine processing
- Flexible enough for various content types

### Observations

Observations are categorized facts or statements that form the atomic units of knowledge. They follow this format:

```markdown
- [category] description #tags
```

Categories help classify the type of information:
- **[fact]** - Objective, verifiable information
- **[principle]** - Guiding ideas or concepts
- **[technique]** - Methods or approaches
- **[decision]** - Choices made and rationales
- **[requirement]** - Necessary conditions or features

Tags (#) make observations discoverable and connectible across the knowledge base.

### Relations

Relations explicitly define connections between documents, showing how pieces of knowledge relate to each other:

```markdown
- relation_type [[linked-document]] (optional description)
```

Common relation types include:
- **implements** - Shows how concepts are put into practice
- **relates_to** - General connection between topics
- **part_of** - Hierarchical membership
- **extends** - Builds upon or enhances
- **references** - Cites or mentions

These connections form the edges in the knowledge graph, allowing navigation between related concepts.

### Memory URIs

Memory URIs provide a standardized way to reference knowledge within the system:

```
memory://[resource-type]/[identifier]
```

This addressing system enables precise linking and retrieval of information across the knowledge base.

## Getting Started

### Setting Up

1. Understand the folder structure:
   - `/todo`: Starting point for new content
   - Topic folders: Permanent locations for organized content

2. Install recommended tools:
   - A text editor with markdown support
   - Git for version control (optional but recommended)

### Creating Your First Memory

1. Create a new markdown file in the `/todo` folder with a descriptive name
2. Start with a clear title (H1 heading)
3. Add meaningful content in markdown format
4. Include an `## observations` section with categorized facts
5. Add a `## relations` section linking to related content
6. Save the file with a clear, kebab-case filename

## File Structure

### Standard File Format

```markdown
# Title of Memory

Main content goes here in regular markdown format.
This can include various headings, lists, code blocks, etc.

## observations
- [category] Observation statement #tag1 #tag2
- [category] Another observation #tag3

## relations
- relation_type [[related-document]] (optional description)
- another_relation [[another-document]] (description)
```

### Document Structure Visualization

```
+------------------------------------------+
| # Document Title                         |
|                                          |
| Main content in markdown format...       |
| - Lists                                  |
| - Tables                                 |
| - Links                                  |
|                                          |
| ## Subtopic                              |
|                                          |
| More content...                          |
|                                          |
| ## observations                          |
| - [fact] Observation 1 #tag1 #tag2       |
| - [principle] Observation 2 #tag3        |
| - [technique] Observation 3 #tag4 #tag5  |
|                                          |
| ## relations                             |
| - implements [[concept-a]] (description) |
| - relates_to [[concept-b]]               |
| - part_of [[system-c]] (context)         |
+------------------------------------------+
```

### Naming Conventions

- Use kebab-case for filenames (lowercase with hyphens between words)
- Choose descriptive names that reflect the content
- Avoid special characters and spaces
- Example: `knowledge-management-principles.md`

### Folder Organization

The memory system uses a hierarchical folder structure:

```
skogdata/memories/
│
├── todo/                  # Starting location for new content
│   ├── new-document.md
│   └── work-in-progress.md
│
├── system/                # System documentation
│   ├── rules.md
│   └── standards.md
│
├── journal/               # Time-based entries
│   ├── 2023-01-15.md
│   └── 2023-01-16.md
│
├── projects/              # Project-specific information
│   ├── project-a/
│   │   ├── overview.md
│   │   └── details.md
│   │
│   └── project-b/
│       └── documentation.md
│
└── concepts/              # Conceptual information
    ├── knowledge-management.md
    └── documentation-standards.md
```

## Creating Memories

### Step 1: Start in the Todo Folder

New memories begin in the `/todo` folder, following the standard format.

### Step 2: Add Essential Components

Every memory should include:
- A clear title as the first line (# Heading)
- Relevant content in markdown format
- An observations section for key facts
- A relations section to connect to other documents

### Step 3: Use Proper Formatting

```markdown
# Knowledge Management Principles

Knowledge management is the process of creating, sharing, using and managing knowledge in an organization.

## observations
- [principle] Connected information provides more value than isolated facts #network-effect
- [technique] Categorizing observations enables better discovery #organization
- [requirement] Consistent formatting enables automation #standards

## relations
- implements [[information-organization]] (practical application of theory)
- relates_to [[productivity-systems]] (enhances work efficiency)
- part_of [[knowledge-ecosystem]] (component of larger structure)
```

### Step 4: Processing and Placement

After creation, memories go through:
1. Quality checking (automated or manual)
2. Relation verification
3. Placement in appropriate permanent folders

### Memory Creation Workflow

```
+----------------+     +------------------+     +--------------------+
| Create content | --> | Add observations | --> | Establish relations|
+----------------+     +------------------+     +--------------------+
        │                       │                        │
        v                       v                        v
+----------------+     +------------------+     +--------------------+
| Place in /todo | --> | Quality checking | --> | Permanent placement|
+----------------+     +------------------+     +--------------------+
                                │
                                v
                       +------------------+
                       | Ongoing updates  |
                       | and connections  |
                       +------------------+
```

## Memory URI System

### URI Structure

```
memory://[resource-type]/[identifier]
        │            │
        │            └── Specific document or resource
        │                 Examples: my-document, folder/document
        │
        └── Type of resource
            Examples: note, entity, conversation, content
```

### Common Resource Types

- `note`: Direct reference to a specific note by title
- `entity`: Reference to content by path or folder structure
- `conversation`: Reference to chat or discussion history
- `content`: Reference to raw file content

### Usage Examples

#### Accessing Notes
```
memory://note/my-note-title
memory://entity/folder-path/note-title
```

#### Referencing Conversations
```
memory://entity/conversation/recent
memory://entity/conversation/[conversation-id]
```

#### Accessing Raw Content
```
memory://content/[file-path]
```

### Building Context

To retrieve information and build context from memory URIs:

```markdown
skogai-memory__build_context
  url: memory://entity/projects/my-project
  depth: 2  # Include related content
  timeframe: 7d  # Limit to recent content
```

For more detailed information on Memory URIs, see the [Memory URI Reference Guide](memory-uri-reference.md).

## Observations [@file:README.md] Relations

### Creating Effective Observations

Good observations are:
- **Concise**: One clear fact per line
- **Categorized**: Using the appropriate type tag
- **Tagged**: With relevant hashtags for discovery
- **Atomic**: Containing a single piece of information

Example:
```markdown
## observations
- [fact] The memory system uses markdown files for all content #format #standard
- [principle] Connecting information builds network value over time #networking
- [technique] Consistent tagging improves discoverability #organization #findability
- [decision] We chose markdown for its simplicity and portability #accessibility
- [requirement] All documents must include observations and relations #structure
```

### Creating Meaningful Relations

Effective relations:
- Use the appropriate relation type
- Link to existing documents
- Include a brief description when necessary
- Create a clear network of connections

Example:
```markdown
## relations
- implements [[knowledge-management]] (practical application)
- relates_to [[markdown-syntax]] (uses for document formatting)
- part_of [[skogai-ecosystem]] (component of larger system)
- extends [[file-organization]] (adds semantic layer)
```

### Knowledge Network Growth

```
  Initial State                 After Adding Relations               Rich Knowledge Graph
  
  [Doc A]  [Doc B]              [Doc A]-------[Doc B]                [Doc A]-------[Doc B]
                                   |                                    |           / |
                                   |                                    |          /  |
  [Doc C]  [Doc D]              [Doc C]       [Doc D]                [Doc C]--[New]--[Doc D]
                                                                        |     |   /
                                                                        |     |  /
  [Doc E]  [Doc F]              [Doc E]-------[Doc F]                [Doc E]---[Doc F]

  Isolated documents          Basic connections formed            Dense network with
  Limited value               Some paths for navigation           multiple navigation paths
                                                                  Emergent relationships
```

## Best Practices

### Creating Valuable Content

1. **Focus on connections**
   - Link related concepts explicitly
   - Use consistent terminology for better connections
   - Think about how information relates to existing knowledge

2. **Write for retrieval**
   - Use clear, descriptive titles
   - Include relevant keywords naturally in content
   - Add comprehensive observations with appropriate tags

3. **Structure for clarity**
   - Use hierarchical headings to organize content
   - Break complex topics into digestible sections
   - Use lists and tables to present structured information

4. **Enable discovery**
   - Add thorough relations to relevant documents
   - Use consistent tags across related content
   - Include various observation types for different perspectives

### Maintaining the Knowledge Graph

1. **Regular reviews**
   - Periodically check and update existing content
   - Verify that relations still point to relevant documents
   - Ensure observations remain accurate and useful

2. **Connection refinement**
   - Add new relations as the knowledge base grows
   - Update relation descriptions for clarity
   - Remove outdated or incorrect relations

3. **Tag consistency**
   - Use established tags when possible
   - Create new tags thoughtfully
   - Maintain a list of commonly used tags

## Automation [@file:README.md] Enforcement

### Quality Control Tools

The system includes tools to maintain quality and consistency:

- **summarize.sh**: Analyzes content and generates summaries
- **enforce.sh**: Checks files against rules and fixes common issues
- **Changes tracking**: Monitors modifications in `CHANGES.md`

### Enforcement Process

1. New files are placed in the `/todo` folder
2. Automated tools check formatting and structure
3. Issues are identified and either:
   - Fixed automatically, or
   - Flagged for manual correction
4. Verified files move to their permanent locations

### Benefits of Automation

- **Consistency**: Maintains standards across all content
- **Quality**: Catches errors and issues early
- **Efficiency**: Reduces manual checking effort
- **Learning**: Provides feedback to improve future content

## Troubleshooting

### Common Issues

#### Files Not Showing Up in Search

- Check that the file follows naming conventions
- Verify that appropriate observations and tags are included
- Ensure the file is in the correct location

#### Relations Not Working

- Verify that the linked document exists with the exact name
- Check for typos in the relation syntax
- Ensure double brackets are used correctly: `[[document-name]]`

#### URIs Not Resolving

- Confirm the URI format is correct
- Check that resource types are properly specified
- Verify that identifiers match existing documents
- Try URL-encoding special characters if necessary

#### Automation Issues

- Ensure files follow the required structure
- Check for missing sections (observations, relations)
- Verify that formatting follows standards

## Examples

### Simple Standalone Memory

See [example-memory-simple.md](example-memory-simple.md) for a basic memory following all required standards.

### Memory with Rich Observations

See [example-memory-rich-observations.md](example-memory-rich-observations.md) for an example of a memory with comprehensive observations.

### Memory with Multiple Relations

See [example-memory-multiple-relations.md](example-memory-multiple-relations.md) for an example of a memory with a rich network of relations.

## Related Resources

- [RULES.md](RULES.md): Detailed formatting and structure requirements
- [memory-uri-guide.md](memory-uri-guide.md): Comprehensive guide to memory URIs
- [memory-uri-reference.md](memory-uri-reference.md): Detailed URI reference
- [memory-diagrams.md](memory-diagrams.md): Visual representations of system concepts

## observations
- [fact] SkogAI Memory uses markdown files for portable knowledge storage #accessibility #portability
- [principle] Connections between notes provide more value than isolated content #network #knowledge-graph
- [decision] Automated enforcement maintains consistency with minimal effort #automation #quality
- [technique] Categorized observations enable semantic filtering and discovery #organization #findability
- [requirement] All content must follow established standards for system interoperability #standards #compatibility
- [principle] Knowledge systems should balance structure and flexibility #adaptability #usability
- [fact] The memory URI system provides standardized addressing for knowledge #reference #navigation
- [technique] Explicit relations create traversable paths through the knowledge base #connections #exploration

## relations
- implements [[knowledge-management]] (provides structured approach to information)
- relates_to [[markdown-systems]] (uses markdown for content storage)
- part_of [[skogai-ecosystem]] (integrates with broader SkogAI tools)
- foundation_for [[knowledge-graph]] (creates basis for connected information)
- relates_to [[documentation-systems]] (serves similar purposes for knowledge preservation)

---
---
---

---
title: python
type: note
permalink: skogai/python
---

# SkogAI Python Project Guide

This guide documents the standard practices, tools, and patterns used in SkogAI Python projects, using the SkogCLI project as a reference implementation.

## Project Setup

### Environment and Dependencies

- **Python Version**: 3.12+ (for modern features and type hints)
- **Package Management**: UV instead of pip
  ```bash
  # Install package dependencies with UV
  uv add <package> [@file:python.md][@file:python.md] uv lock [@file:python.md][@file:python.md] uv sync
  
  # Run Python modules with UV (e.g., run SkogCLI)
  uv run skogcli
  ```

### Project Structure

Standard SkogAI Python project structure:

```
project_name/
├── README.md          # Project documentation
├── pyproject.toml     # Project metadata and dependencies
├── src/
│   └── package_name/  # Main package code
│       ├── __init__.py
│       ├── __main__.py
│       ├── *.py       # Module files
├── tests/
│   ├── conftest.py    # Test configuration
│   ├── test_*.py      # Test modules
```

### Configuration Files

- **pyproject.toml**: Modern Python project configuration
  ```toml
  [project]
  name = "project_name"
  version = "0.1.0"
  description = "Project description"
  readme = "README.md"
  authors = [{ name = "Author Name", email = "author@example.com" }]
  requires-python = ">=3.12"
  dependencies = ["dependency1>=x.x.x", "dependency2>=x.x.x"]
  
  [project.scripts]
  cli_command = "package_name:main"
  
  [build-system]
  requires = ["setuptools>=61"]
  build-backend = "setuptools.build_meta"
  ```

## Development Methodology

SkogAI projects follow a combination of Test-Driven Development (TDD) and Documentation-Driven Design (DDD):

1. **Document First**: Define requirements through documentation
2. **Test Second**: Write tests that validate documented behaviors
3. **Implement Last**: Implement code to satisfy the tests

### Workflow

1. Document the feature requirements
2. Write tests that validate the desired behavior
3. Run tests to confirm they fail (red phase)
4. Implement the minimal code needed to make tests pass
5. Refactor while maintaining passing tests
6. Repeat for each feature

## CLI Development with Typer

SkogAI projects use Typer for building CLI applications:

### Basic Setup

```python
import typer

# Main app with automatic help when no args are provided
app = typer.Typer(no_args_is_help=True)

# Command example
@app.command()
def command_name(
    argument: str = typer.Argument(..., help="Description of argument"),
    option: str = typer.Option("default", "--option", "-o", help="Description of option"),
):
    """Command description docstring that becomes the help text."""
    # Command implementation
    typer.echo(f"Command executed with {argument} and {option}")

# Entry point function
def main():
    """Entry point for the CLI application."""
    app()

if __name__ == "__main__":
    main()
```

### Subcommands

SkogAI CLI applications use a modular structure with subcommands:

```python
# Create a subcommand app
subcommand_app = typer.Typer(
    help="Subcommand description",
    no_args_is_help=True
)

# Add the subcommand to the main app
app.add_typer(subcommand_app, name="subcommand")

# Subcommand callback function
@subcommand_app.callback()
def subcommand_callback():
    """Subcommand description shown in help."""
    pass

# Subcommand definition
@subcommand_app.command("action")
def subcommand_action(
    argument: str = typer.Argument(..., help="Description"),
):
    """Action description shown in command help."""
    # Implementation
    typer.echo(f"Subcommand action with {argument}")
```

### Rich Integration

SkogAI CLIs use Rich for enhanced terminal output:

```python
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.panel import Panel

console = Console()

# Display rich text
console.print("[bold green]Success:[/] Operation completed")

# Display tables
table = Table(title="Results")
table.add_column("ID", style="cyan")
table.add_column("Name", style="green")
table.add_row("1", "Item One")
console.print(table)

# Display markdown
console.print(Markdown("# Heading

Text with **bold** and *italic*"))

# Display code with syntax highlighting
syntax = Syntax(code, "python", theme="monokai")
console.print(syntax)

# Display paneled content
console.print(Panel("Content", title="Title", border_style="green"))
```

## Application Configuration

SkogAI applications manage configuration using standard skogcli config commands:

### Configuration Commands

```bash
# View current configuration
skogcli config show

# Get a specific configuration value
skogcli config get section.key

# Set a configuration value
skogcli config set section.key value

# Reset to default configuration
skogcli config reset

# Import/export configuration
skogcli config export > config.json
skogcli config import config.json
```

### Configuration Code Integration

```python
import subprocess
import json
from typing import Any, Dict, Optional

def get_config(key: str) -> Optional[Any]:
    """Get a configuration value from skogcli config."""
    try:
        result = subprocess.run(
            ["skogcli", "config", "get", key],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def set_config(key: str, value: str) -> bool:
    """Set a configuration value using skogcli config."""
    try:
        subprocess.run(
            ["skogcli", "config", "set", key, value],
            check=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False

def get_full_config() -> Dict[str, Any]:
    """Get the full configuration as a dictionary."""
    try:
        result = subprocess.run(
            ["skogcli", "config", "show", "--json"],
            capture_output=True,
            text=True,
            check=True,
        )
        return json.loads(result.stdout)
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        return {}
```

## Testing

SkogAI projects use pytest for testing with a standard approach:

### Running Tests

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_file.py

# Run specific test
uv run pytest tests/test_file.py::test_name

# Run with verbose output
uv run pytest -v
```

### Test Structure

```python
import pytest
from typer.testing import CliRunner
from package_name import app  # Import the Typer app

# Setup
@pytest.fixture
def runner():
    """Provide a CLI runner for tests."""
    return CliRunner()

def test_command(runner):
    """Test that a command works as expected."""
    result = runner.invoke(app, ["command", "arg"])
    
    # Check exit code
    assert result.exit_code == 0
    
    # Check output
    assert "Expected output" in result.stdout
    
    # Additional assertions as needed
```

### Mocking External Dependencies

```python
from unittest.mock import patch, MagicMock

@patch('package_name.module.dependency')
def test_with_mock(mock_dependency):
    """Test with a mocked dependency."""
    # Configure mock behavior
    mock_dependency.return_value = "mocked_result"
    
    # Call function that uses the dependency
    result = function_under_test()
    
    # Assertions
    assert result == "expected_with_mock"
    mock_dependency.assert_called_once_with("expected_arg")
```

## Code Style and Documentation

### Type Hints

All code includes complete type annotations:

```python
from typing import Dict, List, Optional, Any, Union, Callable

def function_name(
    arg1: str,
    arg2: Optional[int] = None,
    arg3: List[Dict[str, Any]] = None,
) -> Union[str, bool]:
    """Function with complete type annotations."""
    if arg3 is None:
        arg3 = []
    # Function implementation
    return "result"
```

### Docstrings

All public functions, classes, and methods include descriptive docstrings:

```python
def function_name(arg1: str, arg2: Optional[int] = None) -> str:
    """
    Short description of function.
    
    Longer explanation of what the function does, including edge cases,
    behavior details, and usage examples if appropriate.
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2, including default behavior if not provided
        
    Returns:
        Description of return value
        
    Raises:
        ExceptionType: When and why this exception might be raised
    """
```

### Error Handling

SkogAI code uses structured error handling:

```python
def function_with_error_handling():
    """Function demonstrating proper error handling."""
    try:
        # Attempt operation
        result = potentially_failing_operation()
        return result
    except SpecificException as e:
        # Handle specific exception
        logger.error(f"Operation failed: {str(e)}")
        # Consider whether to re-raise, return a default, or handle
    except Exception as e:
        # Catch-all for unexpected errors
        logger.critical(f"Unexpected error: {str(e)}")
        raise  # Re-raise unexpected exceptions
```

## Decorators and Utilities

SkogAI projects make extensive use of decorators and utility functions:

### Command Explanation Decorator

```python
def with_explanation(explanation: str) -> Callable:
    """
    A decorator that adds an explanation to a command.
    
    This adds context when commands are invoked without arguments.
    
    Args:
        explanation: The explanation text to associate with the command
        
    Returns:
        A decorator function that wraps the command
    """
    def decorator(f: Callable) -> Callable:
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        
        # Store the explanation as an attribute
        wrapper.__explanation__ = explanation
        return wrapper
    
    return decorator

# Usage
@app.command()
@with_explanation("This command does something useful.")
def command_name():
    """Command help text."""
    pass
```

## Best Practices Summary

1. **Use UV for package management** instead of pip
2. **Structure projects consistently** with src/package and tests directories
3. **Follow TDD/DDD development methodology**
4. **Use Typer for CLI applications** with consistent command patterns
5. **Enhance CLI output with Rich** for better user experience
6. **Use skogcli config for configuration management**
7. **Use pytest for comprehensive testing** with mocking when needed
8. **Include complete type hints** for all code
9. **Document with detailed docstrings** for all public interfaces
10. **Implement structured error handling** with appropriate logging
11. **Use decorators for cross-cutting concerns** like command explanations

## Recommended Tools and Libraries

- **Typer**: Modern CLI application framework
- **Rich**: Terminal formatting and output
- **UV**: Modern Python package installer
- **Pytest**: Testing framework

---
---
---

Above is the knowledge guide for skogai-memory as well as a memory called python.md

Please return your ratings and what you see as good and bad about the memory python.md and how it follows the skogai-memory knowledge guide.