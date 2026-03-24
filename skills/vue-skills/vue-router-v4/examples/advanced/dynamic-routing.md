# Dynamic Routing | 动态路由

**官方文档**: https://router.vuejs.org/guide/advanced/dynamic-routing.html

## 适用场景
- 根据权限动态添加路由
- 运行时移除不需要的路由

## 核心用法
```ts
// addAdminRoutes(): 按权限添加路由
function addAdminRoutes() {
  router.addRoute({
    path: '/admin',
    name: 'Admin',
    component: () => import('@/views/Admin.vue')
  })
}

// removeAdminRoutes(): 移除路由
function removeAdminRoutes() {
  router.removeRoute('Admin')
}
```
