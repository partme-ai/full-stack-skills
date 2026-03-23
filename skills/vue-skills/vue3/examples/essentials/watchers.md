## Instructions

- Use watch() for side effects.
- Use watchEffect() for automatic dependency tracking.
- Use the immediate option when needed.

### Example

```vue
<script setup>
import { ref, watch } from 'vue'

const count = ref(0)

// Watch changes to count
watch(count, (value) => {
  console.log('count changed:', value)
})
</script>
```

Reference: https://cn.vuejs.org/guide/essentials/watchers.html
