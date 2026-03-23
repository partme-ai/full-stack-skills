# Using Matchers | 使用匹配器

**官方文档**: https://jestjs.io/docs/using-matchers


## Instructions

This example demonstrates how to use Jest matchers for assertions.

### Key Concepts

- Common matchers
- Equality matchers
- Truthiness matchers
- Number matchers
- String matchers
- Array matchers
- Object matchers
- Exception matchers

### Example: Common Matchers

```javascript
test('basic matchers', () => {
  // toBe uses Object.is for exact equality
  expect(2 + 2).toBe(4);

  // toEqual checks value equality
  expect({ name: 'John' }).toEqual({ name: 'John' });

  // toBeNull matches only null
  expect(null).toBeNull();

  // toBeUndefined matches only undefined
  expect(undefined).toBeUndefined();

  // toBeDefined is opposite of toBeUndefined
  expect('value').toBeDefined();

  // toBeTruthy matches anything that if statement treats as true
  expect(1).toBeTruthy();

  // toBeFalsy matches anything that if statement treats as false
  expect(0).toBeFalsy();
});
```

### Example: Number Matchers

```javascript
test('number matchers', () => {
  const value = 2 + 2;

  expect(value).toBeGreaterThan(3);
  expect(value).toBeGreaterThanOrEqual(4);
  expect(value).toBeLessThan(5);
  expect(value).toBeLessThanOrEqual(4);
  expect(value).toBe(4);
  expect(value).toEqual(4);

  // For floating point equality
  expect(0.1 + 0.2).toBeCloseTo(0.3);
});
```

### Example: String Matchers

```javascript
test('string matchers', () => {
  expect('team').not.toMatch(/I/);
  expect('Christoph').toMatch(/stop/);
  expect('Hello World').toContain('World');
});
```

### Example: Array Matchers

```javascript
test('array matchers', () => {
  const shoppingList = [
    'diapers',
    'kleenex',
    'trash bags',
    'paper towels',
    'milk',
  ];

  expect(shoppingList).toContain('milk');
  expect(new Set(shoppingList)).toContain('milk');
});
```

### Example: Object Matchers

```javascript
test('object matchers', () => {
  const data = { one: 1, two: 2 };

  expect(data).toEqual({ one: 1, two: 2 });
  expect(data).toHaveProperty('one');
  expect(data).toHaveProperty('one', 1);
});
```

### Example: Exception Matchers

```javascript
test('exception matchers', () => {
  function compileAndroidCode() {
    throw new Error('you are using the wrong JDK');
  }

  expect(() => compileAndroidCode()).toThrow();
  expect(() => compileAndroidCode()).toThrow(Error);
  expect(() => compileAndroidCode()).toThrow('you are using the wrong JDK');
  expect(() => compileAndroidCode()).toThrow(/JDK/);
});
```

### Example: Async Matchers

```javascript
test('async matchers', async () => {
  // Resolves
  await expect(Promise.resolve('lemon')).resolves.toBe('lemon');
  await expect(Promise.resolve('lemon')).resolves.not.toBe('octopus');

  // Rejects
  await expect(Promise.reject(new Error('octopus'))).rejects.toThrow('octopus');
});
```

### Key Points

- Use `toBe()` for primitive values and object identity
- Use `toEqual()` for object/array value equality
- Use `toContain()` for arrays and strings
- Use `toMatch()` for regex matching
- Use `toThrow()` for exception testing
- Use `resolves`/`rejects` for promise testing
- Use `not` to negate any matcher
- Choose the right matcher for each assertion
