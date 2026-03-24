## Instructions

Use this API section to confirm options for `router options`.

## Examples

```js
const router = new VueRouter({
  mode: 'history',
  base: '/app/',
  routes
})
```

```js
const router = new VueRouter({
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { x: 0, y: 0 }
  }
})
```

## Scenarios

### History mode on production

- Enable history mode for clean URLs.
- Ensure server rewrite to index.html.

```js
const router = new VueRouter({
  mode: 'history',
  routes
})
```

### Scroll restoration

- Restore saved position on back/forward.
- Reset to top on new navigation.

```js
const router = new VueRouter({
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { x: 0, y: 0 }
  }
})
```

Reference: https://v3.router.vuejs.org/api/#router-options

## Parameters

- `routes` (Array<RouteConfig>) - Route definitions.
- `mode` (string) - `hash` or `history`.
- `base` (string) - Base URL for the app.
- `scrollBehavior` (function) - Scroll restoration.
- `linkActiveClass` / `linkExactActiveClass` - Global classes.

## Returns

- Creates a router instance with the provided configuration.

## Common Errors

- History mode without server fallback causes 404 on refresh.
- Incorrect base leads to broken links.

## Best Practices

- Use history mode with proper server rewrite.
- Centralize scrollBehavior for SPA UX.
