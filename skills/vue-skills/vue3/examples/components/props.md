## Instructions

- Define props with types and defaults.
- Treat props as read-only.
- Validate inputs when needed.

### Example

```vue
<script setup>
const props = defineProps({
  title: { type: String, required: true }
})
</script>

<template>
  <h3>{{ props.title }}</h3>
</template>
```

Reference: https://cn.vuejs.org/guide/components/props.html
