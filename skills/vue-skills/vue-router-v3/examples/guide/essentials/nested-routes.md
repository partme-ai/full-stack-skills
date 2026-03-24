## Instructions

- Define children routes for nested UI.
- Use <router-view> in parent components.
- Keep nested paths relative.

### Example

```js
const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      { path: 'profile', component: UserProfile },
      { path: 'posts', component: UserPosts }
    ]
  }
]
```

### Example

```html
<!-- User.vue -->
<router-view />
```

Reference: https://v3.router.vuejs.org/guide/essentials/nested-routes.html
