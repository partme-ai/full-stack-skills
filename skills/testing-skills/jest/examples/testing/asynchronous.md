# Asynchronous | 异步测试

**官方文档**: https://jestjs.io/docs/asynchronous


## Instructions

This example demonstrates how to test asynchronous code in Jest.

### Key Concepts

- Testing callbacks
- Testing promises
- Testing async/await
- Using done callback
- Using resolves/rejects matchers

### Example: Testing Callbacks

```javascript
test('callback test', (done) => {
  function fetchData(callback) {
    setTimeout(() => {
      callback('peanut butter');
    }, 100);
  }

  function callback(data) {
    try {
      expect(data).toBe('peanut butter');
      done();
    } catch (error) {
      done(error);
    }
  }

  fetchData(callback);
});
```

### Example: Testing Promises

```javascript
test('promise test', () => {
  function fetchData() {
    return Promise.resolve('peanut butter');
  }

  return fetchData().then(data => {
    expect(data).toBe('peanut butter');
  });
});
```

### Example: Testing Promises with .resolves

```javascript
test('promise with resolves', () => {
  function fetchData() {
    return Promise.resolve('peanut butter');
  }

  return expect(fetchData()).resolves.toBe('peanut butter');
});
```

### Example: Testing Rejected Promises

```javascript
test('rejected promise', () => {
  function fetchData() {
    return Promise.reject('error');
  }

  return expect(fetchData()).rejects.toBe('error');
});
```

### Example: Testing Async/Await

```javascript
test('async/await test', async () => {
  function fetchData() {
    return Promise.resolve('peanut butter');
  }

  const data = await fetchData();
  expect(data).toBe('peanut butter');
});
```

### Example: Combining Async/Await with .resolves

```javascript
test('async/await with resolves', async () => {
  function fetchData() {
    return Promise.resolve('peanut butter');
  }

  await expect(fetchData()).resolves.toBe('peanut butter');
});
```

### Example: Multiple Async Operations

```javascript
test('multiple async operations', async () => {
  async function fetchUser() {
    return Promise.resolve({ id: 1, name: 'John' });
  }

  async function fetchPosts(userId) {
    return Promise.resolve([{ id: 1, title: 'Post 1' }]);
  }

  const user = await fetchUser();
  const posts = await fetchPosts(user.id);

  expect(user).toEqual({ id: 1, name: 'John' });
  expect(posts).toHaveLength(1);
});
```

### Key Points

- Use `done` callback for callback-based async code
- Return promises from tests for promise-based code
- Use `async/await` for cleaner async test code
- Use `.resolves` and `.rejects` matchers for promises
- Always handle errors in async tests
- Jest waits for promises to resolve/reject
- Don't forget to return promises or use await
