# Pruning to Production

<objective>
Transform working explosive-phase code into production-ready implementation through systematic pruning and refinement.
</objective>

<when_to_use>
- MVP works, but code is messy
- Ready to remove failed experiments
- Need to extract the 50% that actually matters
- Preparing for .skogai/claude/ migration
</when_to_use>

<mindset_shift>

**Explosive Phase:** "Does it work?"
**Pruning Phase:** "What can I remove while keeping it working?"

The goal is SUBTRACTION, not addition.

</mindset_shift>

<process>

## 1. Identify What Actually Works

Map out which parts of the explosive code are:
- Actually used vs theoretical
- Core functionality vs nice-to-have
- Simple effective solutions vs over-engineered attempts

Ask: "If I removed this, would core functionality break?"
- Yes → keep
- No → candidate for removal

## 2. Remove Failed Experiments

Delete:
- Approaches that didn't work
- Duplicate implementations
- Over-abstracted code that added complexity
- Verbose docs explaining failed approaches
- Theoretical features never actually needed

Be ruthless. If you're not sure it's needed, it probably isn't.

## 3. Consolidate

Merge similar patterns:
- Multiple similar functions → one well-designed function
- Scattered docs → focused single-source-of-truth
- Redundant files → minimal essential structure

## 4. Simplify

Apply anti-bloat principles:
- Remove unnecessary abstractions
- Inline single-use functions
- Cut verbose explanations down to essence
- Remove "just in case" code

## 5. Test Coverage

Now add tests:
- Only for functionality that stayed
- Focus on core workflows
- Don't test removed experiments

## 6. Document Minimally

Write docs that:
- Explain WHY, not WHAT (code should be self-documenting)
- Focus on non-obvious decisions
- Point to related concepts (progressive disclosure)
- Remove step-by-step explanations for obvious code

</process>

<anti_patterns>

**Don't do this:**
- Keep "just in case" code "because it might be useful later"
- Add more features during pruning
- Try to make failed experiments work
- Document everything comprehensively
- Preserve all historical approaches

**Do this:**
- Delete failed experiments completely
- Focus on what works
- Trust git history for archeology
- Minimal targeted docs
- Preserve only successful patterns

</anti_patterns>

<concrete_example>

**Before pruning (explosive):**
```
.skogai/skogix/src/routing/
├── attempt-1-tree-structure.md (failed - unreadable)
├── attempt-2-flat-list.md (failed - too long)
├── attempt-3-progressive.md (works!)
├── helpers.sh (unused)
├── experimental-viz.py (interesting but not needed)
└── docs/
    ├── design-decisions.md (verbose, historical)
    ├── api-reference.md (over-documented)
    └── examples/ (10 examples, 2 actually useful)
```

**After pruning (production-ready):**
```
.skogai/claude/skills/skogai-routing/
├── SKILL.md (progressive disclosure pattern only)
└── references/
    └── routing-examples.md (2 key examples)
```

Reduced from 10 files to 2. Lost nothing of value.

</concrete_example>

<functional_first>

Apply F# principles:
- Pure functions over stateful objects
- Immutable data structures
- Function composition
- Type signatures as documentation
- Simple data transformations

If code is getting complex, simplify the data model.

</functional_first>

<success_criteria>

You've successfully pruned when:
- Code is 30-50% smaller but functionality unchanged
- Can explain every remaining line's purpose
- No "just in case" code remains
- Tests cover core workflows
- Docs are minimal but sufficient
- Ready to move to .skogai/claude/

</success_criteria>

<next_step>
When pruned and polished: `@workflows/migration-path.md`
</next_step>
