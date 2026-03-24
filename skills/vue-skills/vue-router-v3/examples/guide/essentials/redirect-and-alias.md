## Instructions

- Use redirect to forward routes.
- Use alias to map multiple paths to same route.
- Keep redirects explicit.

### Example

```js
const routes = [
  { path: '/home', redirect: '/' },
  { path: '/user/:id', component: User, alias: '/u/:id' }
]
```

Reference: https://v3.router.vuejs.org/guide/essentials/redirect-and-alias.html
