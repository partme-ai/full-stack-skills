## Instructions

- Use <TransitionGroup> for list transitions.
- Always provide keys for list items.
- Define move class for FLIP animations.

### Example

```vue
<template>
  <TransitionGroup name="list" tag="ul">
    <li v-for="item in items" :key="item.id">{{ item.name }}</li>
  </TransitionGroup>
</template>
```

Reference: https://cn.vuejs.org/guide/built-ins/transition-group.html
