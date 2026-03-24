# Mock Functions API | Mock 函数 API

**官方文档**: https://jestjs.io/docs/mock-functions


## API Reference

Mock functions API and methods.

### jest.fn()

Creates a mock function.

**Signature:**
```typescript
function jest.fn(implementation?: Function): Mock
```

**Example:**
```javascript
const mockFn = jest.fn();
const mockFnWithImpl = jest.fn((x) => x + 1);
```

### jest.mock()

Mocks a module.

**Signature:**
```typescript
function jest.mock(moduleName: string, factory?: Function, options?: Object): void
```

**Example:**
```javascript
jest.mock('./api');
jest.mock('./utils', () => ({
  helper: jest.fn(),
}));
```

### jest.spyOn()

Creates a spy on an object method.

**Signature:**
```typescript
function jest.spyOn(object: Object, methodName: string): Spy
```

**Example:**
```javascript
const spy = jest.spyOn(obj, 'method');
```

### Mock Function Methods

#### mockReturnValue()

Sets return value.

**Example:**
```javascript
mockFn.mockReturnValue(42);
```

#### mockReturnValueOnce()

Sets return value for one call.

**Example:**
```javascript
mockFn.mockReturnValueOnce(10).mockReturnValueOnce(20);
```

#### mockResolvedValue()

Sets resolved value for promise.

**Example:**
```javascript
mockFn.mockResolvedValue('value');
```

#### mockRejectedValue()

Sets rejected value for promise.

**Example:**
```javascript
mockFn.mockRejectedValue(new Error('error'));
```

#### mockImplementation()

Sets implementation.

**Example:**
```javascript
mockFn.mockImplementation((x) => x * 2);
```

### Mock Function Properties

#### mock.calls

Array of call arguments.

**Example:**
```javascript
mockFn('arg1', 'arg2');
expect(mockFn.mock.calls[0]).toEqual(['arg1', 'arg2']);
```

#### mock.results

Array of return values.

**Example:**
```javascript
mockFn.mockReturnValue(42);
mockFn();
expect(mockFn.mock.results[0].value).toBe(42);
```

#### mock.instances

Array of instances (for constructor mocks).

**Example:**
```javascript
const MockClass = jest.fn();
const instance = new MockClass();
expect(MockClass.mock.instances[0]).toBe(instance);
```

### Key Points

- `jest.fn()` creates mock functions
- `jest.mock()` mocks modules
- `jest.spyOn()` creates spies
- Mock functions track calls and results
- Use mock methods to configure behavior
- Access call history via `mock.calls`
