#\!/bin/bash
# docs_integration_setup.sh - Setup script for docs-cli integration with skogcli

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/script_metadata.json"

# Add docs entry to script_metadata.json if it doesn't exist
if [ -f "$CONFIG_FILE" ]; then
  # Check if docs entry already exists
  if \! grep -q '"name": "docs"' "$CONFIG_FILE"; then
    # Create a temporary file with the updated content
    TMP_FILE=$(mktemp)
    jq '. += [{"name": "docs", "description": "Docs CLI integration for managing SkogAI/docs repository", "category": "tools", "path": "scripts/docs.sh", "icon": "📄"}]' "$CONFIG_FILE" > "$TMP_FILE"
    mv "$TMP_FILE" "$CONFIG_FILE"
    echo "Added docs entry to script_metadata.json"
  else
    echo "docs entry already exists in script_metadata.json"
  fi
else
  echo "Error: script_metadata.json not found at $CONFIG_FILE"
fi

# Create votes directory if it doesn't exist
VOTES_FILE="$SCRIPT_DIR/misc/docs_votes.json"
if [ \! -f "$VOTES_FILE" ]; then
  mkdir -p "$(dirname "$VOTES_FILE")"
  echo '{"votes": {}}' > "$VOTES_FILE"
  echo "Created votes file at $VOTES_FILE"
fi

echo ""
echo "SkogCLI to docs-cli integration setup complete\!"
echo ""
echo "You can now use the following commands:"
echo "  skogcli docs ...            # Run docs-cli commands from skogcli"
echo "  skogcli docs context        # Generate docs context"
echo "  skogcli docs vote NAME      # Vote for a proposal"
echo "  skogcli docs votes          # Show all votes"
echo ""
echo "To complete the bidirectional integration:"
echo "Please add the skogcli command support to docs-cli by adding this code to the case statement in docs-cli:"
echo ""
echo 'skogcli)'
echo '  if [ -f "$REPO_ROOT/scripts/extensions/skogcli.sh" ]; then'
echo '    "$REPO_ROOT/scripts/extensions/skogcli.sh" "${@:2}"'
echo '  else'
echo '    echo "Error: skogcli extension not found"'
echo '  fi'
echo '  ;;'
