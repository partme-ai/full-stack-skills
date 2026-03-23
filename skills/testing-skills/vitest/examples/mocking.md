# Mocking

**官方文档**: https://vitest.dev/guide/mocking.html


## Instructions

This example demonstrates mocking in Vitest.

### Key Concepts

- vi.fn()
- vi.mock()
- vi.spyOn()
- Auto-mocking

### Example: Mock Functions

```typescript
import { describe, it, expect, vi } from 'vitest'

describe('Mocking', () => {
  it('mocks a function', () => {
    const mockFn = vi.fn()
    mockFn('hello')
    expect(mockFn).toHaveBeenCalledWith('hello')
  })
})
```

### Example: Mock Implementation

```typescript
import { describe, it, expect, vi } from 'vitest'

const mockFn = vi.fn((x) => x + 1)
expect(mockFn(1)).toBe(2)
```

### Example: Mock Modules

```typescript
// __mocks__/api.ts
export const fetchData = vi.fn(() => Promise.resolve({ data: 'test' }))

// api.test.ts
import { vi } from 'vitest'
import { fetchData } from './api'

vi.mock('./api')

it('mocks module', async () => {
  const data = await fetchData()
  expect(data).toEqual({ data: 'test' })
})
```

### Example: Spy On

```typescript
import { describe, it, expect, vi } from 'vitest'

const obj = {
  method: () => 'original'
}

const spy = vi.spyOn(obj, 'method')
obj.method()
expect(spy).toHaveBeenCalled()
```

### Example: Auto-Mocking

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    globals: true,
  },
})

// test.ts
// vi is available globally
const mockFn = vi.fn()
```

### Key Points

- Use vi.fn() for function mocks
- Use vi.mock() for module mocks
- Use vi.spyOn() to spy on methods
- Auto-mocking with globals: true
- Reset mocks with vi.clearAllMocks()
