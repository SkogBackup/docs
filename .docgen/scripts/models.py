"""
Pydantic models for frontmatter generation.

These models define the structure of frontmatter and ensure
validated, typed output from the LLM.
"""

from datetime import datetime
from pathlib import Path
from typing import List, Literal, Optional

from pydantic import BaseModel, Field, field_validator


class Frontmatter(BaseModel):
    """LLM-generated frontmatter fields.

    These are the fields that the LLM generates based on document content.
    """

    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Concise document title (3-8 words)",
    )
    tags: List[str] = Field(
        ...,
        min_length=3,
        max_length=7,
        description="3-7 keywords describing content (kebab-case)",
    )
    type: Literal["note", "guide", "reference"] = Field(
        default="note",
        description="Document classification: note (general), guide (how-to), reference (lookup)",
    )

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, v: List[str]) -> List[str]:
        """Ensure tags are lowercase and kebab-case."""
        return [tag.lower().replace(" ", "-").replace("_", "-") for tag in v]

    @field_validator("title")
    @classmethod
    def validate_title(cls, v: str) -> str:
        """Clean up title - remove excessive whitespace."""
        return " ".join(v.split())


class DocumentMeta(BaseModel):
    """Complete document metadata including auto-generated fields.

    Combines LLM-generated frontmatter with auto-generated fields
    like categories (from path), permalink, and timestamp.
    """

    categories: List[str] = Field(
        default_factory=list, description="Auto-generated from file path"
    )
    permalink: str = Field(..., description="URL-friendly path to document")
    generated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Timestamp of frontmatter generation",
    )
    title: str
    tags: List[str]
    type: Literal["note", "guide", "reference"] = "note"

    @classmethod
    def from_file_path(
        cls, file_path: Path, frontmatter: Frontmatter
    ) -> "DocumentMeta":
        """Create DocumentMeta from file path and LLM-generated frontmatter.

        Args:
            file_path: Path to the markdown file (relative to docs root)
            frontmatter: LLM-generated frontmatter

        Returns:
            Complete DocumentMeta with auto-generated fields
        """
        # Ensure we're working with a Path object
        path = Path(file_path)

        # Extract categories from parent directories
        # e.g., agents/claude/journal/file.md -> ["agents", "claude", "journal"]
        categories = list(path.parent.parts)

        # Generate permalink (strip .md extension)
        permalink = str(path.with_suffix(""))

        return cls(
            categories=categories,
            permalink=permalink,
            generated_at=datetime.utcnow(),
            title=frontmatter.title,
            tags=frontmatter.tags,
            type=frontmatter.type,
        )

    def to_yaml(self) -> str:
        """Convert to YAML frontmatter string.

        Returns:
            YAML string wrapped in --- delimiters
        """
        import yaml

        data = {
            "categories": self.categories,
            "permalink": self.permalink,
            "generated_at": self.generated_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "title": self.title,
            "tags": self.tags,
            "type": self.type,
        }

        yaml_content = yaml.dump(
            data, default_flow_style=False, sort_keys=False, allow_unicode=True
        )

        return f"---\n{yaml_content}---"


class ProcessingResult(BaseModel):
    """Result of processing a single file."""

    file_path: str
    success: bool
    error: Optional[str] = None
    frontmatter: Optional[DocumentMeta] = None
    duration_ms: float = 0.0
