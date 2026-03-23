# Mocking API

**官方文档**: https://vitest.dev/api/vi.html


## API Reference

Vitest mocking API for functions and modules.

### vi.fn()

Create a mock function.

**Example:**
```typescript
const mockFn = vi.fn()
```

### vi.mock()

Mock a module.

**Example:**
```typescript
vi.mock('./api', () => ({
  fetchData: vi.fn()
}))
```

### vi.spyOn()

Spy on an object method.

**Example:**
```typescript
const spy = vi.spyOn(obj, 'method')
```

### vi.mocked()

Type helper for mocked functions.

**Example:**
```typescript
import { vi } from 'vitest'
import { fetchData } from './api'

vi.mock('./api')
const mockedFetch = vi.mocked(fetchData)
```

### Auto-Mocking

Enable with `globals: true` in config.

**Example:**
```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    globals: true,
  },
})

// test.ts - vi is available globally
const mockFn = vi.fn()
```

### Mock Implementation

```typescript
const mockFn = vi.fn((x) => x + 1)
expect(mockFn(1)).toBe(2)
```

### Mock Return Values

```typescript
const mockFn = vi.fn()
mockFn.mockReturnValue(42)
expect(mockFn()).toBe(42)
```

**See also:** `examples/mocking.md`
