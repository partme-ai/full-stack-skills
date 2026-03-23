## Instructions

- Use v-for to render arrays and objects.
- Always provide a stable :key.
- Avoid using array index as key when possible.

### Example

```vue
<script setup>
import { ref } from 'vue'

const items = ref([{ id: 1, name: 'A' }, { id: 2, name: 'B' }])
</script>

<template>
  <li v-for="item in items" :key="item.id">{{ item.name }}</li>
</template>
```

Reference: https://cn.vuejs.org/guide/essentials/list.html
