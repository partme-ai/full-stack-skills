# Browser Configuration

**官方文档**: https://vitest.dev/config/#browser


## Instructions

This example demonstrates browser mode configuration.

### Key Concepts

- Browser mode setup
- Provider configuration
- Browser options
- Viewport settings

### Example: Basic Browser Config

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

### Example: Provider Options

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    browser: {
      enabled: true,
      provider: 'webdriverio',
      // WebdriverIO specific options
    },
  },
})
```

### Key Points

- Enable with browser.enabled: true
- Choose provider: playwright or webdriverio
- Configure browsers and viewport
- Set headless mode
- Install provider packages
