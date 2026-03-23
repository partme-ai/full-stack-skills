# Data Fetching | 数据获取

**官方文档**: https://router.vuejs.org/guide/advanced/data-fetching.html

## 适用场景
- 进入路由前加载数据
- 路由参数变化时刷新数据

## 核心用法
```ts
// fetchUser(): 根据路由参数获取数据
async function fetchUser(id: string) {
  return await api.getUser(id)
}

// beforeEnter(): 进入路由前加载数据
const routes = [
  {
    path: '/users/:id',
    component: UserView,
    beforeEnter: async (to) => {
      to.meta.user = await fetchUser(String(to.params.id))
    }
  }
]
```

## 关键点
- 在进入路由前或组件内触发数据请求
- 配合 `watch(() => route.params)` 处理参数变化
