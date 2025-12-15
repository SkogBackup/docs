---
title: Implement run.sh and context system integration
state: new
priority: high
type: feature
created: "2025-06-05"
tags: [context, run.sh, claude-code]
depends: []
---

# Implement run.sh and Context System Integration

## Context

We were working on combining the legacy context system (run.sh generating tmp/context.md) with Claude Code's native file inclusion (@tmp/context-*.md in CLAUDE.md).

## Current Status

- ✅ Identified the approach: modular tmp files + CLAUDE.md includes
- ✅ Understood legacy compatibility requirements
- ✅ Planned standardized parameters (--workspace, --model, etc.)
- ❌ run.sh implementation incomplete

## Requirements

### Core Implementation
- [ ] Update run.sh to generate individual tmp/context-*.md files from each scripts/context-*.sh
- [ ] Generate consolidated tmp/context.md for legacy compatibility
- [ ] Support standard parameters: --workspace, --model, --resume, --no-confirm, --non-interactive, --system, --no-stream
- [ ] Preserve dry-run functionality from run.sh.bak

### CLAUDE.md Integration
- [ ] Add @tmp/context-*.md includes to CLAUDE.md for each context script
- [ ] Make includes toggleable (comment/uncomment as needed)
- [ ] Test file watching and hot reloading

### Legacy Compatibility
- [ ] Ensure other agents can run ./run.sh and get tmp/context.md
- [ ] Follow base implementation patterns from /home/skogix/.old-skogai/scripts
- [ ] Support the dry-run pattern for debugging

## Files to Update
- [ ] run.sh - main implementation
- [ ] CLAUDE.md - add @tmp/context-*.md includes
- [ ] Test with existing scripts/context-*.sh files

## Success Criteria
- [ ] ./run.sh generates all tmp/context-*.md files
- [ ] tmp/context.md consolidates everything for legacy use
- [ ] CLAUDE.md includes work with Claude Code file watching
- [ ] Other agents can visit and generate context successfully
