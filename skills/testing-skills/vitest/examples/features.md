# Features

**官方文档**: https://vitest.dev/guide/features.html


## Instructions

This example highlights key features of Vitest.

### Key Concepts

- Vite integration
- Watch mode
- TypeScript support
- Component testing
- Browser mode

### Example: Vite Integration

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  test: {
    // Uses same Vite config
  },
})
```

### Example: Watch Mode

```bash
# Smart watch mode - only reruns affected tests
vitest

# Watch mode with UI
vitest --ui
```

### Example: TypeScript Support

```typescript
// math.test.ts
import { describe, it, expect } from 'vitest'

describe('Math', () => {
  it('works with TypeScript', () => {
    const result: number = 1 + 1
    expect(result).toBe(2)
  })
})
```

### Example: ESM Support

```javascript
// Uses native ESM - no need for babel/transpilation
import { sum } from './sum.js'
```

### Example: Component Testing

```typescript
// Button.test.tsx
import { render, screen } from '@testing-library/vue'
import { describe, it, expect } from 'vitest'
import Button from './Button.vue'

describe('Button', () => {
  it('renders', () => {
    render(Button)
    expect(screen.getByRole('button')).toBeDefined()
  })
})
```

### Key Points

- Seamless Vite integration
- Fast watch mode with HMR
- Native TypeScript/ESM support
- Component testing support
- Browser mode available
- Jest-compatible API
