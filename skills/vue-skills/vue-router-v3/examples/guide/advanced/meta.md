## Instructions

- Attach meta fields to routes.
- Read meta in guards for access control.
- Use meta for titles or permissions.

### Example

```js
const routes = [
  { path: '/admin', component: Admin, meta: { requiresAuth: true } }
]
```

### Example

```js
router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(r => r.meta.requiresAuth)
  next(requiresAuth ? '/login' : true)
})
```

Reference: https://v3.router.vuejs.org/guide/advanced/meta.html
