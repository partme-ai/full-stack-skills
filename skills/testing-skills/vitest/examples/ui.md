# UI

**官方文档**: https://vitest.dev/guide/ui.html


## Instructions

This example demonstrates Vitest UI for interactive testing.

### Key Concepts

- Starting UI mode
- UI features
- Test filtering
- Test debugging

### Example: Starting UI

```bash
# Start UI mode
vitest --ui

# Or with npm script
npm run test:ui
```

### Example: UI Features

Vitest UI provides:
- **Test Explorer**: Browse and filter tests
- **Test Runner**: Run tests interactively
- **Coverage View**: View code coverage
- **Time Travel**: See test execution timeline

### Example: Filtering Tests

In UI mode, you can:
- Filter by test name
- Filter by file
- Run specific tests
- Skip tests

### Example: Debugging

```typescript
// Use debugger in tests
it('debugs test', () => {
  debugger // Breakpoint works in UI
  expect(true).toBe(true)
})
```

### Key Points

- Start with --ui flag
- Interactive test running
- Real-time test results
- Coverage visualization
- Better debugging experience
