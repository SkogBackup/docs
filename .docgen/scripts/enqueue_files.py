#!/usr/bin/env python3
"""
Enqueue markdown files for batch frontmatter generation.
Scans directories and adds files to processing queue.
"""

import os
import re
import sqlite3
import argparse
from pathlib import Path
from datetime import datetime


def init_queue_schema(db_path):
    """Ensure queue table exists"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS processing_queue (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT NOT NULL,
        prompt TEXT NOT NULL,
        status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'processing', 'completed', 'failed')),
        priority INTEGER DEFAULT 0,
        retries INTEGER DEFAULT 0,
        max_retries INTEGER DEFAULT 3,
        error_message TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        started_at TIMESTAMP,
        completed_at TIMESTAMP
    )
    """)

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_queue_status ON processing_queue(status)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_queue_priority ON processing_queue(priority DESC, created_at ASC)")

    conn.commit()
    conn.close()


def has_frontmatter(file_path):
    """Check if file already has YAML frontmatter"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content.strip().startswith('---')
    except Exception:
        return False


def load_prompt_template(template_name):
    """Load prompt template from .docgen/prompts/"""
    template_path = Path('.docgen/prompts') / f'{template_name}.txt'

    if not template_path.exists():
        # Use default frontmatter template
        template_path = Path('.docgen/prompts/create-frontmatter.txt')

    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def generate_prompt_for_file(file_path, template_name='create-frontmatter'):
    """Generate Ollama prompt for a specific file"""
    # Convert to absolute path
    abs_path = Path(file_path).resolve()

    # Read file content
    with open(abs_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract existing frontmatter if present
    if content.strip().startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            body = '---'.join(parts[2:]).strip()
        else:
            body = content
    else:
        body = content

    # Get path info for context (relative to cwd)
    try:
        rel_path = abs_path.relative_to(Path.cwd().resolve())
    except ValueError:
        # If not relative to cwd, just use the filename
        rel_path = abs_path
    categories = list(rel_path.parent.parts) if rel_path.parent.parts else []

    # Load template
    template = load_prompt_template(template_name)

    # Build full prompt
    prompt = f"""File path: {rel_path}
Suggested categories: {', '.join(categories) if categories else 'none'}

File content:
{body[:1000]}...

{template}

Return ONLY the YAML frontmatter block (starting and ending with ---), nothing else.
"""

    return prompt


def enqueue_file(db_path, file_path, template='create-frontmatter', priority=0, force=False):
    """Add a single file to the processing queue"""

    # Normalize path - convert to relative path from cwd
    abs_path = Path(file_path).resolve()
    try:
        normalized_path = str(abs_path.relative_to(Path.cwd().resolve()))
    except ValueError:
        normalized_path = str(abs_path)

    # Check if already has frontmatter (unless forced)
    if not force and has_frontmatter(normalized_path):
        return 'skipped', 'Already has frontmatter'

    # Check if already in queue
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, status FROM processing_queue
        WHERE file_path = ? AND status IN ('pending', 'processing')
    """, (normalized_path,))

    existing = cursor.fetchone()
    if existing and not force:
        conn.close()
        return 'skipped', f'Already in queue (ID: {existing[0]}, Status: {existing[1]})'

    # Generate prompt
    try:
        prompt = generate_prompt_for_file(file_path, template)
    except Exception as e:
        conn.close()
        return 'error', f'Failed to generate prompt: {e}'

    # Insert into queue
    cursor.execute("""
        INSERT INTO processing_queue (file_path, prompt, priority)
        VALUES (?, ?, ?)
    """, (normalized_path, prompt, priority))

    queue_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return 'enqueued', f'Queue ID: {queue_id}'


def enqueue_directory(db_path, directory, template='create-frontmatter', priority=0, force=False, exclude_patterns=None):
    """Recursively enqueue all markdown files in directory"""

    if exclude_patterns is None:
        exclude_patterns = ['.git', 'node_modules', '.docgen', 'generated']

    results = {
        'enqueued': [],
        'skipped': [],
        'error': []
    }

    for root, dirs, files in os.walk(directory):
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_patterns]

        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                status, message = enqueue_file(db_path, file_path, template, priority, force)
                results[status].append((str(file_path), message))

    return results


def main():
    parser = argparse.ArgumentParser(description='Enqueue markdown files for batch frontmatter generation')
    parser.add_argument('--file', help='Single file to enqueue')
    parser.add_argument('--dir', help='Directory to scan recursively')
    parser.add_argument('--db', default='.docgen/docs.db', help='Database path')
    parser.add_argument('--template', default='create-frontmatter', help='Prompt template name')
    parser.add_argument('--priority', type=int, default=0, help='Priority (higher = processed first)')
    parser.add_argument('--force', action='store_true', help='Enqueue even if file has frontmatter or already queued')
    parser.add_argument('--exclude', nargs='*', help='Directory patterns to exclude')

    args = parser.parse_args()

    # Initialize queue schema
    init_queue_schema(args.db)

    if args.file:
        # Enqueue single file
        status, message = enqueue_file(args.db, args.file, args.template, args.priority, args.force)
        print(f"{status.upper()}: {args.file}")
        print(f"  {message}")

    elif args.dir:
        # Enqueue directory
        print(f"Scanning {args.dir} for markdown files...\n")
        results = enqueue_directory(args.db, args.dir, args.template, args.priority, args.force, args.exclude)

        print(f"\n=== Results ===")
        print(f"Enqueued: {len(results['enqueued'])}")
        print(f"Skipped:  {len(results['skipped'])}")
        print(f"Errors:   {len(results['error'])}")

        if results['enqueued']:
            print(f"\nEnqueued files:")
            for file_path, message in results['enqueued'][:10]:
                print(f"  ✓ {file_path}")
            if len(results['enqueued']) > 10:
                print(f"  ... and {len(results['enqueued']) - 10} more")

        if results['error']:
            print(f"\nErrors:")
            for file_path, message in results['error']:
                print(f"  ✗ {file_path}: {message}")

    else:
        parser.print_help()
        print("\nExamples:")
        print("  # Enqueue single file")
        print("  python3 .docgen/scripts/enqueue_files.py --file agents/claude/profile.md")
        print()
        print("  # Enqueue entire directory")
        print("  python3 .docgen/scripts/enqueue_files.py --dir agents/")
        print()
        print("  # Enqueue with priority (process first)")
        print("  python3 .docgen/scripts/enqueue_files.py --dir skogix/ --priority 10")
        print()
        print("  # Force re-enqueue files that already have frontmatter")
        print("  python3 .docgen/scripts/enqueue_files.py --dir agents/ --force")


if __name__ == '__main__':
    main()
