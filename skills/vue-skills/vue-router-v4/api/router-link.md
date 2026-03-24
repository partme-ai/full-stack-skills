# RouterLink | 路由链接组件

**官方文档**: https://router.vuejs.org/api/#routerlink

## 常用属性
- `to` / `replace` / `custom`
- `active-class` / `exact-active-class`

## 示例
```vue
<template>
  <RouterLink :to="{ name: 'Home' }">Home</RouterLink>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>
```
