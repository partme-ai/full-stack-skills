## Instructions

- Use ref() for primitives and reactive() for objects.
- Access ref values with .value in script.
- Let Vue track dependencies automatically.

### Example

```vue
<script setup>
import { ref, reactive } from 'vue'

const count = ref(0)
const user = reactive({ name: 'Vue' })

// Update reactive state
function increment() {
  count.value += 1
}
</script>

<template>
  <p>{{ user.name }}: {{ count }}</p>
  <button @click="increment">+1</button>
</template>
```

Reference: https://cn.vuejs.org/guide/essentials/reactivity-fundamentals.html
