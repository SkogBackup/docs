#!/usr/bin/env python3
"""
Add or update YAML frontmatter for markdown files in tools/ directory.
Follows the template in .docgen/templates/frontmatter.yaml
"""

import os
import re
from datetime import datetime
from pathlib import Path

def has_frontmatter(content):
    """Check if content starts with YAML frontmatter"""
    return content.strip().startswith('---')

def extract_existing_frontmatter(content):
    """Extract existing frontmatter if present"""
    if not has_frontmatter(content):
        return None, content

    parts = content.split('---', 2)
    if len(parts) >= 3:
        return parts[1].strip(), '---'.join(parts[2:]).lstrip()
    return None, content

def parse_frontmatter_field(fm_text, field):
    """Extract a field from frontmatter text"""
    # Handle list fields (tags, categories)
    list_match = re.search(rf'^{field}:\s*\n((?:^\s*-\s+.+$\n?)*)', fm_text, re.MULTILINE)
    if list_match:
        items = re.findall(r'^\s*-\s+(.+)$', list_match.group(1), re.MULTILINE)
        return items

    # Handle single-line fields
    single_match = re.search(rf'^{field}:\s*(.+)$', fm_text, re.MULTILINE)
    if single_match:
        value = single_match.group(1).strip()
        # Handle list on single line: [item1, item2]
        if value.startswith('[') and value.endswith(']'):
            items = [item.strip().strip('"\'') for item in value[1:-1].split(',')]
            return [item for item in items if item]
        return value

    return None

def generate_frontmatter(file_path, existing_fm=None):
    """Generate standardized frontmatter for a file"""
    path = Path(file_path)
    rel_path = path.relative_to(Path.cwd())

    # Extract categories from path (e.g., tools/argc/index.md → ["tools", "argc"])
    categories = list(rel_path.parent.parts) if rel_path.parent.parts else []

    # Determine title
    title = path.stem if path.stem.lower() not in ['index', 'readme'] else path.parent.name

    # Extract existing values if available
    tags = []
    permalink = str(rel_path)
    doc_type = "note"

    if existing_fm:
        # Try to preserve existing tags
        existing_tags = parse_frontmatter_field(existing_fm, 'tags')
        if existing_tags:
            tags = existing_tags

        # Try to preserve type
        existing_type = parse_frontmatter_field(existing_fm, 'type')
        if existing_type and isinstance(existing_type, str):
            doc_type = existing_type

        # Try to preserve title if it's meaningful
        existing_title = parse_frontmatter_field(existing_fm, 'title')
        if existing_title and isinstance(existing_title, str):
            title = existing_title

    # Generate timestamp
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Build frontmatter
    fm_lines = ['---']

    # Categories
    if categories:
        fm_lines.append('categories:')
        for cat in categories:
            fm_lines.append(f'  - {cat}')
    else:
        fm_lines.append('categories: []')

    # Tags
    if tags:
        fm_lines.append('tags:')
        for tag in tags:
            fm_lines.append(f'  - {tag}')
    else:
        fm_lines.append('tags: []')

    # Other fields
    fm_lines.append(f'permalink: {permalink}')
    fm_lines.append(f'title: {title}')
    fm_lines.append(f'type: {doc_type}')
    fm_lines.append(f'generated_at: {timestamp}')
    fm_lines.append('---')

    return '\n'.join(fm_lines)

def process_file(file_path):
    """Process a single markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    existing_fm, body = extract_existing_frontmatter(content)

    # Generate new frontmatter
    new_fm = generate_frontmatter(file_path, existing_fm)

    # Combine with body
    new_content = new_fm + '\n\n' + body.lstrip()

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    action = "Updated" if existing_fm else "Added"
    print(f"{action} frontmatter: {file_path}")

def main():
    """Process all markdown files in tools/ directory"""
    tools_dir = Path('tools')

    if not tools_dir.exists():
        print(f"Error: {tools_dir} directory not found")
        return

    md_files = list(tools_dir.glob('**/*.md'))

    print(f"Processing {len(md_files)} markdown files...\n")

    for md_file in sorted(md_files):
        process_file(md_file)

    print(f"\nDone! Processed {len(md_files)} files.")

if __name__ == '__main__':
    main()
