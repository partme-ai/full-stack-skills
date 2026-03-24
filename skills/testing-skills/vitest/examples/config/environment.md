# Environment Configuration

**官方文档**: https://vitest.dev/config/#environment


## Instructions

This example demonstrates environment configuration in Vitest.

### Key Concepts

- Test environments
- jsdom
- happy-dom
- node environment
- Custom environments

### Example: jsdom Environment

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    environment: 'jsdom',
  },
})
```

### Example: happy-dom Environment

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    environment: 'happy-dom', // Faster than jsdom
  },
})
```

### Example: Node Environment

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    environment: 'node',
  },
})
```

### Example: Per-File Environment

```typescript
// component.test.ts
import { describe, it, expect } from 'vitest'

// @vitest-environment jsdom
describe('Component', () => {
  it('works', () => {
    expect(window).toBeDefined()
  })
})
```

### Example: Multiple Environments

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    environment: 'jsdom',
    environmentMatchGlobs: [
      ['**/*.node.test.ts', 'node'],
      ['**/*.dom.test.ts', 'jsdom'],
    ],
  },
})
```

### Key Points

- Choose environment: node, jsdom, happy-dom
- happy-dom is faster than jsdom
- Set per-file with comment
- Match globs for different environments
- Install environment packages
