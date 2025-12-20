#!/usr/bin/env python3
"""
Enqueue markdown files for frontmatter generation using external queue system.

This version outputs `queue add <command>` calls instead of using internal SQLite queue.
Unifies with the bash approach for consistent queue management.
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List

def has_frontmatter(file_path: Path) -> bool:
    """Check if file already has YAML frontmatter."""
    try:
        with file_path.open('r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            return first_line == '---'
    except (IOError, UnicodeDecodeError):
        return False

def find_markdown_files(directory: Path, excludes: List[str] = None) -> List[Path]:
    """Find all markdown files in directory, excluding specified patterns."""
    if excludes is None:
        excludes = ['.git', 'node_modules', '.docgen', 'generated', '.worktrees']
    
    markdown_files = []
    
    for md_file in directory.rglob('*.md'):
        # Check if file should be excluded
        if any(exclude in str(md_file) for exclude in excludes):
            continue
        markdown_files.append(md_file)
    
    return sorted(markdown_files)

def enqueue_file(file_path: Path, force: bool = False, dry_run: bool = False) -> bool:
    """Enqueue a single file using external queue system.
    
    Args:
        file_path: Path to markdown file
        force: Re-process files with existing frontmatter
        dry_run: Print commands without executing
        
    Returns:
        True if enqueued/would be enqueued, False if skipped
    """
    # Skip non-markdown files
    if file_path.suffix != '.md':
        return False
    
    # Check for existing frontmatter
    if not force and has_frontmatter(file_path):
        print(f"SKIP: Has frontmatter: {file_path}")
        return False
    
    # Build command
    cmd = f"docgen-process"
    if force:
        cmd += " --force"
    cmd += f" {file_path}"
    
    if dry_run:
        print(f"[DRY RUN] queue add \"{cmd}\"")
        return True
    else:
        try:
            # Execute queue add command
            result = subprocess.run(
                ["queue", "add", cmd],
                capture_output=True,
                text=True,
                check=True
            )
            print(f"ENQUEUED: {file_path}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"ERROR: Failed to enqueue {file_path}: {e}")
            return False
        except FileNotFoundError:
            print("ERROR: 'queue' command not found. Ensure SkogAI queue system is installed.")
            return False

def main():
    parser = argparse.ArgumentParser(
        description="Enqueue markdown files for frontmatter generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Enqueue all files in directory
  python enqueue_files_v2.py --dir agents/
  
  # Enqueue single file
  python enqueue_files_v2.py --file agents/claude/profile.md
  
  # Force re-process files with frontmatter
  python enqueue_files_v2.py --dir agents/ --force
  
  # Dry run to see what would be enqueued
  python enqueue_files_v2.py --dir . --dry-run
  
After enqueueing:
  queue status                     # Check queue
  QUEUE_PARALLEL_JOBS=2 queue run  # Process with parallelism
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", "-f", type=Path, help="Single file to enqueue")
    group.add_argument("--dir", "-d", type=Path, help="Directory to scan for markdown files")
    
    parser.add_argument("--force", action="store_true", 
                       help="Re-process files that already have frontmatter")
    parser.add_argument("--dry-run", action="store_true",
                       help="Show what would be enqueued without adding to queue")
    parser.add_argument("--exclude", action="append", default=[],
                       help="Exclude directory pattern (can be used multiple times)")
    
    args = parser.parse_args()
    
    # Default excludes
    excludes = ['.git', 'node_modules', '.docgen', 'generated', '.worktrees'] + args.exclude
    
    enqueued = 0
    skipped = 0
    errors = 0
    
    if args.file:
        # Single file
        if args.file.exists():
            if enqueue_file(args.file, args.force, args.dry_run):
                enqueued += 1
            else:
                skipped += 1
        else:
            print(f"ERROR: File not found: {args.file}")
            errors += 1
            
    elif args.dir:
        # Directory scan
        if not args.dir.exists():
            print(f"ERROR: Directory not found: {args.dir}")
            return 1
            
        print(f"Scanning: {args.dir}")
        markdown_files = find_markdown_files(args.dir, excludes)
        
        for file_path in markdown_files:
            if enqueue_file(file_path, args.force, args.dry_run):
                enqueued += 1
            else:
                skipped += 1
    
    # Summary
    print(f"\n=== Summary ===")
    print(f"Enqueued: {enqueued}")
    print(f"Skipped:  {skipped}")
    print(f"Errors:   {errors}")
    
    if enqueued > 0 and not args.dry_run:
        print(f"\nNext steps:")
        print(f"  queue status                     # Check queue")
        print(f"  QUEUE_PARALLEL_JOBS=2 queue run  # Process with parallelism")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
