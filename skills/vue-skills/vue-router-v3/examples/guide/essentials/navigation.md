## Instructions

- Use <router-link> for declarative navigation.
- Use this.$router.push for programmatic navigation.
- Prefer named routes for maintainability.

### Example

```html
<router-link :to="{ name: 'profile', params: { id: 1 } }">Profile</router-link>
```

### Example

```js
export default {
  methods: {
    // Navigate to profile
    goProfile() {
      this.$router.push({ name: 'profile', params: { id: 1 } })
    }
  }
}
```

Reference: https://v3.router.vuejs.org/guide/essentials/navigation.html
