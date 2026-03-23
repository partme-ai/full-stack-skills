## Instructions

- Introduce core routing concepts.
- Explain route mapping and router-view.
- Use as the entry point for all guide topics.

### Example

```js
// routes.js
export const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About }
]
```

### Example

```html
<router-view />
```

### Notes

- Use <router-link> for navigation.

Reference: https://v3.router.vuejs.org/guide/
