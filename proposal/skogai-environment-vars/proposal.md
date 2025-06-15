# Proposal: SKOGAI Environment Variables Standard and Documentation

## Summary

This proposal establishes an official standard for using SKOGAI environment variables throughout the project to eliminate hardcoded paths. It defines a set of core variables, their purpose, usage patterns, and implementation guidelines to ensure consistency across all components of the SkogAI ecosystem.

## Background

Currently, many scripts within the SkogAI ecosystem use hardcoded paths, which creates several problems:

1. **Portability issues**: Scripts fail when run on systems with different directory structures
2. **Maintenance challenges**: Path changes require updates in multiple files
3. **Inconsistent implementations**: Different scripts handle paths in different ways
4. **Lack of documentation**: No clear standard exists for how environment variables should be used

Recent changes have begun replacing hardcoded paths with the `$SKOGAI` environment variable, but this effort needs standardization and documentation.

A critical aspect of the SKOGAI environment variable is that "the SKOGAI you have is what you are designated." Different entities should have different SKOGAI values based on their use case:

- **Developers**: May point SKOGAI to their development directory
- **Production systems**: Point to production installations
- **AI agents**: Each agent may have its own SKOGAI location
- **End users**: Different users have their own instances

This flexibility is by design, allowing each entity to work within its own appropriate context while the same code runs unchanged across all environments.

## Proposal

### 1. Core Environment Variables

Establish the following core environment variables:

| Variable | Purpose | Example Value |
|----------|---------|---------------|
| `SKOGAI` | Base directory for all SkogAI components | `/home/skogix/skogai` |
| `SKOGAI_DOCS` | Documentation directory | `$SKOGAI/docs/` |
| `SKOGAI_DOCS_OFFICIAL` | Official documentation | `$SKOGAI_DOCS/official/` |

Additional environment variables may be defined for specific components, following the naming pattern `SKOGAI_<COMPONENT>_<SUBCOMPONENT>`.

### 2. Implementation Guidelines

#### a. Variable Usage

- All scripts MUST use environment variables instead of hardcoded paths
- Variables MUST be referenced with `$` prefix (e.g., `$SKOGAI`)
- Variables SHOULD be quoted in scripts: `"$SKOGAI/path"`
- Variables MUST NOT include trailing slashes in their definitions

#### b. Variable Definition

- Variables SHOULD be defined in `.env.skogai` and `.env.skogai.export`
- No single source of truth should be enforced - variables by definition are meant to be flexible
- Lower-level variables SHOULD reference higher-level ones: `SKOGAI_DOCS="$SKOGAI/docs"`

#### c. Error Handling

- Scripts SHOULD check if required variables are set before using them
- Scripts SHOULD provide helpful error messages if variables are missing

### 3. Migration Strategy

1. Identify all hardcoded paths using grep
2. Replace paths with appropriate variables
3. Add variable checking at the beginning of scripts
4. Update documentation to reference environment variables

### 4. Documentation

Create an official document in `$SKOGAI_DOCS_OFFICIAL` titled "Environment Variables Guide" with:

- List of all standard variables
- Examples of correct usage
- Guidelines for defining new variables
- Troubleshooting information

## Current Usage

Based on a grep search, these are the current usages of SKOGAI variables in the codebase:

```
# Core variables defined in .env.skogai and .env.skogai.export
SKOGAI="/home/skogix/skogai"
SKOGAI_DOCS="$SKOGAI/docs/"
SKOGAI_DOCS_OFFICIAL="$SKOGAI_DOCS/official/"

# Service-specific variables found in various scripts
SKOGAI_TARGET_DIRS=("/home/skogix/.dot" "/home/skogix/.skogai" ...)
SKOGAI_WAIT_TIME=10
SKOGAI_BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKOGAI_SERVICE_DIR="${SKOGAI_BASE_DIR}/services"
SKOGAI_CONFIG_DIR="${SKOGAI_BASE_DIR}/config"
SKOGAI_EXCLUDE_PATTERN
```

## Benefits

1. **Improved portability**: Scripts will work regardless of installation location
2. **Easier maintenance**: Changing paths requires modifying only environment variables
3. **Consistency**: Standardized approach across the project
4. **Flexibility**: Users can customize paths without modifying scripts

## Implementation Details

### Documentation

Create the following files:
- `/docs/official/environment-variables.md`: Complete guide to environment variables
- `/docs/examples/env-usage-examples.sh`: Examples of correct variable usage

### Script Updates

1. Add a function to check for required variables:
```bash
check_skogai_env() {
  if [ -z "$SKOGAI" ]; then
    echo "Error: SKOGAI environment variable is not set"
    echo "Please set it to the path of your SkogAI directory"
    exit 1
  fi
}
```

2. Add variable checking to the beginning of scripts:
```bash
check_skogai_env
```

### Environment Variable Definition

Update `.env.skogai` and `.env.skogai.export` to include all standardized variables.

## Compatibility and Migration

This change is backward compatible when implemented correctly. Scripts using hardcoded paths will be updated progressively, with a goal of eliminating all hardcoded paths within three months.

## Next Steps

If this proposal is accepted:

1. Create the official environment variables documentation
2. Update critical scripts to use environment variables
3. Create tools to help identify and replace hardcoded paths
4. Establish a review process for new scripts to ensure they follow the standard