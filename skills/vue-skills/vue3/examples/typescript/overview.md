## Instructions

- Use TypeScript for type safety.
- Enable TS in Vite scaffolding.
- Use defineProps and defineEmits with types.

### Example

```vue
<script setup lang="ts">
interface Props {
  title: string
}

const props = defineProps<Props>()
</script>

<template>
  <h1>{{ props.title }}</h1>
</template>
```

Reference: https://cn.vuejs.org/guide/typescript/overview.html
