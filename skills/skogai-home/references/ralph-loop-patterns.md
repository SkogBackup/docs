# Ralph Loop Patterns - Self-Improvement Through Iteration

## What is Ralph?

Ralph Wiggum is a technique for iterative AI development using self-referential feedback loops. Named after The Simpsons character, it embodies persistent iteration despite setbacks.

### Core Concept

A Ralph loop is implemented via a **Stop hook** that intercepts Claude's session exit:

```bash
# You run ONCE:
/ralph-loop "Your task" --completion-promise "DONE"

# Claude automatically:
# 1. Works on task
# 2. Tries to exit
# 3. Stop hook blocks exit
# 4. Stop hook feeds same prompt back
# 5. Repeat until completion
```

The loop happens **inside your current session** - no external bash loops needed.

### Self-Referential Feedback

Key properties:

- **Prompt never changes** between iterations
- **Previous work persists in files**
- **Each iteration sees modified files** and git history
- **Claude autonomously improves** by reading its own past work

## Pattern 1: Test-Driven Improvement

**Use case:** Improve code quality through automated testing

```bash
/ralph-loop "Implement feature X with TDD:
1. Write failing test
2. Implement minimal code to pass
3. Run tests
4. If failures: debug and fix
5. Refactor for clarity
6. Repeat until all tests pass
7. Output <promise>TESTS_PASS</promise>

Success criteria:
- All tests pass
- Coverage > 80%
- No linter warnings

Max iterations: 25" \
--max-iterations 25 \
--completion-promise "TESTS_PASS"
```

**Why it works:**

- Test output provides clear feedback
- Each iteration sees test results in files
- Objective success criteria (tests pass)

## Pattern 2: Incremental Feature Building

**Use case:** Build complex features step-by-step

```bash
/ralph-loop "Build REST API for todos:

Phase 1: Basic CRUD
- GET /todos (list)
- POST /todos (create)
- Tests pass

Phase 2: Validation
- Input validation
- Error responses
- Tests pass

Phase 3: Persistence
- Database integration
- Migration scripts
- Tests pass

After each phase: commit, tag, document
Output <promise>COMPLETE</promise> when all phases done.

Max iterations: 50" \
--max-iterations 50 \
--completion-promise "COMPLETE"
```

**Why it works:**

- Clear incremental goals
- Each phase builds on previous
- Progress persists in git history

## Pattern 3: Documentation Completeness

**Use case:** Ensure documentation covers all features

```bash
/ralph-loop "Complete API documentation:

For each endpoint in src/routes/:
1. Check if documented in docs/api.md
2. If missing: add section with:
   - Purpose
   - Parameters
   - Example request/response
   - Error cases
3. Verify example works
4. Mark endpoint as documented

When all endpoints documented:
Output <promise>DOCS_COMPLETE</promise>

Max iterations: 20" \
--max-iterations 20 \
--completion-promise "DOCS_COMPLETE"
```

**Why it works:**

- Checklist of endpoints is finite
- Each iteration adds documentation
- Can verify completeness objectively

## Pattern 4: Bug Hunt and Fix

**Use case:** Systematically eliminate bugs

```bash
/ralph-loop "Fix all test failures:

1. Run test suite
2. Pick first failing test
3. Read test and code
4. Identify root cause
5. Implement fix
6. Re-run tests
7. If test passes: move to next failure
8. If test fails: try different approach

When all tests pass:
Output <promise>BUGS_FIXED</promise>

Max iterations: 30" \
--max-iterations 30 \
--completion-promise "BUGS_FIXED"
```

**Why it works:**

- Test output guides debugging
- Progress measured by passing tests
- Systematic approach prevents thrashing

## Pattern 5: Skill Improvement

**Use case:** Improve agent skills through iteration

```bash
/ralph-loop "Improve create-custom-tool skill:

Issues identified:
- Workflow has ambiguous steps
- Missing examples for common cases
- No error handling guidance

Improvements:
1. Read workflows/create-custom-tool.md
2. Add examples for each step
3. Add decision trees for choices
4. Add error handling section
5. Test by walking through workflow
6. Document changes

Success criteria:
- All steps have examples
- Decision points have guidance
- Error cases covered

Output <promise>IMPROVED</promise> when done.

Max iterations: 15" \
--max-iterations 15 \
--completion-promise "IMPROVED"
```

**Why it works:**

- Clear improvement targets
- Can verify by reading result
- Focused scope prevents endless iteration

## Anti-Patterns to Avoid

### ❌ Vague Success Criteria

```bash
# BAD
/ralph-loop "Make the code better"
```

**Problem:** No way to know when "better" is achieved
**Fix:** Define measurable criteria

```bash
# GOOD
/ralph-loop "Improve code quality:
- All linter warnings resolved
- Test coverage > 80%
- No functions > 50 lines
Output <promise>DONE</promise>"
```

### ❌ No Escape Hatch

```bash
# BAD
/ralph-loop "Fix all bugs" --max-iterations 1000
```

**Problem:** May never complete, wastes resources
**Fix:** Reasonable iteration limit + blocked handling

```bash
# GOOD
/ralph-loop "Fix critical bugs (P0/P1 priority):
- After 20 iterations, if not done:
  - Document remaining bugs
  - Estimate effort for each
  - Suggest alternative approaches
Output <promise>DONE</promise>" \
--max-iterations 20
```

### ❌ Task Requires Human Judgment

```bash
# BAD
/ralph-loop "Design the perfect UX"
```

**Problem:** "Perfect" is subjective, no objective criteria
**Fix:** Use Ralph for implementation, not design

```bash
# GOOD (after human design decision)
/ralph-loop "Implement approved UX design from mockups/:
- All components match mockups
- Responsive on mobile/desktop
- Accessibility score > 90
Output <promise>DONE</promise>"
```

### ❌ One-Shot Operation

```bash
# BAD
/ralph-loop "Rename function foo to bar"
```

**Problem:** Single operation doesn't benefit from iteration
**Fix:** Just do it directly, no loop needed

## Success Indicators

A well-designed Ralph loop has:

- **Clear, measurable success criteria** - Can objectively determine completion
- **Escape hatch** - Max iterations with blocked-state handling
- **Incremental progress** - Each iteration moves toward goal
- **Automated verification** - Tests, linters, or other automated checks
- **Appropriate scope** - Not too narrow (one-shot), not too broad (endless)
- **Persistence** - Work saved to files between iterations

## When to Use Ralph

**✓ Good for:**

- Test-driven development
- Incremental feature building
- Systematic bug fixing
- Documentation completeness
- Code quality improvements
- Refactoring with tests

**✗ Not good for:**

- Design decisions requiring human judgment
- One-shot operations
- Tasks without clear success criteria
- Production debugging (use targeted debugging)
- Exploratory tasks (use exploration, then implement with Ralph)

## Monitoring Progress

During a Ralph loop, watch for:

### Healthy Progress

- ✓ Test passes increase each iteration
- ✓ Different approaches tried when stuck
- ✓ Clear progress toward completion
- ✓ Reasonable iteration count

### Unhealthy Patterns

- ✗ Same error repeated across iterations
- ✗ Rapid completion without real progress
- ✗ Max iterations reached without progress
- ✗ Changes that move away from goal

Use `/cancel-ralph` if loop shows unhealthy patterns, then adjust prompt.

## Real-World Results

Geoffrey Huntley's experience with Ralph:

- **6 repositories** generated overnight during Y Combinator hackathon testing
- **$50k contract** completed for $297 in API costs
- **"cursed" programming language** created over 3 months using this approach

The technique proves that:

- Iteration beats perfection
- Operator skill (prompt writing) matters more than model alone
- Persistence wins on well-defined tasks
- Automated verification enables autonomous improvement

## Learn More

- Original technique: https://ghuntley.com/ralph/
- Ralph Orchestrator: https://github.com/mikeyobrien/ralph-orchestrator
- Philosophy: "Ralph is deterministically bad" - failures are predictable and fixable
