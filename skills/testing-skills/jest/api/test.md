# test and describe API | test 和 describe API

**官方文档**: https://jestjs.io/docs/api#testname-fn-timeout


## API Reference

Test functions and test suite organization.

### test() / it()

Creates a test case.

**Signature:**
```typescript
function test(name: string, fn: () => void, timeout?: number): void
function it(name: string, fn: () => void, timeout?: number): void
```

**Parameters:**
- `name`: Test name/description
- `fn`: Test function
- `timeout`: Test timeout in milliseconds (optional)

**Example:**
```javascript
test('adds 1 + 2 to equal 3', () => {
  expect(1 + 2).toBe(3);
});

it('should return true', () => {
  expect(true).toBeTruthy();
});
```

### describe()

Creates a test suite/block.

**Signature:**
```typescript
function describe(name: string, fn: () => void): void
```

**Parameters:**
- `name`: Suite name/description
- `fn`: Suite function containing tests

**Example:**
```javascript
describe('Math operations', () => {
  test('addition', () => {
    expect(1 + 1).toBe(2);
  });

  test('subtraction', () => {
    expect(2 - 1).toBe(1);
  });
});
```

### beforeEach()

Runs before each test in the suite.

**Signature:**
```typescript
function beforeEach(fn: () => void, timeout?: number): void
```

**Example:**
```javascript
describe('database', () => {
  beforeEach(() => {
    clearDatabase();
  });

  test('insert', () => {
    // Test code
  });
});
```

### afterEach()

Runs after each test in the suite.

**Signature:**
```typescript
function afterEach(fn: () => void, timeout?: number): void
```

**Example:**
```javascript
describe('database', () => {
  afterEach(() => {
    cleanup();
  });

  test('insert', () => {
    // Test code
  });
});
```

### beforeAll()

Runs once before all tests in the suite.

**Signature:**
```typescript
function beforeAll(fn: () => void, timeout?: number): void
```

**Example:**
```javascript
describe('database', () => {
  beforeAll(() => {
    initializeDatabase();
  });

  test('insert', () => {
    // Test code
  });
});
```

### afterAll()

Runs once after all tests in the suite.

**Signature:**
```typescript
function afterAll(fn: () => void, timeout?: number): void
```

**Example:**
```javascript
describe('database', () => {
  afterAll(() => {
    closeDatabase();
  });

  test('insert', () => {
    // Test code
  });
});
```

### Key Points

- `test()` and `it()` are aliases
- `describe()` groups related tests
- Setup/teardown functions are scoped to describe blocks
- Can nest describe blocks
- Setup/teardown can be async
- Use timeout parameter for long-running tests
