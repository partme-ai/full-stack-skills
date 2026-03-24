# Named Views | 命名视图

**官方文档**: https://router.vuejs.org/guide/essentials/named-views.html


## Instructions

This example demonstrates how to use named views to display multiple RouterView components simultaneously.

### Key Concepts

- Named views with `components` property
- Multiple RouterView components
- Default view
- Using named views with nested routes

### Example: Basic Named Views

```javascript
// router/index.js
const routes = [
  {
    path: '/settings',
    components: {
      default: SettingsMain,
      sidebar: SettingsSidebar,
      header: SettingsHeader
    }
  }
]
```

```vue
<!-- App.vue -->
<template>
  <div>
    <RouterView name="header" />
    <div class="container">
      <RouterView name="sidebar" />
      <RouterView />
    </div>
  </div>
</template>
```

### Example: Named Views with Nested Routes

```javascript
const routes = [
  {
    path: '/user/:id',
    component: UserLayout,
    children: [
      {
        path: '',
        components: {
          default: UserProfile,
          sidebar: UserSidebar
        }
      },
      {
        path: 'posts',
        components: {
          default: UserPosts,
          sidebar: UserPostsSidebar
        }
      }
    ]
  }
]
```

### Example: Using in Components

```vue
<!-- UserLayout.vue -->
<template>
  <div class="user-layout">
    <RouterView name="sidebar" />
    <main>
      <RouterView />
    </main>
  </div>
</template>
```

### Example: Navigation to Named Views

```javascript
// Navigation doesn't change, router handles which views to show
router.push('/settings')
```

### Key Points

- Use `components` (plural) instead of `component` for named views
- Default view uses `default` key
- Each RouterView needs a `name` prop matching the component key
- Named views allow multiple components per route
- Useful for complex layouts with sidebars, headers, etc.
