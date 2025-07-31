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