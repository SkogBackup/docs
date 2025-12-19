#!/usr/bin/env bash

.docgen/scripts/make-prompt.sh "$3" >"$1"
aichat --model openrouter:qwen/qwen-2.5-coder-32b-instruct --file "$1" -- >"$2"
cat $2
echo "categories: [$(dirname "$1" | sed 's|/|, |g')]"
echo "permalink: ${1%.md}"
echo "generated_at: $(date -u +%Y-%m-%dT%H:%M:%SZ)\n"
