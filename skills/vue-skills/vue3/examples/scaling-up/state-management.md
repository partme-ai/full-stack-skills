## Instructions

- Use Pinia for global state management.
- Keep stores modular and feature-based.
- Avoid overusing global state.

### Example

```ts
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => ({ count: 0 })
})
```

Reference: https://cn.vuejs.org/guide/scaling-up/state-management.html
