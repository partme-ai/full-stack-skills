# Getting Started

**官方文档**: https://vitest.dev/guide/getting-started.html


## Instructions

This example demonstrates how to get started with Vitest.

### Key Concepts

- Installation
- First test
- Running tests
- Configuration

### Example: Installation

```bash
# Using npm
npm install -D vitest

# Using yarn
yarn add -D vitest

# Using pnpm
pnpm add -D vitest
```

### Example: First Test

```javascript
// sum.js
export function sum(a, b) {
  return a + b
}

// sum.test.js
import { describe, it, expect } from 'vitest'
import { sum } from './sum'

describe('sum', () => {
  it('adds two numbers', () => {
    expect(sum(1, 2)).toBe(3)
  })
})
```

### Example: Package.json Scripts

```json
{
  "scripts": {
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:run": "vitest run",
    "test:coverage": "vitest --coverage"
  }
}
```

### Example: Basic Configuration

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    // Test configuration
  },
})
```

### Example: Running Tests

```bash
# Watch mode (default)
npm test

# Run once
npm run test:run

# UI mode
npm run test:ui
```

### Key Points

- Install vitest as dev dependency
- Write tests using describe/it/expect
- Run tests with vitest command
- Use --ui for interactive UI
- Configure via vitest.config.ts
