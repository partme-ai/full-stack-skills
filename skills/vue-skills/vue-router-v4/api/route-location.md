# RouteLocation | 路由位置类型

**官方文档**: https://router.vuejs.org/api/#routelocationraw

## 关键类型
- `RouteLocationRaw`
- `RouteLocationNormalized`

## 示例
```ts
// buildLocation(): 构建路由位置对象
function buildLocation(id: string): RouteLocationRaw {
  return { name: 'User', params: { id } }
}
```
