# Testing Patterns

**Analysis Date:** 2026-01-09

## Test Framework

**Runner:**
- Not applicable (documentation repository)
- No automated test suite

**Validation:**
- Manual review of documents
- YAML frontmatter must be valid syntax
- Cross-references should resolve

## Validation Patterns

**Frontmatter Validation:**
- Check YAML syntax is valid
- Verify required fields present (`title`, `type`)
- Ensure consistent field naming

**Reference Validation:**
- `@-notation` paths may point to external systems
- Internal links should resolve
- Symlinks should have valid targets

**Prompt Validation:**
- Verify Objective/Inputs/Output/Prompt structure
- Check variable substitution format (`$name`)
- Test with actual LLM execution

## Quality Checks

**Pre-commit (Manual):**
1. YAML frontmatter parses correctly
2. File follows naming conventions
3. Required sections present in prompts
4. No broken internal links

**Review Checklist:**
- [ ] Frontmatter complete and valid
- [ ] File named with kebab-case
- [ ] Prompt has all sections (Objective, Inputs, Expected Output, Prompt)
- [ ] Examples provided where appropriate
- [ ] No duplicate content across files

## Coverage

**Requirements:**
- No automated coverage tracking
- Focus on completeness over metrics

**Current Gaps:**
- Many directories missing README.md
- Some prompts incomplete (see CONCERNS.md)
- Cross-references to external systems unvalidated

## Test Types

**Manual Validation:**
- Review documents for structure and completeness
- Test prompts with actual LLM execution
- Verify cross-references resolve

**Integration Testing:**
- Test prompts with target LLM (OpenRouter, OpenAI)
- Verify output format matches Expected Output
- Check variable substitution works

## Common Patterns

**Prompt Testing:**
```bash
# Manual test of prompt with LLM
# 1. Copy prompt content
# 2. Substitute variables ($title, $name, etc.)
# 3. Execute with target LLM
# 4. Compare output to Expected Output spec
```

**Frontmatter Validation:**
```bash
# Check YAML syntax
head -20 document.md | grep -A 20 '---' | head -n -1 | tail -n +2
# Should parse as valid YAML
```

---

*Testing analysis: 2026-01-09*
*Update when test patterns change*
