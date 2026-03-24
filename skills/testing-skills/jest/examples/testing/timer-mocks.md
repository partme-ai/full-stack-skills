# Timer Mocks | 定时器 Mock

**官方文档**: https://jestjs.io/docs/timer-mocks


## Instructions

This example demonstrates how to mock timers in Jest.

### Key Concepts

- Using fake timers
- Advancing timers
- Running pending timers
- Real timers

### Example: Basic Timer Mock

```javascript
jest.useFakeTimers();

test('timer mock', () => {
  const callback = jest.fn();
  
  setTimeout(callback, 1000);
  
  expect(callback).not.toHaveBeenCalled();
  
  jest.advanceTimersByTime(1000);
  
  expect(callback).toHaveBeenCalled();
});
```

### Example: setInterval

```javascript
jest.useFakeTimers();

test('interval mock', () => {
  const callback = jest.fn();
  
  setInterval(callback, 1000);
  
  jest.advanceTimersByTime(5000);
  
  expect(callback).toHaveBeenCalledTimes(5);
});
```

### Example: runOnlyPendingTimers

```javascript
jest.useFakeTimers();

test('run pending timers', () => {
  const callback = jest.fn();
  
  setTimeout(callback, 1000);
  setTimeout(callback, 2000);
  
  jest.runOnlyPendingTimers();
  
  expect(callback).toHaveBeenCalledTimes(1);
});
```

### Example: runAllTimers

```javascript
jest.useFakeTimers();

test('run all timers', () => {
  const callback = jest.fn();
  
  setTimeout(() => {
    setTimeout(callback, 100);
  }, 100);
  
  jest.runAllTimers();
  
  expect(callback).toHaveBeenCalled();
});
```

### Example: Real Timers

```javascript
jest.useRealTimers();

test('real timers', async () => {
  const callback = jest.fn();
  
  setTimeout(callback, 100);
  
  await new Promise(resolve => setTimeout(resolve, 150));
  
  expect(callback).toHaveBeenCalled();
});
```

### Key Points

- Use `jest.useFakeTimers()` to enable fake timers
- Use `jest.useRealTimers()` to use real timers
- `advanceTimersByTime()` advances timers by specified time
- `runOnlyPendingTimers()` runs only currently pending timers
- `runAllTimers()` runs all timers including nested ones
- Fake timers are useful for testing time-dependent code
