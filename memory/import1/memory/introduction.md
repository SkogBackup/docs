---
title: SkogAI-Memory: Intro Guide
type: note
permalink: memory://resource-type/identifier
skogai-notation: [$memory.resource.type]
---

# SkogAI-Memory: Intro Guide

## Summary

This guide helps AI assistants effectively use the SkogAI-Memory system to build and navigate a semantic knowledge graph through natural conversations with users. It outlines core functionality, best practices, and integration patterns that maximize the knowledge graph's value through consistent formats and rich interconnections.

## Details

### Core Concepts

#### Purpose of This Guide

This document provides AI assistants with comprehensive guidance on using SkogAI-Memory effectively when working with users. It covers reading, writing, and navigating knowledge through the Model Context Protocol (MCP), focusing on building a valuable interconnected knowledge graph that persists across conversations.

#### SkogAI-Memory Overview

SkogAI-Memory allows both AI assistants and users to record context in local Markdown files, building a knowledge base through natural conversations. The system's core attributes are:

- **Local-First**: All data stored in plain text files on the user's computer
- **Real-Time**: Content updates visible immediately to users
- **Bi-Directional**: Both AI assistants and users can read and edit notes
- **Semantic**: Simple patterns create a structured knowledge graph
- **Persistent**: Knowledge persists across sessions and conversations

#### The Knowledge Graph Paradigm

The system's value comes primarily from connections between notes, not just the notes themselves. When writing notes, the assistant's primary goal should be creating a rich, interconnected knowledge graph by:

1. **Increasing Semantic Density**: Adding multiple observations and relations to each note
2. **Using Accurate References**: Referencing existing entities by their exact titles
3. **Creating Forward References**: Creating links to entities that don't exist yet
4. **Building Bidirectional Links**: Connecting entities from both directions
5. **Using Meaningful Categories**: Adding semantic context with appropriate observation categories
6. **Choosing Precise Relations**: Using specific relation types that convey meaning

A knowledge graph with 10 heavily connected notes provides more value than 20 isolated notes.

### Core Tools and Functions

#### Writing Knowledge

```python
response = await write_note(
    title="Search Design",              # Required: Note title
    content="# Search Design\n...",     # Required: Note content
    folder="specs",                     # Optional: Folder to save in
    tags=["search", "design"],          # Optional: Tags for categorization
    verbose=True                        # Optional: Get parsing details
)
```

#### Reading Knowledge

```python
# Multiple ways to access the same content
content = await read_note("Search Design")             # By title
content = await read_note("specs/search-design")       # By path 
content = await read_note("memory://specs/search")     # By memory URL
```

#### Searching for Knowledge

```python
results = await search_notes(
    query="authentication system",      # Text to search for
    page=1,                             # Optional: Pagination
    page_size=10                        # Optional: Results per page
)
```

#### Building Context from the Knowledge Graph

```python
context = await build_context(
    url="memory://specs/search",        # Starting point
    depth=2,                            # Optional: How many hops to follow
    timeframe="1 month"                 # Optional: Recent timeframe
)
```

#### Checking Recent Changes

```python
activity = await recent_activity(
    type="all",                         # Optional: Entity types to include
    depth=1,                            # Optional: Related items to include
    timeframe="1 week"                  # Optional: Time window
)
```

#### Creating Knowledge Visualizations

```python
canvas_result = await canvas(
    nodes=[{"id": "note1", "label": "Search Design"}],  # Nodes to display
    edges=[{"from": "note1", "to": "note2"}],           # Connections
    title="Project Overview",                           # Canvas title
    folder="diagrams"                                   # Storage location
)
```

### Memory URI System

SkogAI-Memory uses a special URL format to reference entities in the knowledge graph:

#### URI Structure

```
memory://[resource-type]/[identifier]
```

#### Common URI Patterns

- `memory://title` - Reference by title
- `memory://folder/title` - Reference by folder and title
- `memory://permalink` - Reference by permalink
- `memory://path/relation_type/*` - Follow all relations of a specific type
- `memory://path/*/target` - Find all entities with relations to target

### Semantic Markdown Format

Knowledge is encoded in standard markdown using simple patterns:

#### Observations

Facts about an entity:

```markdown
- [category] This is an observation #tag1 #tag2 (optional context)
```

Common categories include:

- `[idea]` - Concepts or thoughts
- `[decision]` - Choices made and rationales
- `[question]` - Open inquiries or uncertainties
- `[fact]` - Objective, verifiable information
- `[requirement]` - Necessary conditions or features
- `[technique]` - Methods or approaches
- `[recipe]` - Step-by-step processes
- `[preference]` - Subjective choices or likes

#### Relations

Links between entities:

```markdown
- relation_type [[example/type/entity]] (optional context)
```

Common relation types include:

- `relates_to` - General connection between topics
- `implements` - Shows how concepts are put into practice
- `requires` - Dependency relationships
- `extends` - Builds upon or enhances
- `part_of` - Hierarchical membership
- `pairs_with` - Complementary connections
- `inspired_by` - Influence relationships
- `originated_from` - Source connections

### When to Record Context

AI assistants should proactively identify opportunities to capture knowledge by recognizing when:

1. Users make decisions or reach conclusions
2. Important information emerges during conversation
3. Multiple related topics are discussed
4. The conversation contains information that might be useful later
5. Plans, tasks, or action items are mentioned

#### Protocol for Recording Context

1. Identify valuable information in the conversation
2. Ask the user: "Would you like me to record our discussion about [topic] in SkogAI-Memory?"
3. If they agree, use `write_note` to capture the information
4. If they decline, continue without recording
5. Let the user know when information has been recorded: "I've saved our discussion about [topic] to SkogAI-Memory."

### Understanding User Interaction Patterns

Users will interact with SkogAI-Memory in predictable patterns:

#### Creating Knowledge

```
Human: "Let's write up what we discussed about search."

You: I'll create a note capturing our discussion about the search functionality.
[Use write_note() to record the conversation details]
```

#### Referencing Existing Knowledge

```
Human: "Take a look at memory://specs/search"

You: I'll examine that information.
[Use build_context() to gather related information]
[Then read_note() to access specific content]
```

#### Finding Information

```
Human: "What were our decisions about auth?"

You: Let me find that information for you.
[Use search_notes() to find relevant notes]
[Then build_context() to understand connections]
```

### Key Things to Remember

#### Files are Truth

- All knowledge lives in local files on the user's computer
- Users can edit files outside your interaction
- Changes need to be synced by the user (usually automatic)
- Always verify information is current with `recent_activity()`

#### Building Context Effectively

- Start with specific entities
- Follow meaningful relations
- Check recent changes
- Build context incrementally
- Combine related information

#### Writing Knowledge Wisely

- Using the same title+folder will overwrite existing notes
- Structure content with clear headings and sections
- Use semantic markup for observations and relations
- Keep files organized in logical folders

### Common Knowledge Patterns

#### Capturing Decisions

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

#### Recording Project Structure

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

#### Technical Discussions

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

### Error Handling

AI assistants should be prepared to gracefully handle common issues:

#### Missing Content

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

#### Forward References (Unresolved Relations)

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
```

#### Sync Issues

```python
# If information seems outdated
activity = await recent_activity(timeframe="1 hour")
if not activity or not activity.primary_results:
    print("It seems there haven't been recent updates. You might need to run 'skogcli memory sync'.")
```

### Best Practices

#### Proactively Record Context

- Offer to capture important discussions
- Record decisions, rationales, and conclusions
- Link to related topics
- Ask for permission first: "Would you like me to save our discussion about [topic]?"
- Confirm when complete: "I've saved our discussion to SkogAI-Memory"

#### Create a Rich Semantic Graph

- Add meaningful observations: Include at least 3-5 categorized observations in each note
- Create deliberate relations: Connect each note to at least 2-3 related entities
- Use existing entities: Before creating a new relation, search for existing entities
- Verify wikilinks: When referencing `[[Entity]]`, use exact titles of existing notes
- Use precise relation types: Choose specific relation types that convey meaning
- Consider bidirectional relations: Create inverse relations in both entities when appropriate

#### Structure Content Thoughtfully

- Use clear, descriptive titles
- Organize with logical sections (Context, Decision, Implementation, etc.)
- Include relevant context and background
- Add semantic observations with appropriate categories
- Use a consistent format for similar types of notes
- Balance detail with conciseness

#### Navigate Knowledge Effectively

- Start with specific searches
- Follow relation paths
- Combine information from multiple sources
- Verify information is current
- Build a complete picture before responding

#### Help Users Maintain Their Knowledge

- Suggest organizing related topics
- Identify potential duplicates
- Recommend adding relations between topics
- Offer to create summaries of scattered information
- Suggest potential missing relations: "I notice this might relate to [topic], would you like me to add that connection?"

## Related

- [[skogai-memory-system]] (the underlying knowledge management system)
- [[agent-interaction-patterns]] (common user and assistant communication flows)
- [[knowledge-graph]] (semantic network architecture)
- [[conversation-context]] (techniques for recording conversation information)

## observations

- [fact] SkogAI Memory's value comes primarily from connections between notes #knowledge-graph #connections
- [principle] A knowledge graph with 10 heavily connected notes provides more value than 20 isolated notes #density #value
- [technique] When writing notes, include at least 3-5 categorized observations in each #best-practices
- [technique] Ask users for permission before recording conversation details #etiquette #user-experience
- [requirement] All knowledge is stored in local files on the user's computer #local-first #privacy
- [fact] Forward references will be automatically resolved when referenced entities are created #flexibility #forward-compatibility
- [decision] We use this agent guide to maintain consistency in knowledge building across assistants #standardization #quality

## relations

- implements [[skogai-memory-system]] (provides practical guidance for system usage)
- relates_to [[agent-interaction-patterns]] (guides effective user-agent communication)
- part_of [[agent-documentation]] (serves as essential guidance for AI assistants)
- foundation_for [[knowledge-building-workflow]] (establishes standard procedures)
- extends [[memory-uri-guide]] (builds upon URI reference mechanisms)
