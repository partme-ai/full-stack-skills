## Instructions

- Use v-model for two-way binding.
- Pair v-model with correct input types.
- Normalize values in script when needed.

### Example

```vue
<script setup>
import { ref } from 'vue'

const text = ref('')
</script>

<template>
  <input v-model="text" />
  <p>{{ text }}</p>
</template>
```

Reference: https://cn.vuejs.org/guide/essentials/forms.html
