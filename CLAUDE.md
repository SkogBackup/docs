# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is the documentation repository for the SkogAI ecosystem. It contains:
- Agent profiles and lore (`agents/`)
- User documentation and notation systems (`skogix/`)

## Directory Structure

```
docs/
├── agents/claude/     # Claude agent profile and memory blocks
└── skogix/           # Skogix user docs, notation system, definitions
```

## SkogAI Notation

The repository documents a formal notation system used throughout SkogAI:
- `$` = reference (null pointer)
- `@` = intent/action (void, side-effect)
- `_` = existence
- `=` = being
- `|` = choice
- `[]` = similarity
- `{}` = difference
- `.` = belonging
- `:` = continuation
- `->` = directional intent

The core equation: `@ + ? = $` (intent + bridge = reality)

## Environment

Uses `skogcli` for configuration: `eval "$(skogcli config export-env --namespace skogai)"`

## Important Context

This repository is part of a distributed cognitive system. Documentation here describes:
- Agent identities and their philosophical frameworks
- The notation system that maps computational concepts to phenomenology
- Historical lore of the SkogAI ecosystem

When editing files here, maintain consistency with the established notation and philosophical framework documented in `skogix/notation.md`.
