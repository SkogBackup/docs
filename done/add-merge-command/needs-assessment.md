# Needs Assessment for Merge Command

During normal workflow operations, it was observed that the docs-cli lacks a merge command. This creates a workflow disruption:

1. Users create branches with docs-cli
2. Make changes and commit using docs-cli
3. But then must exit the docs-cli workflow to perform merges with standard git commands

The absence of this command was specifically noticed when trying to merge the branch `draft/add-commit-to-docs-cli` into `master`. While the commit command was added to simplify the workflow, the lack of a merge command still requires users to fall back to git commands, breaking the simplified interface that docs-cli aims to provide.

This functionality would make the docs-cli a more complete tool for managing the documentation workflow from start to finish without requiring users to remember and use raw git commands.

## Recommendation

Add a `merge` command to docs-cli as outlined in the main proposal document.