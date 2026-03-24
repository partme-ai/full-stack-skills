## Instructions

- Use global guards for auth checks.
- Use per-route and in-component guards.
- Always call next() to resolve navigation.

### Example

```js
router.beforeEach((to, from, next) => {
  // Check auth
  if (to.meta.requiresAuth && !isLoggedIn()) {
    next('/login')
  } else {
    next()
  }
})
```

### Example

```js
export default {
  beforeRouteLeave(to, from, next) {
    // confirm leave
    next()
  }
}
```

Reference: https://v3.router.vuejs.org/guide/advanced/navigation-guards.html
