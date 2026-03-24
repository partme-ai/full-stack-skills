## Instructions

- Wrap router-view with <transition>.
- Use transition mode for proper sequencing.
- Use dynamic transitions if needed.

### Example

```html
<transition name="fade" mode="out-in">
  <router-view />
</transition>
```

Reference: https://v3.router.vuejs.org/guide/advanced/transitions.html
