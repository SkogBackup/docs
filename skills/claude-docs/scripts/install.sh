#!/bin/bash
set -e

echo "Installing docs plugin"
echo "Plugin: $PLUGIN_NAME v$PLUGIN_VERSION"

# Fetch latest Claude Code documentation
node "$PLUGIN_CACHE_PATH/scripts/update_docs.js"
