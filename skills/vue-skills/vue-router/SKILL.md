---
name: vue-router
description: "Provides comprehensive guidance for Vue Router including route configuration, navigation, dynamic routes, nested routes, route guards, programmatic navigation, and route meta. Use when the user asks about Vue Router, needs to set up routing, implement navigation guards, handle route parameters, or manage route transitions."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Configure routing in Vue 2 or Vue 3 projects
- Implement dynamic routes, nested routes, and named routes
- Set up navigation guards (beforeEach, beforeResolve, afterEach)
- Use programmatic navigation with `router.push`, `router.replace`
- Implement lazy-loaded routes for code splitting
- Handle route meta fields for permissions and layout control

## How to use this skill

### Workflow

1. **Identify the Vue version** (Vue 2 uses Vue Router 3.x, Vue 3 uses Vue Router 4.x)
2. **Configure routes** with the appropriate API
3. **Add navigation guards** for authentication and authorization
4. **Implement lazy loading** for large page components

### 1. Vue Router 4 (Vue 3) Setup

```typescript
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  { path: '/', component: () => import('./views/Home.vue') },
  { path: '/users/:id', component: () => import('./views/UserDetail.vue'), props: true },
  {
    path: '/admin',
    component: () => import('./views/Admin.vue'),
    meta: { requiresAuth: true },
    children: [
      { path: 'dashboard', component: () => import('./views/AdminDashboard.vue') },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation guard
router.beforeEach((to, from) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {
    return { path: '/login' };
  }
});

export default router;
```

### 2. Vue Router 3 (Vue 2) Setup

```javascript
import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: () => import('./views/Home.vue') },
    { path: '/about', component: () => import('./views/About.vue') },
  ],
});
```

### 3. Programmatic Navigation

```typescript
// Vue 3 with Composition API
import { useRouter } from 'vue-router';

const router = useRouter();
router.push({ name: 'user', params: { id: '123' } });
router.replace('/home');
router.go(-1);
```

## Best Practices

- Centralize route guards for permission checks; lazy-load large page components
- Use named routes with `params`/`query` for type-safe navigation; avoid storing sensitive data in routes
- Prefer `createWebHistory` for clean URLs; configure server-side fallback for HTML5 history mode
- Use route `meta` fields for layout control, breadcrumbs, and access control

## Resources

- Vue Router 4: https://router.vuejs.org/
- Vue Router 3: https://v3.router.vuejs.org/

## Keywords

vue router, routing, navigation guards, Vue 3, Vue 2, lazy loading, dynamic routes, nested routes, meta fields, programmatic navigation, createRouter
