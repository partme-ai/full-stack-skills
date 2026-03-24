## Instructions

- Cache component instances with <KeepAlive>.
- Use include/exclude to control caching.
- Use activated/deactivated hooks when needed.

### Example

```vue
<template>
  <KeepAlive>
    <component :is="currentView" />
  </KeepAlive>
</template>
```

Reference: https://cn.vuejs.org/guide/built-ins/keep-alive.html
