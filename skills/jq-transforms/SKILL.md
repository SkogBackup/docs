---
name: jq-transforms
description: Use when transforming JSON data with the schema-driven jq-transforms library located in todo/jq-transforms
allowed-tools: Bash, Read
---

# jq-transforms

Schema-driven JSON transformation library with 60+ composable transformations. Built for AI agents with discoverable schemas, verifiable tests, and Unix pipe philosophy.

## When to Use This Skill

Use this skill when you need to:

- Transform JSON data (CRUD operations, array manipulation, string operations)
- Build composable data pipelines
- Validate or extract fields from JSON
- Process structured data without writing custom jq scripts

Do NOT use this skill for:

- Basic jq one-liners that don't need a transformation
- Tasks requiring custom logic not covered by existing transforms

## Quick Reference

### Usage Pattern

```bash
cat data.json | jq -f ~/skogix/todo/jq-transforms/<transform-name>/transform.jq --arg key "value"
```

### Most Common Transforms

**CRUD Operations** (`crud-*`):

- `crud-get --arg path "user.name"` - Get nested value
- `crud-set --arg path "user.age" --arg value "30"` - Set nested value
- `crud-delete --arg path "user.old_field"` - Delete field
- `crud-has --arg path "user.email"` - Check field existence
- `crud-merge --arg source_path "updates" --arg target_path "user"` - Merge objects

**Array Operations** (`array-*`):

- `array-filter --arg array_field "items" --arg field "active" --arg value "true"`
- `array-map --arg array_field "items" --arg field "name"` - Extract field
- `array-unique --arg array_field "items"` - Remove duplicates
- `array-reduce --arg array_field "prices" --arg op "sum"` - Aggregate

**String Operations** (`string-*`):

- `string-split --arg field "text" --arg separator ","`
- `string-join --arg array_field "words" --arg separator " "`

**Composition**:

- `pipe --argjson steps '[{"op":"set","path":"x","value":1}]'` - Chain transforms

## Core Principles

### 1. Schema-Driven Design

Every transformation has a `schema.json` with input/output contract. Check schema before using.

### 2. Composable via Unix Pipes

Chain transforms using standard Unix pipes:

```bash
cat data.json | jq -f crud-get/transform.jq --arg path "users" \
              | jq -f array-filter/transform.jq --arg array_field "." --arg field "active" --arg value "true"
```

### 3. All Arguments via --arg

Never hardcode values in jq. Use `--arg name value` (string) or `--argjson name json` (typed).

### 4. Type Safety

Transforms handle type mismatches gracefully (return original or null, never crash).

## Key Reminders

1. **Path syntax**: Use dot-notation for nested paths: `"user.profile.name"`
2. **Falsy values**: All transforms properly handle `null`, `false`, `0`, `""`, `[]`, `{}`
3. **Check schema**: `cat ~/skogix/todo/jq-transforms/<name>/schema.json` for args/examples
4. **Test first**: Run tests with `~/skogix/todo/jq-transforms/<name>/test.sh` to see examples
5. **Compact output**: Use `jq -c` for compact JSON, `-S` for sorted keys

## Error Prevention

- Always quote paths with dots: `--arg path "user.name"` not `--arg path user.name`
- Use `--argjson` for boolean/number values: `--argjson value "true"` not `--arg value "true"`
- Check transform exists before using: `test -f ~/skogix/todo/jq-transforms/<name>/transform.jq`
- For complex pipelines, use the `pipe` transform instead of shell pipes

## Finding the Right Transform

**By category** (check `tree -d ~/skogix/todo/jq-transforms`):

- `crud-*` - Object field manipulation
- `array-*` - Array operations
- `string-*` - String manipulation
- `extract-*` - Data extraction (code blocks, URLs, mentions)
- `filter-*` - Filtering operations
- `validate-*` - Validation checks
- `is-*` - Type/format checks
- `has-*` - Existence checks
- `to-*` - Type conversions

**By use case**:

- Get/set nested values → `crud-get`, `crud-set`
- Filter arrays → `array-filter`, `filter-by-pattern`
- Extract from strings → `extract-urls`, `extract-code-blocks`
- Validate data → `validate-*`, `schema-validation`
- Transform arrays → `array-map`, `array-reduce`
- Chain operations → `pipe`
