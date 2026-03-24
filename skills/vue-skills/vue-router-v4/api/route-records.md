# RouteRecordRaw | 路由记录

**官方文档**: https://router.vuejs.org/api/#routerecordraw

## 关键字段
- `path` / `name` / `component` / `children`
- `redirect` / `alias` / `meta`

## 示例
```ts
// buildRoutes(): 定义路由记录
function buildRoutes(): RouteRecordRaw[] {
  return [
    {
      path: '/users/:id',
      name: 'User',
      component: () => import('@/views/User.vue'),
      meta: { requiresAuth: true }
    }
  ]
}
```
