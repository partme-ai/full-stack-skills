## Instructions

- Use <Transition> for entering/leaving elements.
- Define transition classes in CSS.
- Prefer CSS transitions for simple cases.

### Example

```vue
<template>
  <Transition name="fade">
    <p v-if="show">Hello</p>
  </Transition>
</template>
```

Reference: https://cn.vuejs.org/guide/built-ins/transition.html
