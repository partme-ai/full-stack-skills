## Instructions

- Use v-if / v-else-if / v-else for conditional blocks.
- Use v-show for frequent toggling.
- Keep conditions simple and readable.

### Example

```vue
<script setup>
import { ref } from 'vue'

const visible = ref(true)
</script>

<template>
  <p v-if="visible">Shown</p>
  <p v-else>Hidden</p>
</template>
```

Reference: https://cn.vuejs.org/guide/essentials/conditional.html
