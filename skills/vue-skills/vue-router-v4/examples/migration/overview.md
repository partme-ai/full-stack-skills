# Migration | 迁移指南

**官方文档**: https://router.vuejs.org/guide/migration/

## 适用场景
- 从 Vue Router 3 迁移到 Vue Router 4

## 关键迁移点
- `new VueRouter()` → `createRouter()`
- `mode: 'history'` → `createWebHistory()`
- `base` → `createWebHistory(base)`
- 组件与 API 接口名称变更
