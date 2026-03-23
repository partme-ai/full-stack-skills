## Instructions

- Use defineAsyncComponent for lazy loading.
- Provide loading and error states.
- Set timeout for slow loads.

### Example

```vue
<script setup>
import { defineAsyncComponent } from 'vue'

const AsyncCard = defineAsyncComponent(() => import('./Card.vue'))
</script>

<template>
  <AsyncCard />
</template>
```

Reference: https://cn.vuejs.org/guide/components/async.html
