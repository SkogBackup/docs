# SkogAI Memory System

## Summary
SkogAI Memory is a semantic knowledge management system that transforms information into an interconnected knowledge graph using simple markdown files. It enables both humans and AI assistants to efficiently store, retrieve, and navigate knowledge through structured patterns and explicit connections, creating a network of information that grows in value over time.

## Details

### Core Concepts

#### Knowledge as a Connected Graph

The system is designed around the principle that *connected knowledge provides more value than isolated information*. By explicitly linking related concepts through structured patterns, SkogAI Memory creates a navigable knowledge graph where:

- Information can be discovered through multiple pathways
- Relationships between concepts are explicit and meaningful
- The overall value of the knowledge base increases as connections grow

#### Markdown Files as Storage

All knowledge in the system is stored in simple markdown (.md) files, which are:
- Human-readable and easily edited
- Version control friendly
- Structured enough for machine processing
- Flexible enough for various content types

#### Observations as Atomic Units

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

#### Relations as Explicit Connections

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

#### Memory URIs for Addressing

Memory URIs provide a standardized way to reference knowledge within the system:

```
memory://[resource-type]/[identifier]
```

This addressing system enables precise linking and retrieval of information across the knowledge base.

##### URI Structure

- `memory://` - protocol identifier for memory system
- `[resource-type]` - content type (entity, note, conversation)
- `[identifier]` - specific item's unique identifier or permalink

##### Common Resource Types

- `note`: Direct reference to a specific note by title
- `entity`: Reference to content by path or folder structure
- `conversation`: Reference to chat or discussion history
- `content`: Reference to raw file content

##### Usage Examples

Accessing Notes:
```
memory://note/my-note-title
memory://entity/folder-path/note-title
```

Referencing Conversations:
```
memory://entity/conversation/recent
memory://entity/conversation/[conversation-id]
```

Accessing Raw Content:
```
memory://content/[file-path]
```

### File Structure and Organization

#### Standard File Format

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

#### Naming Conventions

- Use kebab-case for filenames (lowercase with hyphens between words)
- Choose descriptive names that reflect the content
- Avoid special characters and spaces
- Example: `knowledge-management-principles.md`

#### Folder Organization

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

### Creating Effective Knowledge

#### Memory Creation Workflow

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

#### Creating Effective Observations

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

#### Creating Meaningful Relations

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

#### Building Context from URIs

To retrieve information and build context from memory URIs:

```markdown
skogai-memory__build_context
  url: memory://entity/projects/my-project
  depth: 2  # Include related content
  timeframe: 7d  # Limit to recent content
```

### Best Practices

#### Creating Valuable Content

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

#### Maintaining the Knowledge Graph

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

#### URI Best Practices

- Use consistent naming patterns for files and folders
- Understand that permalinks are derived from folder paths and titles
- Create explicit links between related notes using URIs
- When continuing work on a topic, use `build_context` with relevant URI

### Troubleshooting

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

#### Knowledge Network Growth

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

## Related
- [[memory-uri-reference]] (detailed specifications for memory addressing)
- [[knowledge-management]] (theoretical foundation)
- [[documentation-systems]] (similar knowledge preservation approaches)
- [[markdown-systems]] (underlying format used for content)
- [[skogai-ecosystem]] (the broader system this is part of)

## observations
- [fact] SkogAI Memory uses markdown files for portable knowledge storage #accessibility #portability
- [principle] Connections between notes provide more value than isolated content #network #knowledge-graph
- [decision] Automated enforcement maintains consistency with minimal effort #automation #quality
- [technique] Categorized observations enable semantic filtering and discovery #organization #findability
- [requirement] All content must follow established standards for system interoperability #standards #compatibility
- [principle] Knowledge systems should balance structure and flexibility #adaptability #usability
- [fact] The memory URI system provides standardized addressing for knowledge #reference #navigation
- [technique] Explicit relations create traversable paths through the knowledge base #connections #exploration
- [fact] Memory URIs create a standardized pattern for referencing knowledge #standards #consistency
- [technique] Using depth parameters allows following semantic connections across notes #exploration #context

## relations
- implements [[knowledge-management]] (provides structured approach to information)
- relates_to [[markdown-systems]] (uses markdown for content storage)
- part_of [[skogai-ecosystem]] (integrates with broader SkogAI tools)
- foundation_for [[knowledge-graph]] (creates basis for connected information)
- relates_to [[documentation-systems]] (serves similar purposes for knowledge preservation)
- implements [[knowledge-graph-navigation]] (provides mechanism for traversing knowledge connections)