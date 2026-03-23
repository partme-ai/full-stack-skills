## Instructions

- Encapsulate reusable stateful logic.
- Return refs and functions from composables.
- Keep composables focused.

### Example

```ts
import { ref } from 'vue'

export function useCounter() {
  const count = ref(0)

  // Increment count
  function inc() {
    count.value += 1
  }

  return { count, inc }
}
```

Reference: https://cn.vuejs.org/guide/reusability/composables.html
