# Typed Routes | 类型化路由

**官方文档**: https://router.vuejs.org/guide/advanced/typed-routes.html


## Instructions

This example demonstrates how to use TypeScript with Vue Router for type-safe routing.

### Key Concepts

- TypeScript route types
- Typed route names
- Typed route params
- Typed route meta
- Type-safe navigation

### Example: Basic TypeScript Setup

```typescript
// router/index.ts
import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/user/:id',
    name: 'User',
    component: () => import('../views/User.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
```

### Example: Typed Route Names

```typescript
// types/router.d.ts
import 'vue-router'

declare module 'vue-router' {
  interface RouteNamedMap {
    'Home': RouteRecordInfo<'Home', '/', Record<never, never>, Record<never, never>>
    'User': RouteRecordInfo<'User', '/user/:id', { id: string }, Record<never, never>>
  }
}
```

### Example: Typed Navigation

```typescript
import { useRouter } from 'vue-router'

const router = useRouter()

// Type-safe navigation
router.push({ name: 'User', params: { id: '123' } })
```

### Example: Typed Route Params

```vue
<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()

// Type-safe params
const userId = route.params.id as string
</script>
```

### Key Points

- Use `RouteRecordRaw` for route definitions
- TypeScript provides type safety for routes
- Typed route names prevent typos
- Typed params ensure correct parameter types
- Better IDE autocomplete and error checking
