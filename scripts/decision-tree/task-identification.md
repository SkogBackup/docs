# Task Identification

This decision tree helps a local LLM identify tasks that need to be performed in the repository.

```mermaid
flowchart TD
    A[Task Identification] --> B[Scan for TODO markers in files]
    B --> C{TODOs found?}
    C -->|Yes| D[Add to task list]
    C -->|No| E[Check active proposals]
    D --> E
    
    E --> F{Proposals need review?}
    F -->|Yes| G[Add to task list]
    F -->|No| H[Check directory structure]
    G --> H
    
    H --> I{Standard directories missing?}
    I -->|Yes| J[Add creation to task list]
    I -->|No| K[Check for unlinked documentation]
    J --> K
    
    K --> L{Unlinked docs in documentation-merge?}
    L -->|Yes| M[Add migration to task list]
    L -->|No| N[PROCEED to Task Prioritization]
    M --> N
```

## Implementation Steps

1. **Scan for TODO Markers**
   ```bash
   TODO_FILES=$(grep -l "TODO" --include="*.md" --include="*.sh" -r .)
   if [[ -n "$TODO_FILES" ]]; then
     # Add to task list
     echo "TODO items found in: $TODO_FILES" >> tasks.txt
   fi
   ```

2. **Check Active Proposals**
   ```bash
   PROPOSAL_BRANCHES=$(git branch | grep "proposal/" | sed 's/^\*//g' | sed 's/^ *//')
   if [[ -n "$PROPOSAL_BRANCHES" ]]; then
     # Check if proposals need review
     for branch in $PROPOSAL_BRANCHES; do
       # Logic to determine if review is needed
       echo "Review needed for: $branch" >> tasks.txt
     done
   fi
   ```

3. **Check Directory Structure**
   ```bash
   REQUIRED_DIRS=("architecture" "standards" "workflows" "features" "agents" "proposals")
   for dir in "${REQUIRED_DIRS[@]}"; do
     if [[ ! -d "$dir" ]]; then
       echo "Create directory: $dir" >> tasks.txt
     fi
   done
   ```

4. **Check for Unlinked Documentation**
   ```bash
   # Logic to find documentation in documentation-merge that isn't in the current repository
   # This would require a more complex script to compare directories
   ```
