# Router | 路由器实例

**官方文档**: https://router.vuejs.org/api/#router

## 关键 API
- `createRouter()`
- `router.push()` / `router.replace()` / `router.go()`
- `router.addRoute()` / `router.removeRoute()` / `router.hasRoute()` / `router.getRoutes()`
- `router.currentRoute`

## 示例
```ts
// createAppRouter(): 创建路由器实例
export function createAppRouter() {
  return createRouter({
    history: createWebHistory(),
    routes
  })
}

// navigateToUser(): 编程式导航
function navigateToUser(id: string) {
  return router.push({ name: 'User', params: { id } })
}
```
