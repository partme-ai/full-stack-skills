# RouterOptions | 路由器配置

**官方文档**: https://router.vuejs.org/api/#routeroptions

## 关键字段
- `history`：历史模式实例
- `routes`：路由记录数组
- `scrollBehavior`：滚动行为

## 示例
```ts
// buildRouterOptions(): 构建路由配置
function buildRouterOptions() {
  return {
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
    scrollBehavior(to, from, savedPosition) {
      return savedPosition ?? { top: 0 }
    }
  }
}
```
