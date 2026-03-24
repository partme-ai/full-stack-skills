# Browser Mode

**官方文档**: https://vitest.dev/guide/browser.html


## Instructions

This example demonstrates browser mode testing in Vitest.

### Key Concepts

- Browser mode setup
- Provider configuration
- Browser options
- Viewport configuration

### Example: Basic Browser Mode

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      name: 'chromium',
      provider: 'playwright',
    },
  },
})
```

### Example: Multiple Browsers

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      name: ['chromium', 'firefox', 'webkit'],
      provider: 'playwright',
    },
  },
})
```

### Example: Browser Options

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      name: 'chromium',
      provider: 'playwright',
      headless: false,
      viewport: {
        width: 1280,
        height: 720,
      },
    },
  },
})
```

### Example: Browser Test

```typescript
// browser.test.ts
import { describe, it, expect } from 'vitest'

describe('Browser Test', () => {
  it('works in browser', () => {
    expect(window).toBeDefined()
    expect(document).toBeDefined()
  })
})
```

### Key Points

- Enable with browser.enabled: true
- Choose provider (playwright, webdriverio)
- Configure browsers and viewport
- Tests run in real browser
- Supports headless and headed modes
