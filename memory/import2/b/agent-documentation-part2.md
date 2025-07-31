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
- relation_type [[Target Entity]] (optional context)
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