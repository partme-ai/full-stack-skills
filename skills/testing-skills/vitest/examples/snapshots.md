# Snapshots

**官方文档**: https://vitest.dev/guide/snapshot.html


## Instructions

This example demonstrates snapshot testing in Vitest.

### Key Concepts

- toMatchSnapshot()
- toMatchInlineSnapshot()
- Updating snapshots
- Snapshot files

### Example: Basic Snapshot

```typescript
import { describe, it, expect } from 'vitest'

describe('Snapshots', () => {
  it('matches snapshot', () => {
    const data = { name: 'John', age: 30 }
    expect(data).toMatchSnapshot()
  })
})
```

### Example: Inline Snapshot

```typescript
import { describe, it, expect } from 'vitest'

describe('Snapshots', () => {
  it('matches inline snapshot', () => {
    const data = { name: 'John', age: 30 }
    expect(data).toMatchInlineSnapshot(`
      {
        "age": 30,
        "name": "John"
      }
    `)
  })
})
```

### Example: Component Snapshot

```typescript
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import Button from './Button.vue'

describe('Button', () => {
  it('matches snapshot', () => {
    const wrapper = mount(Button, {
      props: { label: 'Click me' }
    })
    expect(wrapper.html()).toMatchSnapshot()
  })
})
```

### Example: Updating Snapshots

```bash
# Update all snapshots
vitest -u

# Or
vitest --update
```

### Key Points

- Use toMatchSnapshot() for file snapshots
- Use toMatchInlineSnapshot() for inline snapshots
- Update with -u flag
- Snapshots stored in __snapshots__ directory
- Great for UI regression testing
