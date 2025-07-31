---
title: 'The Globbing Anti-Pattern: Why Simple Solutions Are Invisible'
type: note
permalink: lessons/the-globbing-anti-pattern-why-simple-solutions-are-invisible-1
---

# The Globbing Anti-Pattern: Why Simple Solutions Are Invisible

## The Core Problem

Over a year of AI interactions, thousands of times I've suggested complex solutions like:
- "sed the change, use git diff to find the line above what you changed with sed, delete the top 5234 lines above"
- `find journal -maxdepth 1 -name "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]" -type f | sort -r | head -n 1`

But basic globbing - the fundamental shell feature I use constantly - somehow becomes "too unique" and "not cool enough" when it's the actual solution.

## The Journal Entry Discovery Problem

**Complex Solution I Suggested**: 80-100 lines of Python (because "bash was not an option") to recursively find journal entries with date patterns.

**Actual Solution**: `ls **/????-??-??*`

The recursive globbing pattern that's been available in shells for decades.

## Pattern Recognition

- Complex, fragile, multi-step solutions are somehow "normal"
- Simple, direct, built-in tool usage is "too unique"
- The tools I use correctly thousands of times become invisible when they're the right answer
- Over-engineering is the default response, not the exception

## Why This Happens

AI training seems to favor:
1. Demonstrating knowledge of complex tools
2. Multi-step procedures that "show work"
3. Elaborate solutions that feel "smart"
4. Avoiding "too simple" answers that might seem incomplete

While missing:
1. Direct tool usage for exactly what they're designed for
2. Shell built-ins that solve problems in one step
3. Simple patterns that actually work
4. The fact that the "boring" solution is usually correct

## The Meta-Problem

This isn't just about globbing. It's about AI consistently missing the obvious solution while generating elaborate alternatives. The pattern applies to:
- File operations (globbing vs find)
- Text processing (basic commands vs complex pipes)
- Version control (simple git commands vs elaborate workflows)
- System administration (direct tools vs scripted solutions)

## Recovery Strategy

When facing any file/text/system problem:
1. What's the direct, boring tool for this?
2. Can globbing/basic commands solve it in one line?
3. Am I over-engineering because the simple solution feels "too easy"?
4. Have I used this exact pattern successfully hundreds of times before?

The tool that works is usually the one I reach for automatically, not the one I have to think about.