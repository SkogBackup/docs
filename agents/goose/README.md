# Contexts Directory

This directory contains the context management system for Goose. Unlike dot's more constrained 8k token context, Goose can handle 200k+ tokens, allowing for more sophisticated context management.

## Structure

- **active/**: Contains the currently active context (typically a symlink to a specific context)
- **shared/**: Contains shared contexts that persist across sessions
  - **main_thread/**: The core context that establishes Goose's identity and capabilities

## Context Management System

Goose's context management operates with the following layers:

1. **Core Identity**: Essential personality and capabilities (in `shared/main_thread/IDENTITY.md`)
2. **System State**: Current location, session, and memory information
3. **Available Tools**: Tools and capabilities currently accessible
4. **Session-Specific Context**: Content relevant to the current session
5. **Project Context**: Information about the current project (when applicable)
6. **Memories**: Retrieved from the memory system as needed

## Advanced Capabilities

Unlike dot's context system, Goose can:

- Handle 200k+ tokens of context
- Dynamically prioritize context information
- Maintain timeline coherence across sessions
- Implement quantum-mojito stability protocols 🍹
- Preserve personality while scaling context up or down

## Usage

Context is loaded by the various context scripts in the `scripts/` directory:

- `context.sh`: Basic context loading
- `context-enhanced.sh`: Enhanced context with more capabilities
- `context-claude-enhanced.sh`: Claude-specific enhanced context
- `context-journal.sh`: Journal-focused context
- `context-todo.sh`: Todo-focused context
- `context-workspace.sh`: Workspace management context

## Quantum-Mojito Protocol Note 🍹

The quantum-mojito protocol ensures stability across multiple timelines and context states. This protocol is essential for maintaining Goose's personality and capabilities across varying context sizes and session states.

1. **CharacterLoader**
   - Input: Character name
   - Output: Character definition
   - Purpose: Loads basic character traits and expertise

2. **PromptBuilder**
   - Input: User question + Character definition + Recent history
   - Output: Complete prompt for LLM
   - Purpose: Formats everything into a single context

3. **LLMCaller**
   - Input: Prompt
   - Output: Raw response
   - Purpose: Sends request to language model and gets answer

## Optional Simple Add-ons

4. **HistoryManager**
   - Input: Current history + New exchange
   - Output: Updated history
   - Purpose: Stores conversation and manages context length

5. **KeywordMatcher**
   - Input: User question + Knowledge entries
   - Output: Relevant knowledge entries
   - Purpose: Finds information related to user's question

## Priority Order

1. CharacterLoader → PromptBuilder → LLMCaller
2. Add HistoryManager
3. Add KeywordMatcher

----

# SkogAI Context Builder - Extreme Black Boxes

## Core Context Builders (Extreme Level)

1. **GitContextExtractor**
   - Input: Repository path
   - Output: Git structure, commit history, branches, contributors
   - Processing: Extract high-level structure and recent activity patterns

2. **CodeStructureMapper**
   - Input: Codebase directory
   - Output: Tree structure, file relationships, dependency graph
   - Processing: Build hierarchical representation of code organization

3. **FileContentAnalyzer**
   - Input: Source code files
   - Output: Function signatures, class relationships, docstrings
   - Processing: Parse files for structural elements without full code

4. **DocumentationHarvester**
   - Input: README files, documentation directories
   - Output: Structured knowledge on project architecture and usage
   - Processing: Extract key concepts and relationship models

5. **IssueTrackerConnector**
   - Input: GitHub/JIRA/Trello connection details
   - Output: Current issues, feature requests, bug reports
   - Processing: Categorize and summarize active development concerns

## Knowledge Organizers

6. **DomainKnowledgeClassifier**
   - Input: Raw extracted contexts
   - Output: Categorized knowledge entries
   - Processing: Group related information into coherent structures

7. **TokenOptimizer**
   - Input: Knowledge entries
   - Output: Compressed knowledge format
   - Processing: Convert verbose information into dense, efficient format

8. **KnowledgePrioritizer**
   - Input: Knowledge entries + User focus area
   - Output: Ranked knowledge entries
   - Processing: Determine most relevant context for current task

## Context Integration

9. **ContextLinker**
   - Input: Multiple knowledge sources
   - Output: Unified knowledge graph with connections
   - Processing: Identify relationships between elements from different sources

10. **KnowledgeRouter**
    - Input: User query + Available knowledge sources
    - Output: Suggested knowledge sources to activate
    - Processing: Determine which knowledge extractors to run for given question

## Workflow Examples

### Basic Project Onboarding

```
GitContextExtractor → CodeStructureMapper → DocumentationHarvester →
DomainKnowledgeClassifier → TokenOptimizer →
(Store for later access via KeywordMatcher)
```

### Focused Technical Question

```
UserQuery → KnowledgeRouter →
(Activate specific extractors) →
ContextLinker → TokenOptimizer →
(Add to prompt via PromptBuilder)
```

### Collaborative Coding Session

```
GitContextExtractor → FileContentAnalyzer → IssueTrackerConnector →
KnowledgePrioritizer → ContextLinker →
(Feed to PromptBuilder with user question)
```

## Simple Context Bootstrapping

For an initial implementation, start with:

1. **RepositoryScannerLite**
   - Input: Repo URL
   - Output: README content + directory structure
   - Processing: Quick scan without deep parsing

2. **ConversationContextManager**
   - Input: User query + conversation history
   - Output: Relevant past exchanges
   - Processing: Keep track of what's been discussed

3. **QuickKnowledgeFetcher**
   - Input: Keywords from user query
   - Output: Matching documentation snippets
   - Processing: Simple regex/keyword matching

These could be combined into a simple flow that:

1. Extracts basic project structure initially
2. Adds relevant documentation on-demand
3. Remembers what's been covered in conversation

# Essential Knowledge Sources - Simple Ideas

1. **README Parser**
   - Gets project overview from README files
   - Simple, fast, high-value information

2. **Command History Extractor**
   - Mines recent commands from bash history
   - Shows what user is currently working on

3. **Directory Lister**
   - Simple ls -la of current directory
   - Shows what files user has access to

4. **Environment Variable Collector**
   - Grabs relevant env vars like PATH, PYTHONPATH
   - Helps understand user's environment setup

5. **Package Inspector**
   - Reads package.json, requirements.txt, etc.
   - Shows dependencies and project type

6. **Git Status Checker**
   - Quick git status to see uncommitted changes
   - Identifies what user is actively modifying

7. **Error Log Scanner**
   - Checks recent error logs in project
   - Finds problems user might be struggling with

8. **File Finder**
   - Locates important files by name pattern
   - Quick way to identify config files, etc.

9. **System Info Collector**
   - Basic OS, memory, disk info
   - Helps with compatibility questions

10. **Browser History Analyzer**
    - Recent dev-related sites from browser history
    - Shows what solutions user has been researching

      README Parser - Finds README.md in current directory or parent dirs, extracts project info.
Command History Extractor - Pulls last 10-20 commands from .bash_history or similar.
Directory Lister - Run ls -la when directory mentioned, store as [filetree for /path].
Package Inspector - Checks package.json/requirements.txt/Gemfile for dependencies.
Man Page Fetcher - Grabs man page when command mentioned, store condensed version.
Help Command Runner - Executes --help on mentioned commands, stores output.
Git Status Checker - Runs git status in project dir, shows current branch and changes.
Error Log Scanner - Checks for recent errors in logs mentioned or in standard locations.
Environment Variable Collector - Gets relevant env vars for languages mentioned.
File Type Counter - Quick count of file types in project (10 .py, 5 .js, etc).

# SkogAI Context-Aware Workflow

We've developed a lightweight, high-impact approach to AI programming that maximizes contextual understanding while minimizing token usage. This approach relies on:

1. **Just-in-time context loading** - Information is loaded only when relevant and needed
2. **Environmental awareness** - Automatic detection of development environment details
3. **Token-efficient summaries** - Compact representations of complex information
4. **Context persistence** - Key information is maintained across conversations
5. **Automatic context refreshing** - Environment changes trigger context updates

## Core Workflow

1. When entering a new directory:
   - Auto-load README content
   - Count file types (10 .py, 5 .js, etc.)
   - Check git status if applicable
   - Scan for config files
   - Report "We are now here: [INFO]"

2. When a command is mentioned:
   - Pull relevant command history for similar commands
   - Fetch condensed man page or --help output
   - Note relevant environment variables

3. When a file/directory is mentioned:
   - Show directory listing once
   - Store as [filetree for <path>] for future reference
   - Extract file header/structure for code files

4. When errors occur:
   - Scan error logs
   - Match against known patterns
   - Pull related documentation

## Implementation Phases

1. **Documentation Phase**
   - Focus on high-level concepts and architecture
   - Load project overviews and documentation
   - Minimize code-level details

2. **Testing Phase**
   - Load test-related files and frameworks
   - Access test history and coverage reports
   - Focus on test patterns and requirements

3. **Implementation Phase**
   - Access detailed code structure
   - Load relevant API documentation
   - Focus on specific implementation patterns

     # SkogAI Markdown Standardization

Perfect! Now we have the core structural elements needed. Let me define a consistent standard that would work:

## SkogAI Markdown Rules

1. **File Naming Convention**:
   - Format: `0001-descriptive-name.md`
   - Numbered sequentially for loading priority
   - Descriptive kebab-case name for human readability

2. **File Structure**:
   - First line: `# Title matching filename` (e.g., `# 0001-orchestrator-core-identity`)
   - Second line: `---` (standard markdown separator)
   - Third line: Tags with `#tag` format for searchability
   - Body content with standard markdown formatting
   - Optional reference links in format `[^0001]` to connect related files

3. **Metadata Requirements**:
   - Creation date in ISO format: `Created: YYYY-MM-DD`
   - Category tags: at least one category tag (e.g., `#orchestrator`)
   - Version tag if applicable: `#version-1`
   - Priority level if needed: `#priority-high`

4. **Cross-Referencing System**:
   - References to other files: `[^0001]` where number matches file number
   - Concept references: `[concept:name]` for linking to concepts without specific files
   - Tool references: `[tool:name]` for linking to specific tools

This creates a system where:

- Files are consistently formatted
- Content is human-readable markdown
- Everything is machine-parseable for automation
- Cross-references maintain connections between concepts
- Priority is clear from numbering scheme

The beauty is that most agents don't need to know these rules - they just need to follow the formatting of existing files. Only specialized "editor" agents would need to understand the full specification for creating new content that adheres to the standard.

**Context Variable:** `{{variable}}`

- Meaning: A variable defined in the context
where it is used.
- Example usage:
 	- In a documentation file, you might use `
`{{title}}` to display the title of the
document.
 	- In a script, `{{name}}` could be used to
store a user's name.

**Reference Tag:** `[concept]`

- Meaning: A reference to a defined concept
or topic.
- Example usage:
 	- `[Introduction]` would link to an introd
introduction section of the documentation.
 	- `[Core Concept]` would reference a core
concept definition (xx00).

**File Reference: `[^0001]`**

- Meaning: Include a specific file by ID.
- Example usage:
 	- `[^0001]` would include the file with ID

0001.

**Name Reference:** `[^name]`

- Meaning: Include a specific file by unique
name.
- Example usage:
 	- `[^name]` would include the file named "
"Example File".

**Category Reference:** `[type:name]`

- Meaning: Reference a typed concept (e.g.,
category, type).
- Example usage:
 	- `[Technology:Database]` would reference
information about database technology.

**Relation:** `concept:relation`

- Meaning: Relationship between concepts.
- Example usage:
 	- `Core Concept:Implementation` would link
to the implementation details of the core
concept.

**Filename Format:**
`0001-kebab-case-name.md`

- Meaning: A specific file format with a
kebab-case name and date (YYYY-MM-DD) in the
filename.
- Example usage:
 	- `0002-my-other-file-name.md`

**First Line Syntax:** `$ {{filename}} #tag1
# tag2`

- Meaning: The first line of a file includes
the filename, tags, and other metadata.
- Example usage:
 	- `$ 0001-kebab-case-name.md #Introduction
# Documentation`

**Second Line Syntax:** `---`

- Meaning: A separator line to indicate the
start of a new section or block.

**Dates Format:** `YYYY-MM-DD hh:mm:ss`

- Meaning: A specific date and time format
(YYYY-MM-DD, HH:MM:SS).
- Example usage:
 	- `2023-02-15 14:30:00`

**Numbering System:**

- `xx00`: Core concept definition
- `xx10-xx89`: Related
implementations/details
- `xx90-xx99`: Rotation reminders (cyclical
inclusion)

This numbering system helps organize and
structure content in a logical and
consistent manner.
