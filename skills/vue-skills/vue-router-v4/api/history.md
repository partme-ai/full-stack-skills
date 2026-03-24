# History | 历史模式 API

**官方文档**: https://router.vuejs.org/api/#history

## 关键 API
- `createWebHistory()`
- `createWebHashHistory()`
- `createMemoryHistory()`

## 示例
```ts
// createHistory(): 根据环境创建 History
function createHistory() {
  return import.meta.env.SSR
    ? createMemoryHistory()
    : createWebHistory()
}
```
