# Programmatic Navigation | 编程式导航

**官方文档**: https://router.vuejs.org/guide/essentials/navigation.html


## Instructions

This example demonstrates how to navigate programmatically using the router instance methods.

### Key Concepts

- `router.push()` - Navigate to a new route
- `router.replace()` - Replace current route
- `router.go()` - Navigate through history
- `router.back()` - Go back in history
- `router.forward()` - Go forward in history
- Using router in Options API and Composition API

### Example: router.push()

```javascript
// String path
router.push('/home')

// Object with path
router.push({ path: '/home' })

// Named route
router.push({ name: 'Home' })

// With params
router.push({ name: 'User', params: { id: '123' } })

// With query
router.push({ path: '/search', query: { q: 'vue' } })

// With hash
router.push({ path: '/home', hash: '#section' })
```

### Example: router.replace()

```javascript
// Replace current route (doesn't add to history)
router.replace('/home')
router.replace({ name: 'Home' })
```

### Example: router.go()

```javascript
// Go forward 1 step
router.go(1)

// Go back 1 step
router.go(-1)

// Go back 3 steps
router.go(-3)
```

### Example: router.back() and router.forward()

```javascript
// Go back (equivalent to router.go(-1))
router.back()

// Go forward (equivalent to router.go(1))
router.forward()
```

### Example: Using in Options API

```vue
<template>
  <button @click="goToHome">Go Home</button>
  <button @click="goToUser">Go to User</button>
</template>

<script>
export default {
  methods: {
    goToHome() {
      this.$router.push('/home')
    },
    goToUser() {
      this.$router.push({ name: 'User', params: { id: '123' } })
    }
  }
}
</script>
```

### Example: Using in Composition API

```vue
<template>
  <button @click="goToHome">Go Home</button>
  <button @click="goToUser">Go to User</button>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function goToHome() {
  router.push('/home')
}

function goToUser() {
  router.push({ name: 'User', params: { id: '123' } })
}
</script>
```

### Example: Navigation with Promise

```javascript
// router.push() returns a Promise
router.push('/home')
  .then(() => {
    console.log('Navigation successful')
  })
  .catch((err) => {
    if (err.name === 'NavigationDuplicated') {
      // Handle duplicate navigation
    }
  })
```

### Example: Conditional Navigation

```vue
<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

async function navigateWithCheck() {
  try {
    await router.push('/protected')
  } catch (err) {
    if (err.name === 'NavigationAborted') {
      console.log('Navigation was aborted')
    }
  }
}
</script>
```

### Key Points

- `router.push()` adds a new entry to history
- `router.replace()` replaces current entry (no history)
- `router.go(n)` navigates n steps in history
- `router.back()` and `router.forward()` are convenience methods
- Navigation methods return Promises
- Can use string paths or route objects
- Use `useRouter()` in Composition API, `$router` in Options API
