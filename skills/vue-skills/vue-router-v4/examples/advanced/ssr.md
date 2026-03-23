# SSR | 服务端渲染

**官方文档**: https://router.vuejs.org/guide/advanced/ssr.html

## 适用场景
- SSR 应用路由初始化
- 为每个请求创建独立路由实例

## 核心用法
```ts
import { createMemoryHistory, createRouter } from 'vue-router'

// createSsrRouter(): 为 SSR 请求创建路由实例
export function createSsrRouter() {
  return createRouter({
    history: createMemoryHistory(),
    routes
  })
}
```
