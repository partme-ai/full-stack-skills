---
name: vue-router
description: Provides comprehensive guidance for Vue Router including route configuration, navigation, dynamic routes, nested routes, route guards, programmatic navigation, and route meta. Use when the user asks about Vue Router, needs to set up routing, implement navigation guards, handle route parameters, or manage route transitions.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- 在 Vue 项目中配置路由、动态路由、守卫与懒加载
- 使用 Vue Router 4（Vue 3）或 3.x（Vue 2）API

## How to use this skill

1. **配置**：createRouter、routes、history 模式；router-link、router-view、useRouter。
2. **进阶**：动态路由、嵌套路由、beforeEach 守卫、meta；懒加载 component: () => import()。
3. **参考**：https://router.vuejs.org/

## Best Practices

- 路由与权限在守卫中集中处理；大页面懒加载。
- 命名路由与 params/query 规范；避免在路由中存敏感数据。

## Keywords

vue router, 路由, 守卫, Vue 3, Vue 2
