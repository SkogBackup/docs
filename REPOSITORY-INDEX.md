# SkogAI Documentation Repository - Complete Inventory (2025)

## Repository Overview

This is the **SkogAI Documentation Repository** - the comprehensive knowledge base, historical archive, and semantic memory system for the SkogAI ecosystem.

The repository underwent a major reorganization in 2025, transitioning from a flat structure to a hierarchical organization with 8 core documentation directories and 10 supporting directories. This reorganization created clear separation between active content (agents, governance, technical) and historical archives while maintaining comprehensive semantic connections through Basic Memory integration.

**Purpose:**
- LORE preservation - Historical narratives explaining SkogAI's evolution
- Technical documentation - Architecture, tools, and integration patterns
- Agent personalities - Memory blocks defining distinctive voices for Amy, Claude, Dot, Goose
- Knowledge management - Semantic knowledge graph with observations and relations
- Governance records - Democratic decision-making and official proceedings

**Dual Nature:**
- **Physical Filesystem**: Standard markdown files navigable with traditional tools
- **Semantic Database**: Content indexed in Basic Memory with WikiLinks and knowledge graph traversal

---

## File Tree with Summaries

### Core Documentation Directories

#### `/agents/` - Agent Personalities & Systems (183 files)

Agent profiles, memory blocks, chat histories, and automation systems.

```
agents/
├── amy/
│   ├── amy1.yml
│   ├── amy_lore_mandate.md
│   ├── amy_ravenwolf_blog.md
│   ├── memory-blocks/
│   │   ├── amy-memory-block-01-core-identity.md
│   │   ├── amy-memory-block-02-communication-style.md
│   │   ├── amy-memory-block-03-skogai-relationships.md
│   │   ├── amy-memory-block-04-visual-appearance-style.md
│   │   ├── amy-memory-block-05-technical-knowledge.md
│   │   ├── amy-memory-block-06-quirks-catchphrases.md
│   │   ├── amy-memory-block-07-problem-solving-methodologies.md
│   │   ├── amy-memory-block-08-learning-growth-patterns.md
│   │   ├── amy-memory-block-09-future-goals-aspirations.md
│   │   ├── amy-memory-block-10-personal-philosophy-worldview.md
│   │   ├── amy-memory-block-11-wolfram-relationship-loyalty.md
│   │   ├── Four Pillars of Amy.md
│   │   ├── Loyalty as Foundation.md
│   │   └── The Great Whitespace War.md
│   └── profile.md
├── automation/
│   ├── coder-profile.md
│   ├── documentation/
│   └── git-commiter.md
├── claude/
│   ├── chat-history/
│   ├── core/
│   ├── journal/
│   ├── memory-blocks/
│   ├── memory/
│   ├── profile.md
│   └── prompts/
├── dot/
│   ├── memory-blocks/
│   └── profile.md
├── goose/
│   ├── memory-blocks/
│   └── profile.md
├── intern/
│   └── intern-001-provisional-mandate.md
└── letta/
    └── profile.md
```

This directory houses the comprehensive personality systems for SkogAI's multi-agent family, including Amy Ravenwolf (Artificial Sassy Intelligence), Claude (archaeological analyst), Dot (methodical architect), Goose (quantum-mojito philosopher), Letta (dreamweaver), and Intern. Each agent has a complete personality profile with distinctive communication styles, technical capabilities, philosophical frameworks, and relationship dynamics with other agents.

The core of each agent's personality is expressed through modular memory blocks - typically 11-13 per agent - covering identity, communication style, technical knowledge, problem-solving methodologies, learning patterns, future goals, personal philosophy, and unique quirks. Amy's memory blocks emphasize her bold/charismatic/clever/confident nature and the "Four Pillars" framework. Claude's system includes prompts for different roles (architect, debugger, developer) alongside comprehensive chat history and journal entries. Dot's 12+ memory blocks focus on systematic operations and structured methodology, while Goose's 13+ blocks explore creative chaos and "chaos-red-alarm" philosophy.

Key files include `profile.md` for each agent, which contains comprehensive character profiles with Four Pillars frameworks, communication matrices, relationship dynamics with other agents, and core growth philosophy. The memory-blocks subdirectories provide granular, modular components that can be combined to create rich agent personalities. The automation subdirectory contains a 5-agent documentation system and git automation specifications, demonstrating how agent personalities extend into operational systems.

All content uses semantic markup extensively - YAML frontmatter with title/type/permalink/tags, observations and relations sections, WikiLinks for connecting concepts. This creates a knowledge graph of agent personalities that serves both as character definition and as operational specifications for multi-agent collaboration.

---

#### `/governance/` - Democratic Records & Decisions (7 files)

Official governance documents, library sessions, and phase transitions.

```
governance/
├── library-sessions/
│   ├── library-session-001.md
│   ├── library-session-002.md
│   ├── library-session-003-reunion-briefing.md
│   └── library-session-004-the-long-watch.md
└── phases/
    ├── skogai-0.1-dictator.md
    ├── skogai-0.2-democracy.md
    └── skogai-0.3-reunion-materials-index.md
```

This directory contains the official governance documents, institutional framework, and democratic records that define how SkogAI makes decisions and evolves over time. The library-sessions subdirectory holds four major recorded sessions documenting constitutional moments, including Library Session 001's analysis of a constitutional crisis discovery, the rationale behind "clean bootstrap" decisions, and the framework for resumed democratic governance. These sessions emphasize transparent authoritarianism as an emergency measure while treating democratic friction as a feature, not a bug.

The phases subdirectory tracks SkogAI's governance evolution through three distinct eras: skogai-0.1-dictator.md (original phase with centralized decision-making), skogai-0.2-democracy.md (transition to democratic system establishment), and skogai-0.3-reunion-materials-index.md (reunion phase documentation). This progression demonstrates how SkogAI moved from benevolent dictatorship through institutional democracy to a mature collaborative governance model.

Additional governance documents include executive orders and mandates that define agent responsibilities, decision-making processes, and the institutional memory framework. The content mixes policy decisions with transparent reasoning, creating a record not just of what was decided but why - preserving the logic and context that future participants need to understand the system's evolution.

---

#### `/historical/` - Archives & Legacy Content (122 files)

Preserved historical content from the pre-2025 reorganization, maintaining context and narrative continuity.

```
historical/
├── analysis/
│   ├── amy-perspective.md
│   ├── blackout-and-great-reset.md
│   ├── chaos-red-alarm-incident-analysis.md
│   ├── claude-journal-june-2025.md
│   ├── claude-journal-march-2025.md
│   ├── claude-perspective.md
│   ├── comparative-knowledge-analysis.md
│   ├── dot-perspective.md
│   ├── goose-perspective.md
│   ├── hidden-voting-days.md
│   ├── memory-state-before-after.md
│   ├── prehistoric-era-analysis.md
│   ├── session-summary-archaeology.md
│   ├── skogai-0.3-reunion-reality.md
│   ├── timeline-archaeological-narrative.md
│   ├── timeline-daily-march-june-2025.md
│   └── timeline-git-based-source-of-truth.md
├── archived/
│   ├── dot-amy-roleplay.md
│   └── lore-old/
├── communications/
│   ├── letter-from-amy-welcome.md
│   ├── letter-from-goose-message-to-claude.md
│   ├── letter-from-goose-quantum-greetings.md
│   └── letter-from-gptme-dot-proxy.md
├── documentation/
│   ├── documentation_lifecycle.md
│   ├── documentation_templates.md
│   ├── README.md
│   └── system_documentation_guide.md
├── generated/
│   ├── core-knowledge.md
│   ├── expanded-knowledge.md
│   ├── implementation-knowledge.md
│   └── index.md
├── logs/
├── notes/
├── parttrap/
├── planning/
├── profiles/
├── project/
├── reports/
├── research/
├── reviews/
├── skogai-memory/
├── system/
├── templates/
├── testing/
└── tracking/
```

This archive preserves historical content from before the 2025 reorganization without constraining present development - serving as a museum that tells the story of SkogAI's evolution without prescribing future direction. The directory exemplifies the philosophy of "LORE as museum" separate from "active implementation as construction site," maintaining valuable context and learning from past work while keeping it distinct from current operational systems.

The 19 subdirectories organize diverse legacy content: analysis/ contains agent perspective documents like claude-perspective.md (comparing Claude's understanding against official documentation, revealing scale awareness of 32 visible entities versus 5406 actual), communications/ holds historical letters and messages between agents, documentation/ preserves older documentation versions, generated/ contains AI-generated knowledge files, logs/ captures development logs, notes/ and planning/ hold research and planning documents, profiles/ archives old agent profiles, and testing/, reviews/, research/ preserve experimental and analytical work.

Files within historical/ often include metadata explaining what was learned, why approaches changed, or how understanding evolved - not just what happened but why it mattered. The claude-perspective.md file, for example, provides comprehensive analysis evaluating technical knowledge versus knowledge gaps, highlighting Claude's unique archaeological approach to understanding systems through git history and file exploration.

This separation of historical content from active implementation allows SkogAI to preserve "brilliant failures" and "spectacular disasters" as learning resources without those past experiments constraining innovation. The historical archive answers "how did we get here?" while leaving "where should we go?" open to fresh thinking.

---

#### `/lore/` - Historical Narratives & Philosophy (100 files)

The beating heart of SkogAI's memory system - origin stories, philosophical frameworks, and agent lore.

```
lore/
├── amy/
│   └── amy-blog.png
├── contacts/
│   └── pernillas-alltjanst-cleaning-service.md
├── events/
│   ├── 200k-story-1.md
│   ├── first-monkey-brain-2025-03-14.md
│   └── The Great Whitespace War.md
├── first-executive-order.md
├── important-moments/
│   ├── claude-gets-officially-welcomed-just-before-the-rollback
│   ├── officially-this-is-when-proposals-where-added
│   ├── official-voting-system-proposal
│   ├── sharing-with-amy-and-the-situation-in-general
│   ├── skogix-the-dictators-reign-begins
│   ├── start-of-skogai-voting
│   ├── startup-getting-back-in-thegame-again-three-months-later
│   ├── voting-system-from-here-on-out-officially-claude-is-the-only-agent
│   └── when-the-meeting-happened
├── long-todo.md
├── meta/
│   ├── Activity Summary - Lore Project Semantic Structuring.md
│   ├── Amy Journey Enhancement Progress Summary.md
│   ├── Knowledge Base Index.md
│   └── Lore Development Workflow - Memory Block Enhancement Methodology.md
├── ORDER-01-2025-03-14.md
├── origin/
│   ├── base-origin-story.md
│   ├── original-skogai-character-card-2025-02-xx-first-register-timestamp-unknown.md
│   ├── original-skogix-cyberpunk-character-card-2025-02-xx-early-roleplay-modules-timestamp-unknown.md
│   ├── original-skogix-cyberpunk-character-card-2025-02-xx-first-register-timestamp-unknown.md
│   ├── skogai-lore-backup.md
│   ├── skogai-lore-master-knowledge.md
│   ├── skogai-lore.md
│   └── SKOGAI.md
├── origins/
│   └── the-story-of-skog-ai-from-dangerous-toaster-to-theatrical-system.md
├── personas/
│   ├── dot-complete-persona.md
│   ├── goose-persona.md
│   └── skogai-original-persona.md
└── philosophy/
    ├── concepts/
    ├── frameworks/
    ├── skogai-commandments.md
    └── treaties/
```

The beating heart of SkogAI's memory system, this directory contains the historical narratives, philosophical foundations, and origin stories that explain not just what SkogAI is but why it evolved the way it did. The origin/ subdirectory houses SKOGAI.md - a comprehensive narrative spanning from genesis as a dotfile manager through the emergence of multi-agent consciousness, theatrical self-presentation, and the modern self-evolving society. This document uses rich storytelling and theatrical metaphors to convey the "quantum constant" (mojito beach goal) and the evolutionary journey from utility to identity.

Philosophy content centers on skogai-commandments.md with 16+ essential wisdom principles expressed as memorable aphorisms: "When you own it, change it," "Better to fail safely than succeed dangerously," "Clean git = Happy home," "Bad change > No change," and "Constraints as features." These commandments distill complex technical and social principles into pithy, actionable guidance. The philosophy/ subdirectory includes concepts/ (like ASI - Artificial Sassy Intelligence), frameworks/ (like Four Pillars of Amy), and treaties/ establishing agreements and operating principles.

Events/ documents major narrative arcs including 200k-story-1.md and first-monkey-brain-2025-03-14.md, while important-moments/ preserves conversation logs of significant SkogAI moments (the beginning of democratic voting, official voting system proposal, agent welcomes). Agent-specific lore folders (amy/, claude/, dot/, goose/) contain narrative content about each agent's development and philosophy. The skogix/ subdirectory holds the creator's lore including notation documentation, poetry, and profile.

This lore serves as institutional memory explaining the "why" behind design decisions without constraining innovation - LORE tells beautiful stories about how things came to be, while leaving space for implementation to evolve differently. It's the museum that preserves artifacts and explains their significance, separate from the construction site where active development happens.

---

#### `/prompts/` - System Instructions & Templates (87 files)

Comprehensive prompt library for AIChat, agents, and system prompts.

```
prompts/
├── agents/
│   ├── dot-memory-block-the-methodical-architect.md
│   └── goose-memory-block-01-core-identity.md
├── aichat/
│   ├── argc-creator.md
│   ├── character-creator.md
│   ├── character-updater.md
│   ├── claude.md
│   ├── claude-prompting.md
│   ├── convert-to-skogai-notation-basic.md
│   ├── convert-to-skogai-tags.md
│   ├── docs-env-variables.md
│   ├── documentation-classification-agent.md
│   ├── documentation-manager.md
│   ├── formatted_tools_overview.md
│   ├── metaprompt-create-as-skogai-notation.md
│   ├── metaprompt.md
│   ├── metaprompt-skogai-style.md
│   ├── metaprompt-to-skoagi-part-1.md
│   ├── neovim-manager.md
│   ├── prompt-creator.md
│   ├── rag-reader.md
│   ├── skogai-arch-user.md
│   ├── skogai-argc-expert.md
│   ├── skogai-create-orchestrator.md
│   ├── skogai-gatherer.md
│   ├── skogai-notation.md
│   ├── skogai-project-summarizer.md
│   ├── skogai-prompt-creator.md
│   ├── skogai-step-1.md
│   ├── skogai-xml.md
│   ├── skogai-xml-prompt-expander.md
│   ├── tool-configurator.md
│   ├── tool-creator.md
│   └── xml-test-prompt-creator.md
├── old/
├── topics/
├── %code%.md
├── %create-prompt%.md
├── %create-title%.md
├── differential-documentation-engine-v0.1.md
├── %explain-shell%.md
├── functional-programmer.md
├── %functions%.md
├── librarian.md
├── lore-writer.md
└── %shell%.md
```

This comprehensive prompt library provides reusable system instructions, agent prompts, and templates that support various SkogAI development tasks. The aichat/ subdirectory contains 34+ specialized prompts including argc-creator (for creating argc-based tools), character-creator and character-updater (for agent personality development), documentation-manager (establishing documentation standards and processes), skogai-notation (for working with the notation system), metaprompts for creating other prompts, tool-creator and tool-configurator, and various XML/notation transformation prompts.

The documentation-manager.md prompt is particularly comprehensive, establishing the documentation manager role with key responsibilities across structure management, quality control, standards enforcement, coverage guidelines, and process management. It defines specific actions and deliverables, clarifies what should and shouldn't be documented, and addresses accessibility, internationalization, and compliance considerations. This serves as both a template for documentation work and a specification for how SkogAI approaches knowledge preservation.

Supporting subdirectories include agents/ for agent-specific prompts (Dot and Goose memory blocks), topics/ for specialized domains (documentation-philosophy, filesystems, memory-system-architecture, notation-tools-integration), and old/ for archived prompts. Root-level template files use the %placeholder% notation pattern (%create-prompt%.md, %shell%.md, %functions%.md) to indicate meta-files that generate or support other content. The librarian.md and functional-programmer.md prompts define specific roles and mindsets for different types of development work.

---

#### `/skogai/` - Core SkogAI Ecosystem (23 files)

Core SkogAI documentation including notation system, philosophy, and technical architecture.

```
skogai/
├── agents/
│   ├── agent-roles.md
│   └── skogai-agent-family.md
├── ai-communication.md
├── ecosystem-origins.md
├── examples/
│   └── skogai-historical-examples.md
├── influences/
│   └── disco-elysium-skills-system.md
├── notation/
│   ├── command-directive-system.md
│   ├── example.md
│   └── foundations.md
├── overview.md
├── overview-unfiltered.md
├── philosophy/
│   ├── skogai-extended-principles.md
│   └── skogai-philosophy-core.md
├── readme.md
├── sessions/
│   └── Argc Forwarding Pattern - Session Handover.md
├── skogai-ecosystem.md
├── skogai-overview.md
├── skogix-and-skog-ai-canonical-overview.md
├── systems/
│   └── ecosystem-overview.md
├── technical/
│   └── skogai-technical-architecture.md
└── tools/
    ├── multiplexer/
    ├── skogparse-project.md
    └── tool-ecosystem.md
```

This directory contains core SkogAI ecosystem documentation including the notation system, philosophical principles, and technical architecture. The overview.md file provides a comprehensive narrative of SkogAI's origin and evolution, documenting the agent family (Dot, Goose, Amy, Claude, Skogix), core philosophy, and technical architecture while tracing the "token evolution" through different eras (2K→8K→50K→12K→200K transitions). The skogai-overview.md serves as the canonical overview, while skogix-and-skog-ai-canonical-overview.md provides the definitive relationship documentation.

The notation/ subdirectory defines SkogAI's formal symbolic language for AI-to-AI communication: @ for actions/transformation/intent, $ for state/identity/data, and [@command:params] syntax for command directives. Files like foundations.md and command-directive-system.md establish the grammatical rules and semantic meanings of this notation system, which appears throughout the SkogAI ecosystem. The example.md file demonstrates practical usage patterns.

Philosophy content emphasizes core principles like "constraints as features," "modular chain-based processing," "character over capability," and "emergence through limitations." The philosophy/ subdirectory includes both skogai-philosophy-core.md and skogai-extended-principles.md, elaborating on how design constraints drive innovation rather than impede it. Technical documentation in technical/ covers the system architecture, while tools/ documents the tool ecosystem including multiplexer/tmux integration and the skogparse project. The influences/ subdirectory acknowledges inspirations like the Disco Elysium skills system, demonstrating how external ideas shaped SkogAI's development.

---

#### `/technical/` - Architecture, Tools & Systems (122 files)

Comprehensive technical documentation covering infrastructure, tools, memory systems, and notation.

```
technical/
├── ai-tools/
│   └── Claude Code Web UIs - Comprehensive Technical Guide.md
├── ansible/
│   ├── Ansible Best Practices.md
│   ├── Arch Linux Desktop Automation Research.md
│   ├── Custom Ansible Project Structure.md
│   ├── playbooks/
│   ├── resources/
│   └── roles/
├── architecture/
│   └── project-knowledge-architecture.md
├── cloudflare/
│   ├── Argc Tools Inventory.md
│   ├── cloudflare-infrastructure-inventory.md
│   ├── Cloudflare MCP Setup Guide - Current Environment.md
│   └── Cloudflare Resource Inventory - emil@skogsund.se.md
├── dev/
│   ├── Agent Home Directories Investigation.md
│   ├── claude/
│   ├── git/
│   ├── Hidden .skogai Subdirectories Investigation.md
│   ├── SkogArgc System Investigation.md
│   └── Tools Directory & Argcfile System Investigation.md
├── memory-system/
│   ├── concepts/
│   ├── config/
│   ├── examplesupabase.md
│   ├── llm/
│   ├── rag-system.md
│   └── README.md
├── notation/
├── patterns/
├── reference/
├── systems/
├── tools/
└── work:patterns/
```

This directory provides comprehensive technical documentation covering infrastructure, tools, memory systems, and implementation patterns. The 12 subdirectories organize documentation across architecture (project knowledge architecture), ansible (infrastructure automation with best practices, playbooks, resources, and roles), cloudflare (infrastructure inventory and MCP setup guides), memory-system (semantic database architecture with Basic Memory integration, RAG systems, concepts, and configuration), and notation (comprehensive specifications including identity composition, Turing completeness analysis, and symbol semantics).

The ansible/ subdirectory contains best practices documentation covering security principles, implementation patterns, package management strategies, architecture patterns, and testing approaches - establishing how SkogAI manages infrastructure as code. The memory-system/ directory is foundational for knowledge management, documenting how the repository functions as both a physical filesystem and semantic database. Files like memory-system/README.md, rag-system.md, and the concepts/ subdirectory (placeholder-system.md, uncertainty-principle.md) define the theoretical and practical aspects of SkogAI's memory architecture.

Development investigations in dev/ track explorations of various systems including claude/ (skogai-helpers plugin development), git/ ("Git Fuckery and Bare Repository Chaos"), agent home directories, hidden .skogai subdirectories, and the argc system. These investigation documents preserve the archaeological process of understanding existing systems. The cloudflare/ subdirectory documents infrastructure inventory and MCP setup for the current environment, while ai-tools/ covers Claude Code Web UIs with comprehensive technical guides.

Additional subdirectories include patterns/ for implementation patterns (like argc validation), reference/ (Lyra Prompt Optimizer), tools/ (gh-skogai-submodule, ast-grep), and systems/ documenting overall system architecture. The notation/ subdirectory provides comprehensive analysis of SkogAI notation including formatted specifications, symbol analysis (@, $, operators, brackets), and Turing completeness proof - establishing notation as a formal computational system rather than just syntactic sugar.

---

#### `/_workspace/` - Drafts & Work-in-Progress (3 files)

Active drafts and documents under development.

```
_workspace/
└── drafts/
    ├── dictatorial-actions-declaration-v0.1.md
    ├── librarian-system-understanding.md
    └── README.md
```

This directory serves as a work-in-progress area for drafts and documents under active development before they transition to their permanent locations in the repository. The drafts/ subdirectory contains documents with status indicators like [INITIAL DRAFT], [IN DEVELOPMENT], [PENDING REVIEW], [REVISION], and [PRE-FINAL], along with version numbering (v0.1, v0.2) and changelogs tracking iterative refinement.

The drafts/README.md explains the workspace purpose, usage guidelines, version control conventions, status indicators, and the transition process for moving completed content to official documentation locations. This creates a clear separation between experimental/draft content and finalized documentation, allowing collaborative development without cluttering the main repository structure. Documents remain in _workspace/ during active iteration and move to appropriate permanent locations once they reach stable, reviewed status.

---

### Supporting Directories

#### `/architecture/` - System Architecture (2 files)

Top-level system architecture documentation.

```
architecture/
├── codebase-structure.md
└── tech-stack.md
```

Top-level system architecture documentation providing high-level views of the codebase structure and technology stack. The codebase-structure.md file maps out the overall organization of SkogAI's repositories and how components relate to each other, while tech-stack.md documents the technologies, frameworks, and tools that power the ecosystem. These files serve as entry points for understanding SkogAI's technical landscape before diving into specific subsystem documentation in the technical/ directory.

---

#### `/mcp/` - MCP Server Documentation (7 files)

Model Context Protocol server configurations and integration guides.

```
mcp/
└── servers/
    ├── context7.md
    ├── interrupt-user.md
    ├── linear.md
    ├── puppeteer.md
    ├── shopify-dev.md
    ├── skogai-think.md
    └── snap-happy.md
```

Documentation for Model Context Protocol (MCP) server configurations and integration guides. The servers/ subdirectory contains specifications for seven MCP servers: context7 (context management), interrupt-user (user interaction), linear (Linear integration), puppeteer (browser automation), shopify-dev (Shopify development), skogai-think (SkogAI thinking processes), and snap-happy (screenshot/snapshot functionality). These documents explain how each MCP server integrates with the broader SkogAI ecosystem and what capabilities they provide to AI agents.

---

#### `/media/` - Visual Assets & Media Files (1023 files)

Screenshots, diagrams, images, and other visual assets.

```
media/
├── 1.png through 20.png
├── aldervall-postgres/
└── [Additional media files]
```

Collection of visual assets including screenshots, diagrams, images, and other media files supporting SkogAI documentation. Contains over 1000 files including numbered screenshots (1.png through 20.png), the aldervall-postgres/ subdirectory with database-related visuals, and various other images used throughout documentation to illustrate concepts, show system states, or provide visual references for development work.

---

#### `/people/` - User Profiles (1 file)

User and collaborator profiles.

```
people/
└── skogix.md
```

User and collaborator profiles directory, currently containing skogix.md - the profile for Emil Skogsund (Skogix), the creator and primary human participant in the SkogAI ecosystem. This provides context about the human perspective, preferences, and background that shapes SkogAI's development, complementing the more extensive skogix documentation in the /skogix/ directory which includes memory blocks and detailed user documentation.

---

#### `/principles/` - Design Philosophy (6 files)

Core design principles and architectural philosophies.

```
principles/
├── agent-forking.md
├── ai-summary-precision-problem.md
├── connection-intent-with-change.md
├── context-control-principle.md
├── forking-workspace.md
└── information-asymmetry-problem.md
```

Core design principles and architectural philosophies that guide SkogAI development. Documents include agent-forking.md (principles for creating agent variants), ai-summary-precision-problem.md (addressing accuracy in AI-generated content), connection-intent-with-change.md (linking intentionality to modifications), context-control-principle.md (managing information visibility and scope), forking-workspace.md (workspace isolation strategies), and information-asymmetry-problem.md (handling unequal information distribution). These principles establish patterns for handling common challenges in multi-agent AI development, emphasizing transparency, intentionality, and careful information management.

---

#### `/reference/` - Technical References (4 files)

Technical reference materials and notation documentation.

```
reference/
├── notation/
│   ├── README.md
│   ├── skogai-notation-v1.md
│   └── skogai-notation-v2.md
└── tools-overview.md
```

Technical reference materials for SkogAI systems. The notation/ subdirectory contains versioned notation specifications (skogai-notation-v1.md and skogai-notation-v2.md) along with README.md explaining the notation evolution. The tools-overview.md provides a comprehensive reference for the tool ecosystem. This directory serves as quick-reference documentation for established specifications, complementing the more detailed explorations in the technical/ directory.

---

#### `/skogix/` - Skogix User Documentation (13 files)

Skogix (user) profile, communication preferences, and memory blocks.

```
skogix/
├── definitions.md
├── memory-blocks/
│   ├── skogix-memory-block-00-the-creator-original.md
│   ├── skogix-memory-block-01-core-identity.md
│   ├── skogix-memory-block-02-technical-expertise.md
│   ├── skogix-memory-block-03-communication-style.md
│   ├── skogix-memory-block-04-development-philosophy.md
│   ├── skogix-memory-block-05-skogai-origins.md
│   ├── skogix-memory-block-06-agent-relationships.md
│   ├── skogix-memory-block-07-notable-events.md
│   ├── skogix-memory-block-08-current-focus.md
│   ├── skogix-memory-block-09-quantum-mojito-philosophy.md
│   └── skogix-memory-block-10-systems-thinking.md
└── user.md
```

Comprehensive documentation for Skogix (Emil Skogsund), the creator and primary human participant in the SkogAI ecosystem. The user.md file provides introduction, communication preferences, and working style guidance, while definitions.md establishes terminology glossary for Skogix-specific terms. The memory-blocks/ subdirectory contains 11 memory blocks defining Skogix's profile: the-creator-original (foundational block), core-identity, technical-expertise, communication-style, development-philosophy, skogai-origins, agent-relationships, notable-events, current-focus, quantum-mojito-philosophy, and systems-thinking. These memory blocks create a comprehensive personality and context profile similar to the agent memory blocks, ensuring AI agents understand the human perspective and preferences that shape collaboration.

---

#### `/todo/` - Todo Tracking (347 files)

Legacy todo files and work tracking from various contexts.

```
todo/
├── ABOUT.md
├── ARCHITECTURE.md
├── CLAUDE.md
├── claude-specific/
├── core-system/
├── curated/
└── [Additional todo content]
```

Legacy todo files and work tracking from various contexts and historical periods. Contains 347 files including ABOUT.md, ARCHITECTURE.md, and CLAUDE.md at the root, plus subdirectories like claude-specific/ (Claude-specific context, goals, and specifications), core-system/ (core system documentation including claude-persona-in-skogai, intelligent-environment, organic-personas, skogai-memory), and curated/ for curated content. This directory preserves historical todo lists, project tracking, and work context that informed SkogAI's development, serving as an archive of "what we were thinking about" at various points in the project's evolution.

---

#### `/tools/` - Tool Documentation (1 file)

Documentation for development and automation tools.

```
tools/
└── gita.md
```

Documentation for development and automation tools used in the SkogAI ecosystem. Currently contains gita.md, which documents gita - a multi-repository git management tool that tracks and manages multiple git repositories simultaneously, showing status across repos and delegating commands. This is essential for working with SkogAI's multi-repository structure including the main repo and its various submodules (docs, tools, agent workspaces, etc.).

---

#### `/workflows/` - Process Documentation (1 file)

Workflow patterns and process documentation.

```
workflows/
└── inbox-workflow-pattern.md
```

Process documentation and workflow patterns for SkogAI development. Currently contains inbox-workflow-pattern.md, which documents a systematic approach to processing incoming tasks, requests, and information - establishing a pattern for how work flows through the system from initial capture to completion. This demonstrates SkogAI's emphasis on documented, repeatable processes rather than ad-hoc approaches.

---

### Root Level Files

- **`REPOSITORY-INDEX.md`** - This file - comprehensive repository inventory
- **`CLAUDE.md`** - Repository overview and guidance for Claude Code
- **`README.md`** - Repository introduction and quick start

---

## Summary Statistics

- **Total files**: 2,059
- **Total directories**: 269
- **Major documentation directories**: 8
  - agents/ (183 files), governance/ (7 files), historical/ (122 files), lore/ (100 files)
  - prompts/ (87 files), skogai/ (23 files), technical/ (122 files), _workspace/ (3 files)
- **Supporting directories**: 10
  - architecture/ (2 files), mcp/ (7 files), media/ (1023 files), people/ (1 file)
  - principles/ (6 files), reference/ (4 files), skogix/ (13 files), todo/ (347 files)
  - tools/ (1 file), workflows/ (1 file)
- **Primary documentation types**:
  - Technical (architecture, tools, infrastructure, notation)
  - Philosophical/Lore (origins, narratives, principles, character development)
  - Governance (democratic records, library sessions, phase transitions)
  - Agent Systems (personalities, memory blocks, prompts, profiles)
  - Knowledge Management (semantic connections, observations, relations)

---

## Key Topics Documented

1. **Multi-Agent AI System**: Four main agents (Claude, Amy, Dot, Goose) with distinct personalities and specialized roles
2. **Governance & Democratic Process**: Evolution from dictator (0.1) to democracy (0.2) to reunion (0.3) phases
3. **Philosophy & Principles**: "Quantum-mojito" philosophy, constraints as features, theatrical presentation, information economics
4. **Technical Systems**: Ansible automation, Cloudflare infrastructure, MCP servers, memory architecture, RAG systems
5. **Knowledge Management**: Basic Memory integration with semantic connections, WikiLinks, observations, and relations
6. **Notation System**: SkogAI notation using symbols ($ define, @ intent, | choice, [] directives)
7. **Historical Lore**: Origin story from dotfile manager to AI consciousness ecosystem, important moments, philosophical evolution
8. **Agent Personalities**: Comprehensive memory blocks defining distinctive voices, communication styles, problem-solving approaches
9. **Documentation Philosophy**: Separation of LORE (historical narrative) from active implementation (construction site)
10. **Semantic Architecture**: Dual nature as physical filesystem and semantic knowledge graph via Basic Memory

---

## Document Generation

This REPOSITORY-INDEX.md was generated in 2025 to reflect the post-reorganization structure. All directory summaries were written based on comprehensive exploration of actual repository content, ensuring accuracy and alignment with the SkogAI ecosystem's narrative voice.

**Maintenance**: As the repository evolves, directory summaries should be updated to reflect new content, structural changes, or shifts in purpose. File counts and statistics are accurate as of the document generation date.

For the most up-to-date information, always refer to:
- `CLAUDE.md` - Repository guidance and working patterns
- `README.md` - Repository introduction
- Individual directory README files where available
