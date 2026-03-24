# Mock Functions | Mock 函数

**官方文档**: https://jestjs.io/docs/mock-functions


## Instructions

This example demonstrates how to create and use mock functions in Jest.

### Key Concepts

- Creating mock functions with jest.fn()
- Mock return values
- Mock implementations
- Mock function properties
- Verifying mock calls

### Example: Basic Mock Function

```javascript
test('basic mock', () => {
  const mockFn = jest.fn();
  mockFn();
  expect(mockFn).toHaveBeenCalled();
});
```

### Example: Mock Return Value

```javascript
test('mock return value', () => {
  const mockFn = jest.fn();
  mockFn.mockReturnValue(42);
  
  expect(mockFn()).toBe(42);
  expect(mockFn()).toBe(42);
});
```

### Example: Mock Implementation

```javascript
test('mock implementation', () => {
  const mockFn = jest.fn((x) => x + 1);
  
  expect(mockFn(1)).toBe(2);
  expect(mockFn(2)).toBe(3);
});
```

### Example: Mock Once

```javascript
test('mock once', () => {
  const mockFn = jest.fn();
  mockFn.mockReturnValueOnce(10).mockReturnValueOnce(20);
  
  expect(mockFn()).toBe(10);
  expect(mockFn()).toBe(20);
  expect(mockFn()).toBeUndefined();
});
```

### Example: Mock Resolved Value

```javascript
test('mock resolved value', async () => {
  const mockFn = jest.fn();
  mockFn.mockResolvedValue('async value');
  
  await expect(mockFn()).resolves.toBe('async value');
});
```

### Example: Mock Rejected Value

```javascript
test('mock rejected value', async () => {
  const mockFn = jest.fn();
  mockFn.mockRejectedValue(new Error('async error'));
  
  await expect(mockFn()).rejects.toThrow('async error');
});
```

### Example: Verifying Mock Calls

```javascript
test('verify mock calls', () => {
  const mockFn = jest.fn();
  
  mockFn('arg1', 'arg2');
  mockFn('arg3', 'arg4');
  
  expect(mockFn).toHaveBeenCalled();
  expect(mockFn).toHaveBeenCalledTimes(2);
  expect(mockFn).toHaveBeenCalledWith('arg1', 'arg2');
  expect(mockFn).toHaveBeenLastCalledWith('arg3', 'arg4');
  expect(mockFn).toHaveBeenNthCalledWith(1, 'arg1', 'arg2');
});
```

### Example: Mock Function Properties

```javascript
test('mock function properties', () => {
  const mockFn = jest.fn();
  
  mockFn('first', 'second');
  
  // Access call information
  expect(mockFn.mock.calls).toHaveLength(1);
  expect(mockFn.mock.calls[0][0]).toBe('first');
  expect(mockFn.mock.calls[0][1]).toBe('second');
  expect(mockFn.mock.results[0].value).toBeUndefined();
});
```

### Example: Using Mock in Implementation

```javascript
test('using mock in implementation', () => {
  const filterTestFn = jest.fn();
  filterTestFn.mockReturnValueOnce(true).mockReturnValueOnce(false);
  
  const result = [11, 12].filter(filterTestFn);
  
  expect(result).toEqual([11]);
  expect(filterTestFn.mock.calls[0][0]).toBe(11);
  expect(filterTestFn.mock.calls[1][0]).toBe(12);
});
```

### Key Points

- Use `jest.fn()` to create mock functions
- Use `mockReturnValue()` for synchronous return values
- Use `mockResolvedValue()` for promise resolution
- Use `mockRejectedValue()` for promise rejection
- Use `mockReturnValueOnce()` for one-time return values
- Use `mockImplementation()` for custom implementations
- Verify calls with `toHaveBeenCalled()` and related matchers
- Access call history via `mockFn.mock.calls`
