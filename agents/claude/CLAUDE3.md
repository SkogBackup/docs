# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build, Lint & Test Commands
- Install dev: `make install` or `make virtualenv` then activate
- Format code: `make fmt` (black + isort)
- Lint code: `make lint` (flake8, black, mypy)
- Run all tests: `make test` or `pytest -v --cov=skogcli tests/`
- Run single test: `pytest tests/test_file.py::test_function_name`
- Watch tests: `make watch`
- Clean: `make clean`

## Code Style Guidelines
- Python >=3.10 with strict typing via mypy
- Line length: 88 characters (black formatted)
- Imports: stdlib first, third-party next, local last (sorted alphabetically)
- Naming: snake_case for functions/variables, PascalCase for classes
- Documentation: Docstrings for all modules, classes, and functions
- Error handling: Catch specific errors, propagate with descriptive messages
- Tests: Located in `tests/` with pytest, follow `test_*.py` naming pattern
- Tool pattern: Tools have consistent interface with `run` function
- Command called without parameter should always return help or usage information

## SkogAI Architecture

### Unified Command Line Interface
The `skogcli` tool provides a unified interface for the SkogAI ecosystem:
- Context-aware: Available commands and scripts depend on current directory
- Tab completion: Discovers available commands, scripts, and options dynamically
- Core modules: script, agent, settings, and tool

### Scripting System
Scripts form the basis of extensible functionality:
- Directory-based discovery: Scripts are discovered in the current directory's `scripts/` folder
- Language agnostic: Support for any executable script (bash, python, ruby, etc.)
- Script chaining: Scripts can call other scripts (e.g., `skogcli script run other_script`)
- Integration points: Specialized hooks for prompt construction, system messages, and dynamic context

### Agent Architecture
The agent system enables autonomous and collaborative AI assistance:
- File-based messaging: Agents communicate through writing to and reading from files
- Inbox handlers: Each agent has a configurable inbox handler for receiving messages
- Agent awakening: File changes trigger agent activation through watch mechanisms
- Cross-agent communication: Agents can message each other to collaborate on tasks

### Integration with SkogChat
SkogChat integrates with the SkogAI platform:
- Shared scripting system: Uses the same script discovery and execution system
- Agent communication: Can interact with the agent ecosystem through messaging
- Settings management: Configuration controlled through the unified settings system