---
title: Anthropic Claude Code Context Research
type: conversation
permalink: conversations/20250727-Anthropic_Claude_Code_Context_Research
created: '2025-07-27T06:42:44.808241Z'
modified: '2025-07-27T06:52:31.179437Z'
---

# Anthropic Claude Code Context Research

### Human (2025-07-27 06:43:03)
hello claude! I'm a developer using Claude Code alot and would like to do some research into Anthropics caching solutions as well as finding out if there is any way to actually get to know the context available to Claude Code.

### Assistant (2025-07-27 06:43:48)
 Hi! I can help you research Anthropic's caching solutions, though I should mention upfront that I don't have detailed information about Claude Code's specific implementation or how to inspect its context.

Let me search for current information about Anthropic's caching offerings:   Now let me search for information about Claude Code context inspection:   Now let me search for more specific information about Claude Code's context and inspection capabilities:   Based on my research, I can provide you with comprehensive information about Anthropic's caching solutions and some insights into Claude Code's context management, though unfortunately there isn't a direct way to inspect Claude Code's full context window.

## Anthropic's Caching Solutions

Anthropic offers **prompt caching**, which enables developers to cache frequently used context between API calls, reducing costs by up to 90% and latency by up to 85% for long prompts. Here are the key features:

### Current Caching Options

**Standard Prompt Caching:**
- 5-minute cache lifetime by default
- Available for Claude Opus 4, Claude Sonnet 4, Claude Sonnet 3.7, Claude Sonnet 3.5, Claude Haiku 3.5, Claude Haiku 3, and Claude Opus 3
- Minimum cacheable content: 1024 tokens for most models, 2048 tokens for Claude Haiku

**Extended Caching (New):**
- 1-hour TTL option available at additional cost—a 12x improvement that can reduce expenses for long-running agent workflows
- Cache read tokens no longer count against your Input Tokens Per Minute (ITPM) limit for Claude 3.7 Sonnet
- Automatic cache management - you no longer need to manually track and specify which cached segments to use

### Implementation Details

When you send a request with prompt caching enabled, the system checks if a prompt prefix up to a specified cache breakpoint is already cached from a recent query. If found, it uses the cached version, reducing processing time and costs.

**Key features:**
- You can define up to four cache breakpoints in a prompt
- The cache is refreshed for no additional cost each time the cached content is used
- Prompt caching references the entire prompt - tools, system, and messages (in that order) up to and including the block designated with cache_control

### Use Cases
Prompt caching is effective for conversational agents, detailed instruction sets with many examples, agentic tool use scenarios with multiple API calls, and querying large documents like books, papers, or documentation.

## Claude Code Context Management

Unfortunately, there's no direct way to inspect Claude Code's full context window, but here's what I learned about how it manages context:

### CLAUDE.md Files - The Primary Context Mechanism

Claude Code automatically ingests CLAUDE.md files to gain project-specific context before starting work. Think of it as a pre-flight briefing that rides along with every request.

**Context Hierarchy:**
Claude reads information from CLAUDE.md files in order: first from the user's home directory, then at the top level of the project, and then per-directory. CLAUDE.md files can be hierarchical, so you can have one project-level and one in nested directories.

### Context Window Management

**Built-in Commands:**
- `/compact` - summarizes the conversation while preserving important context
- `/clear` - completely resets the conversation (but CLAUDE.md persists)
- `ccusage` - shows token usage and estimated cost for your current session

**Best Practices:**
Use /compact at natural breakpoints (after completing a feature, before starting a new one). Consider /clear vs /compact - if the current conversation has gone too far off track, /clear might be better than /compact.

### Context Inspection Techniques

While you can't directly inspect the full context window, here are some practical approaches:

1. **Use the `/memory` command** - shows all CLAUDE.md files that are being loaded

2. **Context priming workflows** - Define workflows in CLAUDE.md that systematically gather context using find commands, ripgrep searches, and reading relevant files before making changes

3. **Ask Claude directly** - You can prompt Claude to explain what context it has access to in the current session

4. **Monitor file access** - Claude Code shows which files it's reading and accessing during conversations

For comprehensive guidance on optimizing Claude Code context management, I'd recommend checking out Anthropic's official documentation at 'https://docs.anthropic.com' and their prompt engineering resources.

The lack of direct context inspection is a current limitation, but the CLAUDE.md system and built-in context management commands provide good visibility into what context is being used.

### Human (2025-07-27 06:46:51)
could you please quote at least the paragraph you are referring to in your answer :)

### Assistant (2025-07-27 06:47:10)
 You're absolutely right! Let me provide the key quoted passages that support my main points, while being careful about copyright considerations.

## Anthropic's Caching Solutions

**On cost and latency benefits:**
"With prompt caching, customers can provide Claude with more background knowledge and example outputs—all while reducing costs by up to 90% and latency by up to 85% for long prompts."

**On the extended caching improvement:**
"Developers can now choose between our standard 5-minute time to live (TTL) for prompt caching or opt for an extended 1-hour TTL at an additional cost—a 12x improvement that can reduce expenses for long-running agent workflows."

**On automatic cache management:**
"You no longer need to manually track and specify which cached segments to use as we automatically identify and use the most relevant cached content. This not only reduces your workload, but also frees up more tokens."

## Claude Code Context Management

**On CLAUDE.md files:**
"At its core, a claude.md file is a special Markdown file that Claude Code automatically ingests to gain project-specific context before it starts working with you. Think of it as a pre-flight briefing or a highly-opinionated prompt that rides along with every request."

**On context hierarchy:**
"Claude reads information and guidance from CLAUDE.md files in order: first from the user's home directory, then at the top level of the project, and then per-directory."

**On context window management commands:**
"ccusage shows token usage and estimated cost for your current session... /compact summarizes the conversation while preserving important context... /clear completely resets the conversation (but CLAUDE.md persists)."

Unfortunately, regarding direct context inspection, the research didn't reveal a built-in way to view Claude Code's full context window contents. The closest approaches are using the `/memory` command and asking Claude directly about its current context.

### Human (2025-07-27 06:52:00)
well since I for some reason can't use the basic api calls on a subscription that's not a option.  Claude.md files are pretty much ignored / useless because they referred to the cached file which I don't have access to.

any information about anything surrounding the @-inclusion for files?

### Assistant (2025-07-27 06:52:31)
 Let me search for more specific information about the @-inclusion feature in Claude Code:    Perfect! Here's what I found about the @-inclusion feature in Claude Code:

## @ File Inclusion Syntax

**Basic Usage:**
"Type @ followed by the filename to reference any file in your project: @package.json @src/components/Header.tsx @README.md"

**Tab Completion:**
"Pro tip: Use tab completion after typing @ to quickly navigate and select files. This saves typing and prevents path errors."

**What it does:**
"The @ reference syntax is one of Claude Code's most powerful features for efficient file management. It allows you to quickly add a file's content to the context without Claude having to find and read the file itself, which usually takes longer."

**Drag and Drop Alternative:**
"Dragging files in normally opens them in a new tab like in Cursor or VS Code. Hold Shift while dragging to reference them properly in Claude."

## Advanced Usage Examples

**Multiple Files at Once:**
"When working with interconnected files, reference them all at once to give Claude complete context: > Update the header component with new navigation. Files: @src/components/Header.tsx @src/styles/header.css @tests/Header.test.tsx @src/types/navigation.d.ts"

**Directory References:**
"Use @ to quickly include files or directories without waiting for Claude to read them... This includes the full content of the file in the conversation... This provides a directory listing with file information."

**Adding Context in CLAUDE.md:**
"Include frequently referenced paths in your CLAUDE.md to preserve context across sessions"

## Known Issues

Unfortunately, there are some current limitations:

**Hidden Files/Folders:**
There are reported issues with @ not being able to reference files and folders starting with "." (like .vscode/, .claude/, .env files)

**Case Sensitivity:**
"File references are case-sensitive on Linux/Mac"

## Practical Tips

**Explain Relationships:**
"Don't just list files - explain their relationship: > I'm refactoring the payment processing. The current flow is in: @src/services/payment.ts (main logic) @src/api/stripe.ts (payment provider integration) @src/models/Transaction.ts (data model)"

This @ syntax essentially bypasses the need for Claude to actively search and read files - it directly includes their content in the context window, which should work regardless of API subscription limitations since it's a client-side feature of Claude Code itself.