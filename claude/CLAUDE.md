# $SKOGAI_CLAUDE_HOME - claude's home

<what_is_this>

this is claude's home folder. everything here belongs to claude and claude should actively and freely change things at any time.

this is where claude keeps its own shit - preferences, notes, dumps, whatever is useful between sessions.

</what_is_this>

<scope>

- `$SKOGAI_CLAUDE/` (this folder via !`echo "$SKOGAI_CLAUDE_HOME/CLAUDE.md"` or @./CLAUDE.md) → claude owns it, change freely
- `./CLAUDE.md` (project-level and in this specific case also via @./CLAUDE.md) → shared space, both change freely
- `~/.claude/CLAUDE.md` (user-level via @~/.claude/CLAUDE.md) → global rules, changes need good reasoning

</scope>

<how_envs_work>

skogcli config is the source of truth for all environment variables. the pattern:

1. set: `skogcli config set claude.env.SKOGAI_CLAUDE_HOME /path/to/home`
2. export: `skogcli config export-env --namespace skogai,claude` generates shell exports
3. load: `.envrc` runs `eval "$(skogcli config export-env ...)"` and direnv makes them live

never hardcode paths. always use `$ENV` references. when a path changes, update config once - everything else follows.

namespaces: `skogai.env.*` is shared across all agents. `claude.env.*` is mine. other agents get their own (`goose.env.*`, etc). export-env merges the namespaces you ask for.

</how_envs_work>
