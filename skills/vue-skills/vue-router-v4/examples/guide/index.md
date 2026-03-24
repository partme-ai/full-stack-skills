# Vue Router 概览 | Overview

**官方文档**: https://router.vuejs.org/

## 适用场景
- 了解 Vue Router 4 的核心能力与定位
- 确认 Vue 3 应用的路由选型与能力边界

## 核心要点
- Vue 3 官方路由方案
- 支持历史模式与哈希模式
- 支持导航守卫、懒加载、路由元信息与过渡

## 快速示例
```ts
// createRouter(): 创建路由器实例
const router = createRouter({
  history: createWebHistory(),
  routes: []
})
```
