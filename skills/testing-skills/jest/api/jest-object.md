# Jest Object API | Jest 对象 API

**官方文档**: https://jestjs.io/docs/jest-object


## API Reference

Jest object methods and utilities.

### jest.clearAllMocks()

Clears all mock call and instance data.

**Signature:**
```typescript
function jest.clearAllMocks(): void
```

**Example:**
```javascript
beforeEach(() => {
  jest.clearAllMocks();
});
```

### jest.resetAllMocks()

Resets all mocks to initial state.

**Signature:**
```typescript
function jest.resetAllMocks(): void
```

**Example:**
```javascript
afterEach(() => {
  jest.resetAllMocks();
});
```

### jest.restoreAllMocks()

Restores all mocks to original implementation.

**Signature:**
```typescript
function jest.restoreAllMocks(): void
```

**Example:**
```javascript
afterEach(() => {
  jest.restoreAllMocks();
});
```

### jest.useFakeTimers()

Uses fake timers.

**Signature:**
```typescript
function jest.useFakeTimers(): void
```

**Example:**
```javascript
jest.useFakeTimers();
setTimeout(() => {
  console.log('delayed');
}, 1000);
jest.advanceTimersByTime(1000);
```

### jest.useRealTimers()

Uses real timers.

**Signature:**
```typescript
function jest.useRealTimers(): void
```

**Example:**
```javascript
jest.useRealTimers();
```

### jest.advanceTimersByTime()

Advances fake timers by time.

**Signature:**
```typescript
function jest.advanceTimersByTime(ms: number): void
```

**Example:**
```javascript
jest.useFakeTimers();
setTimeout(callback, 1000);
jest.advanceTimersByTime(1000);
```

### jest.runOnlyPendingTimers()

Runs only pending timers.

**Signature:**
```typescript
function jest.runOnlyPendingTimers(): void
```

**Example:**
```javascript
jest.useFakeTimers();
setTimeout(callback, 1000);
jest.runOnlyPendingTimers();
```

### jest.setSystemTime()

Sets system time for fake timers.

**Signature:**
```typescript
function jest.setSystemTime(now: number | Date): void
```

**Example:**
```javascript
jest.useFakeTimers();
jest.setSystemTime(new Date('2020-01-01'));
```

### Key Points

- `clearAllMocks()` clears call history
- `resetAllMocks()` resets to initial state
- `restoreAllMocks()` restores original implementations
- `useFakeTimers()` enables timer mocking
- `useRealTimers()` disables timer mocking
- Timer methods control fake timer behavior
