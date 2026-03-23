# Named Routes | 命名路由

**官方文档**: https://router.vuejs.org/guide/essentials/named-routes.html


## Instructions

This example demonstrates how to use named routes for navigation and route configuration.

### Key Concepts

- Defining named routes with `name` property
- Navigating to named routes
- Benefits of named routes
- Using named routes with params and query

### Example: Defining Named Routes

```javascript
// router/index.js
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/user/:id',
    name: 'User',
    component: User
  },
  {
    path: '/user/:id/posts/:postId',
    name: 'UserPost',
    component: UserPost
  }
]
```

### Example: Navigating to Named Routes

```javascript
// Using router.push()
router.push({ name: 'Home' })
router.push({ name: 'User', params: { id: '123' } })
router.push({ name: 'UserPost', params: { id: '123', postId: '456' } })

// Using RouterLink
<RouterLink :to="{ name: 'Home' }">Home</RouterLink>
<RouterLink :to="{ name: 'User', params: { id: '123' } }">User</RouterLink>
```

### Example: Named Routes with Query

```javascript
router.push({
  name: 'User',
  params: { id: '123' },
  query: { tab: 'profile' }
})
```

### Example: Using in Components

```vue
<template>
  <div>
    <RouterLink :to="{ name: 'Home' }">Home</RouterLink>
    <RouterLink :to="{ name: 'User', params: { id: userId } }">
      User Profile
    </RouterLink>
    <button @click="goToUser">Go to User</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const userId = '123'

function goToUser() {
  router.push({ name: 'User', params: { id: userId } })
}
</script>
```

### Example: Benefits of Named Routes

```javascript
// Without named routes (fragile - breaks if path changes)
router.push('/user/123')

// With named routes (robust - path can change, name stays the same)
router.push({ name: 'User', params: { id: '123' } })
```

### Example: TypeScript with Named Routes

```typescript
// router/index.ts
import { RouteRecordRaw } from 'vue-router'

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

export default routes
```

### Key Points

- Use `name` property to define named routes
- Named routes make navigation more maintainable
- Paths can change without breaking navigation code
- Can combine with params and query
- Better for refactoring and large applications
- TypeScript support for typed route names
