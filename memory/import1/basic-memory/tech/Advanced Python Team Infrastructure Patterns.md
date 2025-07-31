---
title: Advanced Python Team Infrastructure Patterns
type: note
permalink: tech/advanced-python-team-infrastructure-patterns
tags:
- '["python"'
- '"testing"'
- '"infrastructure"'
- '"patterns"'
- '"advanced"]'
---

# Advanced Python Team Infrastructure Patterns

## Pytest Advanced Configuration Patterns

### conftest.py Architecture
**Fixture Hierarchy for Team Testing**:
```python
@pytest.fixture(scope="session")
def test_data_dir() -> Path:
    """Session-wide test data directory"""

@pytest.fixture  
def temp_dir() -> Generator[Path, None, None]:
    """Per-test temporary directory with cleanup"""

@pytest.fixture
def isolated_config(temp_config_dir: Path, mock_config: Dict[str, Any]):
    """Isolated configuration for tests with patching"""
    # Creates config file + patches config directory getter
    with patch('skogcli.settings.get_config_dir', return_value=temp_config_dir):
        yield config_file
```

**Automatic Test Categorization**:
```python
def pytest_collection_modifyitems(config, items):
    """Auto-add markers based on directory structure"""
    for item in items:
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
```

**Mock Response Pattern for External APIs**:
```python
class MockResponse:
    def __init__(self, json_data: Dict[str, Any], status_code: int = 200):
        self.json_data = json_data
        self.status_code = status_code
    
    def json(self):
        return self.json_data

@pytest.fixture
def mock_http_requests():
    with patch('requests.post') as mock_post:
        mock_post.return_value = MockResponse({
            "choices": [{"message": {"content": "Generated code here"}}]
        })
        yield {'post': mock_post}
```

## GitHub Actions Advanced Patterns

### Matrix Testing with Artifact Coordination
```yaml
test-suite:
  strategy:
    matrix:
      test-type: [unit, integration, functional]
  steps:
    - name: Run ${{ matrix.test-type }} tests
      run: pytest tests/${{ matrix.test-type }}/ -m "${{ matrix.test-type }}"
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        flags: ${{ matrix.test-type }}
```

### Automated PR Review Checklist Injection
```yaml
- name: Add review checklist
  uses: actions/github-script@v6
  with:
    script: |
      const body = `## 🔍 Code Review Checklist...`;
      github.rest.issues.createComment({
        issue_number: context.issue.number,
        body: body
      });
```

### Quality Gate Coordination
```yaml
review-requirements:
  needs: [code-quality, test-suite, documentation, commit-quality]
  if: always()
  steps:
    - name: Check all requirements
      run: |
        if [ "${{ needs.code-quality.result }}" != "success" ]; then
          echo "❌ Quality gates failed"
          exit 1
        fi
```

## MkDocs Advanced Configuration

### Plugin Chain for API Documentation
```yaml
plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          options:
            docstring_style: google
            show_source: true
            merge_init_into_class: true
  - gen-files:
      scripts:
        - docs/scripts/gen_ref_pages.py
  - literate-nav:
      nav_file: SUMMARY.md
  - autorefs
```

### Theme Configuration for Team Branding
```yaml
theme:
  name: material
  palette:
    - scheme: default
      primary: deep purple
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
  features:
    - navigation.tabs.sticky
    - navigation.sections
    - content.code.copy
    - search.highlight
```

## pyproject.toml Advanced Patterns

### Tool Configuration Consolidation
```toml
[tool.pytest.ini_options]
addopts = "-ra -q --strict-markers --strict-config --cov=skogcli"
markers = [
    "slow: marks tests as slow running",
    "integration: marks tests as integration tests",
    "benchmark: marks tests as benchmarks",
]
filterwarnings = [
    "error",
    "ignore::UserWarning",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if __name__ == .__main__.:",
    "@(abc\\.)?abstractmethod",
]

[tool.commitizen]
name = "cz_conventional_commits"
tag_format = "v$version"
bump_message = "bump: version $current_version → $new_version"

[tool.semantic_release]
version_toml = ["pyproject.toml:project.version"]
upload_to_repository = true
build_command = "python -m build"
```

### Dependency Group Strategy
```toml
[project.optional-dependencies]
dev = ["black>=24.0.0", "ruff>=0.1.0", "mypy>=1.8.0", ...]
docs = ["mkdocs>=1.5.0", "mkdocs-material>=9.4.0", ...]
testing = ["pytest>=8.0.0", "hypothesis>=6.90.0", ...]
team = ["commitizen>=3.13.0", "python-semantic-release>=8.0.0", ...]
monitoring = ["structlog>=24.0.0", "sentry-sdk>=1.40.0", ...]
```

## Makefile Team Automation

### Progressive Onboarding Commands
```makefile
team-setup: dev-install
	@echo "Setting up team development environment..."
	pre-commit install
	@echo "Team setup complete! 🚀"

onboard: team-setup
	@echo "🎉 Welcome to the SkogCLI team!"
	@echo "Next steps:"
	@echo "1. Read ONBOARDING.md"
	@echo "4. Start mkdocs server: 'make docs-serve'"
```

### Quality Gate Coordination
```makefile
check: all-checks test
	@echo "Ready to commit! 🚀"

ci: clean dev-install all-checks test-cov
	@echo "CI checks complete! ✅"
```

## Advanced Testing Patterns

### Functional Test User Journey Simulation
```python
def test_developer_workflow(cli_runner, mock_environment, isolated_config):
    """Test complete developer workflow from setup to daily use."""
    # Developer first-time setup
    version_check = cli_runner.invoke(app, ["version"])
    
    # Developer configures environment
    config_setup = [
        cli_runner.invoke(app, ["config", "set", "user.name", "Developer"]),
        cli_runner.invoke(app, ["config", "backup"])
    ]
    
    # Developer creates utility script
    create_attempt = cli_runner.invoke(app, [
        "script", "create", "dev_utils", "--no-edit"
    ])
```

### Parametrized Testing for Edge Cases
```python
@pytest.mark.parametrize("version,expected", [
    (0, True),   # Should migrate
    (1, False),  # Current version
    (2, False),  # Future version
])
def test_version_based_migration(self, version, expected):
    config = {"settings": {"meta": {"version": version}}}
    result = migrate_config(config)
    # Assertions based on expected behavior
```

## Team Documentation Architecture

### Progressive Disclosure Pattern
```
ONBOARDING.md:
  - 15-minute quick start
  - Week 1-3 learning path
  - Success metrics

TEAM_STANDARDS.md:
  - Code style examples
  - Testing patterns
  - Review guidelines
  
Development docs:
  - Architecture decisions
  - Troubleshooting guides
  - Performance considerations
```

These patterns create **enterprise-grade team development infrastructure** that scales from individual contributors to large distributed teams.