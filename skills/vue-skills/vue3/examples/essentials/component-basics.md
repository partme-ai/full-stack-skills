## Instructions

- Define components and pass props.
- Use emits for child-to-parent communication.
- Keep components single-purpose.

### Example

```vue
<script setup>
import ChildCard from './ChildCard.vue'

// Handle child save event
function handleSave() {
  // no-op
}
</script>

<template>
  <ChildCard title="Card" @save="handleSave" />
</template>
```

Reference: https://cn.vuejs.org/guide/essentials/component-basics.html
