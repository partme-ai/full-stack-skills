# Navigation Failures | 导航失败

**官方文档**: https://router.vuejs.org/guide/advanced/navigation-failures.html

## 适用场景
- 处理重复导航与导航被取消
- 统一错误提示与埋点

## 核心用法
```ts
import { isNavigationFailure, NavigationFailureType } from 'vue-router'

// handleNavigation(): 处理导航失败
async function handleNavigation() {
  const failure = await router.push('/dashboard')
  if (isNavigationFailure(failure, NavigationFailureType.duplicated)) {
    console.warn('重复导航被忽略')
  }
}
```
