#!/usr/bin/env python3
"""
Generate docs directly from markdown input files (no database needed)
"""

import subprocess
import os
from datetime import datetime
from pathlib import Path
import argparse
import re

def parse_frontmatter(content):
    """Extract YAML frontmatter"""
    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    frontmatter = parts[1].strip()
    body = parts[2].strip()

    fm_dict = {}
    current_key = None
    current_list = []

    for line in frontmatter.split('\n'):
        line = line.strip()
        if not line:
            continue

        if line.startswith('- '):
            # List item
            if current_key:
                current_list.append(line[2:])
        elif ':' in line:
            # Save previous list if exists
            if current_key and current_list:
                fm_dict[current_key] = current_list
                current_list = []

            # Parse new key
            key, value = line.split(':', 1)
            current_key = key.strip()
            value = value.strip()

            if value:
                fm_dict[current_key] = value

    # Save last list
    if current_key and current_list:
        fm_dict[current_key] = current_list

    return fm_dict, body

def call_ollama(model, prompt):
    """Call Ollama to generate content"""
    try:
        result = subprocess.run(
            ['ollama', 'run', model, prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error calling Ollama: {e}")
        return None

def generate_frontmatter(metadata):
    """Generate YAML frontmatter"""
    timestamp = datetime.now().isoformat()

    fm = "---\n"

    # Categories
    if 'categories' in metadata and metadata['categories']:
        fm += "categories:\n"
        cats = metadata['categories'] if isinstance(metadata['categories'], list) else [metadata['categories']]
        for cat in cats:
            fm += f"- {cat}\n"
    else:
        fm += "categories: []\n"

    # Tags
    if 'tags' in metadata and metadata['tags']:
        fm += "tags:\n"
        tags = metadata['tags'] if isinstance(metadata['tags'], list) else [metadata['tags']]
        for tag in tags:
            fm += f"- {tag}\n"
    else:
        fm += "tags: []\n"

    # Other fields
    if 'permalink' in metadata:
        fm += f"permalink: {metadata['permalink']}\n"
    if 'title' in metadata:
        fm += f"title: {metadata['title']}\n"
    if 'type' in metadata:
        fm += f"type: {metadata['type']}\n"

    fm += f"generated_at: {timestamp}\n"
    fm += "---\n\n"

    return fm

def load_prompt_template(template_name, prompts_dir):
    """Load prompt template"""
    template_path = Path(prompts_dir) / f"{template_name}.txt"
    with open(template_path, 'r') as f:
        return f.read()

def process_markdown_file(input_file, output_file, prompt_template, model, prompts_dir):
    """Process a single markdown file"""
    print(f"Processing: {input_file}")

    # Read input markdown
    with open(input_file, 'r') as f:
        content = f.read()

    # Parse existing frontmatter and body
    metadata, body = parse_frontmatter(content)

    # Load prompt template
    template = load_prompt_template(prompt_template, prompts_dir)

    # Fill template
    prompt = template.replace("{input_context}", body)
    prompt = prompt.replace("{title}", metadata.get('title', Path(input_file).stem))
    prompt = prompt.replace("{agent_name}", metadata.get('title', Path(input_file).stem))

    # Generate via Ollama
    generated = call_ollama(model, prompt)

    if not generated:
        print(f"  ✗ Failed to generate")
        return False

    # Create new frontmatter
    new_frontmatter = generate_frontmatter(metadata)

    # Combine
    final_content = new_frontmatter + generated

    # Write output
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(final_content)

    print(f"  ✓ Generated: {output_file}")
    return True

def process_directory(input_dir, output_dir, prompt_template, model, prompts_dir):
    """Process all markdown files in a directory"""
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    md_files = list(input_path.rglob('*.md'))
    print(f"\nProcessing {len(md_files)} files...\n")

    success = 0
    for md_file in md_files:
        # Calculate relative path
        rel_path = md_file.relative_to(input_path)
        out_file = output_path / rel_path

        if process_markdown_file(md_file, out_file, prompt_template, model, prompts_dir):
            success += 1

    print(f"\nProcessed {success}/{len(md_files)} files")

def main():
    parser = argparse.ArgumentParser(description='Generate docs from markdown input files')
    parser.add_argument('--input', required=True, help='Input markdown file or directory')
    parser.add_argument('--output', required=True, help='Output file or directory')
    parser.add_argument('--template', required=True, help='Prompt template name')
    parser.add_argument('--model', default='llama3.2', help='Ollama model')
    parser.add_argument('--prompts', default='.docgen/prompts', help='Prompts directory')

    args = parser.parse_args()

    input_path = Path(args.input)

    if input_path.is_file():
        process_markdown_file(args.input, args.output, args.template, args.model, args.prompts)
    elif input_path.is_dir():
        process_directory(args.input, args.output, args.template, args.model, args.prompts)
    else:
        print(f"Error: {args.input} not found")

if __name__ == "__main__":
    main()
