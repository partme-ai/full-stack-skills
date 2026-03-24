## Instructions

Use this API section to confirm options for `navigation guards`.

## Examples

```js
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !isLoggedIn()) {
    next('/login')
  } else {
    next()
  }
})
```

```js
export default {
  beforeRouteLeave(to, from, next) {
    // confirm leave
    next()
  }
}
```

## Scenarios

### Auth and role checks

- Use global guards with meta roles.
- Redirect or block appropriately.

```js
router.beforeEach((to, from, next) => {
  const role = getUserRole()
  if (to.meta.role && to.meta.role !== role) {
    next('/403')
  } else {
    next()
  }
})
```

### Unsaved changes

- Use beforeRouteLeave for confirmation.
- Prevent accidental navigation loss.

```js
export default {
  beforeRouteLeave(to, from, next) {
    const ok = window.confirm('Discard changes?')
    next(ok)
  }
}
```

Reference: https://v3.router.vuejs.org/api/#navigation-guards

## Parameters

- `beforeEach` / `beforeResolve` / `afterEach` - Global hooks.
- `beforeEnter` - Per-route guard.
- `beforeRouteEnter` / `beforeRouteUpdate` / `beforeRouteLeave` - In-component.

## Returns

- Guards control navigation flow via `next()`.
- After hooks run after navigation completes.

## Common Errors

- Not calling next() blocks navigation.
- Calling next() multiple times causes errors.

## Best Practices

- Use meta fields to centralize access control.
- Prefer async/await with try/catch in guards.
