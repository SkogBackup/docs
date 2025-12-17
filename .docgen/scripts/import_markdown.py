#!/usr/bin/env python3
"""
Import existing markdown files to use as input context for doc generation
"""

import sqlite3
import argparse
from pathlib import Path
import re

def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown"""
    if not content.startswith('---'):
        return None, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content

    frontmatter = parts[1].strip()
    body = parts[2].strip()

    # Parse frontmatter into dict
    fm_dict = {}
    for line in frontmatter.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            fm_dict[key.strip()] = value.strip()

    return fm_dict, body

def import_markdown_file(conn, md_path, output_path, prompt_template, categories=None, tags=None):
    """Import a markdown file into the database"""

    # Read the file
    with open(md_path, 'r') as f:
        content = f.read()

    # Parse frontmatter if exists
    frontmatter, body = parse_frontmatter(content)

    # Use frontmatter title if available, otherwise filename
    if frontmatter and 'title' in frontmatter:
        title = frontmatter['title']
    else:
        title = Path(md_path).stem.replace('-', ' ').title()

    # Extract categories/tags from frontmatter if not provided
    if not categories and frontmatter:
        if 'categories' in frontmatter:
            categories = [c.strip() for c in frontmatter['categories'].split(',')]

    if not tags and frontmatter:
        if 'tags' in frontmatter:
            tags = [t.strip() for t in frontmatter['tags'].split(',')]

    # Use the markdown body as input context
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO documents (path, title, type, content, prompt_template)
        VALUES (?, ?, ?, ?, ?)
    """, (output_path, title, 'note', body, prompt_template))

    doc_id = cursor.lastrowid

    # Add categories
    if categories:
        for cat_name in categories:
            cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (cat_name,))
            cursor.execute("SELECT id FROM categories WHERE name = ?", (cat_name,))
            cat_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO document_categories (document_id, category_id) VALUES (?, ?)",
                         (doc_id, cat_id))

    # Add tags
    if tags:
        for tag_name in tags:
            cursor.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (tag_name,))
            cursor.execute("SELECT id FROM tags WHERE name = ?", (tag_name,))
            tag_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO document_tags (document_id, tag_id) VALUES (?, ?)",
                         (doc_id, tag_id))

    conn.commit()
    print(f"  ✓ Imported: {md_path} → {output_path}")
    return doc_id

def import_directory(conn, input_dir, prompt_template, categories=None, tags=None):
    """Import all markdown files from a directory"""
    input_path = Path(input_dir)

    md_files = list(input_path.rglob('*.md'))

    print(f"\nImporting {len(md_files)} markdown files from {input_dir}...")

    for md_file in md_files:
        # Calculate relative output path
        rel_path = md_file.relative_to(input_path)
        output_path = str(rel_path)

        try:
            import_markdown_file(conn, md_file, output_path, prompt_template, categories, tags)
        except Exception as e:
            print(f"  ✗ Failed to import {md_file}: {e}")

    print(f"✓ Import complete\n")

def main():
    parser = argparse.ArgumentParser(description='Import markdown files as input context')
    parser.add_argument('--db', default='.docgen/docs.db', help='Path to database')
    parser.add_argument('--file', help='Import single markdown file')
    parser.add_argument('--dir', help='Import directory of markdown files')
    parser.add_argument('--output', help='Output path for single file')
    parser.add_argument('--template', required=True, help='Prompt template to use')
    parser.add_argument('--categories', help='Comma-separated categories')
    parser.add_argument('--tags', help='Comma-separated tags')

    args = parser.parse_args()

    # Parse categories and tags
    categories = [c.strip() for c in args.categories.split(',')] if args.categories else None
    tags = [t.strip() for t in args.tags.split(',')] if args.tags else None

    conn = sqlite3.connect(args.db)

    if args.file:
        if not args.output:
            print("Error: --output required when using --file")
            return
        import_markdown_file(conn, args.file, args.output, args.template, categories, tags)
    elif args.dir:
        import_directory(conn, args.dir, args.template, categories, tags)
    else:
        print("Error: Must specify either --file or --dir")

    conn.close()

if __name__ == "__main__":
    main()
