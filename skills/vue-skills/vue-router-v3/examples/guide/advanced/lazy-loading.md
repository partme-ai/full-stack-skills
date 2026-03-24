## Instructions

- Use dynamic imports for route components.
- Split bundles by route.
- Use webpackChunkName for naming chunks.

### Example

```js
const User = () => import(/* webpackChunkName: "user" */ './User.vue')

const routes = [
  { path: '/user/:id', component: User }
]
```

Reference: https://v3.router.vuejs.org/guide/advanced/lazy-loading.html
