"""
Frontmatter writer for markdown files.

Handles injecting generated frontmatter into files while
preserving the original content.
"""

import asyncio
import logging
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional, Union

import aiofiles

try:
    from .models import DocumentMeta
except ImportError:
    from models import DocumentMeta

logger = logging.getLogger(__name__)

# Regex to match existing YAML frontmatter
FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def has_frontmatter(content: str) -> bool:
    """Check if content already has YAML frontmatter.

    Args:
        content: File content to check

    Returns:
        True if content starts with YAML frontmatter
    """
    return content.strip().startswith("---")


def extract_body(content: str) -> str:
    """Extract body content, removing existing frontmatter if present.

    Args:
        content: Full file content

    Returns:
        Content without frontmatter
    """
    if not has_frontmatter(content):
        return content

    # Find the second --- delimiter
    match = FRONTMATTER_PATTERN.match(content)
    if match:
        return content[match.end() :].lstrip()

    # Fallback: split on ---
    parts = content.split("---", 2)
    if len(parts) >= 3:
        return parts[2].lstrip()

    return content


def extract_existing_frontmatter(content: str) -> Optional[str]:
    """Extract existing frontmatter YAML if present.

    Args:
        content: File content

    Returns:
        Frontmatter YAML string (without delimiters) or None
    """
    if not has_frontmatter(content):
        return None

    match = FRONTMATTER_PATTERN.match(content)
    if match:
        return match.group(1)

    return None


async def inject_frontmatter(
    file_path: Union[str, Path],
    doc_meta: DocumentMeta,
    backup: bool = True,
) -> bool:
    """Inject frontmatter into a markdown file.

    Preserves existing content while adding/replacing frontmatter.

    Args:
        file_path: Path to the markdown file
        doc_meta: Document metadata to inject as frontmatter
        backup: Create .bak backup before modifying (default: True)

    Returns:
        True if successful

    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If file can't be written
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Read current content
    async with aiofiles.open(path, "r", encoding="utf-8") as f:
        content = await f.read()

    # Extract body (without existing frontmatter)
    body = extract_body(content)

    # Generate new frontmatter
    frontmatter_yaml = doc_meta.to_yaml()

    # Combine frontmatter + body
    new_content = f"{frontmatter_yaml}\n\n{body}"

    # Create backup if requested
    if backup:
        backup_path = path.with_suffix(path.suffix + ".bak")
        try:
            shutil.copy2(path, backup_path)
            logger.debug(f"Created backup: {backup_path}")
        except Exception as e:
            logger.warning(f"Could not create backup: {e}")

    # Write new content
    async with aiofiles.open(path, "w", encoding="utf-8") as f:
        await f.write(new_content)

    logger.info(f"Injected frontmatter into: {file_path}")
    return True


async def inject_frontmatter_sync(
    file_path: Union[str, Path],
    doc_meta: DocumentMeta,
    backup: bool = True,
) -> bool:
    """Synchronous version of inject_frontmatter.

    For use in non-async contexts.
    """
    return await inject_frontmatter(file_path, doc_meta, backup)


def format_frontmatter_dict(data: dict) -> str:
    """Format a dictionary as YAML frontmatter.

    Args:
        data: Dictionary to format

    Returns:
        YAML string with --- delimiters
    """
    import yaml

    yaml_content = yaml.dump(
        data,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
    )

    return f"---\n{yaml_content}---"


async def update_frontmatter_field(
    file_path: Union[str, Path],
    field: str,
    value: any,
) -> bool:
    """Update a single field in existing frontmatter.

    Args:
        file_path: Path to the markdown file
        field: Field name to update
        value: New value for the field

    Returns:
        True if successful
    """
    import yaml

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    async with aiofiles.open(path, "r", encoding="utf-8") as f:
        content = await f.read()

    existing_fm = extract_existing_frontmatter(content)
    if not existing_fm:
        logger.warning(f"No existing frontmatter in: {file_path}")
        return False

    # Parse existing frontmatter
    try:
        fm_data = yaml.safe_load(existing_fm) or {}
    except yaml.YAMLError as e:
        logger.error(f"Invalid YAML in {file_path}: {e}")
        return False

    # Update field
    fm_data[field] = value

    # Extract body
    body = extract_body(content)

    # Format new frontmatter
    new_fm = format_frontmatter_dict(fm_data)

    # Combine and write
    new_content = f"{new_fm}\n\n{body}"

    async with aiofiles.open(path, "w", encoding="utf-8") as f:
        await f.write(new_content)

    logger.info(f"Updated field '{field}' in: {file_path}")
    return True
