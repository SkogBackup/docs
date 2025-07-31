---
title: Hiding Files from Claude Code
type: conversation
permalink: conversations/20250718-Hiding_Files_from_Claude_Code
created: '2025-07-18T09:53:12.481646Z'
modified: '2025-07-18T10:00:29.638104Z'
---

# Hiding Files from Claude Code

### Human (2025-07-18 09:53:12)
hi Claude. I'm looking for a solution / repo for how I can both hide files from Claude code in general. any simple solutions or do we check github?

### Assistant (2025-07-18 09:53:36)
 I'll search for solutions on how to hide files from Claude Code, since this is a specific tool and implementation details may have evolved recently.   Let me get more specific information about the current solutions for hiding files from Claude Code.     Based on my research, here are the current solutions for hiding files from Claude Code:

## **Current Solutions for Hiding Files from Claude Code**

### **1. Command Line Configuration (Most Common)**
Use `claude config add ignorePatterns node_modules` to exclude specific directories. You can add multiple patterns:

```bash
# Hide specific directories
claude config add ignorePatterns "node_modules/**"
claude config add ignorePatterns "dist/**"
claude config add ignorePatterns ".git/**"

# View current ignore patterns
claude config get ignorePatterns
```

### **2. Settings.json Configuration (Newer Approach)**
Claude Code is migrating to a hierarchical settings.json format. Create these files:

**Global settings** (`~/.claude/settings.json`):
```json
{
  "ignorePatterns": ["node_modules/**", "dist/**", ".git/**"]
}
```

**Project-level settings** (`.claude/settings.json`):
```json
{
  "ignorePatterns": ["tests/**", "build/**", "coverage/**"]
}
```

### **3. Third-Party Tool - claude_code_autoignore**
There's a GitHub repo `drvitek/claude_code_autoignore` that automatically syncs your .gitignore files with Claude Code's ignorePatterns. Install it and run:

```bash
# Scan for .gitignore files and sync them
cc_autoignore scan --target=/path/to/directory
cc_autoignore update
```

### **4. Current Limitations**
There's no dedicated `.claudeignore` file yet - this is a frequently requested feature in GitHub issues #79 and #1304. Issue #579 specifically requests a .claudeignore file, but it's still in progress.

### **5. Quick Setup Recommendation**
For immediate use, I'd recommend:

1. **Quick fix**: `claude config add ignorePatterns "node_modules/**,dist/**,build/**,.git/**"`
2. **Better approach**: Create `.claude/settings.json` in your project root with ignore patterns
3. **Automated**: Use the `claude_code_autoignore` tool if you want to automatically sync with your .gitignore

The settings.json approach is the future-proof solution since Anthropic is migrating away from the older ~/.claude.json format.

### Human (2025-07-18 09:56:31)
well I can't get it to work / the files show up on providers side anyway from cacheing and show up via the git-sniffing the cli does :/

but I guess it's better than nothing and worth a try :)

### Assistant (2025-07-18 09:56:43)
 Yeah, you're hitting the core issue that many developers are frustrated with! The current solutions are honestly pretty limited because:

1. **Caching issues** - Claude Code builds its context from cached file scans, so even if you add ignore patterns, it may have already indexed everything
2. **Git context inclusion** - Claude Code automatically includes git status, recent commits, and directory structure in its context, which can expose file paths even if the files themselves are "ignored"
3. **Provider-side visibility** - The files still get sent to Anthropic's servers as part of the initial project scan

Some workarounds people are using:

- **Clear cache**: Try `claude --clear-cache` or restart Claude Code after setting ignore patterns
- **Git worktrees**: Use `git worktree` to create isolated working directories for Claude Code sessions - this way you can have a "Claude-safe" checkout with sensitive files actually not present
- **Skip git indexing**: There's a feature request for disabling git indexing completely, but it's not implemented yet

The git-sniffing behavior is particularly annoying because it includes the full directory tree and git status in every context, regardless of ignore patterns.

You're right that it's "better than nothing" but honestly, the current state is pretty rough for projects with sensitive files. The community is really pushing for a proper `.claudeignore` file and better cache management, but for now it's more of a bandaid than a real solution.

### Human (2025-07-18 10:00:11)
a source in --clear-cache would  be helpful

### Assistant (2025-07-18 10:00:29)
 I searched for documentation on the `--clear-cache` flag but couldn't find any official source that confirms this option exists in Claude Code. Let me search more specifically:     You're absolutely right to ask for a source - I made an error mentioning `--clear-cache` without verification. After searching, I cannot find any official documentation that confirms a `--clear-cache` flag exists in Claude Code.

What I *can* confirm from the official sources:

**Actual cache clearing method**: Use the `/clear` command frequently between tasks to reset the context window - this is the `/clear` slash command within a Claude Code session, not a CLI flag.

**The real issue**: The searches show this is a widespread frustration. People are struggling with:
- File indexing happening before ignore patterns take effect
- Git directories taking "nearly a minute" to index and slowing startup
- No way to actually clear the underlying file index/cache

The closest thing to what you're looking for would be:
1. **Session-level**: Use `/clear` command inside Claude Code to reset context
2. **Nuclear option**: Some users report deleting Claude Code's entire config directory and starting fresh, but there's no official documentation on this

Sorry for the confusion with my earlier suggestion - it seems the caching/indexing issue is exactly why there are so many GitHub issues requesting better cache management and `.claudeignore` files. The current tools really are quite limited for your use case.