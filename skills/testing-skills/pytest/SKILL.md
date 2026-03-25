---
name: pytest
description: "Provides comprehensive guidance for pytest testing framework including test writing, fixtures, parametrization, mocking, and plugins. Use when the user asks about pytest, needs to write Python tests, use pytest fixtures, or configure pytest for Python projects."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write and run Python unit tests with pytest
- Use fixtures for test setup, teardown, and dependency injection
- Parametrize tests to run with multiple input sets
- Mock dependencies with `pytest-mock` or `unittest.mock`
- Configure pytest via `pytest.ini`, `pyproject.toml`, or `conftest.py`
- Generate coverage reports with `pytest-cov`
- Run tests in parallel with `pytest-xdist`

## How to use this skill

### Workflow

1. **Write test functions** with `test_` prefix or `Test` class
2. **Use fixtures** in `conftest.py` for shared setup and dependency injection
3. **Run tests** with `pytest` CLI, applying markers and filters as needed
4. **Analyze results** with coverage and reporting plugins

### 1. Basic Test

```python
def test_addition():
    assert 1 + 1 == 2

def test_string_upper():
    assert "hello".upper() == "HELLO"
```

### 2. Fixtures

```python
import pytest

@pytest.fixture
def sample_user():
    return {"name": "Alice", "email": "alice@example.com"}

def test_user_name(sample_user):
    assert sample_user["name"] == "Alice"

@pytest.fixture(autouse=True)
def reset_database(db):
    db.clear()
    yield
    db.clear()
```

### 3. Parametrize

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    ("hello", 5),
    ("", 0),
    ("pytest", 6),
])
def test_string_length(input, expected):
    assert len(input) == expected
```

### 4. Mocking

```python
def test_api_call(mocker):
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.json.return_value = {"status": "ok"}

    result = fetch_status()
    assert result == "ok"
    mock_get.assert_called_once()
```

### 5. Running Tests

```bash
# Run all tests
pytest

# Verbose with pattern filter
pytest -v -k "test_user"

# With coverage
pytest --cov=mypackage --cov-report=html

# Parallel execution
pytest -n auto
```

## Best Practices

- Keep tests independent with no shared mutable state; use fixtures for setup and teardown
- Use clear, descriptive test names that explain the expected behavior
- Avoid depending on test execution order; use `conftest.py` for shared fixtures
- Run the full test suite in CI; use `--cov` for coverage and `--maxfail=1` to fail fast
- Use markers (`@pytest.mark.slow`) to categorize tests and run subsets

## Resources

- Official documentation: https://docs.pytest.org/
- pytest-cov: https://pytest-cov.readthedocs.io/
- pytest-xdist: https://github.com/pytest-dev/pytest-xdist

## Keywords

pytest, Python testing, fixtures, parametrize, mocking, conftest, coverage, pytest-cov, pytest-xdist, unit testing, markers
