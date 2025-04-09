#!/bin/bash
set -e

# Context System Patch for the fork.sh script
# Applies the context system enhancements to the agent forking process

# Display usage information
show_usage() {
  echo "Usage: $0 [OPTIONS] [FORK_SCRIPT_PATH]"
  echo "Applies the context system patch to the agent forking script"
  echo ""
  echo "Options:"
  echo "  -h, --help         Show this help message"
  echo "  -n, --no-backup    Skip backup of existing files"
  echo "  -y, --yes          Automatic yes to all prompts"
  echo ""
  echo "Example:"
  echo "  $0 # Patches the fork.sh in the current directory structure"
  echo "  $0 /path/to/custom/fork.sh"
  exit 1
}

# Default values
BACKUP=true
AUTO_YES=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -h|--help)
      show_usage
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
      FORK_SCRIPT="$1"
      shift
      ;;
  esac
done

# Get the directory containing this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

# If no fork script path provided, use the default location
if [ -z "$FORK_SCRIPT" ]; then
  FORK_SCRIPT="${SOURCE_DIR}/fork.sh"
fi

# Expand path if it's using ~
FORK_SCRIPT="${FORK_SCRIPT/#\~/$HOME}"

# Check if fork.sh exists
if [ ! -f "$FORK_SCRIPT" ]; then
  echo "Error: fork.sh not found at $FORK_SCRIPT"
  exit 1
fi

echo "=== Fork Script Patch ==="
echo "Source: ${SOURCE_DIR}"
echo "Target: ${FORK_SCRIPT}"

if [ "$AUTO_YES" = false ]; then
  read -p "Continue with patching? (y/n): " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Patch aborted."
    exit 1
  fi
fi

echo "Patching ${FORK_SCRIPT} with context system support..."

# Backup the original script if requested
if [ "$BACKUP" = true ]; then
  cp "$FORK_SCRIPT" "${FORK_SCRIPT}.bak"
  echo "Created backup at ${FORK_SCRIPT}.bak"
fi

# Update directory creation to include journal/templates and tmp
sed -i 's|mkdir -p "\${TARGET_DIR}"/{journal,tasks/{active,done,new,paused,cancelled,templates},projects,knowledge,people/templates,scripts/precommit}|mkdir -p "${TARGET_DIR}"/{journal/{templates},tasks/{active,done,new,paused,cancelled,templates},projects,knowledge/{integration},people/templates,scripts/{precommit,patch},tmp}|g' "$FORK_SCRIPT"

# Add copy of context scripts after regular script copying
sed -i '/copy_file scripts/a \
\n# Copy context system scripts\
copy_file scripts/context-claude-enhanced.sh\
copy_file scripts/context-enhanced.sh\
copy_file scripts/load-claude-context.sh\
copy_file scripts/context-todo.sh\
copy_file scripts/patch/patch-agent.sh\
copy_file scripts/patch/patch-fork.sh' "$FORK_SCRIPT"

# Add copy of context implementation documentation
sed -i '/copy_file knowledge\/forking-workspace.md/a \
copy_file knowledge/claude-context-implementation.md\
copy_file knowledge/integration/' "$FORK_SCRIPT"

# Add creation of the agent's identity file with appropriate name
sed -i '/# Create basic ABOUT.md template/i \
# Create specific agent identity file\
cat > "${TARGET_DIR}/${NEW_AGENT}.md" << EOL\
# ${NEW_AGENT}'"'"'s Workspace Guide\
\
## My Role and Principles\
- I serve as an agent within the SkogAI ecosystem\
- My strengths lie in: [To be determined]\
- I prioritize:\
  - Documentation-first approach\
  - Clean workflows\
  - Structured problem-solving\
\
## Core Workflows\
[To be determined during initial setup]\
\
## Tools and Capabilities\
[To be customized during setup]\
\
## Working Style\
[To be determined during initial setup]\
EOL\
\
' "$FORK_SCRIPT"

# Update the gptme.toml template to include agent identity file
sed -i 's|  "README.md",\n  "ARCHITECTURE.md",\n  "ABOUT.md",\n  "TASKS.md",\n  "projects/README.md",|  "README.md",\n  "ARCHITECTURE.md",\n  "ABOUT.md",\n  "TASKS.md",\n  "${NEW_AGENT}.md",\n  "projects/README.md",|g' "$FORK_SCRIPT"

# Change script testing from dry-run to context-only
sed -i 's|(cd "${TARGET_DIR}" && ./run.sh --dry-run > /dev/null)|(cd "${TARGET_DIR}" && ./run.sh --context-only > /dev/null || echo "Context generation not yet functional - will need manual setup")|g' "$FORK_SCRIPT"

# Add reminder to create agent config file
sed -i '/echo "The new agent workspace is ready in: ${TARGET_DIR}"/a \
echo -e "\nRemember to create agent configuration:\ncat > agent_${NEW_AGENT,,}.yaml << EOL\nname: ${NEW_AGENT,,}\nchat_command: cd ${TARGET_DIR} && ./run.sh\ninbox: echo {message} >> ${TARGET_DIR}/inbox.md\nlegacy_compatible: true\ncontext_system: true\nEOL\n\nskogcli settings add-file agent_${NEW_AGENT,,} agent_${NEW_AGENT,,}.yaml"' "$FORK_SCRIPT"

echo
echo "Patch applied successfully to $FORK_SCRIPT"
echo
echo "✓ You can now use the patched fork.sh to create new agents with context system support"
echo "  Example: $FORK_SCRIPT /path/to/newagent NewAgent"
echo
