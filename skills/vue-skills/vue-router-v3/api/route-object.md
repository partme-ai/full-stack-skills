## Instructions

Use this API section to confirm options for `route object`.

## Examples

```js
export default {
  computed: {
    userId() {
      return this.$route.params.id
    }
  }
}
```

```js
router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(r => r.meta.requiresAuth)
  next(requiresAuth ? '/login' : true)
})
```

## Scenarios

### Reading params and query

- Prefer props for params when possible.
- Use $route.query for filters.

```js
export default {
  computed: {
    userId() { return this.$route.params.id },
    q() { return this.$route.query.q }
  }
}
```

### Meta-based access

- Use matched records to read meta.
- Centralize access checks in guards.

```js
const requiresAuth = this.$route.matched.some(r => r.meta.requiresAuth)
```

Reference: https://v3.router.vuejs.org/api/#the-route-object

## Parameters

- `$route.path` - Current path.
- `$route.params` - Dynamic params.
- `$route.query` - Query parameters.
- `$route.hash` - Hash fragment.
- `$route.matched` - Matched route records.

## Returns

- Route object describes the current location.
- Reactive and updates on navigation.

## Common Errors

- Directly mutating $route is unsupported.
- Reading params not defined on route yields undefined.

## Best Practices

- Prefer props over $route where possible.
- Use matched records for meta checks.
