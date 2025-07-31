---
title: skogai-memory-filename-standards
type: note
permalink: reference/skogai-memory-filename-standards-1
---

# skogai-memory-filename-standards

## Summary
This document provides a concise reference for the file naming and formatting standards used in SkogAI Memory. Following these standards ensures compatibility across systems, CLI tools, and automation processes.

## Naming Conventions

### Filenames
- Use lowercase for all filenames
- Use hyphens for word separation (kebab-case)
- Avoid spaces, underscores, and special characters
- Keep names concise but descriptive
- Avoid redundancy with folder structure

**Good examples:**
- `project-overview.md`
- `file-naming-standards.md`
- `ci-workflow.md`

**Bad examples:**
- `Project Overview.md` (uses spaces and capital letters)
- `file_naming_standards.md` (uses underscores)
- `FILENAMINGSTANDARDS.md` (no word separation)

### Special Files
- System files may use uppercase: README.md, RULES.md, TODO.md
- These are exceptions to the standard lowercase rule
- Regular content files must always use kebab-case

## File Structure

### Standard Sections
Every memory file should include:
- A top-level heading (# Title)
- A summary section
- Main content with hierarchical headings
- An observations section
- A relations section

### Observations Format
```
## observations
- [category] Description text #tag1 #tag2
```

Where categories typically include:
- fact
- decision
- principle
- technique
- requirement

### Relations Format
```
## relations
- relation_type [[linked-document]] (optional description)
```

Where relation types typically include:
- relates_to
- implements
- part_of
- extends
- references

## Why These Standards Matter
- Ensures compatibility with command-line tools
- Prevents escaping issues in terminals
- Facilitates automation of file processing
- Creates consistency across the knowledge base
- Enables predictable searching and linking

## observations
- [fact] Filename standards prevent common system compatibility issues #interoperability #standards
- [principle] Consistent formatting improves both human and machine readability #consistency #usability
- [requirement] All regular content filenames must use lowercase with hyphens #naming #standards
- [technique] Avoiding redundancy in filenames simplifies maintenance and navigation #organization #simplicity
- [decision] We allow exceptions for conventional special files like README.md #conventions #exceptions

## relations
- part_of [[system-rules-and-standards]] (core file naming requirements)
- implements [[documentation-standards]] (best practices for technical documentation)
- relates_to [[cli-compatibility]] (ensures tools can process files properly)