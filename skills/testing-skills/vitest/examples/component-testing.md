# Component Testing

**官方文档**: https://vitest.dev/guide/testing-components.html


## Instructions

This example demonstrates component testing with Vitest.

### Key Concepts

- Vue component testing
- React component testing
- Testing library integration
- DOM environment

### Example: Vue Component Testing

```typescript
// Button.test.ts
import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import Button from './Button.vue'

describe('Button', () => {
  it('renders correctly', () => {
    const wrapper = mount(Button, {
      props: {
        label: 'Click me'
      }
    })
    expect(wrapper.text()).toContain('Click me')
  })
})
```

### Example: React Component Testing

```typescript
// Button.test.tsx
import { render, screen } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import Button from './Button'

describe('Button', () => {
  it('renders', () => {
    render(<Button label="Click me" />)
    expect(screen.getByText('Click me')).toBeDefined()
  })
})
```

### Example: Configuration for Component Testing

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  test: {
    environment: 'jsdom', // or 'happy-dom'
  },
})
```

### Example: Testing User Interactions

```typescript
import { render, screen, fireEvent } from '@testing-library/vue'
import { describe, it, expect } from 'vitest'
import Counter from './Counter.vue'

describe('Counter', () => {
  it('increments on click', async () => {
    render(Counter)
    const button = screen.getByRole('button')
    await fireEvent.click(button)
    expect(screen.getByText('Count: 1')).toBeDefined()
  })
})
```

### Key Points

- Supports Vue, React, Svelte
- Use testing-library or vue-test-utils
- Configure environment (jsdom/happy-dom)
- Test user interactions
- Fast component testing
