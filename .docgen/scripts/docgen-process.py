#!/usr/bin/env python3
"""
Atomic frontmatter processor for a single file.

Designed to be called from the skogai queue system:
  queue add "docgen-process agents/claude/profile.md"

Uses structured output (Pydantic) for reliable parsing.
"""

import asyncio
import sys
from pathlib import Path

# Add scripts directory to path for local imports
sys.path.insert(0, str(Path(__file__).parent))

from llm import generate_frontmatter, check_ollama_health, LLMError
from models import DocumentMeta


def has_frontmatter(content: str) -> bool:
    """Check if content already has YAML frontmatter."""
    return content.strip().startswith("---")


def strip_existing_frontmatter(content: str) -> str:
    """Remove existing frontmatter from content."""
    if not has_frontmatter(content):
        return content.lstrip()

    parts = content.split("---", 2)
    if len(parts) >= 3:
        return parts[2].lstrip()
    return content.lstrip()


def write_frontmatter(file_path: Path, meta: DocumentMeta, body: str) -> None:
    """Write frontmatter + body back to file."""
    new_content = f"{meta.to_yaml()}\n\n{body}"
    file_path.write_text(new_content, encoding="utf-8")


async def process_file(file_path: str, force: bool = False) -> bool:
    """Process a single file: generate and inject frontmatter.

    Args:
        file_path: Path to markdown file
        force: Overwrite existing frontmatter if True

    Returns:
        True if successful, False otherwise
    """
    path = Path(file_path)

    # Validate file exists
    if not path.exists():
        print(f"ERROR: File not found: {file_path}", file=sys.stderr)
        return False

    if not path.suffix == ".md":
        print(f"ERROR: Not a markdown file: {file_path}", file=sys.stderr)
        return False

    # Read content
    content = path.read_text(encoding="utf-8")

    # Check existing frontmatter
    if has_frontmatter(content) and not force:
        print(f"SKIP: Already has frontmatter: {file_path}")
        return True  # Not an error, just skip

    # Extract body (without frontmatter)
    body = strip_existing_frontmatter(content)

    print(f"Processing: {file_path}")

    # Check Ollama health
    if not await check_ollama_health():
        print("ERROR: Ollama not available", file=sys.stderr)
        return False

    try:
        # Generate frontmatter via LLM
        frontmatter = await generate_frontmatter(content)

        # Create full document metadata (adds categories, permalink, timestamp)
        meta = DocumentMeta.from_file_path(path, frontmatter)

        # Write back to file
        write_frontmatter(path, meta, body)

        print(f"OK: {file_path}")
        print(f"    title: {meta.title}")
        print(f"    tags: {', '.join(meta.tags)}")
        print(f"    type: {meta.type}")
        return True

    except LLMError as e:
        print(f"ERROR: LLM failed: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: docgen-process <file.md> [--force]", file=sys.stderr)
        print()
        print("Process a single markdown file:")
        print("  - Generates frontmatter via Ollama")
        print("  - Injects YAML frontmatter into file")
        print()
        print("Options:")
        print("  --force    Overwrite existing frontmatter")
        print()
        print("Designed for use with skogai queue:")
        print("  queue add 'docgen-process agents/claude/profile.md'")
        sys.exit(1)

    file_path = sys.argv[1]
    force = "--force" in sys.argv

    success = asyncio.run(process_file(file_path, force))
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
