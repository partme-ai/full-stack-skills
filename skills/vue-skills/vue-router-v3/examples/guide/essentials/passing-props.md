## Instructions

- Use props: true to pass params as props.
- Use function mode for custom mapping.
- Prefer props over $route in components.

### Example

```js
const routes = [
  { path: '/user/:id', component: User, props: true }
]
```

### Example

```js
{ path: '/search', component: Search, props: route => ({ q: route.query.q }) }
```

Reference: https://v3.router.vuejs.org/guide/essentials/passing-props.html
