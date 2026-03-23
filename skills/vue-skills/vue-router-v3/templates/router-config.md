# Router Configuration Templates

## Basic Router Configuration

```javascript
// router/index.js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: Home }
]

const router = new VueRouter({
  routes
})

export default router
```

## Router with History Mode

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { path: '/', component: Home }
  ]
})

export default router
```

## Router with Custom Active Classes

```javascript
const router = new VueRouter({
  routes: [...],
  linkActiveClass: 'active',
  linkExactActiveClass: 'exact-active'
})
```

## Router with Scroll Behavior

```javascript
const router = new VueRouter({
  routes: [...],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  }
})
```

## Router with Navigation Guards

```javascript
const router = new VueRouter({
  routes: [...]
})

router.beforeEach((to, from, next) => {
  // Authentication check
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated()) {
      next('/login')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
```
