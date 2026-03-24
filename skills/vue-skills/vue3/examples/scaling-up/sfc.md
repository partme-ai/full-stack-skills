## Instructions

- Use .vue files to co-locate template, script, and style.
- Prefer <script setup> for Composition API.
- Use scoped styles when appropriate.

### Example

```vue
<script setup>
const title = 'SFC'
</script>

<template>
  <h1>{{ title }}</h1>
</template>

<style scoped>
 h1 { color: #42b883; }
</style>
```

Reference: https://cn.vuejs.org/guide/scaling-up/sfc.html
