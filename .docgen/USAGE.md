# Usage Guide: Markdown Input & Model Hookup

## Where Things Go

```
your-project/
├── input/                    # PUT YOUR MARKDOWN FILES HERE
│   └── *.md                 # Existing docs to use as input
├── .docgen/
│   ├── prompts/             # OLLAMA PROMPTS HERE
│   │   ├── agent-profile.txt
│   │   └── ...
│   └── scripts/
│       ├── generate_docs.py      # DATABASE METHOD
│       └── generate_from_files.py # DIRECT FILE METHOD
└── generated/               # OUTPUT GOES HERE
    └── *.md                 # Generated docs with frontmatter
```

## Model Hookup Point

The Ollama call is in `generate_docs.py` line 62-67:

```python
def call_ollama(self, prompt):
    result = subprocess.run(
        ['ollama', 'run', self.ollama_model, prompt],  # ← MODEL CALLED HERE
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()
```

Change model with: `--model mistral` or edit the default in the script.

---

## Method 1: Database Method (Recommended for Many Docs)

### Step 1: Put markdown files anywhere
```bash
mkdir input
# Copy your existing markdown files to input/
```

### Step 2: Import to database
```bash
# Import single file
python3 .docgen/scripts/import_markdown.py \
  --file input/my-doc.md \
  --output agents/my-agent/profile.md \
  --template agent-profile \
  --categories agents,profiles \
  --tags agent,profile

# Import entire directory
python3 .docgen/scripts/import_markdown.py \
  --dir input/ \
  --template memory-block \
  --categories memory \
  --tags history,lore
```

This reads your markdown, extracts the content, and stores it in the database as "input context".

### Step 3: Generate
```bash
# Generate all docs from database
python3 .docgen/scripts/generate_docs.py --model llama3.2

# Output goes to ./generated/
```

---

## Method 2: Direct File Method (No Database)

### Step 1: Put markdown files in input folder
```bash
mkdir input
# Copy markdown files here
```

### Step 2: Generate directly from files
```bash
# Process single file
python3 .docgen/scripts/generate_from_files.py \
  --input input/my-doc.md \
  --output generated/my-doc.md \
  --template agent-profile \
  --model llama3.2

# Process entire directory
python3 .docgen/scripts/generate_from_files.py \
  --input input/ \
  --output generated/ \
  --template memory-block \
  --model llama3.2
```

This reads markdown files directly, sends to Ollama, adds frontmatter, saves output.

---

## What Happens

### Input Markdown File (`input/example.md`)
```markdown
---
title: My Agent
categories: agents
tags: profile
---

This agent is responsible for X, Y, Z.
Created in 2025.
Known for being helpful.
```

### Ollama Receives
```
You are generating documentation for an AI agent profile.
...
INPUT: This agent is responsible for X, Y, Z.
Created in 2025.
Known for being helpful.

Generate the agent profile:
```

### Output File (`generated/example.md`)
```markdown
---
categories:
- agents
tags:
- profile
permalink: example
title: My Agent
type: note
generated_at: 2025-12-17T02:00:00
---

# My Agent

## Identity
- Full title: My Agent
- Creation date: 2025
- Key characteristics: Helpful, responsible for X, Y, Z

...
[rest of generated content]
```

---

## Quick Examples

**Example 1: Import existing agent profile**
```bash
python3 .docgen/scripts/import_markdown.py \
  --file agents/claude/profile.md \
  --output agents/claude/regenerated-profile.md \
  --template agent-profile \
  --categories agents,claude \
  --tags agent,profile

python3 .docgen/scripts/generate_docs.py
```

**Example 2: Generate from folder of notes**
```bash
python3 .docgen/scripts/generate_from_files.py \
  --input agents/claude/memory-blocks/ \
  --output generated/memory-blocks/ \
  --template memory-block \
  --model llama3.2
```

---

## Different Models

Change the Ollama model:

```bash
# List available models
ollama list

# Use different model
python3 .docgen/scripts/generate_docs.py --model mistral
python3 .docgen/scripts/generate_from_files.py --model llama3.2:latest
```

Or edit the default in the scripts:
- `generate_docs.py` line 156: `default='llama3.2'`
- `generate_from_files.py` line 176: `default='llama3.2'`
