# Discussion: SKOGAI Environment Variables Standard and Documentation

## The Problem with Hardcoded Paths

During recent work with the SkogAI scripts, we encountered several issues related to hardcoded paths:

1. When modifying `/home/skogix/skogai/democracy/scripts/docs-cli`, we found it was using a hardcoded path:
   ```bash
   REPO_ROOT="$HOME/SkogAI/democracy/"
   ```

2. This caused problems because:
   - The actual directory structure used lowercase (`skogai` instead of `SkogAI`)
   - The path was not portable to other installations
   - Any change in directory structure would break the script

3. After changing this to use `$SKOGAI`:
   ```bash
   REPO_ROOT="$SKOGAI/democracy/"
   ```
   The script functioned correctly regardless of where SkogAI was installed.

## Flexibility vs. Single Source of Truth

A key insight from our work is that environment variables should *not* have a single source of truth - that's precisely what a hardcoded path is. The power of environment variables comes from their flexibility:

1. **Development environments**: A developer might set `SKOGAI=/home/dev/projects/skogai`
2. **Production environments**: A server might use `SKOGAI=/opt/skogai`
3. **Different users**: Each user can have their own configuration

By embracing this flexibility rather than trying to enforce a single "correct" value, we make the system more adaptable to different use cases and environments.

## Current Variable Usage Analysis

Our grep search revealed several patterns in the current codebase:

1. **Core path variables** like `SKOGAI` and `SKOGAI_DOCS` are already defined in environment files

2. **Component-specific variables** like `SKOGAI_SERVICE_DIR` are used extensively in the service management scripts:
   ```bash
   SKOGAI_BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
   SKOGAI_SERVICE_DIR="${SKOGAI_BASE_DIR}/services"
   SKOGAI_CONFIG_DIR="${SKOGAI_BASE_DIR}/config"
   ```

3. **Configuration variables** that don't represent paths but control behavior:
   ```bash
   SKOGAI_WAIT_TIME=10
   SKOGAI_TARGET_DIRS=("/home/skogix/.dot")
   ```

This reveals a mix of path-related variables and configuration variables, all using the SKOGAI prefix. We should clarify when to use this prefix and establish consistent patterns.

## Lessons from Recent Changes

When we changed `docs-cli` and `docs-context` to use `$SKOGAI` instead of hardcoded paths, we observed:

1. The changes were minimal and straightforward
2. The scripts immediately became more portable
3. The environment variable approach provided flexibility without losing functionality

However, we also found that:

1. There was no documentation on how to use SKOGAI variables
2. There was no standard for checking if variables are set
3. Different scripts had different approaches to using variables

## Benefits of a Standardized Approach

Standardizing environment variable usage would provide several benefits:

1. **Consistency**: All scripts would approach paths in the same way
2. **Discoverability**: Developers could easily understand how paths are managed
3. **Resilience**: Scripts would gracefully handle missing variables
4. **Portability**: The entire system would work in any valid installation

## Implementation Considerations

When implementing the environment variables standard, we should consider:

1. **Backward compatibility**: Changes should not break existing scripts
2. **Error handling**: Scripts should provide helpful messages when variables are missing
3. **Documentation**: Clear examples should be provided for different scenarios
4. **Progressive implementation**: We can update scripts over time rather than all at once

## Example: Variable Checking Implementation

Here's a proposed implementation for checking required variables:

```bash
check_required_env_vars() {
  local missing=0
  
  for var in "$@"; do
    if [ -z "${!var}" ]; then
      echo "Error: Required environment variable $var is not set."
      missing=1
    fi
  done
  
  if [ $missing -eq 1 ]; then
    echo "Please set the missing environment variables and try again."
    echo "Tip: You may need to source the environment file: source \$SKOGAI/.env.skogai.export"
    exit 1
  fi
}

# Usage:
check_required_env_vars SKOGAI SKOGAI_DOCS
```

This provides a reusable function that can be included in scripts to check for required environment variables before proceeding.

## Next Steps Discussion

If this proposal is accepted, we should:

1. Start by documenting the current environment variables in use
2. Establish clear guidelines for naming and using new variables
3. Create helper functions for common tasks (checking if variables exist, etc.)
4. Gradually update scripts to remove hardcoded paths

This approach allows for incremental improvements while moving toward a more maintainable and flexible system.