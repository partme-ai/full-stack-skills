# Test API

**官方文档**: https://vitest.dev/api/


## API Reference

Vitest test API functions and options.

### test(name, fn, options?)

**Type:** `Function`

Create a test case.

**Parameters:**
- `name` - Test name (string)
- `fn` - Test function
- `options` - Test options (optional)

**Example:**
```typescript
import { test, expect } from 'vitest'

test('adds numbers', () => {
  expect(1 + 1).toBe(2)
})
```

### it(name, fn, options?)

**Type:** `Function`

Alias for `test()`.

**Example:**
```typescript
import { it, expect } from 'vitest'

it('works', () => {
  expect(true).toBe(true)
})
```

### describe(name, fn)

**Type:** `Function`

Group related tests.

**Example:**
```typescript
import { describe, it, expect } from 'vitest'

describe('Math', () => {
  it('adds', () => {
    expect(1 + 1).toBe(2)
  })
})
```

### Hooks

#### beforeAll(fn)

Run before all tests in suite.

#### beforeEach(fn)

Run before each test.

#### afterEach(fn)

Run after each test.

#### afterAll(fn)

Run after all tests in suite.

**Example:**
```typescript
import { describe, it, beforeAll, beforeEach } from 'vitest'

describe('Suite', () => {
  beforeAll(() => {
    // Setup
  })

  beforeEach(() => {
    // Per-test setup
  })
})
```

### Test Modifiers

#### test.skip(name, fn)

Skip this test.

#### test.only(name, fn)

Run only this test.

#### test.todo(name)

Mark test as todo.

**Example:**
```typescript
test.skip('skipped', () => {})
test.only('only this', () => {})
test.todo('todo test')
```

### Test Options

- `timeout` - Test timeout in ms
- `retry` - Number of retries
- `repeat` - Repeat test N times

**See also:** `examples/test-api.md`
