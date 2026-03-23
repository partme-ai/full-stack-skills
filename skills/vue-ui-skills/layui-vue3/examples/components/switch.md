# Switch Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/switch


## Instructions

This example demonstrates the Switch component in Layui Vue.

### Key Concepts

- Switch state
- Switch sizes
- Switch colors
- Switch events

### Example: Basic Switch

```vue
<template>
  <lay-switch v-model="checked"></lay-switch>
</template>

<script setup>
import { ref } from 'vue'
import { LaySwitch } from '@layui/layui-vue'

const checked = ref(false)
</script>
```

### Example: Switch with Label

```vue
<template>
  <lay-switch v-model="checked">Enable Feature</lay-switch>
</template>
```

### Example: Switch Sizes

```vue
<template>
  <lay-switch v-model="checked1" size="lg"></lay-switch>
  <lay-switch v-model="checked2" size="md"></lay-switch>
  <lay-switch v-model="checked3" size="sm"></lay-switch>
</template>
```

### Example: Switch States

```vue
<template>
  <lay-switch v-model="checked" disabled>Disabled</lay-switch>
  <lay-switch v-model="checked" loading>Loading</lay-switch>
</template>
```

### Example: Switch Events

```vue
<template>
  <lay-switch 
    v-model="checked"
    @change="handleChange"
  ></lay-switch>
</template>

<script setup>
import { ref } from 'vue'
import { LaySwitch } from '@layui/layui-vue'

const checked = ref(false)

const handleChange = (val) => {
  console.log('Switch:', val)
}
</script>
```

### Key Points

- Use v-model for two-way binding
- Support label text
- Multiple sizes: lg, md, sm
- Support disabled and loading states
- Handle change events
