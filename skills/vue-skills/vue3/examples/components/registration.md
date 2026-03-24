## Instructions

- Register components globally or locally.
- Prefer local registration for tree-shaking.
- Use PascalCase for component names.

### Example

```vue
<script setup>
import BaseButton from './BaseButton.vue'
</script>

<template>
  <BaseButton />
</template>
```

Reference: https://cn.vuejs.org/guide/components/registration.html
