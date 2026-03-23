# Coverage

**官方文档**: https://vitest.dev/guide/coverage.html


## Instructions

This example demonstrates code coverage in Vitest.

### Key Concepts

- Coverage configuration
- Coverage providers
- Coverage reports
- Coverage thresholds

### Example: Basic Coverage

```bash
# Run with coverage
vitest --coverage

# Or with npm script
npm run test:coverage
```

### Example: Coverage Configuration

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    coverage: {
      provider: 'v8', // or 'istanbul'
      reporter: ['text', 'json', 'html'],
    },
  },
})
```

### Example: Coverage Providers

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    coverage: {
      provider: 'v8', // Fast, native
      // or
      // provider: 'istanbul' // More compatible
    },
  },
})
```

### Example: Coverage Thresholds

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    coverage: {
      thresholds: {
        lines: 80,
        functions: 80,
        branches: 80,
        statements: 80,
      },
    },
  },
})
```

### Example: Coverage Exclusions

```typescript
// vitest.config.ts
export default defineConfig({
  test: {
    coverage: {
      exclude: [
        'node_modules/',
        'src/**/*.test.ts',
        'src/**/*.spec.ts',
      ],
    },
  },
})
```

### Key Points

- Use --coverage flag
- Choose provider (v8 or istanbul)
- Configure reporters
- Set thresholds
- Exclude files from coverage
