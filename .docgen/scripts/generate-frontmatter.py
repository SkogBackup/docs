#!/usr/bin/env python3
"""
Generate frontmatter for markdown files using local LLM (ollama).
"""

import sys
import json
import subprocess
import re
from pathlib import Path
from datetime import datetime

def call_ollama(prompt, model="llama3.2"):
    """Call ollama API with a prompt"""
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    result = subprocess.run(
        ["curl", "-s", "http://localhost:11434/api/generate",
         "-d", json.dumps(payload)],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(f"Ollama call failed: {result.stderr}")

    response = json.loads(result.stdout)
    return response.get("response", "")

def extract_output_tags(text):
    """Extract content between <output> tags"""
    match = re.search(r'<output>(.*?)</output>', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()

def build_prompt(file_path, content):
    """Build the prompt for LLM"""
    file_path = Path(file_path)
    # If already relative, use it; otherwise make it relative
    try:
        rel_path = file_path.relative_to(Path.cwd())
    except ValueError:
        rel_path = file_path

    # Read the base prompt
    prompt_file = Path('.docgen/prompts/create-frontmatter.txt')
    with open(prompt_file, 'r') as f:
        base_prompt = f.read()

    # Add file context
    full_prompt = f"""{base_prompt}

<file_path>{rel_path}</file_path>

<content>
{content}
</content>

Now generate the frontmatter with:
- categories from path: {list(rel_path.parent.parts)}
- permalink: {rel_path}
- generated_at: {datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}
- appropriate tags based on content (3-5 keywords)
- appropriate title (filename or more descriptive if obvious)
- type: note (or guide/reference if more appropriate)
"""

    return full_prompt

def has_frontmatter(content):
    """Check if content already has frontmatter"""
    return content.strip().startswith('---')

def extract_body(content):
    """Extract body, removing existing frontmatter if present"""
    if not has_frontmatter(content):
        return content

    parts = content.split('---', 2)
    if len(parts) >= 3:
        return parts[2].lstrip()
    return content

def process_file(file_path):
    """Process a single markdown file"""
    print(f"Processing: {file_path}")

    # Read file
    with open(file_path, 'r') as f:
        content = f.read()

    # Extract body (remove old frontmatter if exists)
    body = extract_body(content)

    # Build prompt and call LLM
    prompt = build_prompt(file_path, body)
    print("  → Calling ollama...")

    response = call_ollama(prompt)

    # Extract frontmatter from response
    frontmatter = extract_output_tags(response)

    print(f"  → Generated frontmatter:\n{frontmatter}\n")

    # Write back
    new_content = frontmatter + '\n\n' + body.lstrip()
    with open(file_path, 'w') as f:
        f.write(new_content)

    print(f"  ✓ Updated {file_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: generate-frontmatter.py <file.md> [file2.md ...]")
        sys.exit(1)

    for file_path in sys.argv[1:]:
        if not Path(file_path).exists():
            print(f"Error: {file_path} not found")
            continue

        try:
            process_file(file_path)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == '__main__':
    main()
