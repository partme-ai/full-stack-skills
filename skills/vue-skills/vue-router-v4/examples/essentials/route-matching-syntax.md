# Routes Matching Syntax | 路由匹配语法

**官方文档**: https://router.vuejs.org/guide/essentials/route-matching-syntax.html


## Instructions

This example demonstrates advanced route matching patterns including catch-all routes, regex patterns, and optional parameters.

### Key Concepts

- Catch-all routes (`*`)
- Regex patterns in route paths
- Optional parameters
- Multiple parameters
- Route matching priority

### Example: Catch-All Routes

```javascript
// Match all routes
{
  path: '/:pathMatch(.*)*',
  name: 'NotFound',
  component: NotFound
}

// Match all routes under a prefix
{
  path: '/user/:pathMatch(.*)*',
  name: 'UserCatchAll',
  component: UserCatchAll
}
```

### Example: Regex Patterns

```javascript
// Only match numeric IDs
{
  path: '/user/:id(\\d+)',
  component: User
}

// Match specific pattern
{
  path: '/post/:year(\\d{4})/:month(\\d{2})',
  component: Post
}

// Multiple patterns
{
  path: '/:type(article|post)/:id',
  component: Content
}
```

### Example: Optional Parameters

```javascript
// Optional parameter
{
  path: '/user/:id?',
  component: User
}

// Optional with default
{
  path: '/user/:id?',
  component: User,
  props: (route) => ({ id: route.params.id || 'default' })
}
```

### Example: Multiple Parameters

```javascript
{
  path: '/user/:username/post/:postId',
  component: UserPost
}
```

### Example: Route Matching Priority

```javascript
const routes = [
  // More specific routes first
  {
    path: '/user/:id/posts',
    component: UserPosts
  },
  {
    path: '/user/:id',
    component: User
  },
  // Catch-all last
  {
    path: '/:pathMatch(.*)*',
    component: NotFound
  }
]
```

### Example: Using Regex in Components

```vue
<template>
  <div>
    <p>User ID: {{ $route.params.id }}</p>
    <p>Year: {{ $route.params.year }}</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
// route.params.id will only be set if it matches \d+
// route.params.year will only be set if it matches \d{4}
</script>
```

### Key Points

- Use `:pathMatch(.*)*` for catch-all routes
- Regex patterns use `:param(regex)` syntax
- Optional parameters use `?`
- More specific routes should be defined before catch-all routes
- Regex patterns must match the entire segment
- Use parentheses for capturing groups in regex
