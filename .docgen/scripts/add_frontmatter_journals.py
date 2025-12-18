#!/usr/bin/env python3
"""Add frontmatter to journal entries that are missing it"""

import os
import re
from pathlib import Path
from datetime import datetime

journal_dir = Path("agents/claude/journal")

for journal_file in sorted(journal_dir.glob("*.md")):
    # Read existing content
    content = journal_file.read_text()

    # Skip if already has frontmatter
    if content.startswith("---"):
        print(f"Skipping {journal_file.name} (already has frontmatter)")
        continue

    # Extract date and title from filename
    filename = journal_file.stem  # filename without extension

    # Extract date if present (YYYY-MM-DD format)
    date_match = re.match(r'(\d{4}-\d{2}-\d{2})', filename)
    date_str = date_match.group(1) if date_match else None

    # Create permalink from filename
    permalink = f"agents/claude/journal/{filename}"

    # Create frontmatter
    frontmatter = f"""---
categories:
- agents
- claude
- journal
tags:
- claude
- journal"""

    if date_str:
        frontmatter += f"\n- {date_str}"

    frontmatter += f"""
permalink: {permalink}
title: {filename}
type: note
generated_at: {datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}
---

"""

    # Prepend frontmatter to content
    new_content = frontmatter + content

    # Write back
    journal_file.write_text(new_content)
    print(f"Added frontmatter to {journal_file.name}")

print("\nDone!")
