## Instructions

- Fetch data before navigation or in component.
- Handle loading states.
- Cancel stale requests on route change.

### Example

```js
export default {
  data() { return { loading: false, post: null } },
  watch: {
    '$route.params.id': {
      immediate: true,
      handler(id) {
        // fetch post by id
      }
    }
  }
}
```

Reference: https://v3.router.vuejs.org/guide/advanced/data-fetching.html
