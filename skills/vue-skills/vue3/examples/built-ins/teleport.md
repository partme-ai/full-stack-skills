## Instructions

- Render content to a different DOM container.
- Use Teleport for modals or overlays.
- Keep target container present in DOM.

### Example

```vue
<template>
  <Teleport to="body">
    <div class="modal">Modal</div>
  </Teleport>
</template>
```

Reference: https://cn.vuejs.org/guide/built-ins/teleport.html
