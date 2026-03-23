# Navigation Guards | 导航守卫

**官方文档**: https://router.vuejs.org/guide/advanced/navigation-guards.html


## Instructions

This example demonstrates how to use navigation guards to control navigation and perform actions before/after route changes.

### Key Concepts

- Global before guards (`beforeEach`)
- Global after guards (`afterEach`)
- Per-route guards (`beforeEnter`)
- In-component guards (`beforeRouteEnter`, `beforeRouteUpdate`, `beforeRouteLeave`)
- Navigation guard arguments and return values

### Example: Global Before Guard

```javascript
// router/index.js
router.beforeEach((to, from, next) => {
  // Check authentication
  if (to.meta.requiresAuth && !isAuthenticated()) {
    next({ name: 'Login' })
  } else {
    next()
  }
})
```

### Example: Global After Guard

```javascript
router.afterEach((to, from) => {
  // Log page views
  console.log(`Navigated from ${from.path} to ${to.path}`)
  
  // Send analytics
  analytics.track('page_view', {
    path: to.path,
    name: to.name
  })
})
```

### Example: Per-Route Guard

```javascript
const routes = [
  {
    path: '/dashboard',
    component: Dashboard,
    beforeEnter: (to, from, next) => {
      if (isAuthenticated()) {
        next()
      } else {
        next({ name: 'Login' })
      }
    }
  }
]
```

### Example: In-Component Guards (Options API)

```vue
<template>
  <div>User Profile</div>
</template>

<script>
export default {
  beforeRouteEnter(to, from, next) {
    // Called before the route is confirmed
    // No access to `this` component instance
    fetchUserData(to.params.id).then(() => {
      next()
    })
  },
  beforeRouteUpdate(to, from, next) {
    // Called when the route changes but component is reused
    // Has access to `this`
    if (to.params.id !== from.params.id) {
      this.fetchUserData(to.params.id)
    }
    next()
  },
  beforeRouteLeave(to, from, next) {
    // Called when leaving the route
    // Has access to `this`
    if (this.hasUnsavedChanges) {
      if (confirm('You have unsaved changes. Are you sure?')) {
        next()
      } else {
        next(false)
      }
    } else {
      next()
    }
  }
}
</script>
```

### Example: In-Component Guards (Composition API)

```vue
<template>
  <div>User Profile</div>
</template>

<script setup>
import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'
import { ref } from 'vue'

const hasUnsavedChanges = ref(false)

onBeforeRouteLeave((to, from) => {
  if (hasUnsavedChanges.value) {
    const answer = confirm('You have unsaved changes. Are you sure?')
    if (!answer) return false
  }
})

onBeforeRouteUpdate(async (to, from) => {
  if (to.params.id !== from.params.id) {
    await fetchUserData(to.params.id)
  }
})
</script>
```

### Example: Navigation Guard with Async Operations

```javascript
router.beforeEach(async (to, from, next) => {
  if (to.meta.requiresAuth) {
    try {
      const user = await checkAuth()
      if (user) {
        next()
      } else {
        next({ name: 'Login' })
      }
    } catch (error) {
      next({ name: 'Error' })
    }
  } else {
    next()
  }
})
```

### Example: Multiple Guards

```javascript
// Guards execute in order
router.beforeEach((to, from, next) => {
  console.log('Guard 1')
  next()
})

router.beforeEach((to, from, next) => {
  console.log('Guard 2')
  next()
})
```

### Key Points

- `beforeEach` and `beforeEnter` can redirect or cancel navigation
- `afterEach` cannot affect navigation
- `beforeRouteEnter` doesn't have access to component instance
- `beforeRouteUpdate` and `beforeRouteLeave` have access to `this`
- Guards can be async
- Multiple guards execute in order
- Use `next(false)` to cancel navigation
- Use `next('/path')` or `next({ name: 'Route' })` to redirect
