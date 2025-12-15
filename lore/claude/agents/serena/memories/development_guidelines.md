# Development Guidelines and Patterns

## Design Patterns

- **Context-driven development**: All work operates within generated context
- **Script-based automation**: Extensive use of shell scripts for common operations
- **State separation**: Clear separation between session state, persistent state, and system state
- **Hook-based automation**: Automatic context updates and file staging via Claude hooks

## Key Design Principles

- **Functional programming**: Data transformations over control flow
- **Immutable state**: State files represent point-in-time snapshots
- **Transparent collaboration**: Direct user-AI collaboration without hidden operations
- **Context management**: Sophisticated system for maintaining AI context across sessions
- **Modularity and extensibility**: Scripts and tools designed for easy extension and modification

## File Organization Patterns

- **Prefix-based grouping**: `context-*`, `git-*` scripts for related functionality
- **State vs Static**: `/state/` for session data, `/static/` for configuration
- **Development isolation**: `/dev/` for experimental/development work
- **Script centralization**: All operations available via `./scripts/`

## Communication Patterns

- **Data over narrative**: Prefer data structures and transformations in explanations
- **Concise responses**: Brief, direct answers without unnecessary elaboration
- **Function signatures**: Use type signatures and data shapes for communication
- **Incremental refinement**: Build simple solutions first, add complexity later

## Session Management Patterns

- **Context regeneration**: Automatic context updates maintain current state
- **Session persistence**: Key agreements and definitions survive session boundaries
- **Knowledge accumulation**: Insights captured in memory system for future use

## Integration Patterns

- **SkogAI ecosystem**: Part of larger AI agent development framework
- **Git flow**: Structured branching for collaborative development

