# vi Utility

**官方文档**: https://vitest.dev/api/vi.html


## API Reference

Vitest vi utility functions for mocking and testing.

### vi.fn(implementation?)

**Type:** `Function`

Create a mock function.

**Example:**
```typescript
import { vi } from 'vitest'

const mockFn = vi.fn()
mockFn('hello')
expect(mockFn).toHaveBeenCalledWith('hello')
```

### vi.mock(path, factory?)

**Type:** `Function`

Mock a module.

**Example:**
```typescript
import { vi } from 'vitest'

vi.mock('./api', () => ({
  fetchData: vi.fn(() => Promise.resolve({ data: 'test' }))
}))
```

### vi.spyOn(object, method)

**Type:** `Function`

Spy on an object method.

**Example:**
```typescript
import { vi } from 'vitest'

const obj = { method: () => 'original' }
const spy = vi.spyOn(obj, 'method')
obj.method()
expect(spy).toHaveBeenCalled()
```

### vi.waitFor(fn, options?)

**Type:** `Function`

Wait for a condition to be true.

**Example:**
```typescript
import { vi } from 'vitest'

await vi.waitFor(() => {
  expect(element).toBeVisible()
})
```

### vi.waitUntil(fn, options?)

**Type:** `Function`

Wait until a condition is met.

**Example:**
```typescript
import { vi } from 'vitest'

await vi.waitUntil(() => {
  return someCondition()
}, { timeout: 5000 })
```

### vi.clearAllMocks()

**Type:** `Function`

Clear all mocks.

### vi.resetAllMocks()

**Type:** `Function`

Reset all mocks.

### vi.restoreAllMocks()

**Type:** `Function`

Restore all mocks.

**See also:** `examples/mocking.md`
