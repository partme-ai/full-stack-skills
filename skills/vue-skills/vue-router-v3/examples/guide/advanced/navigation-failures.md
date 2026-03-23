## Instructions

- Handle navigation failures from redundant navigation.
- Use router.onError or router.push().catch.
- Use isNavigationFailure when needed.

### Example

```js
this.$router.push('/same').catch(err => {
  // ignore NavigationDuplicated
})
```

Reference: https://v3.router.vuejs.org/guide/advanced/navigation-failures.html
