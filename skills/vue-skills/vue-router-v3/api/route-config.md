## Instructions

Use this API section to confirm options for `route config`.

## Examples

```js
const routes = [
  { path: '/', component: Home },
  { path: '/user/:id', name: 'user', component: User, props: true }
]
```

```js
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      { path: 'profile', component: UserProfile }
    ]
  }
]
```

## Scenarios

### Nested user routes

- Use children for nested UI.
- Keep child paths relative.

```js
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      { path: 'profile', component: UserProfile },
      { path: 'posts', component: UserPosts }
    ]
  }
]
```

### Passing props

- Use props: true to simplify components.
- Avoid direct $route usage in components.

```js
{ path: '/user/:id', component: User, props: true }
```

Reference: https://v3.router.vuejs.org/api/#routes

## Parameters

- `path` (string) - URL path pattern.
- `component` / `components` - Component(s) to render.
- `name` (string) - Named route.
- `children` (Array<RouteConfig>) - Nested routes.
- `redirect` / `alias` - Routing aliases.
- `props` (boolean | object | function) - Pass props.

## Returns

- Defines how URLs map to components.
- Nested routes create nested UI via router-view.

## Common Errors

- Missing leading slash in path for top-level routes.
- Conflicting paths lead to unexpected matches.

## Best Practices

- Use names for stable navigation.
- Prefer lazy loading for large route components.
