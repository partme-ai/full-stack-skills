## Instructions

- Use ref() with template refs for DOM access.
- Access refs after mount.
- Prefer refs over direct DOM queries.

### Example

```vue
<script setup>
import { ref, onMounted } from 'vue'

const inputRef = ref(null)

// Focus input after mount
onMounted(() => {
  inputRef.value?.focus()
})
</script>

<template>
  <input ref="inputRef" />
</template>
```

Reference: https://cn.vuejs.org/guide/essentials/template-refs.html
