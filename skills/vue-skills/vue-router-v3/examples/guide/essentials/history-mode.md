## Instructions

- Enable history mode for clean URLs.
- Ensure server fallback to index.html.
- Use hash mode when server config is not possible.

### Example

```js
const router = new VueRouter({
  mode: 'history',
  routes
})
```

### Example

```md
Server must redirect all routes to index.html
```

Reference: https://v3.router.vuejs.org/guide/essentials/history-mode.html
