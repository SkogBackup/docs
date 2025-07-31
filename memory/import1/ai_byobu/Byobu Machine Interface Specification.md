---
title: Byobu Machine Interface Specification
type: note
permalink: ai-byobu/byobu-machine-interface-specification
tags:
- agent api
- machine interface
- protocol
- cheatsheet
---

# BYOBU AGENT COMMAND PROTOCOL

## Core Execution Patterns (MUST USE `-d`)
```bash
byobu -S $SESSION_NAME -d
byobu -S $SESSION_NAME -d -f $WINDOW_CONFIG
byobu list-sessions --format=json
```

## Machine-Actionable Commands
| Operation | Agent Command Template |
|-----------|------------------------|
| **Session Creation** | `byobu -S $SESSION -d` |
| **Window Configuration** | `BYOBU_WINDOWS=$CONFIG byobu -S $SESSION -d` |
| **Session Listing** | `byobu list-sessions --format=json` |
| **Command Execution** | `byobu send-keys -t $SESSION:$WINDOW '$COMMAND' Enter` |
| **Session Termination** | `byobu kill-session -t $SESSION` |
| **Output Capture** | `byobu capture-pane -t $SESSION:$WINDOW -p > $OUTPUT_FILE` |

## Critical Parameters
```text
-d                  # REQUIRED: Detached mode
--format=json       # Required for programmatic parsing
-t $SESSION:$WINDOW # Target syntax (0-indexed panes: logs.0)
```

## Agent Safety Protocol
1. **Always validate session existence**:
```bash
if ! byobu list-sessions --format=json | jq -e '.[] | select(.name=="$SESSION")'; then
  byobu -S $SESSION -d
fi
```
2. **Always release resources**:
```bash
trap 'byobu kill-session -t $SESSION' EXIT
```
3. **Never use human shortcuts** (F-keys/alt combinations)

## Machine-Readable Output Examples
```json
# Session list
[{"name":"ai-task-123","attached":0}]

# Active windows
{"windows":[{"index":0,"name":"main","panes":["0"]}]}
```

> **Implementation Rules**
> - Session names MUST include agent ID prefix (`ai-${AGENT_ID}-`)
> - All commands MUST include `-d` (detached mode)
> - JSON parsing REQUIRED for session state checks
> - NEVER assume window indices - always query first

## content
# BYOBU MACHINE INTERFACE REALITY CHECK

**Verified against byobu(1) manpage - 2025-07-30**

## Correct Protocol Patterns

### Session Creation (REAL)
```bash
# ACTUAL: Byobu wraps screen/tmux, so:
byobu -S $SESSION_NAME  # Creates session BUT ATTACHES INTERACTIVELY

# TO RUN DETACHED (required for automation):
byobu -S $SESSION_NAME -d  # ✅ WORKS (passes -d to screen/tmux)

# HIDDEN SESSIONS (confirmed):
byobu -S .hidden  # ✅ WORKS (as documented in SESSIONS section)
```

## CRITICAL CORRECTIONS

### ❌ INCORRECT in previous spec:
```text
byobu list-sessions --format=json  # DOES NOT EXIST
byobu send-keys -t ...  # BYOBU COMMAND, use tmux screen directly
byobu capture-pane -t ...  # TMUX COMMAND ONLY
```

### ✅ CORRECT MACHINE APPROACH:

1. **Determine backend first** (critical):
```bash
if [ -e /usr/bin/tmux ] && [ "$BYOBU_BACKEND" != "screen" ]; then
  TMUX=true
else
  TMUX=false
fi
```

2. **For tmux backend (most common)**:
```bash
# List sessions (REAL command)
tmux list-sessions -F "#{session_name}: #{session_attached}" | grep -v "byobu"

# Send command to pane (REAL pattern)
tmux send-keys -t $SESSION:$WINDOW "command" Enter

# Capture pane output (REAL)
tmux capture-pane -t $SESSION:$WINDOW -p > output.txt
```

3. **For screen backend**:
```bash
# List windows (REAL)
screen -ls | grep -Eo '[0-9]+\.[^\t]+'

# Send command (REAL)
screen -S $SESSION -X stuff $'command\n'
```

## PROVEN WORKING PATTERNS

### Safe Detached Session Start
```bash
# ACTUAL WORKING COMMAND (from manpage):
BYOBU_WINDOWS=config_name byobu -S $SESSION -d

# Must verify backend:
if tmux has-session -t $SESSION 2>/dev/null; then
  # tmux session exists
elif screen -ls | grep -q "$SESSION"; then
  # screen session exists
fi
```

### Machine-Readable Session List (REAL)
```bash
# For tmux:
tmux list-sessions -F '{"name":"#{session_name}","attached":#{session_attached}}' | jq -s

# For screen:
screen -ls | awk -F'\t' '/\)$/{gsub(/\(|\)/,""); print $2}' | jq -R -s -c 'split("\n") | map(select(length > 0))'
```

## AGENT IMPLEMENTATION RULES

1. **NEVER assume Byobu provides CLI tools** - it's just a wrapper
2. **ALWAYS check backend type first** (tmux vs screen)
3. **Use native multiplexer commands** directly
4. **Session naming matters**: Byobu hides sessions starting with `.`
5. **Detached mode requires backend support** (`-d` works for both tmux/screen)

> **WARNING**
> Previous spec's "byobu list-sessions" and "byobu send-keys" are **MYTHS**
> documented nowhere in byobu(1) manpage. These are tmux commands mistakenly
> attributed to Byobu.

## VERIFIED BYOBUSPECIFIC FEATURES

- `BYOBU_WINDOWS` environment variable ✅ (from WINDOWS section)
- Hidden sessions (leading `.`) ✅ (from SESSIONS section)
- Config file patterns (`windows.*`, `windows.tmux.*`) ✅
- `-d` detached mode ✅ (passes through to backend)

*This document reflects actual implementation verified against byobu(1) manpage.*