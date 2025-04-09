#!/bin/bash
set -e

# SkogAI Context System Patching Tool
# Master script for patching different components with context system

# Display usage information
show_usage() {
  echo "SkogAI Context System Patching Tool"
  echo "Usage: $0 COMMAND [OPTIONS]"
  echo ""
  echo "Commands:"
  echo "  agent TARGET_DIR    Patch an agent directory with context system"
  echo "  fork [FORK_PATH]    Patch a fork.sh script with context system support"
  echo "  help               Show this help message"
  echo ""
  echo "Examples:"
  echo "  $0 agent ~/.skogai-base        # Patch .skogai-base"
  echo "  $0 agent -a CustomName ~/agent # Patch with custom agent name"
  echo "  $0 fork                        # Patch fork.sh in the current directory structure"
  echo "  $0 fork ~/custom/fork.sh       # Patch a specific fork.sh"
  echo ""
  echo "For more options, run with the specific command and add --help"
  exit 1
}

# Get the directory containing this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Make sure at least one argument is provided
if [ $# -eq 0 ]; then
  show_usage
fi

# Process the command
COMMAND="$1"
shift

case "$COMMAND" in
  agent)
    "$SCRIPT_DIR/patch-agent.sh" "$@"
    ;;
  fork)
    "$SCRIPT_DIR/patch-fork.sh" "$@"
    ;;
  help)
    show_usage
    ;;
  *)
    echo "Error: Unknown command '$COMMAND'"
    show_usage
    ;;
esac
