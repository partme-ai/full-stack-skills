# Segmented Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/segmented


## Instructions

This example demonstrates the Segmented component in Layui Vue.

### Key Concepts

- Segmented options
- Segmented selection
- Segmented events
- Segmented styling

### Example: Basic Segmented

```vue
<template>
  <lay-segmented v-model="value" :options="options"></lay-segmented>
</template>

<script setup>
import { ref } from 'vue'
import { LaySegmented } from '@layui/layui-vue'

const value = ref('1')
const options = [
  { label: 'Option 1', value: '1' },
  { label: 'Option 2', value: '2' },
  { label: 'Option 3', value: '3' }
]
</script>
```

### Example: Segmented with Icons

```vue
<template>
  <lay-segmented v-model="value" :options="options"></lay-segmented>
</template>

<script setup>
import { ref } from 'vue'
import { LaySegmented } from '@layui/layui-vue'

const value = ref('1')
const options = [
  { label: 'List', value: '1', icon: 'layui-icon-list' },
  { label: 'Grid', value: '2', icon: 'layui-icon-grid' }
]
</script>
```

### Example: Segmented Events

```vue
<template>
  <lay-segmented 
    v-model="value" 
    :options="options"
    @change="handleChange"
  ></lay-segmented>
</template>

<script setup>
import { ref } from 'vue'
import { LaySegmented } from '@layui/layui-vue'

const value = ref('1')
const options = [
  { label: 'Option 1', value: '1' },
  { label: 'Option 2', value: '2' }
]

const handleChange = (val) => {
  console.log('Selected:', val)
}
</script>
```

### Key Points

- Use v-model for two-way binding
- Configure options array
- Support icons in options
- Handle change events
- Customize appearance
