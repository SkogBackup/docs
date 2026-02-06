---
name: gh
description: GitHub CLI expertise - use when working with GitHub repositories, pull requests, issues, releases, workflows, or GitHub Actions. Provides best practices, patterns, and JSON output strategies.
allowed-tools: Bash
---

# gh - GitHub CLI Skill

This skill provides comprehensive knowledge of the GitHub CLI for working with GitHub repositories, pull requests, issues, releases, and workflows.

## When to Use This Skill

Use this skill when you need to:

- Work with GitHub repositories (view, clone, fork, create)
- Manage pull requests (create, review, merge)
- Handle issues and filtering
- Work with GitHub Actions workflows and runs
- Create and manage releases
- Access GitHub API directly
- Get structured JSON output from commands

## Core Principles

### 1. Always Use JSON Output for Data Extraction

Never parse text output with grep, awk, cut, or sed. Always use built-in --json and --jq flags for structured data extraction.

### 2. Filter at Source, Not After

Use native filter flags (--assignee, --label, --state, etc.) instead of fetching all data and filtering with jq afterwards.

### 3. Get Multiple Fields at Once

Request all needed fields in a single API call rather than making multiple calls for different fields.

## Supporting Documentation

This skill includes detailed documentation for:

- **repo.md** - Repository operations (view, clone, fork, create, sync)
- **api.md** - Direct API access (REST and GraphQL)
- **pr.md** - Pull request operations (create, review, merge)
- **workflows.md** - GitHub Actions workflows and runs
- **filtering.md** - Filtering issues and PRs efficiently
- **release.md** - Release management
- **json.md** - JSON output and formatting patterns

Consult these files for specific command syntax, flags, and examples.

## Key Reminders

1. Authentication is automatic
2. Pagination available with --paginate
3. Built-in jq support with --jq flag
4. Template support with --template flag
5. Web fallback with --web flag
6. Discover available JSON fields by running commands with --json and no field list

## Error Prevention

- Always check if resource exists before operations
- Verify state before destructive actions
- Use --draft for PRs and releases when iterating
- Check reviewDecision and mergeable before merging PRs
