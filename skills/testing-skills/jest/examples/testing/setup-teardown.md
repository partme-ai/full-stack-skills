# Setup and Teardown | 设置和清理

**官方文档**: https://jestjs.io/docs/setup-teardown


## Instructions

This example demonstrates how to use setup and teardown functions in Jest.

### Key Concepts

- beforeAll() - Run once before all tests
- afterAll() - Run once after all tests
- beforeEach() - Run before each test
- afterEach() - Run after each test
- Scoping setup and teardown

### Example: Basic Setup and Teardown

```javascript
describe('database operations', () => {
  let database;

  beforeAll(() => {
    database = initializeDatabase();
  });

  afterAll(() => {
    closeDatabase(database);
  });

  beforeEach(() => {
    clearDatabase(database);
  });

  test('insert user', () => {
    database.insert({ name: 'John' });
    expect(database.find('John')).toBeDefined();
  });

  test('delete user', () => {
    database.insert({ name: 'Jane' });
    database.delete('Jane');
    expect(database.find('Jane')).toBeUndefined();
  });
});
```

### Example: Async Setup

```javascript
describe('async setup', () => {
  let data;

  beforeAll(async () => {
    data = await fetchData();
  });

  test('use data', () => {
    expect(data).toBeDefined();
  });
});
```

### Example: Scoped Setup

```javascript
describe('outer scope', () => {
  beforeAll(() => {
    console.log('outer beforeAll');
  });

  beforeEach(() => {
    console.log('outer beforeEach');
  });

  test('outer test', () => {
    console.log('outer test');
  });

  describe('inner scope', () => {
    beforeAll(() => {
      console.log('inner beforeAll');
    });

    beforeEach(() => {
      console.log('inner beforeEach');
    });

    test('inner test', () => {
      console.log('inner test');
    });
  });
});
```

### Example: Conditional Setup

```javascript
describe('conditional setup', () => {
  beforeAll(() => {
    if (process.env.NODE_ENV === 'test') {
      setupTestEnvironment();
    }
  });
});
```

### Key Points

- `beforeAll()` runs once before all tests in a describe block
- `afterAll()` runs once after all tests in a describe block
- `beforeEach()` runs before each test
- `afterEach()` runs after each test
- Setup and teardown can be async
- Setup and teardown are scoped to describe blocks
- Use setup for initialization, teardown for cleanup
- Order: beforeAll → beforeEach → test → afterEach → afterAll
