# Start Ralph Loop - Self-Improvement Workflow

<required_reading>
Before starting, read:

- references/ralph-loop-patterns.md
- references/improvement-metrics.md
  </required_reading>

<process>
## Step 1: Define Improvement Goal

Ask user:

```
What capability do you want to improve?

Common improvement targets:
- Skill effectiveness (better prompts, clearer workflows)
- Tool reliability (handle edge cases, better error messages)
- Knowledge completeness (fill gaps, update outdated info)
- Hook robustness (handle failures gracefully)
- Command usability (clearer output, better UX)
```

Record the target component and desired outcome.

## Step 2: Establish Success Criteria

Create clear, measurable criteria:

**For skills:**

- Solves X problem in Y steps or fewer
- Provides correct guidance Z% of the time
- Users can complete task without asking questions

**For tools:**

- Handles all input types correctly
- Provides helpful error messages
- Completes in reasonable time
- Works in all expected environments

**For knowledge:**

- Covers all key concepts in domain
- Examples work without modification
- References are current and accessible
- No contradictions or outdated info

**For hooks/commands:**

- Runs without errors
- Provides useful output
- Handles edge cases gracefully
- Minimal latency impact

## Step 3: Create Improvement Prompt

Write prompt following Ralph best practices:

```markdown
Improve [component-name] to achieve [goal].

Current state:

- [What exists now]
- [Known issues]
- [Limitations]

Target state:

- [Specific improvements]
- [Success criteria]
- [Acceptance tests]

Workflow:

1. Read current implementation
2. Identify specific improvements
3. Implement changes
4. Test changes
5. Document what was improved
6. If all criteria met: Output <promise>COMPLETE</promise>
7. If blocked after 15 iterations: Document blockers and suggest alternatives

Max iterations: 20
```

## Step 4: Start Ralph Loop

Execute:

```bash
/ralph-loop "$(cat improvement-prompt.md)" \
  --max-iterations 20 \
  --completion-promise "COMPLETE"
```

## Step 5: Monitor Progress

Watch for:

- Repeated failed attempts (prompt may be unclear)
- Quick completion (success criteria may be too easy)
- Max iterations reached (task may be too complex)
- Unexpected behavior (may need to cancel and adjust)

Use `/cancel-ralph` if loop needs adjustment.

## Step 6: Extract Learnings

After completion, document:

1. **What worked** - Effective techniques, good prompts
2. **What didn't** - Failed approaches, unclear criteria
3. **Patterns discovered** - Reusable insights
4. **Next improvements** - Follow-up work identified

Store in `~/.claude/knowledge/improvement-logs/[date]-[component].md`

## Step 7: Update Component Documentation

Ensure improved component has:

- Clear description of what changed
- Why changes were made
- How to verify improvements
- Known limitations (if any remain)
  </process>

<examples>
## Example 1: Improve Skill Workflow Clarity

```bash
/ralph-loop "Improve the create-custom-tool skill workflow.

Current: Workflow exists but users ask clarifying questions mid-execution.
Target: Users complete workflow without questions 95% of time.

Tasks:
1. Read workflows/create-custom-tool.md
2. Identify ambiguous steps
3. Add examples for each step
4. Add decision trees for common choices
5. Test by walking through workflow mentally
6. Output <promise>COMPLETE</promise> when clarity achieved

Max iterations: 15" \
--max-iterations 15 \
--completion-promise "COMPLETE"
```

## Example 2: Make Tool More Robust

```bash
/ralph-loop "Make workspace-audit tool handle edge cases.

Current: Fails on missing directories, empty files, broken symlinks.
Target: Handles all edge cases gracefully with helpful messages.

Tasks:
1. Read scripts/workspace-audit.sh
2. Test with edge case inputs
3. Add error handling for each failure mode
4. Add helpful error messages
5. Test all edge cases pass
6. Output <promise>COMPLETE</promise> when robust

Test cases:
- Missing ~/.claude/ directory
- Empty skill directories
- Broken symlinks
- Permission denied errors
- Large files (>1MB)

Max iterations: 20" \
--max-iterations 20 \
--completion-promise "COMPLETE"
```

## Example 3: Update Outdated Knowledge

```bash
/ralph-loop "Update claude-code-features knowledge base.

Current: Last updated 2024-09-15, missing new features.
Target: Complete and current as of today.

Tasks:
1. Read references/claude-code-features.md
2. Check official docs for changes since 2024-09-15
3. Add new features with examples
4. Update deprecated/removed features
5. Verify all examples still work
6. Update 'last_updated' date
7. Output <promise>COMPLETE</promise> when current

Max iterations: 10" \
--max-iterations 10 \
--completion-promise "COMPLETE"
```

</examples>

<success_criteria>
Ralph loop completed when:

- ✓ Clear improvement goal defined
- ✓ Measurable success criteria established
- ✓ Well-structured prompt created
- ✓ Loop completed or reached max iterations
- ✓ Learnings documented
- ✓ Component documentation updated
- ✓ Improvement is verifiable
  </success_criteria>

<troubleshooting>
## Loop Not Making Progress

**Symptoms:** Same errors repeated across iterations
**Fix:** Cancel and make prompt more specific about how to debug

## Loop Completes Too Fast

**Symptoms:** Outputs promise without real improvement
**Fix:** Add verification steps and objective tests to prompt

## Loop Hits Max Iterations

**Symptoms:** Reaches limit without completion
**Fix:** Task too complex - break into smaller improvements or increase limit

## Loop Makes Wrong Changes

**Symptoms:** Changes that don't align with goal
**Fix:** Add explicit constraints and examples of desired vs undesired changes
</troubleshooting>
