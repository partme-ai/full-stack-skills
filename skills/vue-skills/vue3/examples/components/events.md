## Instructions

- Emit events to communicate upward.
- Document event names and payloads.
- Prefer kebab-case event names.

### Example

```vue
<script setup>
const emit = defineEmits(['save'])

// Emit a save event
function handleClick() {
  emit('save')
}
</script>

<template>
  <button @click="handleClick">Save</button>
</template>
```

Reference: https://cn.vuejs.org/guide/components/events.html
