#!/bin/bash
find . -type f -name "*.md" | while read -r file; do
  echo "Processing: $file"
  summary=$(cat "$file" | ollama run llama3.2 "
    please summarize this file but also keep this in mind:     1. **Linking/Relations** (most important):
       - Create bidirectional connections between notes
       - Use specific relation types (not just generic links)
       - Include both existing references and forward references
       - Aim for 2-3 meaningful relations per note

    2. **Observations** (equally important):
       - Add categorized observations (3-5 per note)
       - Use proper observation syntax: $(
    - [category] description #tags
  )
       - Common categories: [idea], [decision], [fact], [technique]
       - Include relevant tags for organization

    3. **Content Structure**:
       - Use clear headings and sections
       - Maintain consistent formatting
       - Include context/background information
       - Balance detail with conciseness

    4. **Proactive Practices**:
       - Verify note titles before linking
       - Check for recent changes/updates
       - Suggest potential missing connections
       - Offer to organize scattered information

    The agent should prioritize creating a dense semantic network where notes are richly connected through both observations and relations, rather than just collecting isolated information.")
  echo "$summary" >>./summaries.md
  echo "---" >>./summaries.md
done
