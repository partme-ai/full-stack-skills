## Instructions

- Use Vue Router for SPA routing.
- Define routes and connect to router-view.
- Use lazy-loaded routes for performance.

### Example

```ts
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [{ path: '/', component: () => import('./Home.vue') }]
})

export default router
```

Reference: https://cn.vuejs.org/guide/scaling-up/routing.html
