# Redirect and Alias | 重定向和别名

**官方文档**: https://router.vuejs.org/guide/essentials/redirect-and-alias.html


## Instructions

This example demonstrates how to use redirects and aliases in Vue Router.

### Key Concepts

- Redirects with `redirect` property
- Aliases with `alias` property
- Named redirects
- Function redirects
- Multiple aliases

### Example: Basic Redirect

```javascript
const routes = [
  {
    path: '/home',
    redirect: '/'
  },
  {
    path: '/old-path',
    redirect: '/new-path'
  }
]
```

### Example: Named Route Redirect

```javascript
const routes = [
  {
    path: '/home',
    redirect: { name: 'Home' }
  }
]
```

### Example: Function Redirect

```javascript
const routes = [
  {
    path: '/user/:id',
    redirect: (to) => {
      // Redirect to a different path based on route params
      return { path: `/profile/${to.params.id}` }
    }
  }
]
```

### Example: Alias

```javascript
const routes = [
  {
    path: '/',
    component: Home,
    alias: '/home'
  },
  {
    path: '/user/:id',
    component: User,
    alias: '/u/:id'
  }
]
```

### Example: Multiple Aliases

```javascript
const routes = [
  {
    path: '/',
    component: Home,
    alias: ['/home', '/index', '/main']
  }
]
```

### Example: Alias with Nested Routes

```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    alias: '/u/:id',
    children: [
      {
        path: 'profile',
        alias: ['profile', 'p'],
        component: UserProfile
      }
    ]
  }
]
```

### Key Points

- Redirects navigate to a different route
- Aliases allow multiple paths to render the same component
- Redirects change the URL, aliases keep the original URL
- Can use string paths, named routes, or functions for redirects
- Aliases can be a string or array of strings
- Useful for maintaining backward compatibility and SEO
