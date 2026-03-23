## Instructions

- Use modelValue and update:modelValue for v-model.
- Support multiple v-model bindings when needed.
- Keep inputs controlled by props.

### Example

```vue
<script setup>
const props = defineProps({ modelValue: String })
const emit = defineEmits(['update:modelValue'])

// Update model value
function onInput(event) {
  emit('update:modelValue', event.target.value)
}
</script>

<template>
  <input :value="props.modelValue" @input="onInput" />
</template>
```

Reference: https://cn.vuejs.org/guide/components/v-model.html
