# RouterView Slot | RouterView 插槽

**官方文档**: https://router.vuejs.org/guide/advanced/router-view-slot.html

## 适用场景
- 自定义路由视图渲染
- 控制过渡与缓存策略

## 核心用法
```vue
<template>
  <RouterView v-slot="{ Component, route }">
    <!-- renderKey(): 生成稳定的渲染 key -->
    <component :is="Component" :key="renderKey(route)" />
  </RouterView>
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router'

// renderKey(): 根据路由生成 key
const renderKey = (route: any) => route.fullPath
</script>
```
