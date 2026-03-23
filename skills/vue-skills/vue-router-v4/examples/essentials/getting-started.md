# Getting Started | 快速开始

**官方文档**: https://router.vuejs.org/guide/


## Instructions

This example demonstrates how to create a Vue Router instance and set up basic routing in a Vue 3 application.

### Key Concepts

- Installing Vue Router
- Creating a router instance with `createRouter()`
- Defining routes
- Registering the router with the Vue app
- Using `RouterLink` and `RouterView` components

### Example: Installation

```bash
# Using npm
npm install vue-router@4

# Using yarn
yarn add vue-router@4

# Using pnpm
pnpm add vue-router@4
```

### Example: Creating a Router

```javascript
// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
```

### Example: Registering Router with App

```javascript
// main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)
app.mount('#app')
```

### Example: Using RouterLink and RouterView

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
```

### Example: TypeScript Setup

```typescript
// router/index.ts
import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
```

### Key Points

- Use `createRouter()` to create a router instance (replaces `new VueRouter()` from Vue Router 3)
- Use `createWebHistory()` for HTML5 history mode (replaces `mode: 'history'`)
- Routes are defined as an array of route objects
- Register the router with `app.use(router)`
- `RouterLink` and `RouterView` are components that need to be imported
- In Vue Router 4, components are automatically available globally when using `app.use(router)`, but you can also import them explicitly
