## Instructions

- Use interpolation for text output.
- Use v-bind and v-on (or shorthands) for bindings and events.
- Use directives for conditional and list rendering.

### Example

```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)
const label = ref('Increment')

// Handle button click
function increment() {
  count.value += 1
}
</script>

<template>
  <button :title="label" @click="increment">{{ count }}</button>
</template>
```

Reference: https://cn.vuejs.org/guide/essentials/template-syntax.html
