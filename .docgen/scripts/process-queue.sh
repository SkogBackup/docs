#!/usr/bin/env bash

# Process all markdown files in .docgen/input/
while IFS= read -r -d '' inputfile; do
    # Get target file path (strip .docgen/input/ prefix)
    targetfile="${inputfile#.docgen/input/}"

    echo "Processing: $targetfile"

    # Generate prompt and call LLM
    .docgen/scripts/make-prompt.sh "$targetfile" > /tmp/prompt.txt
    aichat --model openrouter:qwen/qwen-2.5-coder-32b-instruct --code --file /tmp/prompt.txt > /tmp/llm-output.txt

    # Extract LLM generated fields (between <output> tags)
    llm_fields=$(sed -n '/<output>/,/<\/output>/p' /tmp/llm-output.txt | grep -v '<output>' | grep -v '</output>')

    # Generate auto fields
    categories="[$(dirname "$targetfile" | sed 's|/|, |g')]"
    permalink="${targetfile%.md}"
    timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)

    # Build complete frontmatter
    frontmatter="---
categories: $categories
permalink: $permalink
generated_at: $timestamp
$llm_fields
---"

    # Get body (strip old frontmatter if exists)
    if head -1 "$targetfile" | grep -q "^---$"; then
        body=$(sed '1,/^---$/d; 1,/^---$/d' "$targetfile")
    else
        body=$(cat "$targetfile")
    fi

    # Write new file
    echo "$frontmatter" > "$targetfile"
    echo "" >> "$targetfile"
    echo "$body" >> "$targetfile"

    # Remove from queue
    rm "$inputfile"

    echo "✓ Done: $targetfile"
    echo ""
done < <(find .docgen/input -name "*.md" -type f -print0)

echo "Queue empty!"
