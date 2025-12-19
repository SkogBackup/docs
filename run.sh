#!/usr/bin/env bash
.docgen/scripts/make-prompt.sh ./tools/path/what-we-currently-know.md >.docgen/input/a.txt
.docgen/scripts/ollama.sh .docgen/input/a.txt .docgen/output/a.txt
cat .docgen/output/a.txt
