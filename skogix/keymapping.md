---
title: skogix/keymappings
usage: scratchpad
intent: creating a self documenting file containing the keymapping philosophy together with the workflow to maintain it
tags: [documentation, keymapping, skogix]
references:
  - /home/skogix/docs/skogix/definitions.md
---

# current workflow: creating the basic structure and workflow for keymapping documentation

**Goal:** Create documentation explaining the users intent, goals and philosophy as well as the current state and implementations. The documentations entry-point will be `/home/skogix/docs/skogix/keymapping.md` and should contain enough information to understand the keybinding philosophy and what workflow to follow for making changes.

**Approach:** Three-phase planning with a end result focusing on: `intent`: where we want to be, `actuality/state`: where we are, and `workflow/changes`: how to get there.

---

## Phase Structure

### Phase 1: Intent (CURRENT)

Document philosophy and desired keybinding approach.

**Status:** Draft exists - user reviewing

**Output:** @/home/skogix/docs/skogix/keymapping.md sections:

- ## intent

- ### philosophy

- ### modality

- ### definitions

**Tasks:**

1. [ ] Restructure keymapping.md to use `## intent` as section header and add subsections where needed to describe the users intent
2. [ ] Add definitions from the $example:definitions below: ($keybind.layer, $input, $mod, $key) to definitions section in a json codeblock

[$example:definitions]
**Definitions:**

- `$keybind.layer` : a abstract layer or group describing the general area of influence. example:
  `$keybind.layer.editor.h` would describe changing focus in neovim, `$keybind.layer.multiplexer` would do the same conceptual thing in tmux and `$keybind.layer.vm.h`
- `$input`: physical key on the keyboard
- `$mod` or `$modifier`: pressed together with a $input creates a $key
- `$key`, `<$mod-$input>` or simply `$mod+$input`: represents the abstraction of he input signal recieved by the system. example: user press b while holding shift could be represented as $key being: `<shift-b>`, `shift+b`, `Uppercase B`, `&#66;` or simply `B`
[$/example:definitions]

### Phase 2: Actuality/State

Research and document the actual workflows, usage and state of the user and the system.

This phase is focused on creating a knowledge base to mirror the actual state of reality to the intended state of the end goal.

User recommends using a standard `keybindings.json` (the user reference vscode and their keybindings.json) structure for the actual representation of the state.

#### Proposed Tasks

1. [ ] Creating a `keybindings.json` including a program from each $layer and the actual keybindings used.

### Phase 3: Implementation

Compare intent vs actuality, generate roadmap.

Example: The users intent is to have vim-style keybindings represent all relational movement and in phase 1 we defined `h` to be "represents the direction left,<-,<left-arrow> or the previous item in a ordered list.". The made up program X have dirty dirty emacs-style keybindings for movement. The implementation roadmap would include steps to change program X's keybindings to match the users intent.

---

## overview/filestructure

[@todo:ask claude for preferred formatting for what is essentially header+description]

- # state

- ## definitions ($keybind.layer, $input, $mod, $key)

- ## keybindings.json (vscode format in a json codeblock)

- # workflow

- ## intent (phase 1:user story)

- ### philosophy (vim-first, defaults baseline, layer separation)

- ### modality table (keyboard, wm, multiplexer, editor)

- ### movement patterns

- ### actions (clipboard, search)

- ## actuality (phase 2:research)

- ### mapping overview (programs used, layers represented)

- ## implementation(phase 3:iteration)

- ### workflows (steps to follow to go from actuality to intent)

- ### roadmap (workflows to follow paired with a expected time frame and expected outcome)

- ### iteration (update `# keymapping state` with new understanding and facts)

---

## Verification

- Intent accurately captures philosophy
- Actuality matches real config files
- Roadmap is actionable
