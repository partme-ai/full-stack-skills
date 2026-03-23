## Instructions

- Use dynamic segments with params.
- Access params via $route.params.
- Update components when params change.

### Example

```js
const routes = [
  { path: '/user/:id', component: User }
]
```

### Example

```js
export default {
  // Handle param changes
  watch: {
    '$route.params.id'(id) {
      // fetch user with id
    }
  }
}
```

Reference: https://v3.router.vuejs.org/guide/essentials/dynamic-matching.html
