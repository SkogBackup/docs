# Repository Status Assessment

This decision tree helps a local LLM assess the current state of the repository before taking action.

```mermaid
flowchart TD
    A[START] --> B{Check current branch}
    B -->|master| C[PROCEED to Task Identification]
    B -->|proposal/*| D[PROCEED to Proposal Management]
    B -->|draft/*| E[PROCEED to Draft Management]
    
    A --> F{Check working directory status}
    F -->|clean| G[PROCEED to next step]
    F -->|changes present| H[Categorize changes]
    
    H --> I[Documentation updates]
    H --> J[Structure changes]
    H --> K[Script improvements]
    H --> L[Proposal updates]
    
    I --> M[Commit with prefix "docs:"]
    J --> N[Commit with prefix "struct:"]
    K --> O[Commit with prefix "script:"]
    L --> P[Commit with prefix "proposal:"]
    
    M --> Q[PROCEED to next step]
    N --> Q
    O --> Q
    P --> Q
    
    Q --> R[PROCEED to Task Identification]
```

## Implementation Steps

1. **Check Current Branch**
   ```bash
   CURRENT_BRANCH=$(git branch --show-current)
   ```

2. **Branch-Based Routing**
   ```bash
   if [[ "$CURRENT_BRANCH" == "master" ]]; then
     # Proceed to Task Identification
   elif [[ "$CURRENT_BRANCH" == proposal/* ]]; then
     # Proceed to Proposal Management
   elif [[ "$CURRENT_BRANCH" == draft/* ]]; then
     # Proceed to Draft Management
   fi
   ```

3. **Check Working Directory Status**
   ```bash
   if [[ -z "$(git status --porcelain)" ]]; then
     # Working directory clean
   else
     # Changes present, need to categorize
   fi
   ```

4. **Categorize and Commit Changes**
   ```bash
   # Example for documentation changes
   git diff --name-only | grep "\.md$"
   git commit -m "docs: Update documentation for X"
   
   # Example for structure changes
   git diff --name-only | grep -v "\.md$"
   git commit -m "struct: Reorganize directory structure"
   ```
