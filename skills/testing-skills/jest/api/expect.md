# expect API | expect API

**官方文档**: https://jestjs.io/docs/expect


## API Reference

The `expect()` function and all available matchers.

### expect()

Creates an expectation for a value.

**Signature:**
```typescript
function expect(value: any): Expect
```

**Example:**
```javascript
expect(value).toBe(4);
expect(value).toEqual({ name: 'John' });
```

### Common Matchers

#### toBe()

Uses Object.is for exact equality.

**Example:**
```javascript
expect(2 + 2).toBe(4);
expect('hello').toBe('hello');
```

#### toEqual()

Checks value equality for objects and arrays.

**Example:**
```javascript
expect({ a: 1 }).toEqual({ a: 1 });
expect([1, 2, 3]).toEqual([1, 2, 3]);
```

#### toBeNull()

Matches only null.

**Example:**
```javascript
expect(null).toBeNull();
```

#### toBeUndefined()

Matches only undefined.

**Example:**
```javascript
expect(undefined).toBeUndefined();
```

#### toBeDefined()

Opposite of toBeUndefined.

**Example:**
```javascript
expect('value').toBeDefined();
```

#### toBeTruthy()

Matches anything that if statement treats as true.

**Example:**
```javascript
expect(1).toBeTruthy();
expect(true).toBeTruthy();
```

#### toBeFalsy()

Matches anything that if statement treats as false.

**Example:**
```javascript
expect(0).toBeFalsy();
expect(false).toBeFalsy();
```

### Number Matchers

#### toBeGreaterThan()

**Example:**
```javascript
expect(5).toBeGreaterThan(3);
```

#### toBeGreaterThanOrEqual()

**Example:**
```javascript
expect(5).toBeGreaterThanOrEqual(5);
```

#### toBeLessThan()

**Example:**
```javascript
expect(3).toBeLessThan(5);
```

#### toBeLessThanOrEqual()

**Example:**
```javascript
expect(3).toBeLessThanOrEqual(3);
```

#### toBeCloseTo()

For floating point equality.

**Example:**
```javascript
expect(0.1 + 0.2).toBeCloseTo(0.3);
```

### String Matchers

#### toMatch()

Matches against a string or regex.

**Example:**
```javascript
expect('Hello World').toMatch(/World/);
expect('Hello World').toMatch('World');
```

#### toContain()

Checks if string or array contains value.

**Example:**
```javascript
expect('Hello World').toContain('World');
expect([1, 2, 3]).toContain(2);
```

### Array Matchers

#### toContain()

**Example:**
```javascript
expect(['apple', 'banana']).toContain('apple');
```

#### toHaveLength()

**Example:**
```javascript
expect([1, 2, 3]).toHaveLength(3);
```

### Object Matchers

#### toHaveProperty()

**Example:**
```javascript
expect({ name: 'John' }).toHaveProperty('name');
expect({ name: 'John' }).toHaveProperty('name', 'John');
```

#### toEqual()

**Example:**
```javascript
expect({ a: 1, b: 2 }).toEqual({ a: 1, b: 2 });
```

### Exception Matchers

#### toThrow()

**Example:**
```javascript
expect(() => { throw new Error('error'); }).toThrow();
expect(() => { throw new Error('error'); }).toThrow('error');
expect(() => { throw new Error('error'); }).toThrow(Error);
```

### Async Matchers

#### resolves

**Example:**
```javascript
await expect(Promise.resolve('value')).resolves.toBe('value');
```

#### rejects

**Example:**
```javascript
await expect(Promise.reject(new Error('error'))).rejects.toThrow('error');
```

### Negation

Use `.not` to negate any matcher.

**Example:**
```javascript
expect(2 + 2).not.toBe(5);
```

### Key Points

- `expect()` creates an expectation
- Use appropriate matcher for each assertion
- `toBe()` for primitives, `toEqual()` for objects
- Use `not` to negate matchers
- Use `resolves`/`rejects` for promises
- Matchers return boolean values
