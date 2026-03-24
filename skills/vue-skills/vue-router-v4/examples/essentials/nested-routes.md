# Nested Routes | 嵌套路由

**官方文档**: https://router.vuejs.org/guide/essentials/nested-routes.html


## Instructions

This example demonstrates how to create nested routes with child routes and nested RouterView components.

### Key Concepts

- Nested routes with `children` property
- Nested RouterView components
- Relative paths in nested routes
- Empty path for nested index routes

### Example: Basic Nested Routes

```javascript
// router/index.js
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      {
        // UserProfile will be rendered inside User's <router-view>
        // when /user/:id/profile is matched
        path: 'profile',
        component: UserProfile
      },
      {
        // UserPosts will be rendered inside User's <router-view>
        // when /user/:id/posts is matched
        path: 'posts',
        component: UserPosts
      }
    ]
  }
]
```

```vue
<!-- User.vue -->
<template>
  <div class="user">
    <h2>User {{ $route.params.id }}</h2>
    <router-view />
  </div>
</template>
```

### Example: Nested Index Route

```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      {
        // Empty path for nested index route
        path: '',
        component: UserHome
      },
      {
        path: 'profile',
        component: UserProfile
      },
      {
        path: 'posts',
        component: UserPosts
      }
    ]
  }
]
```

### Example: Absolute Paths in Nested Routes

```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      {
        // Relative path (default)
        path: 'profile',
        component: UserProfile
      },
      {
        // Absolute path (starts with /)
        path: '/settings',
        component: Settings
      }
    ]
  }
]
```

### Example: Multiple Levels of Nesting

```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      {
        path: 'posts',
        component: UserPosts,
        children: [
          {
            path: ':postId',
            component: PostDetail
          }
        ]
      }
    ]
  }
]
```

### Example: Using Composition API

```vue
<!-- User.vue -->
<template>
  <div class="user">
    <h2>User {{ route.params.id }}</h2>
    <RouterView />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { RouterView } from 'vue-router'

const route = useRoute()
</script>
```

### Key Points

- Use `children` property to define nested routes
- Nested routes require a `RouterView` in the parent component
- Child route paths are relative to the parent by default
- Use empty path `''` for nested index routes
- Absolute paths (starting with `/`) ignore parent path
- Can nest multiple levels deep
