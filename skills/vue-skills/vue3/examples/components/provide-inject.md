## Instructions

- Provide values at ancestor components.
- Inject in descendants without prop drilling.
- Use symbols or strings as keys.

### Example

```vue
<script setup>
import { provide } from 'vue'

// Provide a theme value
provide('theme', 'dark')
</script>
```

Reference: https://cn.vuejs.org/guide/components/provide-inject.html
