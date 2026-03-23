# Navigation Failures | 导航失败

**官方文档**: https://router.vuejs.org/api/#navigationfailure

## 关键 API
- `NavigationFailureType`
- `isNavigationFailure()`

## 示例
```ts
// handleFailure(): 处理导航失败
async function handleFailure() {
  const failure = await router.push('/dashboard')
  if (isNavigationFailure(failure, NavigationFailureType.duplicated)) {
    console.warn('重复导航被忽略')
  }
}
```
