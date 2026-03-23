## Instructions

Use this API section to confirm options for `router view`.

## Examples

```html
<router-view />
<router-view name="sidebar" />
```

```js
const routes = [
  {
    path: '/dashboard',
    components: {
      default: Dashboard,
      sidebar: Sidebar
    }
  }
]
```

## Scenarios

### Layout with sidebar

- Render default and named views for layout regions.
- Keep layout components thin.

```html
<router-view />
<router-view name="sidebar" />
```

### Nested routes outlet

- Place router-view inside parent to render children.
- Use nested routes for sub-sections.

```html
<!-- Parent.vue -->
<router-view />
```

Reference: https://v3.router.vuejs.org/api/#router-view

## Parameters

- `name` (string) - Named view to render (default: `default`).

## Returns

- Renders the matched component for the current route.
- Supports named views for multiple outlets.

## Common Errors

- Missing `<router-view>` yields no route component output.
- Name mismatch prevents named view from rendering.

## Best Practices

- Keep a single router-view per layout region.
- Use named views only when needed.
