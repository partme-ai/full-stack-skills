# Installation | 安装

**官方文档**: https://router.vuejs.org/guide/installation.html

## 适用场景
- 新项目集成 Vue Router 4
- 升级到 Vue Router 4

## 安装
```bash
npm install vue-router@4
```

## 基础初始化
```ts
// createRouter(): 创建路由器实例
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// installRouter(): 将路由器注册到应用
app.use(router)
```
