## Instructions

- Implement scrollBehavior for saved position.
- Return coordinates or selector.
- Use for SPA scroll restoration.

### Example

```js
const router = new VueRouter({
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    return { x: 0, y: 0 }
  }
})
```

Reference: https://v3.router.vuejs.org/guide/advanced/scroll-behavior.html
