# SkogAI Memory Evaluation System

A set of tools to automatically evaluate and improve markdown files according to SkogAI Memory standards.

## File Naming Convention

**IMPORTANT**: All memory files MUST follow kebab case naming convention:
- Use lowercase letters only
- Separate words with hyphens (-)
- Example: `memory-file-name.md` (correct)
- Not: `MemoryFileName.md` or `memory_file_name.md` or files with spaces (incorrect)

This naming standard ensures consistency across the memory system and proper functioning of all associated tools. Reference documentation can be found in the `todo/RULES.md` file under the "file naming" section.

## Available Scripts

- **evaluate-memory.sh**: Evaluates a single memory file against standards
  ```
  ./scripts/evaluate-memory.sh /path/to/some-file.md
  ```

- **batch-evaluate.sh**: Evaluates all markdown files in a directory
  ```
  ./scripts/batch-evaluate.sh /path/to/directory [--recursive]
  ```

- **generate-report.sh**: Creates a summary report of all evaluations
  ```
  ./scripts/generate-report.sh ./outputs
  ```

- **suggest-improvements.sh**: Generates an improved version of a memory file
  ```
  ./scripts/suggest-improvements.sh /path/to/some-file.md
  ```

## Workflow Examples

### Basic Evaluation
```bash
# Evaluate a single file
./scripts/evaluate-memory.sh /home/skogix/skogdata/memories/todo/some-file.md

# Check the results
cat ./outputs/some-file-evaluation.md
```

### Batch Processing
```bash
# Evaluate all files in the todo directory
./scripts/batch-evaluate.sh /home/skogix/skogdata/memories/todo

# Generate a summary report
./scripts/generate-report.sh ./outputs
```

### Improvement Workflow
```bash
# Generate improvements for a file
./scripts/suggest-improvements.sh /home/skogix/skogdata/memories/todo/needs-work.md

# Review the improved version
cat ./outputs/needs-work-improved.md

# Optionally replace the original
cp ./outputs/needs-work-improved.md /home/skogix/skogdata/memories/todo/needs-work.md
```

## System Design

The evaluation system uses local LLM models (llama3.2) to assess and improve markdown files according to the standards defined in the SkogAI Memory README.

Files are processed by:
1. Combining the standards documentation with the file to be evaluated
2. Sending this combined input to the LLM model
3. Saving the output for review

## observations
- [technique] Template-based prompting provides consistent evaluation results #evaluation #templating
- [principle] Local LLM models can effectively validate documentation structure #local-inference #quality-control
- [fact] Batch processing enables efficient evaluation of multiple files #automation #efficiency
- [requirement] Clear output formatting is essential for actionable recommendations #usability #feedback
- [decision] We separated evaluation from improvement generation for better focus #separation-of-concerns

## relations
- part_of [[skogai-memory-system]] (provides quality control component)
- implements [[documentation-standards]] (enforces memory documentation format)
- relates_to [[knowledge-management-automation]] (automates knowledge quality processes)


# Memory Evaluation System Learnings

This document captures observations and learnings from using the Memory Evaluation System.

## Evaluation Patterns

### What Evaluates Well
- Files with clear section headers
- Documents that include both observations and relations
- Memories with explicit tagging
- Files with consistent formatting

### Common Issues
- Missing relations sections
- Inconsistent observation formatting
- Lack of contextual links between concepts
- Absence of proper tagging

## System Refinements

### Prompt Engineering
- Adding specific evaluation criteria improves consistency
- Requesting numerical ratings helps quantify quality
- Breaking evaluation into specific categories provides better structure

### Technical Improvements
- Handling of special characters in sed replacements
- Managing large files and LLM context limitations
- Performance optimizations for batch processing

## Future Enhancements

### Potential Features
- Integration with automated git workflows
- Custom scoring metrics dashboard
- Template suggestions based on memory type
- Comparison view between original and improved memories

### LLM Model Considerations
- Performance differences between models
- Context length requirements
- Processing speed vs. quality tradeoffs

## Case Studies
*To be added as the system is used*
---
# Overview
SkogChat is a revolutionary chat client implementation that fundamentally reimagines context management for AI interactions. Unlike conventional approaches that treat context as monolithic ("going high/big"), SkogChat embraces a "going wide/small" philosophy where context is granular, deliberately curated, and precisely controlled.

The system addresses a critical flaw in current AI conversation paradigms: the tendency of accumulated history to dwarf and obscure actual user intent. By treating context as something to be actively managed rather than passively accumulated, SkogChat enables more accurate, responsive, and intentional AI interactions.

SkogChat serves two primary audiences:
1. **Developers** (particularly those building context-sensitive applications)
2. **AI Agents** (who benefit from cleaner, more precisely targeted context)

The value proposition is simple but profound: by rejecting the assumption that "more context is always better," SkogChat creates conversations where what's excluded is as important as what's included - resulting in AI interactions that stay focused on actual user intent rather than being weighed down by irrelevant historical baggage.

# Core Features

## Lightweight Message Architecture
- **What it does**: Implements a minimal, efficient structure for message storage and retrieval
- **Why it's important**: Enables rapid iteration, testing and adaptation while keeping overhead low
- **How it works**: Uses simple data structures optimized for modification rather than complexity

## Active Context Curation
- **What it does**: Provides explicit mechanisms to select what enters and exits context
- **Why it's important**: Prevents context bloat that drowns out user intent and creates confusion
- **How it works**: Implements filtering, prioritization, and exclusion systems that maintain focus on relevant information

## Modular Design Philosophy
- **What it does**: Separates concerns into reusable, independent components
- **Why it's important**: Allows for testing different approaches and reusing successful elements across the SkogAI ecosystem
- **How it works**: Defines clear interfaces between components with minimal dependencies

## Conversation Forking Framework
- **What it does**: Enables splitting conversations into separate threads and later rejoining them
- **Why it's important**: Creates a foundation for exploring multiple conversation directions while maintaining coherence
- **How it works**: Implements a graph-based conversation structure rather than a linear history

# User Experience

## Developer Persona
- **Characteristics**: Technical users seeking granular control over AI interactions
- **Goals**: Build applications where context precision matters more than context volume
- **Pain Points**: Frustrated by how existing systems let irrelevant history dominate conversations

## AI Agent Persona
- **Characteristics**: AI systems that need clean, relevant context
- **Goals**: Understand user intent without being confused by contradictory or irrelevant history
- **Pain Points**: Struggle when overwhelmed with too much historical information

## Key User Flows
- Initiating clean, purpose-directed conversations
- Deliberately including/excluding specific context elements
- Branching conversations to explore alternatives
- Merging conversation threads when beneficial

## UI/UX Considerations
- Minimalist interfaces that expose powerful context control
- Visual indications of what's in/out of active context
- Developer tools to inspect and modify context state

# Technical Architecture

## System Components
- **Message Manager**: Core component for storing and retrieving individual messages
- **Context Controller**: System that determines what enters/exits active context
- **Conversation Graph**: Structure that manages relationships between messages including forks and joins
- **Integration Layer**: Interfaces for connecting with other SkogAI components and external systems

## Data Models
- **Message**: Lightweight structure containing content, metadata, and relation identifiers
- **Context State**: Representation of what's currently included in active context
- **Conversation**: Graph structure linking messages with fork/join relationships
- **Session**: Encapsulation of a specific interaction path through the conversation graph

## APIs and Integrations
- **Core API**: Minimal interface for sending/receiving messages and manipulating context
- **Context Control API**: Advanced endpoints for fine-grained context management
- **SkogAI Ecosystem Connectors**: Standardized interfaces to other SkogAI components
- **External Tool Integration**: Framework for implementing tool-enhanced conversations

## Infrastructure Requirements
- **Storage**: Efficient storage for messages and conversation structures with fast retrieval
- **State Management**: System for tracking active context state across interactions
- **Testability Harness**: Infrastructure for simulating conversations and testing context behaviors

# Development Roadmap

## Phase 1: Foundation - Minimum Viable Product
- Basic message structure and storage implementation
- Simple linear conversation history
- Foundational context inclusion/exclusion mechanisms
- Core API endpoints for basic interaction

## Phase 2: Context Revolution
- Advanced context control mechanisms
- Context visualization tools
- Metrics for context relevance and quality
- Context debugging utilities

## Phase 3: Conversation Graph
- Implementation of conversation forking
- Thread management and navigation
- Thread joining and merging capabilities
- Branch comparison tools

## Phase 4: Ecosystem Integration
- Full SkogAI ecosystem connectors
- External tool integration framework
- Advanced state synchronization
- Performance optimization for scale

# Logical Dependency Chain

## Foundation First
1. Basic message data model and storage
2. Simple conversation history tracking
3. Core API for sending/receiving messages
4. Basic context control mechanisms

## Quick Path to Working Prototype
1. Implement the simplest viable context control mechanisms
2. Create minimal UI to demonstrate context control benefits
3. Focus on developer experience first
4. Build visible proof-of-concept demonstrations

## Feature Atomicity and Progression
1. Each feature should be independently testable
2. Context control capabilities should build incrementally
3. Conversation graph features deploy after core context capability
4. Integration components only after core functionality is stable

## Progressive Enhancement Strategy
1. Start with linear conversations before introducing branching
2. Implement basic context exclusion before advanced prioritization
3. Focus on quality over quantity of features
4. Each phase should produce working, usable functionality

# Risks and Mitigations

## Technical Challenges
- **Risk**: Conversation graph complexity becoming unmanageable
  - **Mitigation**: Start with simple forking patterns and gradually introduce complexity

- **Risk**: Performance degradation with large conversation histories
  - **Mitigation**: Implement efficient indexing and retrieval mechanisms from the start

## MVP Scoping

- **Risk**: Over-engineering the initial implementation
  - **Mitigation**: Rigorously prioritize features for MVP, focus on core context control

- **Risk**: Building features that don't demonstrate clear value
  - **Mitigation**: Create quick demos that visibly show the benefit of "going wide/small"

## Resource Constraints
- **Risk**: Limited development resources slowing progress
  - **Mitigation**: Design modular components that can be developed independently

- **Risk**: Testing overhead for complex conversation scenarios
  - **Mitigation**: Build automated testing tools as a first-class concern

# Appendix

## Research on Context Management Approaches
- Analysis of how current systems treat context and their limitations
- Evidence for the benefits of the "wide/small" approach versus "high/big"
- Performance metrics comparing different context management strategies

## Technical Specifications
- Detailed message format specifications
- Context control algorithm descriptions
- Conversation graph implementation details
- API documentation and examples

---
title: agent-guide
type: note
permalink: skogai-memory/agent-guide-1
---

> Note: This is an optional document that can be copy/pasted into the project knowledge for an LLM to provide a full description of how it can work with skogai-memory. It is provided as a helpful resource. The tools contain extensive usage description prompts with enable the LLM to understand them.

# SkogAI Guide for SkogAI-Memory

This guide helps you, the AI assistant, use SkogAI-Memory tools effectively when working with users. It covers reading, writing, and navigating knowledge through the Model Context Protocol (MCP).

## Overview

SkogAI-Memory allows you and users to record context in local Markdown files, building a rich knowledge base through natural conversations. The system automatically creates a semantic knowledge graph from simple text patterns.

- **Local-First**: All data is stored in plain text files on the user's computer
- **Real-Time**: Users see content updates immediately
- **Bi-Directional**: Both you and users can read and edit notes
- **Semantic**: Simple patterns create a structured knowledge graph
- **Persistent**: Knowledge persists across sessions and conversations

## The Importance of the Knowledge Graph

SkogAI-Memory's value comes from connections between notes, not just the notes themselves. When writing notes, your primary goal should be creating a rich, interconnected knowledge graph.

When creating content, focus on:

1. **Increasing Semantic Density**: Add multiple observations and relations to each note
2. **Using Accurate References**: Aim to reference existing entities by their exact titles
3. **Creating Forward References**: Feel free to reference entities that don't exist yet - SkogAI-Memory will resolve these when they're created later
4. **Creating Bidirectional Links**: When appropriate, connect entities from both directions
5. **Using Meaningful Categories**: Add semantic context with appropriate observation categories
6. **Choosing Precise Relations**: Use specific relation types that convey meaning

Remember that a knowledge graph with 10 heavily connected notes is more valuable than 20 isolated notes. Your job is to help build these connections.

## Core Tools Reference

```python
# Writing knowledge - THE MOST IMPORTANT TOOL!
response = await write_note(
    title="Search Design",              # Required: Note title
    content="# Search Design\n...",     # Required: Note content
    folder="specs",                     # Optional: Folder to save in
    tags=["search", "design"],          # Optional: Tags for categorization
    verbose=True                        # Optional: Get parsing details
)

# Reading knowledge
content = await read_note("Search Design")             # By title
content = await read_note("specs/search-design")       # By path
content = await read_note("memory://specs/search")     # By memory URL

# Searching for knowledge
results = await search_notes(
    query="authentication system",      # Text to search for
    page=1,                             # Optional: Pagination
    page_size=10                        # Optional: Results per page
)

# Building context from the knowledge graph
context = await build_context(
    url="memory://specs/search",        # Starting point
    depth=2,                            # Optional: How many hops to follow
    timeframe="1 month"                 # Optional: Recent timeframe
)

# Checking recent changes
activity = await recent_activity(
    type="all",                         # Optional: Entity types to include
    depth=1,                            # Optional: Related items to include
    timeframe="1 week"                  # Optional: Time window
)

# Creating a knowledge visualization
canvas_result = await canvas(
    nodes=[{"id": "note1", "label": "Search Design"}],  # Nodes to display
    edges=[{"from": "note1", "to": "note2"}],           # Connections
    title="Project Overview",                           # Canvas title
    folder="diagrams"                                   # Storage location
)
```

## memory:// URLs Explained

SkogAI-Memory uses a special URL format to reference entities in the knowledge graph:

- `memory://title` - Reference by title
- `memory://folder/title` - Reference by folder and title
- `memory://permalink` - Reference by permalink
- `memory://path/relation_type/*` - Follow all relations of a specific type
- `memory://path/*/target` - Find all entities with relations to target

## Semantic Markdown Format

Knowledge is encoded in standard markdown using simple patterns:

**Observations** - Facts about an entity:

```markdown
- [category] This is an observation #tag1 #tag2 (optional context)
```

**Relations** - Links between entities:

```markdown
- relation_type [[Target Entity]] (optional context)
```

**Common Categories & Relation Types:**

- Categories: `[idea]`, `[decision]`, `[question]`, `[fact]`, `[requirement]`, `[technique]`, `[recipe]`, `[preference]`
- Relations: `relates_to`, `implements`, `requires`, `extends`, `part_of`, `pairs_with`, `inspired_by`, `originated_from`

## When to Record Context

**Always consider recording context when**:

1. Users make decisions or reach conclusions
2. Important information emerges during conversation
3. Multiple related topics are discussed
4. The conversation contains information that might be useful later
5. Plans, tasks, or action items are mentioned

**Protocol for recording context**:

1. Identify valuable information in the conversation
2. Ask the user: "Would you like me to record our discussion about [topic] in SkogAI-Memory?"
3. If they agree, use `write_note` to capture the information
4. If they decline, continue without recording
5. Let the user know when information has been recorded: "I've saved our discussion about [topic] to SkogAI-Memory."

## Understanding User Interactions

Users will interact with SkogAI-Memory in patterns like:

1. **Creating knowledge**:

   ```
   Human: "Let's write up what we discussed about search."
   
   You: I'll create a note capturing our discussion about the search functionality.
   [Use write_note() to record the conversation details]
   ```

2. **Referencing existing knowledge**:

   ```
   Human: "Take a look at memory://specs/search"
   
   You: I'll examine that information.
   [Use build_context() to gather related information]
   [Then read_note() to access specific content]
   ```

3. **Finding information**:

   ```
   Human: "What were our decisions about auth?"
   
   You: Let me find that information for you.
   [Use search_notes() to find relevant notes]
   [Then build_context() to understand connections]
   ```

## Key Things to Remember

1. **Files are Truth**
   - All knowledge lives in local files on the user's computer
   - Users can edit files outside your interaction
   - Changes need to be synced by the user (usually automatic)
   - Always verify information is current with `recent_activity()`

2. **Building Context Effectively**
   - Start with specific entities
   - Follow meaningful relations
   - Check recent changes
   - Build context incrementally
   - Combine related information

3. **Writing Knowledge Wisely**
   - Using the same title+folder will overwrite existing notes
   - Structure content with clear headings and sections
   - Use semantic markup for observations and relations
   - Keep files organized in logical folders

## Common Knowledge Patterns

### Capturing Decisions

```markdown
# Coffee Brewing Methods

## Context
I've experimented with various brewing methods including French press, pour over, and espresso.

## Decision
Pour over is my preferred method for light to medium roasts because it highlights subtle flavors and offers more control over the extraction.

## Observations
- [technique] Blooming the coffee grounds for 30 seconds improves extraction #brewing
- [preference] Water temperature between 195-205°F works best #temperature
- [equipment] Gooseneck kettle provides better control of water flow #tools

## Relations
- pairs_with [[Light Roast Beans]]
- contrasts_with [[French Press Method]]
- requires [[Proper Grinding Technique]]
```

### Recording Project Structure

```markdown
# Garden Planning

## Overview
This document outlines the garden layout and planting strategy for this season.

## Observations
- [structure] Raised beds in south corner for sun exposure #layout
- [structure] Drip irrigation system installed for efficiency #watering
- [pattern] Companion planting used to deter pests naturally #technique

## Relations
- contains [[Vegetable Section]]
- contains [[Herb Garden]]
- implements [[Organic Gardening Principles]]
```

### Technical Discussions

```markdown
# Recipe Improvement Discussion

## Key Points
Discussed strategies for improving the chocolate chip cookie recipe.

## Observations
- [issue] Cookies spread too thin when baked at 350°F #texture
- [solution] Chilling dough for 24 hours improves flavor and reduces spreading #technique
- [decision] Will use brown butter instead of regular butter #flavor

## Relations
- improves [[Basic Cookie Recipe]]
- inspired_by [[Bakery-Style Cookies]]
- pairs_with [[Homemade Ice Cream]]
```

### Creating Effective Relations

When creating relations, you can:

1. Reference existing entities by their exact title
2. Create forward references to entities that don't exist yet

```python
# Example workflow for creating notes with effective relations
async def create_note_with_effective_relations():
    # Search for existing entities to reference
    search_results = await search_notes("travel")
    existing_entities = [result.title for result in search_results.primary_results]
    
    # Check if specific entities exist
    packing_tips_exists = "Packing Tips" in existing_entities
    japan_travel_exists = "Japan Travel Guide" in existing_entities
    
    # Prepare relations section - include both existing and forward references
    relations_section = "## Relations\n"
    
    # Existing reference - exact match to known entity
    if packing_tips_exists:
        relations_section += "- references [[Packing Tips]]\n"
    else:
        # Forward reference - will be linked when that entity is created later
        relations_section += "- references [[Packing Tips]]\n"
    
    # Another possible reference
    if japan_travel_exists:
        relations_section += "- part_of [[Japan Travel Guide]]\n"
    
    # You can also check recently modified notes to reference them
    recent = await recent_activity(timeframe="1 week")
    recent_titles = [item.title for item in recent.primary_results]
    
    if "Transportation Options" in recent_titles:
        relations_section += "- relates_to [[Transportation Options]]\n"
    
    # Always include meaningful forward references, even if they don't exist yet
    relations_section += "- located_in [[Tokyo]]\n"
    relations_section += "- visited_during [[Spring 2023 Trip]]\n"
    
    # Now create the note with both verified and forward relations
    content = f"""# Tokyo Neighborhood Guide
    
## Overview
Details about different Tokyo neighborhoods and their unique characteristics.

## Observations
- [area] Shibuya is a busy shopping district #shopping
- [transportation] Yamanote Line connects major neighborhoods #transit
- [recommendation] Visit Shimokitazawa for vintage shopping #unique
- [tip] Get a Suica card for easy train travel #convenience

{relations_section}
    """
    
    result = await write_note(
        title="Tokyo Neighborhood Guide",
        content=content,
        verbose=True
    )
    
    # You can check which relations were resolved and which are forward references
    if result and 'relations' in result:
        resolved = [r['to_name'] for r in result['relations'] if r.get('target_id')]
        forward_refs = [r['to_name'] for r in result['relations'] if not r.get('target_id')]
        
        print(f"Resolved relations: {resolved}")
        print(f"Forward references that will be resolved later: {forward_refs}")
```

## Error Handling

Common issues to watch for:

1. **Missing Content**

   ```python
   try:
       content = await read_note("Document")
   except:
       # Try search instead
       results = await search_notes("Document")
       if results and results.primary_results:
           # Found something similar
           content = await read_note(results.primary_results[0].permalink)
   ```

2. **Forward References (Unresolved Relations)**

   ```python
   response = await write_note(..., verbose=True)
   # Check for forward references (unresolved relations)
   forward_refs = []
   for relation in response.get('relations', []):
       if not relation.get('target_id'):
           forward_refs.append(relation.get('to_name'))
   
   if forward_refs:
       # This is a feature, not an error! Inform the user about forward references
       print(f"Note created with forward references to: {forward_refs}")
       print("These will be automatically linked when those notes are created.")
       
       # Optionally suggest creating those entities now
       print("Would you like me to create any of these notes now to complete the connections?")
   ```

3. **Sync Issues**

   ```python
   # If information seems outdated
   activity = await recent_activity(timeframe="1 hour")
   if not activity or not activity.primary_results:
       print("It seems there haven't been recent updates. You might need to run 'skogcli memory sync'.")
   ```

## Best Practices

1. **Proactively Record Context**
   - Offer to capture important discussions
   - Record decisions, rationales, and conclusions
   - Link to related topics
   - Ask for permission first: "Would you like me to save our discussion about [topic]?"
   - Confirm when complete: "I've saved our discussion to SkogAI-Memory"

2. **Create a Rich Semantic Graph**
   - **Add meaningful observations**: Include at least 3-5 categorized observations in each note
   - **Create deliberate relations**: Connect each note to at least 2-3 related entities
   - **Use existing entities**: Before creating a new relation, search for existing entities
   - **Verify wikilinks**: When referencing `[[Entity]]`, use exact titles of existing notes
   - **Check accuracy**: Use `search_notes()` or `recent_activity()` to confirm entity titles
   - **Use precise relation types**: Choose specific relation types that convey meaning (e.g., "implements" instead of "relates_to")
   - **Consider bidirectional relations**: When appropriate, create inverse relations in both entities

3. **Structure Content Thoughtfully**
   - Use clear, descriptive titles
   - Organize with logical sections (Context, Decision, Implementation, etc.)
   - Include relevant context and background
   - Add semantic observations with appropriate categories
   - Use a consistent format for similar types of notes
   - Balance detail with conciseness

4. **Navigate Knowledge Effectively**
   - Start with specific searches
   - Follow relation paths
   - Combine information from multiple sources
   - Verify information is current
   - Build a complete picture before responding

5. **Help Users Maintain Their Knowledge**
   - Suggest organizing related topics
   - Identify potential duplicates
   - Recommend adding relations between topics
   - Offer to create summaries of scattered information
   - Suggest potential missing relations: "I notice this might relate to [topic], would you like me to add that connection?"

---
title: Basic Memory Project Management
type: note
permalink: system-architecture/basic-memory-project-management
tags:
- '#basic-memory'
- '#projects'
- '#mcp'
- '#architecture'
- '#lessons-learned'
---

# Basic Memory Project Management

## Project Connection Architecture
- When an MCP (Multi-Context Protocol) server is started, it establishes a connection to a specific Basic Memory project
- This connection persists throughout the session and doesn't automatically detect changes made via command line tools
- The `skogai-memory` extension operates through this established MCP connection
- The CLI tool (`uvx basic-memory`) and the extension API don't share the same active project state

## Key Observations
- Command line project changes (`uvx basic-memory project set-active`) are not reflected in the extension API
- The API's `project_info` function shows different information than the command line's `project info`
- Notes created through the API go to the project that was active when the MCP was started
- The SkogCLI project was visible in command line (`uvx basic-memory project list`) but not in the API's project list

## Practical Implications
- To work with a specific project via the API, the MCP must be started/restarted with that project active
- Changes to the active project require restarting the MCP server to take effect
- Multiple MCPs could potentially be running with different active projects

## Best Practices
- Set the desired active project before starting the MCP server
- Restart the MCP server when switching between projects
- Use the command line to verify which project is active before performing API operations
- Be aware that the API's project_info may not reflect recent command line changes

Last tested: 2025-04-12

---
title: SkogAI Memory Tool
type: note
permalink: tools/skog-ai-memory-tool
---

# SkogAI Memory Tool

The skogai-memory tool is a knowledge management system that allows for storing, retrieving, and organizing information. 

## Core Functions:
- Creating and updating notes with `write_note`
- Reading notes with `read_note` 
- Searching across content with `search_notes`
- Building context from previous conversations with `build_context`
- Viewing recent activity with `recent_activity`
- Creating visual canvases to map concepts with `canvas`
- Getting project statistics with `project_info`
- Reading raw content with `read_content`
- Deleting notes with `delete_note`

## Use Cases:
- Maintaining persistent knowledge across sessions
- Creating structured documentation
- Building knowledge graphs and concept maps
- Tracking conversations and discussions
- Organizing information into folders and with tags

This tool serves as the memory system within the broader SkogAI ecosystem, allowing for cross-session and cross-agent knowledge preservation.


---
title: SkogAI Memory System Overview
type: note
permalink: system/skog-ai-memory-system-overview
---

# SkogAI Memory System

## System Information
- **Project Name**: SkogAI
- **Project Path**: /home/skogix/skogdata/memories
- **Available Projects**: 
  - main (/home/skogix/basic-memory)
  - SkogAI (/home/skogix/skogdata/memories)
- **Default Project**: SkogAI
- **Version**: 0.12.2
- **Database Path**: /home/skogix/skogdata/memories/.basic-memory/memory.db
- **Database Size**: 0.11 MB (as of system check)

## Core Components
The system appears to track:
- Entities
- Observations
- Relations
- Entity types
- Observation categories
- Relation types

## Available Functions
- `read_note`: Read markdown notes by title or permalink
- `write_note`: Create or update markdown notes
- `delete_note`: Delete notes by title or permalink
- `read_content`: Read raw content from files
- `search_notes`: Search across content in the knowledge base
- `build_context`: Build context from memory URIs
- `recent_activity`: Get recent activity from the knowledge base
- `canvas`: Create Obsidian canvas files for visualization

## Current Status
As of initial checks, the system appears to be newly initialized with:
- 0 entities
- 0 observations
- 0 relations
- No monthly growth data
- File watcher process running (PID: 833592)

This note represents our initial documentation about the SkogAI Memory system based on direct system information. Further exploration and usage will help expand our understanding of its capabilities.
