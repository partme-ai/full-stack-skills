# Lazy Loading Routes | 懒加载路由

**官方文档**: https://router.vuejs.org/guide/advanced/lazy-loading.html


## Instructions

This example demonstrates how to implement lazy loading for routes to enable code splitting and improve performance.

### Key Concepts

- Dynamic imports with `import()`
- Code splitting
- Route-level code splitting
- Grouping routes for chunking
- Webpack chunk names

### Example: Basic Lazy Loading

```javascript
// router/index.js
const routes = [
  {
    path: '/',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/about',
    component: () => import('../views/About.vue')
  }
]
```

### Example: Named Chunks

```javascript
const routes = [
  {
    path: '/user/:id',
    component: () => import(/* webpackChunkName: "user" */ '../views/User.vue')
  }
]
```

### Example: Grouping Routes

```javascript
const routes = [
  {
    path: '/user/:id',
    component: () => import(/* webpackChunkName: "user-group" */ '../views/User.vue')
  },
  {
    path: '/user/:id/posts',
    component: () => import(/* webpackChunkName: "user-group" */ '../views/UserPosts.vue')
  }
]
```

### Example: With Loading Component

```vue
<template>
  <Suspense>
    <template #default>
      <RouterView />
    </template>
    <template #fallback>
      <div>Loading...</div>
    </template>
  </Suspense>
</template>
```

### Example: Error Handling

```javascript
const routes = [
  {
    path: '/user/:id',
    component: () => import('../views/User.vue').catch(() => {
      // Handle import error
      return import('../views/Error.vue')
    })
  }
]
```

### Key Points

- Use dynamic `import()` for lazy loading
- Enables code splitting automatically
- Reduces initial bundle size
- Routes are loaded on-demand
- Can use webpack chunk names for grouping
- Works with Vite and other bundlers
