#!/usr/bin/env bash
#
# LLM Summary Generation Script for REPOSITORY-INDEX.md
#
# This script generates prompts for a local LLM (via aichat) to create
# file summaries for each directory in the SkogAI docs repository.
#
# Usage: ./generate-summaries.sh
#
# Output: Creates summaries/ directory with one .md file per directory
#

set -e

DOCS_ROOT="/home/skogix/skogai/docs"
SUMMARIES_DIR="$DOCS_ROOT/summaries"
PROMPT_FILE="$DOCS_ROOT/prompts/documentation-manager.md"

# Create summaries directory
mkdir -p "$SUMMARIES_DIR"

echo "=== SkogAI Docs - LLM Summary Generation ==="
echo "Generating summaries for 18 directories..."
echo ""

# Core Documentation Directories (8)

echo "[1/18] Generating summary for agents/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/agents.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/agents/ and create a comprehensive summary.

Directory: agents/ (183 files)
Purpose: Agent personalities, memory blocks, chat histories, and automation systems

Key subdirectories:
- amy/ - Amy Ravenwolf's profile and memory blocks
- claude/ - Claude's profile, memory blocks, prompts, journal, chat history
- dot/ - Dot's profile and memory blocks
- goose/ - Goose's profile and memory blocks
- intern/ - Intern agent mandate
- letta/ - Letta agent profile
- automation/ - Documentation and git automation agents

Task: Create a 3-4 paragraph summary describing:
1. What this directory contains (agent profiles, memory blocks, etc.)
2. Key files and their purposes (profile.md, memory-blocks/, chat-history/, etc.)
3. The role this content plays in the SkogAI ecosystem

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[2/18] Generating summary for governance/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/governance.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/governance/ and create a comprehensive summary.

Directory: governance/ (7 files)
Purpose: Official governance documents, library sessions, and phase transitions

Key subdirectories:
- library-sessions/ - Four library sessions documenting major discussions
- phases/ - SkogAI evolution phases (0.1-dictator, 0.2-democracy, 0.3-reunion)

Task: Create a 2-3 paragraph summary describing:
1. The governance documents and their role
2. Library sessions and what they contain
3. The three phases of SkogAI governance evolution

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[3/18] Generating summary for historical/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/historical.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/historical/ and create a comprehensive summary.

Directory: historical/ (122 files)
Purpose: Preserved historical content from pre-2025 reorganization

Key subdirectories (19 total):
- analysis/ - Agent perspectives, timelines, incident analyses
- archived/ - Old lore content
- communications/ - Historical letters and messages
- documentation/ - Legacy documentation guides
- generated/ - AI-generated knowledge files
- logs/ - Development logs
- notes/ - Development notes
- profiles/ - Archived agent profiles
- reports/, research/, reviews/, testing/, tracking/ - Various historical records

Task: Create a 3-4 paragraph summary describing:
1. Purpose of historical/ as an archive
2. Major subdirectories and what they preserve
3. Why this content was moved here during 2025 reorganization

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[4/18] Generating summary for lore/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/lore.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/lore/ and create a comprehensive summary.

Directory: lore/ (100 files)
Purpose: Historical narratives, philosophical frameworks, and origin stories

Key subdirectories:
- origin/ - SKOGAI.md, base-origin-story, character cards
- events/ - Important events (200k-story, first-monkey-brain, Great Whitespace War)
- philosophy/ - Concepts, frameworks, commandments, treaties
- important-moments/ - Conversation logs of significant SkogAI events
- meta/ - Lore development workflows and activity summaries
- personas/ - Agent persona definitions

Task: Create a 3-4 paragraph summary describing:
1. The role of lore/ as the "beating heart" of SkogAI's memory
2. Key files like SKOGAI.md and their importance
3. How this content explains the "why" behind SkogAI's evolution

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[5/18] Generating summary for prompts/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/prompts.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/prompts/ and create a comprehensive summary.

Directory: prompts/ (87 files)
Purpose: System instructions, templates, and prompt library

Key subdirectories:
- aichat/ - 30+ prompts for AIChat (argc-creator, documentation-manager, skogai-notation, etc.)
- agents/ - Agent-specific prompts
- topics/ - Topic-specific prompts
- old/ - Archived prompts

Task: Create a 2-3 paragraph summary describing:
1. The comprehensive prompt library
2. Key prompts and their purposes (documentation-manager, metaprompts, etc.)
3. How these prompts support SkogAI development

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[6/18] Generating summary for skogai/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/skogai.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/skogai/ and create a comprehensive summary.

Directory: skogai/ (23 files)
Purpose: Core SkogAI ecosystem documentation

Key subdirectories:
- notation/ - SkogAI notation system (command directives, foundations)
- philosophy/ - Core principles and extended philosophy
- agents/ - Agent roles and family structure
- tools/ - Tool ecosystem, multiplexer, skogparse
- technical/ - Technical architecture
- systems/ - Ecosystem overview

Key files:
- overview.md - Main ecosystem overview
- skogai-overview.md - Canonical overview
- ai-communication.md - AI-to-AI communication patterns

Task: Create a 3 paragraph summary describing:
1. Core SkogAI documentation and its purpose
2. Notation system and its role
3. Philosophy and technical architecture

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[7/18] Generating summary for technical/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/technical.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/technical/ and create a comprehensive summary.

Directory: technical/ (122 files)
Purpose: Architecture, tools, infrastructure, and technical systems

Key subdirectories (12 total):
- ansible/ - Ansible best practices, roles, playbooks
- cloudflare/ - Cloudflare infrastructure and MCP setup
- memory-system/ - Memory architecture, concepts, config
- notation/ - Comprehensive notation specifications
- dev/ - Development investigations (git, claude/, argc system)
- architecture/ - Project knowledge architecture
- ai-tools/ - Claude Code Web UIs guide
- patterns/ - Technical patterns
- systems/ - System architecture
- tools/ - Tool documentation

Task: Create a 3-4 paragraph summary describing:
1. Technical documentation scope
2. Key systems (ansible, cloudflare, memory-system, notation)
3. Development investigations and architecture docs

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[8/18] Generating summary for _workspace/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/_workspace.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/_workspace/ and create a brief summary.

Directory: _workspace/ (3 files)
Purpose: Drafts and work-in-progress

Contents:
- drafts/dictatorial-actions-declaration-v0.1.md
- drafts/librarian-system-understanding.md
- drafts/README.md

Task: Create a 1-2 paragraph summary describing:
1. Purpose of _workspace/ for active drafts
2. What types of content are developed here

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

# Supporting Directories (10)

echo "[9/18] Generating summary for architecture/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/architecture.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/architecture/ and create a brief summary.

Directory: architecture/ (2 files)
Contents: codebase-structure.md, tech-stack.md

Task: Create a 1-2 paragraph summary describing system architecture documentation.

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[10/18] Generating summary for mcp/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/mcp.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/mcp/ and create a brief summary.

Directory: mcp/ (7 files)
Purpose: Model Context Protocol server documentation

Servers documented:
- context7, interrupt-user, linear, puppeteer, shopify-dev, skogai-think, snap-happy

Task: Create a 1-2 paragraph summary describing MCP server integration and documentation.

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[11/18] Generating summary for media/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/media.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/media/ and create a brief summary.

Directory: media/ (1023 files)
Purpose: Visual assets and media files

Contents: Screenshots (1.png through 20.png), diagrams, images, aldervall-postgres/ subdirectory

Task: Create a 1 paragraph summary describing the media assets collection.

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[12/18] Generating summary for people/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/people.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/people/ and create a brief summary.

Directory: people/ (1 file)
Contents: skogix.md - Skogix user profile

Task: Create a 1 paragraph summary describing user profiles directory.

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[13/18] Generating summary for principles/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/principles.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/principles/ and create a brief summary.

Directory: principles/ (6 files)
Contents:
- agent-forking.md
- ai-summary-precision-problem.md
- connection-intent-with-change.md
- context-control-principle.md
- forking-workspace.md
- information-asymmetry-problem.md

Task: Create a 2 paragraph summary describing core design principles and philosophies.

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[14/18] Generating summary for reference/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/reference.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/reference/ and create a brief summary.

Directory: reference/ (4 files)
Contents:
- notation/ (skogai-notation-v1.md, skogai-notation-v2.md, README.md)
- tools-overview.md

Task: Create a 1-2 paragraph summary describing technical reference materials.

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[15/18] Generating summary for skogix/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/skogix.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/skogix/ and create a brief summary.

Directory: skogix/ (13 files)
Purpose: Skogix (user) documentation and memory blocks

Contents:
- user.md - User introduction and communication preferences
- definitions.md - Terminology glossary
- memory-blocks/ - 11 memory blocks defining Skogix's profile (core identity, technical expertise, communication style, development philosophy, etc.)

Task: Create a 2 paragraph summary describing Skogix user documentation.

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[16/18] Generating summary for todo/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/todo.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/todo/ and create a brief summary.

Directory: todo/ (347 files)
Purpose: Legacy todo files and work tracking

Contents:
- claude-specific/ - Claude-specific context and goals
- core-system/ - Core system documentation
- curated/ - Curated content
- Various ABOUT.md, ARCHITECTURE.md, CLAUDE.md files

Task: Create a 1-2 paragraph summary describing the todo tracking directory.

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[17/18] Generating summary for tools/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/tools.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/tools/ and create a brief summary.

Directory: tools/ (1 file)
Contents: gita.md - Multi-repository git management documentation

Task: Create a 1 paragraph summary describing tools documentation.

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo "[18/18] Generating summary for workflows/..."
aichat -f "$PROMPT_FILE" > "$SUMMARIES_DIR/workflows.md" <<'EOF'
Analyze the files in /home/skogix/skogai/docs/workflows/ and create a brief summary.

Directory: workflows/ (1 file)
Contents: inbox-workflow-pattern.md - Workflow pattern documentation

Task: Create a 1 paragraph summary describing workflow patterns.

Output format: Clean markdown paragraphs suitable for REPOSITORY-INDEX.md
EOF

echo ""
echo "=== Summary Generation Complete ==="
echo "Generated 18 summary files in: $SUMMARIES_DIR/"
echo ""
echo "Next steps:"
echo "1. Review the generated summaries"
echo "2. Edit if needed for accuracy and tone"
echo "3. Integrate into REPOSITORY-INDEX.md by replacing [LLM-SUMMARY-PLACEHOLDER: dir/] markers"
echo ""
