# Visual Regression Testing

**官方文档**: https://vitest.dev/guide/visual-regression.html


## Instructions

This example demonstrates visual regression testing with Vitest.

### Key Concepts

- Visual testing setup
- Screenshot comparison
- Visual diff tools
- CI integration

### Example: Visual Testing Setup

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      name: 'chromium',
    },
  },
})
```

### Example: Screenshot Testing

```typescript
import { describe, it, expect } from 'vitest'

describe('Visual Tests', () => {
  it('matches screenshot', async () => {
    await page.goto('http://localhost:3000')
    await expect(page).toHaveScreenshot()
  })
})
```

### Key Points

- Requires browser mode
- Compare screenshots
- Detect visual changes
- Integrate with CI/CD
- Use with component testing
