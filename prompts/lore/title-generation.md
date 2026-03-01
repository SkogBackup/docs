---
title: title-generation
type: prompt
category: lore
tags: [generation, lorebook, titles]
---

# Objective

Generate a numbered list of lore entry titles with categories for populating a new lorebook.

# Inputs

- `$entry_count` - Number of entries to generate (e.g., 5)
- `$title` - The lorebook title/world name
- `$description` - Brief lorebook description

# Expected Output

Numbered list in exact format:
```
1. [Category: place] Entry Title
2. [Category: character] Entry Title
3. [Category: object] Entry Title
```

# Prompt

Generate $entry_count unique lore entry titles for a fantasy/sci-fi world called '$title'. $description

CRITICAL RULES:
1. Output ONLY the numbered list below
2. NO meta-commentary, explanations, or preamble
3. START IMMEDIATELY with "1."

REQUIRED FORMAT:
1. [Category: place] Entry Title
2. [Category: character] Entry Title
3. [Category: object] Entry Title

FORMATTING RULES:
- Categories MUST be: place, character, object, event, or concept
- Each line: number, category in brackets, title
- No blank lines or extra text

BEGIN LIST NOW:
