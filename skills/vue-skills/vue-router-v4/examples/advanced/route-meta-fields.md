# Route Meta Fields | 路由元信息

**官方文档**: https://router.vuejs.org/guide/advanced/meta.html


## Instructions

This example demonstrates how to use route meta fields to attach custom data to routes.

### Key Concepts

- Defining meta fields in route configuration
- Accessing meta in components
- Using meta in navigation guards
- TypeScript support for meta

### Example: Defining Meta Fields

```javascript
const routes = [
  {
    path: '/dashboard',
    component: Dashboard,
    meta: {
      requiresAuth: true,
      title: 'Dashboard',
      roles: ['admin', 'user']
    }
  },
  {
    path: '/admin',
    component: Admin,
    meta: {
      requiresAuth: true,
      requiresAdmin: true,
      title: 'Admin Panel'
    }
  }
]
```

### Example: Accessing Meta in Components

```vue
<template>
  <div>
    <h1>{{ route.meta.title }}</h1>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>
```

### Example: Using Meta in Guards

```javascript
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isAuthenticated()) {
    next({ name: 'Login' })
  } else if (to.meta.requiresAdmin && !isAdmin()) {
    next({ name: 'Forbidden' })
  } else {
    next()
  }
})
```

### Example: TypeScript Meta Types

```typescript
// router/index.ts
import 'vue-router'

declare module 'vue-router' {
  interface RouteMeta {
    requiresAuth?: boolean
    requiresAdmin?: boolean
    title?: string
    roles?: string[]
  }
}

const routes = [
  {
    path: '/dashboard',
    meta: {
      requiresAuth: true,
      title: 'Dashboard'
    }
  }
]
```

### Key Points

- Meta fields are arbitrary data attached to routes
- Access via `route.meta` in components or guards
- Useful for permissions, titles, breadcrumbs, etc.
- Can be typed with TypeScript
- Available in all route-related contexts
