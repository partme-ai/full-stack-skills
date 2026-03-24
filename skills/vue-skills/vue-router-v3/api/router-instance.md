## Instructions

Use this API section to confirm options for `router instance`.

## Examples

```js
// programmatic navigation
this.$router.push({ name: 'user', params: { id: 1 } })
this.$router.replace('/login')
```

```js
// global guard
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isLoggedIn()) {
    next('/login')
  } else {
    next()
  }
})
```

## Scenarios

### Guarded routes

- Check meta flags before navigation.
- Redirect to login when unauthenticated.

```js
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isLoggedIn()) {
    next('/login')
  } else {
    next()
  }
})
```

### Error handling

- Handle NavigationDuplicated errors gracefully.
- Avoid unhandled promise rejections.

```js
this.$router.push('/same').catch(() => {})
```

Reference: https://v3.router.vuejs.org/api/#router-instance

## Parameters

- `router.push(location)` - Navigate to a new route.
- `router.replace(location)` - Replace current history entry.
- `router.go(n)` - Move forward/back in history.
- `router.back()` / `router.forward()` - History helpers.
- `router.beforeEach(fn)` - Global guard.
- `router.afterEach(fn)` - Global after hook.

## Returns

- Most navigation methods return a Promise.
- Guards return control via `next()` callbacks.

## Common Errors

- Unhandled NavigationDuplicated errors on same route.
- Missing `next()` in guards causes navigation to hang.

## Best Practices

- Use named routes for push/replace.
- Handle promise rejections from push/replace.
- Keep guards minimal and async-safe.
