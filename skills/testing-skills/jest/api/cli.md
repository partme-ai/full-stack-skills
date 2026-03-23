# CLI API | CLI API

**官方文档**: https://jestjs.io/docs/cli


## API Reference

Jest CLI commands and options.

### jest

Runs tests.

**Usage:**
```bash
jest
jest [options]
jest [pattern]
```

### Common Options

#### --watch

Runs tests in watch mode.

**Example:**
```bash
jest --watch
```

#### --coverage

Generates coverage report.

**Example:**
```bash
jest --coverage
```

#### --updateSnapshot

Updates snapshots.

**Example:**
```bash
jest --updateSnapshot
```

#### --testNamePattern

Runs tests matching pattern.

**Example:**
```bash
jest --testNamePattern="adds"
```

#### --testPathPattern

Runs tests in files matching pattern.

**Example:**
```bash
jest --testPathPattern="math"
```

#### --maxWorkers

Sets maximum number of workers.

**Example:**
```bash
jest --maxWorkers=4
```

#### --bail

Exit after first test failure.

**Example:**
```bash
jest --bail
```

#### --verbose

Shows individual test results.

**Example:**
```bash
jest --verbose
```

#### --silent

Suppresses console output.

**Example:**
```bash
jest --silent
```

#### --no-cache

Disables cache.

**Example:**
```bash
jest --no-cache
```

### Key Points

- Run `jest` to execute all tests
- Use `--watch` for development
- Use `--coverage` for coverage reports
- Use `--updateSnapshot` to update snapshots
- Use patterns to filter tests
- Use `--bail` to stop on first failure
- Use `--verbose` for detailed output
