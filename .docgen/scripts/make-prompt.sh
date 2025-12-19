#!/usr/bin/env bash
[[ ! -f "$1" ]] && echo "Usage: $0 <file.md>" && exit 1

cat .docgen/prompts/create-frontmatter.txt
echo -e "\n<file_path>$1</file_path>\n\n<auto_fields>"
echo -e "<content>"
cat "$1"
echo "</content>"
echo "<output>"
echo "tags: [TAGS]"
echo "title: <TITLE>"
echo "type: <TYPE>"
echo "</output>"
