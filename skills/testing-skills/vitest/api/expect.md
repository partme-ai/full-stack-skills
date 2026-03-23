# Expect API

**官方文档**: https://vitest.dev/api/expect.html


## API Reference

Vitest expect assertions and matchers.

### expect(actual)

**Type:** `Function`

Create an expectation.

**Example:**
```typescript
import { expect } from 'vitest'

expect(1 + 1).toBe(2)
```

### Matchers

#### toBe(expected)

Strict equality (===).

**Example:**
```typescript
expect(1).toBe(1)
```

#### toEqual(expected)

Deep equality.

**Example:**
```typescript
expect({ a: 1 }).toEqual({ a: 1 })
```

#### toMatchSnapshot()

Match snapshot.

**Example:**
```typescript
expect(data).toMatchSnapshot()
```

#### toMatchInlineSnapshot()

Match inline snapshot.

**Example:**
```typescript
expect(data).toMatchInlineSnapshot(`{ "a": 1 }`)
```

#### toBeTruthy()

Check if value is truthy.

#### toBeFalsy()

Check if value is falsy.

#### toContain(item)

Check if array/string contains item.

**Example:**
```typescript
expect([1, 2, 3]).toContain(2)
expect('hello').toContain('ell')
```

#### toHaveBeenCalled()

Check if mock was called.

#### toHaveBeenCalledWith(...args)

Check if mock was called with args.

**Example:**
```typescript
const mockFn = vi.fn()
mockFn('hello', 'world')
expect(mockFn).toHaveBeenCalledWith('hello', 'world')
```

### Custom Matchers

```typescript
expect.extend({
  toBeWithinRange(received, floor, ceiling) {
    const pass = received >= floor && received <= ceiling
    return {
      message: () => `expected ${received} to be within range`,
      pass,
    }
  },
})
```

**See also:** `examples/test-api.md`, `examples/snapshots.md`
