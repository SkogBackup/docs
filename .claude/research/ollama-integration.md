# Ollama Integration Research

## Overview

Comprehensive guide for integrating Ollama with automated documentation workflows, specifically for frontmatter generation.

---

## 1. API Methods

### Method A: Python Library (Recommended)

```python
import ollama

# Simple generation
response = ollama.generate(
    model='qwen3:4b',
    prompt='Generate frontmatter for this document...',
    options={'temperature': 0}
)
print(response['response'])

# Chat with system prompt
response = ollama.chat(
    model='qwen3:4b',
    messages=[
        {'role': 'system', 'content': 'You are a documentation assistant'},
        {'role': 'user', 'content': 'Generate YAML frontmatter...'}
    ]
)
```

### Method B: HTTP API (Current System Uses)

```python
import json
import subprocess

payload = {
    "model": "llama3.2",
    "prompt": "Generate frontmatter...",
    "stream": False
}

result = subprocess.run(
    ["curl", "-s", "http://localhost:11434/api/generate",
     "-d", json.dumps(payload)],
    capture_output=True, text=True
)
```

### Method C: AsyncClient (High Throughput)

```python
import asyncio
import ollama

async def generate_async(prompts: list[str]):
    client = ollama.AsyncClient()
    tasks = [
        client.generate(model='qwen3:4b', prompt=p)
        for p in prompts
    ]
    return await asyncio.gather(*tasks)
```

---

## 2. Structured Output (Critical for Frontmatter)

### JSON Schema Enforcement (Recommended)

Ollama supports constrained decoding via Pydantic schemas:

```python
from pydantic import BaseModel
from typing import List
import ollama

class Frontmatter(BaseModel):
    title: str
    tags: List[str]
    type: str  # note, guide, reference

response = ollama.chat(
    model='qwen3:4b',
    messages=[{
        'role': 'user',
        'content': 'Generate frontmatter for: [content]'
    }],
    format=Frontmatter.model_json_schema(),  # Enforces structure
    options={'temperature': 0}
)

# Guaranteed valid JSON matching schema
frontmatter = Frontmatter.model_validate_json(response.message.content)
```

### Why This Matters
- **Eliminates parsing errors** from malformed output
- **Guaranteed structure** - no missing fields
- **Type validation** - tags is always a list, not a string

### Current System Problem
The current system uses regex extraction:
```python
match = re.search(r'<output>(.*?)</output>', text, re.DOTALL)
```

This is fragile. Structured output is more reliable.

---

## 3. Model Selection

### For Frontmatter Generation

| Model | Size | Speed | Quality | Recommended |
|-------|------|-------|---------|-------------|
| `tinyllama:1.1b` | 1.1B | 50 tok/s | Basic | 🔴 No |
| `qwen3:4b` | 4B | 30 tok/s | Excellent | ✅ **Yes** |
| `llama3.1:8b` | 8B | 20 tok/s | Superior | ⚠️ If quality issues |
| `gemma3:9b` | 9B | 15 tok/s | Superior | ⚠️ Complex analysis |

**Recommendation**: Start with `qwen3:4b` for optimal balance.

### Model Selection in Code

```python
def get_model_for_task(task_type: str) -> str:
    """Select appropriate model based on task complexity."""
    models = {
        'frontmatter': 'qwen3:4b',      # Fast, good structure
        'summary': 'llama3.1:8b',        # Better context
        'analysis': 'gemma3:9b',         # Complex reasoning
        'quick': 'tinyllama:1.1b'        # Speed priority
    }
    return models.get(task_type, 'qwen3:4b')
```

---

## 4. Error Handling & Retry

### Production Pattern

```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)
import ollama

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type((
        ollama.ResponseError,
        ConnectionError,
        TimeoutError
    ))
)
def generate_frontmatter(content: str) -> dict:
    """Generate with automatic retry on transient failures."""
    response = ollama.chat(
        model='qwen3:4b',
        messages=[{
            'role': 'user',
            'content': f'Generate frontmatter for:\n{content[:500]}'
        }],
        format=Frontmatter.model_json_schema(),
        options={'temperature': 0, 'timeout': 120}
    )
    return Frontmatter.model_validate_json(response.message.content).model_dump()
```

### Error Types to Handle

| Error | Cause | Recovery |
|-------|-------|----------|
| `ResponseError (404)` | Model not pulled | `ollama pull model` |
| `ResponseError (503)` | Service unavailable | Retry with backoff |
| `ConnectionError` | Ollama not running | Start service |
| `TimeoutError` | Model too slow | Increase timeout |

---

## 5. Performance Optimization

### Environment Variables

```bash
# Keep models loaded (avoid cold starts)
export OLLAMA_KEEP_ALIVE="24h"

# Enable parallel requests
export OLLAMA_NUM_PARALLEL=2

# Multiple models loaded
export OLLAMA_MAX_LOADED_MODELS=2
```

### Batch Processing

```python
import asyncio
from asyncio import Queue

class OllamaWorkerPool:
    def __init__(self, num_workers: int = 4):
        self.queue = Queue()
        self.num_workers = num_workers
    
    async def worker(self):
        client = ollama.AsyncClient()
        while True:
            file_path, content = await self.queue.get()
            try:
                result = await client.chat(
                    model='qwen3:4b',
                    messages=[{'role': 'user', 'content': content}],
                    format=Frontmatter.model_json_schema()
                )
                # Process result...
            finally:
                self.queue.task_done()
    
    async def process_files(self, files: list):
        # Start workers
        workers = [
            asyncio.create_task(self.worker())
            for _ in range(self.num_workers)
        ]
        
        # Add files to queue
        for f in files:
            await self.queue.put(f)
        
        # Wait for completion
        await self.queue.join()
        
        # Cancel workers
        for w in workers:
            w.cancel()
```

---

## 6. Load Balancing Multiple Instances

For high-throughput scenarios:

```python
import httpx
import random

OLLAMA_INSTANCES = [
    "http://localhost:11434",
    "http://localhost:11435",
    "http://localhost:11436"
]

async def get_healthy_instance():
    """Round-robin with health check."""
    for instance in OLLAMA_INSTANCES:
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(f"{instance}/api/tags", timeout=2.0)
                if resp.status_code == 200:
                    return instance
        except:
            continue
    raise Exception("No healthy Ollama instances")

async def generate_with_lb(prompt: str) -> str:
    """Generate using load-balanced instances."""
    instance = await get_healthy_instance()
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{instance}/api/generate",
            json={"model": "qwen3:4b", "prompt": prompt, "stream": False},
            timeout=120.0
        )
        return resp.json()['response']
```

---

## 7. Prompt Engineering for Frontmatter

### Current Prompt (from create-frontmatter.txt)

```xml
<task>
Read the document content and generate YAML frontmatter.
You must generate: tags, title, type
Return ONLY the complete frontmatter between <output> tags.
</task>
```

### Improved Prompt (with schema)

```python
SYSTEM_PROMPT = """You are a documentation metadata generator.
Given document content, generate accurate YAML frontmatter.

Field definitions:
- title: Concise document title (3-8 words)
- tags: 3-7 keywords describing content (kebab-case)
- type: "note" (general), "guide" (how-to), or "reference" (lookup)

Always analyze the actual content. Never fabricate tags."""

USER_TEMPLATE = """Generate frontmatter for this document:

File: {file_path}
Content preview:
{content_preview}

Categories (auto-generated from path): {categories}
Permalink: {permalink}"""
```

### Why This Works Better
1. **System prompt** sets consistent behavior
2. **Clear field definitions** reduce ambiguity
3. **Anti-hallucination instruction** prevents fabricated tags
4. **Structured context** with file path helps inference

---

## 8. Integration with Current System

### Recommended Changes

1. **Replace curl with ollama library**
   ```python
   # Before
   subprocess.run(["curl", "-s", "http://localhost:11434/api/generate", ...])
   
   # After
   ollama.generate(model='qwen3:4b', prompt=prompt)
   ```

2. **Add Pydantic schema**
   ```python
   from pydantic import BaseModel
   
   class Frontmatter(BaseModel):
       title: str
       tags: list[str]
       type: str
   ```

3. **Use structured output**
   ```python
   response = ollama.chat(
       model='qwen3:4b',
       format=Frontmatter.model_json_schema()
   )
   ```

4. **Add retry logic**
   ```python
   @retry(stop=stop_after_attempt(3), wait=wait_exponential())
   def generate_frontmatter(content: str) -> Frontmatter:
       ...
   ```

---

## 9. Monitoring & Metrics

```python
import time
from dataclasses import dataclass

@dataclass
class GenerationMetrics:
    prompt_tokens: int
    completion_tokens: int
    duration_ms: float
    tokens_per_second: float
    model: str

def generate_with_metrics(prompt: str) -> tuple[str, GenerationMetrics]:
    start = time.time()
    
    response = ollama.generate(
        model='qwen3:4b',
        prompt=prompt
    )
    
    duration_ms = (time.time() - start) * 1000
    eval_count = response.get('eval_count', 0)
    eval_duration_ns = response.get('eval_duration', 1)
    
    metrics = GenerationMetrics(
        prompt_tokens=response.get('prompt_eval_count', 0),
        completion_tokens=eval_count,
        duration_ms=duration_ms,
        tokens_per_second=(eval_count / eval_duration_ns) * 1e9,
        model='qwen3:4b'
    )
    
    return response['response'], metrics
```

---

## 10. Docker Deployment

```yaml
# docker-compose.yml
version: '3.8'
services:
  ollama:
    image: ollama/ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama-data:/root/.ollama
    environment:
      - OLLAMA_KEEP_ALIVE=24h
      - OLLAMA_NUM_PARALLEL=2
    deploy:
      resources:
        limits:
          memory: 16G
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    restart: always

volumes:
  ollama-data:
```

---

## Summary

| Aspect | Current System | Recommended |
|--------|----------------|-------------|
| API | curl subprocess | ollama library |
| Output parsing | Regex `<output>` | Pydantic schema |
| Error handling | None | tenacity retry |
| Model | llama3.2 | qwen3:4b |
| Concurrency | Sequential | AsyncClient + workers |
| Monitoring | None | Metrics collection |
