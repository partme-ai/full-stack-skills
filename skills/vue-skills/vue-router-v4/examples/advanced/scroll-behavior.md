# Scroll Behavior | 滚动行为

**官方文档**: https://router.vuejs.org/guide/advanced/scroll-behavior.html


## Instructions

This example demonstrates how to configure scroll behavior when navigating between routes.

### Key Concepts

- Configuring scroll behavior in router options
- Scroll to top on navigation
- Preserving scroll position
- Smooth scrolling
- Custom scroll behavior

### Example: Basic Scroll Behavior

```javascript
const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    // Always scroll to top
    return { top: 0 }
  }
})
```

### Example: Preserve Scroll Position

```javascript
scrollBehavior(to, from, savedPosition) {
  if (savedPosition) {
    return savedPosition
  } else {
    return { top: 0 }
  }
}
```

### Example: Smooth Scrolling

```javascript
scrollBehavior(to, from, savedPosition) {
  if (savedPosition) {
    return savedPosition
  } else {
    return {
      top: 0,
      behavior: 'smooth'
    }
  }
}
```

### Example: Scroll to Element

```javascript
scrollBehavior(to, from, savedPosition) {
  if (to.hash) {
    return {
      el: to.hash,
      behavior: 'smooth'
    }
  }
  return { top: 0 }
}
```

### Key Points

- Configure in router options
- `savedPosition` is available when using browser back/forward
- Can return position object or Promise
- Use `el` to scroll to specific element
- Use `behavior: 'smooth'` for smooth scrolling
