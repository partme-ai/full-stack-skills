# Dynamic Route Matching | 动态路由匹配

**官方文档**: https://router.vuejs.org/guide/essentials/dynamic-matching.html


## Instructions

This example demonstrates how to use dynamic route parameters and query strings in Vue Router.

### Key Concepts

- Dynamic route parameters with `:param`
- Accessing route params with `$route.params` or `useRoute()`
- Route query strings
- Multiple dynamic segments
- Optional parameters

### Example: Basic Dynamic Route

```javascript
// router/index.js
const routes = [
  {
    path: '/user/:id',
    name: 'User',
    component: User
  }
]
```

```vue
<!-- User.vue -->
<template>
  <div>
    <h1>User {{ $route.params.id }}</h1>
  </div>
</template>
```

### Example: Multiple Dynamic Segments

```javascript
const routes = [
  {
    path: '/user/:username/post/:postId',
    name: 'UserPost',
    component: UserPost
  }
]
```

```vue
<!-- UserPost.vue -->
<template>
  <div>
    <h1>User: {{ $route.params.username }}</h1>
    <h2>Post: {{ $route.params.postId }}</h2>
  </div>
</template>
```

### Example: Using Composition API

```vue
<!-- User.vue -->
<template>
  <div>
    <h1>User {{ route.params.id }}</h1>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>
```

### Example: Route Query Strings

```javascript
// Navigation with query
router.push({ path: '/search', query: { q: 'vue' } })
// Results in: /search?q=vue
```

```vue
<!-- Search.vue -->
<template>
  <div>
    <h1>Search: {{ $route.query.q }}</h1>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
const searchQuery = route.query.q
</script>
```

### Example: Optional Parameters

```javascript
const routes = [
  {
    path: '/user/:id?',
    name: 'User',
    component: User
  }
]
```

### Example: Reacting to Route Changes

```vue
<!-- User.vue -->
<template>
  <div>
    <h1>User {{ userId }}</h1>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { computed, watch } from 'vue'

const route = useRoute()
const userId = computed(() => route.params.id)

// Watch for route changes
watch(() => route.params.id, (newId, oldId) => {
  // Fetch new user data
  console.log(`User changed from ${oldId} to ${newId}`)
})
</script>
```

### Key Points

- Dynamic segments start with `:` (e.g., `:id`)
- Access params via `$route.params` (Options API) or `useRoute().params` (Composition API)
- Query strings are accessed via `$route.query` or `useRoute().query`
- Use `watch` to react to route parameter changes
- Optional parameters use `?` (e.g., `:id?`)
