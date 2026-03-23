## Instructions

- Give routes a name for stable navigation.
- Use name in router-link and router.push.
- Prefer names over hard-coded paths.

### Example

```js
const routes = [
  { path: '/user/:id', name: 'user', component: User }
]
```

### Example

```js
this.$router.push({ name: 'user', params: { id: 123 } })
```

Reference: https://v3.router.vuejs.org/guide/essentials/named-routes.html
