## Instructions

- Use named views to render multiple views.
- Define components object per route.
- Use named <router-view> outlets.

### Example

```js
const routes = [
  {
    path: '/dashboard',
    components: {
      default: Dashboard,
      sidebar: Sidebar
    }
  }
]
```

### Example

```html
<router-view />
<router-view name="sidebar" />
```

Reference: https://v3.router.vuejs.org/guide/essentials/named-views.html
