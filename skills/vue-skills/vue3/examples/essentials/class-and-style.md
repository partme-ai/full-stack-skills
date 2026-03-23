## Instructions

- Bind class and style with object or array syntax.
- Use computed for complex class logic.
- Prefer inline style bindings for dynamic style values.

### Example

```vue
<script setup>
import { ref, computed } from 'vue'

const isActive = ref(true)
const classes = computed(() => ({ active: isActive.value }))
</script>

<template>
  <div :class="classes" :style="{ color: isActive ? 'green' : 'gray' }">Text</div>
</template>
```

Reference: https://cn.vuejs.org/guide/essentials/class-and-style.html
