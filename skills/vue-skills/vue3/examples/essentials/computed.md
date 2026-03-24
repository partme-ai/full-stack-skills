## Instructions

- Use computed() for derived state.
- Computed values are cached by dependency.
- Prefer computed over methods for repeated derivations.

### Example

```vue
<script setup>
import { ref, computed } from 'vue'

const count = ref(2)
const double = computed(() => count.value * 2)
</script>

<template>
  <p>double: {{ double }}</p>
</template>
```

Reference: https://cn.vuejs.org/guide/essentials/computed.html
