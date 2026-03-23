## Instructions

- Use $attrs to pass through attributes.
- Control inheritAttrs when necessary.
- Avoid leaking unintended attributes.

### Example

```vue
<script setup>
defineOptions({ inheritAttrs: false })
</script>

<template>
  <button v-bind="$attrs">Button</button>
</template>
```

Reference: https://cn.vuejs.org/guide/components/attrs.html
