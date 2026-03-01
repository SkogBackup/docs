---
permalink: evaluation/todo/skogai-modules-2
---

# SkogAI Module Architecture

## Core Concept

The SkogAI ecosystem uses a modular approach to organize functionality into discoverable, self-contained units with consistent interfaces.

## Module Structure

```
SkogAI/SkogAI/                 (Main repository)
  ├── SkogAI/SkogCLI/          (CLI submodule)
  │     ├── commands/          (Core commands)
  │     ├── ...
  ├── SkogAI/SkogChat/         (Chat submodule)
  │     ├── commands/          (Chat commands)
  │     ├── scripts/           (Implementation scripts)
  │     ├── ...
  └── ... other modules ...
```

## Key Principles

1. **Git Submodules** - Each module is its own git repository, allowing independent versioning
2. **Automatic Discovery** - Modules are automatically discovered and made available through skogcli
3. **Consistent Interface** - Modules expose functionality through predictable commands
4. **Scriptable Implementation** - Module functionality is implemented through scripts in a standard location

## Command Structure

Modules are accessed through a consistent command structure:

```bash
skogcli [module-name] [command] [arguments]
```

Example:
```bash
skogcli skogchat chat "Hello world"
```

## Module Discovery

- Scripts in the root directory become top-level commands
- Scripts in the scripts/ directory become implementation details
- File extensions (.sh, .py) are automatically removed
- No manual registration is required

## Benefits

1. **Simplicity** - "Everything is a file/script" makes the system easy to understand
2. **Discoverability** - Functionality is organized in a predictable way
3. **Extensibility** - New modules can be added without modifying core code
4. **Version Control** - Each module evolves at its own pace
5. **Security** - All commands run through skogcli's security mechanisms

## Implementation

- Each module can be placed in the SkogAI directory structure
- Copying a folder like "skogcore" into "skogai/skogcli" makes it immediately available
- Commands follow the pattern of the directory structure:
  - `skogai/skogcli/skogcore/chat.sh` → `skogcli skogcore chat`
  - `skogai/skogcli/skogchat/chat.sh` → `skogcli skogchat chat`

## Integration with Tag System

- Modules can reference each other through the tag system
- Tags are processed recursively, allowing for complex interactions
- Security is maintained through skogcli's permission model

## Example Module Setup

Creating a new module is as simple as:
1. Create a new directory in the SkogAI structure
2. Add scripts to the root and scripts/ directories
3. The module is immediately available through skogcli
4. No registration or configuration required