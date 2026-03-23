# Basic Configuration

**官方文档**: https://vitest.dev/config/


## Instructions

This example demonstrates basic Vitest configuration.

### Key Concepts

- Configuration file
- Test options
- Include/exclude patterns
- Global setup

### Example: Basic Config

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
  },
})
```

### Example: Include/Exclude

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    include: ['**/*.{test,spec}.{js,ts}'],
    exclude: ['node_modules', 'dist'],
  },
})
```

### Example: Global Setup

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    globalSetup: './tests/setup.ts',
    setupFiles: './tests/setup-file.ts',
  },
})
```

### Example: Timeout

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    testTimeout: 10000,
    hookTimeout: 10000,
  },
})
```

### Key Points

- Configure via vitest.config.ts
- Set include/exclude patterns
- Configure global setup
- Set timeouts
- Use defineConfig for type safety
