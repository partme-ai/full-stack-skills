# Composables | 组合式 API

**官方文档**: https://router.vuejs.org/api/#userouter

## 关键 API
- `useRouter()` / `useRoute()`
- `onBeforeRouteLeave()` / `onBeforeRouteUpdate()`

## 示例
```ts
// useRouteInfo(): 读取当前路由信息
function useRouteInfo() {
  const router = useRouter()
  const route = useRoute()
  return { router, route }
}
```
