# Test API

**官方文档**: https://vitest.dev/api/


## Instructions

This example demonstrates Vitest test API.

### Key Concepts

- test() and it()
- describe()
- Hooks
- Test modifiers

### Example: Basic Test

```typescript
import { test, expect } from 'vitest'

test('adds numbers', () => {
  expect(1 + 1).toBe(2)
})
```

### Example: Using it()

```typescript
import { it, expect } from 'vitest'

it('should work', () => {
  expect(true).toBe(true)
})
```

### Example: describe() Blocks

```typescript
import { describe, it, expect } from 'vitest'

describe('Math', () => {
  it('adds', () => {
    expect(1 + 1).toBe(2)
  })

  it('multiplies', () => {
    expect(2 * 3).toBe(6)
  })
})
```

### Example: Hooks

```typescript
import { describe, it, expect, beforeAll, beforeEach, afterEach, afterAll } from 'vitest'

describe('Database', () => {
  beforeAll(() => {
    // Run once before all tests
  })

  beforeEach(() => {
    // Run before each test
  })

  afterEach(() => {
    // Run after each test
  })

  afterAll(() => {
    // Run once after all tests
  })
})
```

### Example: Test Modifiers

```typescript
import { describe, it, expect } from 'vitest'

describe('Tests', () => {
  it.skip('skipped test', () => {
    // This test is skipped
  })

  it.only('only this runs', () => {
    // Only this test runs
  })

  it.todo('todo test', () => {
    // Marked as todo
  })
})
```

### Example: Test Options

```typescript
import { test, expect } from 'vitest'

test('with timeout', async () => {
  // Test with custom timeout
}, { timeout: 5000 })

test('with retries', () => {
  // Retry on failure
}, { retry: 3 })
```

### Key Points

- test() and it() are aliases
- Use describe() to group tests
- Hooks for setup/teardown
- Modifiers: skip, only, todo
- Configure timeout and retries
