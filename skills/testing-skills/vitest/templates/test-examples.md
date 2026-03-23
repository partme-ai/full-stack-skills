# Test Example Templates

## Basic Test

```typescript
// sum.test.ts
import { describe, it, expect } from 'vitest'
import { sum } from './sum'

describe('sum', () => {
  it('adds two numbers', () => {
    expect(sum(1, 2)).toBe(3)
  })
})
```

## Vue Component Test

```typescript
// Button.test.ts
import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import Button from './Button.vue'

describe('Button', () => {
  it('renders', () => {
    const wrapper = mount(Button, {
      props: { label: 'Click me' }
    })
    expect(wrapper.text()).toContain('Click me')
  })
})
```

## React Component Test

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

## Test with Mocking

```typescript
// api.test.ts
import { describe, it, expect, vi } from 'vitest'
import { fetchData } from './api'

vi.mock('./api')

describe('API', () => {
  it('fetches data', async () => {
    const mockData = { data: 'test' }
    vi.mocked(fetchData).mockResolvedValue(mockData)
    
    const result = await fetchData()
    expect(result).toEqual(mockData)
  })
})
```

## Test with Hooks

```typescript
// database.test.ts
import { describe, it, expect, beforeAll, beforeEach, afterEach } from 'vitest'

describe('Database', () => {
  beforeAll(() => {
    // Setup database
  })

  beforeEach(() => {
    // Clear data
  })

  afterEach(() => {
    // Cleanup
  })

  it('creates record', () => {
    // Test
  })
})
```

## Async Test

```typescript
// async.test.ts
import { describe, it, expect } from 'vitest'

describe('Async', () => {
  it('handles async operations', async () => {
    const result = await fetch('/api/data')
    expect(result.ok).toBe(true)
  })
})
```
