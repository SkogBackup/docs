#\!/bin/bash
# skogcli.sh - Integration script to run skogcli commands from docs-cli

# Function to show help information
show_help() {
  echo "SkogCLI Integration for docs-cli"
  echo ""
  echo "This is an extension for docs-cli that allows running skogcli commands directly."
  echo ""
  echo "Usage: ./scripts/docs-cli skogcli COMMAND [ARGUMENTS]"
  echo ""
  echo "Examples:"
  echo "  ./scripts/docs-cli skogcli help"
  echo "  ./scripts/docs-cli skogcli list"
  echo "  ./scripts/docs-cli skogcli run SCRIPT"
  echo ""
}

# Check if skogcli command exists
if \! command -v skogcli &> /dev/null; then
  echo "Error: skogcli command not found"
  exit 1
fi

# Parse command line arguments
if [ -z "$1" ] || [ "$1" == "help" ]; then
  show_help
else
  # Forward all arguments to skogcli
  skogcli "$@"
fi

exit 0
