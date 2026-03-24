# Passing Props to Route Components | 向路由组件传递 Props

**官方文档**: https://router.vuejs.org/guide/essentials/passing-props.html


## Instructions

This example demonstrates how to pass props to route components instead of using `$route.params`.

### Key Concepts

- Boolean mode for props
- Object mode for props
- Function mode for props
- Accessing route params as props

### Example: Boolean Mode

```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    props: true
  }
]
```

```vue
<!-- User.vue -->
<template>
  <div>User {{ id }}</div>
</template>

<script setup>
defineProps({
  id: String
})
</script>
```

### Example: Object Mode

```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    props: {
      id: 'default-id',
      showDetails: true
    }
  }
]
```

```vue
<!-- User.vue -->
<template>
  <div>
    <p>User {{ id }}</p>
    <div v-if="showDetails">Details...</div>
  </div>
</template>

<script setup>
defineProps({
  id: String,
  showDetails: Boolean
})
</script>
```

### Example: Function Mode

```javascript
const routes = [
  {
    path: '/user/:id',
    component: User,
    props: (route) => ({
      id: route.params.id,
      query: route.query,
      hash: route.hash
    })
  }
]
```

```vue
<!-- User.vue -->
<template>
  <div>
    <p>User {{ id }}</p>
    <p>Query: {{ query }}</p>
  </div>
</template>

<script setup>
defineProps({
  id: String,
  query: Object,
  hash: String
})
</script>
```

### Example: Multiple Props

```javascript
const routes = [
  {
    path: '/user/:id/posts/:postId',
    component: UserPost,
    props: true
  }
]
```

```vue
<!-- UserPost.vue -->
<template>
  <div>
    <p>User {{ id }}</p>
    <p>Post {{ postId }}</p>
  </div>
</template>

<script setup>
defineProps({
  id: String,
  postId: String
})
</script>
```

### Example: With Named Views

```javascript
const routes = [
  {
    path: '/user/:id',
    components: {
      default: User,
      sidebar: UserSidebar
    },
    props: {
      default: true,
      sidebar: false
    }
  }
]
```

### Key Points

- `props: true` passes route params as props
- Object mode passes static props
- Function mode allows custom prop mapping
- Makes components more reusable and testable
- Components don't need to know about routing
- Can use different prop modes for different named views
