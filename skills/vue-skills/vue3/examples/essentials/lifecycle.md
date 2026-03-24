## Instructions

- Use lifecycle hooks for side effects.
- Keep mount/unmount logic paired.
- Avoid heavy work in render.

### Example

```vue
<script setup>
import { onMounted, onUnmounted } from 'vue'

// Initialize on mount
onMounted(() => {
  console.log('mounted')
})

// Cleanup on unmount
onUnmounted(() => {
  console.log('unmounted')
})
</script>
```

Reference: https://cn.vuejs.org/guide/essentials/lifecycle.html
