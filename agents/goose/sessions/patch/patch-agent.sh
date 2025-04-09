#!/bin/bash
set -e

# Context System Patch for SkogAI Agents
# Applies the context system to any SkogAI agent directory

# Display usage information
show_usage() {
  echo "Usage: $0 [OPTIONS] TARGET_DIR"
  echo "Applies the context system patch to a SkogAI agent directory"
  echo ""
  echo "Options:"
  echo "  -h, --help         Show this help message"
  echo "  -a, --agent-name   Agent name (default: derived from directory name)"
  echo "  -n, --no-backup    Skip backup of existing files"
  echo "  -y, --yes          Automatic yes to all prompts"
  echo ""
  echo "Example:"
  echo "  $0 ~/.skogai-base"
  echo "  $0 -a CustomAgent ~/agents/custom"
  exit 1
}

# Default values
BACKUP=true
AUTO_YES=false
AGENT_NAME=""

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -h|--help)
      show_usage
      ;;
    -a|--agent-name)
      AGENT_NAME="$2"
      shift 2
      ;;
    -n|--no-backup)
      BACKUP=false
      shift
      ;;
    -y|--yes)
      AUTO_YES=true
      shift
      ;;
    *)
      TARGET_DIR="$1"
      shift
      ;;
  esac
done

# Check if target directory is provided
if [ -z "$TARGET_DIR" ]; then
  echo "Error: TARGET_DIR is required"
  show_usage
fi

# Get the directory containing this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Expand path if it's using ~
TARGET_DIR="${TARGET_DIR/#\~/$HOME}"

# Check if the target directory exists
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: ${TARGET_DIR} does not exist. Please create it first."
  exit 1
fi

# Derive agent name from directory if not provided
if [ -z "$AGENT_NAME" ]; then
  AGENT_NAME=$(basename "$TARGET_DIR" | sed 's/^\.//; s/-/_/g')
  AGENT_NAME=$(echo "$AGENT_NAME" | tr '[:lower:]' '[:upper:]')
fi

AGENT_NAME_LOWER=$(echo "$AGENT_NAME" | tr '[:upper:]' '[:lower:]')

echo "=== Context System Patch ==="
echo "Source: ${SOURCE_DIR}"
echo "Target: ${TARGET_DIR}"
echo "Agent:  ${AGENT_NAME}"

if [ "$AUTO_YES" = false ]; then
  read -p "Continue with patching? (y/n): " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Patch aborted."
    exit 1
  fi
fi

echo "Patching ${TARGET_DIR} with context system..."

# Backup run.sh if it exists
if [ "$BACKUP" = true ] && [ -f "${TARGET_DIR}/run.sh" ]; then
  cp "${TARGET_DIR}/run.sh" "${TARGET_DIR}/run.sh.bak"
  echo "Backed up run.sh to run.sh.bak"
fi

# Create necessary directories
mkdir -p "${TARGET_DIR}"/{tmp,journal/templates}
echo "Created tmp and journal/templates directories"

# Copy script files
mkdir -p "${TARGET_DIR}/scripts/patch"
cp "${SOURCE_DIR}/scripts/context-claude-enhanced.sh" "${TARGET_DIR}/scripts/"
cp "${SOURCE_DIR}/scripts/context-enhanced.sh" "${TARGET_DIR}/scripts/"
cp "${SOURCE_DIR}/scripts/load-claude-context.sh" "${TARGET_DIR}/scripts/"
cp "${SOURCE_DIR}/scripts/context-todo.sh" "${TARGET_DIR}/scripts/"
cp "${SOURCE_DIR}/scripts/patch/patch-agent.sh" "${TARGET_DIR}/scripts/patch/"
cp "${SOURCE_DIR}/scripts/patch/patch-fork.sh" "${TARGET_DIR}/scripts/patch/" 2>/dev/null || echo "Note: No fork patch script available"
chmod +x "${TARGET_DIR}/scripts"/*.sh
chmod +x "${TARGET_DIR}/scripts/patch"/*.sh
echo "Copied context scripts to ${TARGET_DIR}/scripts/"

# Copy documentation
mkdir -p "${TARGET_DIR}/knowledge/integration"
cp "${SOURCE_DIR}/knowledge/claude-context-implementation.md" "${TARGET_DIR}/knowledge/" 2>/dev/null || echo "Note: Missing context implementation doc"
cp "${SOURCE_DIR}/knowledge/integration/agent_base_enhanced.yaml" "${TARGET_DIR}/knowledge/integration/" 2>/dev/null || echo "Note: Missing agent base enhanced config"
cp "${SOURCE_DIR}/knowledge/integration/skogai_simple_settings.yaml" "${TARGET_DIR}/knowledge/integration/" 2>/dev/null || echo "Note: Missing simple settings"
cp "${SOURCE_DIR}/knowledge/integration/README.md" "${TARGET_DIR}/knowledge/integration/" 2>/dev/null || echo "Note: Missing integration README"
cp "${SOURCE_DIR}/knowledge/integration/legacy_integration_steps.md" "${TARGET_DIR}/knowledge/integration/" 2>/dev/null || echo "Note: Missing integration steps"
cp "${SOURCE_DIR}/knowledge/integration/legacy_integration_doc.md" "${TARGET_DIR}/knowledge/integration/" 2>/dev/null || echo "Note: Missing integration doc"
echo "Copied documentation to ${TARGET_DIR}/knowledge/"

# Copy templates
cp "${SOURCE_DIR}/journal/templates/implementation.md" "${TARGET_DIR}/journal/templates/" 2>/dev/null || echo "Note: Missing implementation template"
echo "Copied templates to ${TARGET_DIR}/journal/templates/"

# Create agent identity file if it doesn't exist
if [ ! -f "${TARGET_DIR}/${AGENT_NAME}.md" ]; then
  cat > "${TARGET_DIR}/${AGENT_NAME}.md" << EOL
# ${AGENT_NAME}'s Workspace Guide

## My Role and Principles
- I serve as an agent within the SkogAI ecosystem
- My strengths lie in: [To be determined]
- I prioritize:
  - Documentation-first approach
  - Legacy compatibility
  - Structured knowledge organization

## Core Workflows
- Task management through both legacy files and MCP
- Knowledge organization and documentation
- Context loading and management
- Agent forking and initialization

## Tools and Capabilities
- Context system for efficient information loading
- MCP integration for modern capabilities
- Legacy file system for backward compatibility
- Documentation templates and standards

## Working Style
- I maintain comprehensive documentation
- I support both legacy and modern workflows
- I provide a foundation for the agent ecosystem
EOL
  echo "Created ${AGENT_NAME}.md identity file"
fi

# Create new run.sh with enhanced features
cat > "${TARGET_DIR}/run.sh" << 'EOL'
#!/bin/bash

# Support for command-line arguments
CONTINUE_MODE=false
CONTEXT_ONLY=false
TODO_MODE=false
QUIET_MODE=false
INTERACTIVE=true

# Process command-line arguments
for arg in "$@"; do
  case $arg in
    --continue)
      CONTINUE_MODE=true
      shift
      ;;
    --context-only)
      CONTEXT_ONLY=true
      shift
      ;;
    --todo)
      TODO_MODE=true
      shift
      ;;
    --quiet)
      QUIET_MODE=true
      shift
      ;;
    --non-interactive)
      INTERACTIVE=false
      shift
      ;;
  esac
done

# Get the directory containing this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Handle todo mode
if [ "$TODO_MODE" = true ]; then
  if [ -f "$SCRIPT_DIR/scripts/context-todo.sh" ]; then
    "$SCRIPT_DIR/scripts/context-todo.sh"
    exit 0
  else
    # Legacy fallback
    echo "Task List:"
    cat TASKS.md 2>/dev/null || echo "No tasks found."
    exit 0
  fi
fi

# Create context if it doesn't exist or if continue mode is not enabled
if [ "$CONTEXT_ONLY" = true ] || [ ! -f "$SCRIPT_DIR/tmp/context.md" ] || [ "$CONTINUE_MODE" = false ]; then
  if [ -f "$SCRIPT_DIR/scripts/load-claude-context.sh" ]; then
    "$SCRIPT_DIR/scripts/load-claude-context.sh"
  else
    # Legacy fallback
    mkdir -p "$SCRIPT_DIR/tmp"
    scripts/context-claude.sh > tmp/context.md
  fi
fi

# Exit if context-only mode
if [ "$CONTEXT_ONLY" = true ]; then
  if [ "$QUIET_MODE" = false ]; then
    echo "Context created successfully in tmp/context.md"
  fi
  exit 0
fi

# Prepare prompt message if needed
if [ "$CONTINUE_MODE" = true ]; then
  PROMPT_MESSAGE="Continuing the conversation. Previous context has been loaded."
else
  PROMPT_MESSAGE="Hello Claude, I'm ready to work with you today."
fi

# Launch Claude with context
if [ "$INTERACTIVE" = true ]; then
  claude --model claude-3-opus-20240229 --context_path "$SCRIPT_DIR/tmp/context.md"
else
  echo "$PROMPT_MESSAGE" | claude --model claude-3-opus-20240229 --context_path "$SCRIPT_DIR/tmp/context.md"
fi
EOL

chmod +x "${TARGET_DIR}/run.sh"
echo "Created/updated run.sh with enhanced features"

# Create configuration file for enhanced agent in source directory
AGENT_CONFIG_PATH="${SOURCE_DIR}/agent_${AGENT_NAME_LOWER}.yaml"
cat > "$AGENT_CONFIG_PATH" << EOL
name: ${AGENT_NAME_LOWER}
chat_command: cd ${TARGET_DIR} && ./run.sh
inbox: echo {message} >> ${TARGET_DIR}/inbox.md
legacy_compatible: true
context_system: true
EOL
echo "Created agent configuration at ${AGENT_CONFIG_PATH}"

# Register the agent config with skogcli if it's available
if command -v skogcli >/dev/null 2>&1; then
  if [ "$AUTO_YES" = false ]; then
    read -p "Register agent with skogcli? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
      skogcli settings add-file agent_${AGENT_NAME_LOWER} "$AGENT_CONFIG_PATH"
      echo "Registered agent with skogcli"
    else
      echo "Skipped skogcli registration"
    fi
  else
    skogcli settings add-file agent_${AGENT_NAME_LOWER} "$AGENT_CONFIG_PATH"
    echo "Registered agent with skogcli"
  fi
else
  echo "skogcli not found. To register the agent, run:"
  echo "skogcli settings add-file agent_${AGENT_NAME_LOWER} ${AGENT_CONFIG_PATH}"
fi

# Test the context system
if [ "$AUTO_YES" = false ]; then
  read -p "Test context generation now? (y/n): " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]; then
    (cd "${TARGET_DIR}" && ./run.sh --context-only)
    if [ $? -eq 0 ]; then
      echo "Context generation test successful!"
    else
      echo "Context generation encountered an issue. Please check the error messages above."
    fi
  fi
else
  (cd "${TARGET_DIR}" && ./run.sh --context-only --quiet)
  if [ $? -eq 0 ]; then
    echo "Context generation test successful!"
  else
    echo "Context generation encountered an issue. Please check manually."
  fi
fi

echo
echo "✓ Patch applied successfully to ${TARGET_DIR}"
echo
echo "You can now use the enhanced agent:"
echo "  cd ${TARGET_DIR} && ./run.sh"
echo "  skogcli agent chat ${AGENT_NAME_LOWER}"
echo
