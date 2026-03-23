## Instructions

Use this API section to confirm options for `router link`.

## Examples

```html
<router-link :to="{ name: 'user', params: { id: 42 } }">
  User 42
</router-link>
```

```html
<router-link to="/about" exact>About</router-link>
```

## Scenarios

### Authentication-aware navigation

- Use named routes to avoid brittle paths.
- Use exact-active-class for precise styling.

```html
<router-link
  :to="{ name: 'dashboard' }"
  exact-active-class="is-active"
>
  Dashboard
</router-link>
```

### External links vs router-link

- Use <a> for external URLs.
- Keep router-link for internal navigation only.

```html
<a href="https://example.com" target="_blank" rel="noopener">Docs</a>
```

Reference: https://v3.router.vuejs.org/api/#router-link

## Parameters

- `to` (string | Location Object) - Target location.
- `tag` (string) - Rendered tag (default: `a`).
- `replace` (boolean) - Use `replace` instead of `push`.
- `append` (boolean) - Append to current path.
- `exact` (boolean) - Apply active class only on exact match.
- `active-class` / `exact-active-class` - Custom active classes.
- `event` (string | array) - Trigger events (default: `click`).

## Returns

- Renders a link component that updates route when activated.
- Applies active classes based on current route.

## Common Errors

- Using invalid `to` format leads to navigation errors.
- Forgetting `exact` causes active class to match child routes.

## Best Practices

- Prefer named routes in `to` for stability.
- Use `exact-active-class` for precise styling.
- Avoid nesting router-links inside anchors.
