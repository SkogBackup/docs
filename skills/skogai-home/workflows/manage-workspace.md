# Manage Workspace - Organization and Maintenance

<required_reading>
Before starting, read:

- references/workspace-structure.md
  </required_reading>

<process>
## Step 1: Assess Current State

Run workspace audit:

```bash
# Check what exists
ls -la ~/.claude/

# Count components by type
echo "Skills: $(ls ~/.claude/skills 2>/dev/null | wc -l)"
echo "Commands: $(ls ~/.claude/commands 2>/dev/null | wc -l)"
echo "Hooks: $(ls ~/.claude/hooks 2>/dev/null | wc -l)"
echo "Agents: $(ls ~/.claude/agents 2>/dev/null | wc -l)"
echo "Knowledge: $(find ~/.claude/knowledge -type f 2>/dev/null | wc -l)"
echo "Tools: $(find ~/.claude/tools -type f -executable 2>/dev/null | wc -l)"

# Find recently modified components
find ~/.claude -type f -mtime -7 | head -10
```

Present findings to user.

## Step 2: Identify Management Task

Ask user:

```
What workspace management task?

1. Create new component (skill/command/hook/tool)
2. Organize existing components (rename/move/categorize)
3. Remove unused components (cleanup/archive)
4. Document existing components (add README/comments)
5. Verify component health (test hooks/tools/commands)
6. Set up new workspace (initialize structure)
```

## Step 3: Execute Based on Choice

### Choice 1: Create New Component

Ask: "What type of component?"

- Skill → Route to /create-agent-skill
- Command → Route to workflows/create-command.md
- Hook → Route to workflows/create-hook.md
- Tool → Route to workflows/create-custom-tool.md
- Knowledge → Route to workflows/curate-knowledge.md

### Choice 2: Organize Existing Components

1. **Identify components to organize:**

   ```bash
   # Find all skills/commands/hooks
   find ~/.claude/{skills,commands,hooks} -mindepth 1 -maxdepth 1 -type d
   ```

2. **Propose organization structure:**

   - Group by purpose (automation, development, documentation, etc.)
   - Group by frequency (daily, weekly, rarely-used)
   - Group by domain (git, system, claude-code, etc.)

3. **Create categories:**

   ```bash
   # Example: Organize skills by domain
   mkdir -p ~/.claude/skills/{automation,development,documentation,system}
   ```

4. **Move components:**

   ```bash
   # Example
   mv ~/.claude/skills/git-helper ~/.claude/skills/development/
   ```

5. **Update references:**
   - Check if moved components are referenced in settings.json
   - Update any hardcoded paths in hooks/commands

### Choice 3: Remove Unused Components

1. **Identify candidates for removal:**

   ```bash
   # Find components not modified in 30+ days
   find ~/.claude/{skills,commands,hooks,tools} -type f -mtime +30
   ```

2. **Check if component is referenced:**

   ```bash
   # Search for references in config
   grep -r "component-name" ~/.claude/settings.json
   grep -r "component-name" ~/.claude/hooks/
   ```

3. **Archive before deleting:**

   ```bash
   # Create archive directory
   mkdir -p ~/.claude/.archived/$(date +%Y-%m-%d)

   # Move to archive (not delete)
   mv ~/.claude/skills/old-skill ~/.claude/.archived/$(date +%Y-%m-%d)/
   ```

4. **Document removal:**
   ```bash
   # Log what was archived and why
   echo "$(date): Archived old-skill - reason: unused for 60+ days" >> ~/.claude/.archived/archive-log.txt
   ```

### Choice 4: Document Existing Components

For each undocumented component:

1. **Create README.md:**

   ```markdown
   # Component Name

   ## Purpose

   What this component does and when to use it.

   ## Usage

   How to invoke/use this component.

   ## Examples

   Concrete examples of usage.

   ## Dependencies

   What this component requires to work.

   ## Maintenance

   How to test/verify this component.
   ```

2. **Add inline comments to code:**

   - Explain non-obvious logic
   - Document expected inputs/outputs
   - Note any limitations or edge cases

3. **Update component metadata:**
   - For skills: Ensure YAML frontmatter is complete
   - For commands: Add description field
   - For hooks: Add header comment explaining trigger

### Choice 5: Verify Component Health

1. **Test hooks:**

   ```bash
   # Manually trigger each hook
   ~/.claude/hooks/SessionStart.sh
   ~/.claude/hooks/PostToolUse.sh
   # Check for errors
   ```

2. **Test commands:**

   ```bash
   # Try each command with sample input
   # Verify expected output
   ```

3. **Test tools:**

   ```bash
   # Run tools with test data
   ~/.claude/tools/workspace-audit --dry-run
   ```

4. **Verify skills:**

   - Read each skill SKILL.md
   - Check for broken file references
   - Ensure workflows/references exist where mentioned

5. **Document failures:**
   ```bash
   # Log broken components
   echo "Hook X fails with error Y" >> ~/.claude/health-check-$(date +%Y-%m-%d).log
   ```

### Choice 6: Set Up New Workspace

1. **Create base structure:**

   ```bash
   mkdir -p ~/.claude/{skills,commands,hooks,agents,knowledge,tools}
   ```

2. **Initialize settings:**

   ```bash
   cat > ~/.claude/settings.json <<'EOF'
   {
     "hooks": {},
     "alwaysThinkingEnabled": true,
     "statusLine": {
       "enabled": false
     }
   }
   EOF
   ```

3. **Create starter knowledge base:**

   ```bash
   mkdir -p ~/.claude/knowledge/{patterns,learnings,domains}

   cat > ~/.claude/knowledge/README.md <<'EOF'
   # Agent Knowledge Base

   Curated knowledge for agent operations.

   - patterns/ - Reusable problem-solving patterns
   - learnings/ - Insights from sessions
   - domains/ - Domain-specific expertise
   EOF
   ```

4. **Install essential skills:**

   - Use /create-agent-skill to build initial skills
   - Or clone from templates

5. **Set up basic hooks:**
   ```bash
   # SessionStart hook - load context
   cat > ~/.claude/hooks/SessionStart.sh <<'EOF'
   #!/usr/bin/env bash
   echo "Loading agent workspace..."
   echo "Active skills: $(ls ~/.claude/skills | wc -l)"
   EOF
   chmod +x ~/.claude/hooks/SessionStart.sh
   ```

## Step 4: Verify Changes

After any workspace change:

1. **Test affected components:**

   - If moved: Verify new paths work
   - If deleted: Verify no broken references
   - If created: Verify component functions

2. **Update documentation:**

   - Add to workspace changelog
   - Update relevant READMEs

3. **Commit changes:**
   ```bash
   cd ~/.claude
   git add .
   git commit -m "workspace: [description of changes]"
   ```
   </process>

<success_criteria>
Workspace management completed when:

- ✓ Current state assessed
- ✓ Management task identified
- ✓ Changes executed successfully
- ✓ Components verified working
- ✓ Documentation updated
- ✓ Changes committed to git
  </success_criteria>
