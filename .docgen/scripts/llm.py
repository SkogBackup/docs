"""
Ollama LLM client wrapper for frontmatter generation.

Uses structured output with Pydantic schemas to guarantee
valid, typed responses from the LLM.
"""

import asyncio
import logging
import os
from typing import Optional

import ollama
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
    before_sleep_log,
)

try:
    from .models import Frontmatter
except ImportError:
    from models import Frontmatter

logger = logging.getLogger(__name__)

# Default model - good balance of speed and quality for frontmatter
# qwen3:8b is available locally, use it as default
DEFAULT_MODEL = os.environ.get("DOCGEN_MODEL", "qwen3:8b")

# System prompt for frontmatter generation
SYSTEM_PROMPT = """You are a documentation metadata generator for the SkogAI ecosystem.
Given document content, generate accurate YAML frontmatter fields.

Field definitions:
- title: Concise document title (3-8 words). Extract from first heading if meaningful.
- tags: 3-7 keywords describing the content (use kebab-case for multi-word tags).
  Focus on: main topics, tools mentioned, concepts explained.
- type: Classification of the document:
  - "note": General documentation, explanations, learnings
  - "guide": Step-by-step instructions, how-tos, tutorials
  - "reference": Command lists, API docs, quick lookup tables

Important:
- Analyze the actual content thoroughly
- Never fabricate tags - only use concepts present in the text
- Keep titles concise but descriptive
- Default to "note" if document type is unclear"""


class LLMError(Exception):
    """Base exception for LLM-related errors."""

    pass


class ModelNotFoundError(LLMError):
    """Raised when the requested model is not available."""

    pass


class ConnectionError(LLMError):
    """Raised when unable to connect to Ollama."""

    pass


def _before_sleep(retry_state):
    """Log before retrying."""
    logger.warning(f"Retrying Ollama call (attempt {retry_state.attempt_number}/3)...")


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(
        (
            ollama.ResponseError,
            ConnectionError,
            TimeoutError,
            asyncio.TimeoutError,
        )
    ),
    before_sleep=_before_sleep,
)
async def generate_frontmatter(
    content: str,
    model: str = DEFAULT_MODEL,
    timeout: float = 120.0,
) -> Frontmatter:
    """Generate structured frontmatter using Ollama.

    Args:
        content: Document content to analyze (will be truncated to first 1500 chars)
        model: Ollama model to use (default: qwen3:4b)
        timeout: Request timeout in seconds

    Returns:
        Validated Frontmatter object

    Raises:
        ModelNotFoundError: If the model is not pulled
        ConnectionError: If Ollama is not running
        LLMError: For other LLM-related errors
    """
    # Truncate content to avoid token limits while keeping enough context
    content_preview = content[:1500]

    try:
        client = ollama.AsyncClient()

        response = await asyncio.wait_for(
            client.chat(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": f"Generate frontmatter for this document:\n\n{content_preview}",
                    },
                ],
                format=Frontmatter.model_json_schema(),
                options={
                    "temperature": 0,  # Deterministic output
                    "num_predict": 200,  # Limit output tokens
                },
            ),
            timeout=timeout,
        )

        # Parse and validate response
        return Frontmatter.model_validate_json(response.message.content)

    except ollama.ResponseError as e:
        if e.status_code == 404:
            raise ModelNotFoundError(
                f"Model '{model}' not found. Pull it first: ollama pull {model}"
            ) from e
        elif e.status_code == 503:
            raise ConnectionError(
                "Ollama service unavailable. Check if server is running: ollama serve"
            ) from e
        else:
            raise LLMError(f"Ollama API error: {e}") from e

    except Exception as e:
        if "Connection refused" in str(e) or "Cannot connect" in str(e):
            raise ConnectionError(
                "Cannot connect to Ollama. Verify it's running: ollama serve"
            ) from e
        raise LLMError(f"Unexpected error: {e}") from e


async def check_ollama_health(model: str = DEFAULT_MODEL) -> bool:
    """Check if Ollama is running and model is available.

    Args:
        model: Model to check for availability

    Returns:
        True if healthy, False otherwise
    """
    try:
        client = ollama.AsyncClient()
        models = await client.list()

        available_models = [m.model for m in models.models]

        if model not in available_models and f"{model}:latest" not in available_models:
            logger.warning(f"Model '{model}' not found. Available: {available_models}")
            return False

        return True

    except Exception as e:
        logger.error(f"Ollama health check failed: {e}")
        return False


async def pull_model_if_needed(model: str = DEFAULT_MODEL) -> bool:
    """Pull model if not already available.

    Args:
        model: Model to pull

    Returns:
        True if model is available (pulled or already present)
    """
    try:
        client = ollama.AsyncClient()
        models = await client.list()

        available_models = [m.model for m in models.models]

        if model in available_models or f"{model}:latest" in available_models:
            logger.info(f"Model '{model}' already available")
            return True

        logger.info(f"Pulling model '{model}'...")
        await client.pull(model)
        logger.info(f"Model '{model}' pulled successfully")
        return True

    except Exception as e:
        logger.error(f"Failed to pull model '{model}': {e}")
        return False
