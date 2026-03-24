# Select Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/select


## Instructions

This example demonstrates the Select component in Layui Vue.

### Key Concepts

- Select options
- Multiple selection
- Searchable select
- Select events

### Example: Basic Select

```vue
<template>
  <lay-select v-model="value" :options="options"></lay-select>
</template>

<script setup>
import { ref } from 'vue'
import { LaySelect } from '@layui/layui-vue'

const value = ref('')
const options = [
  { label: 'Option 1', value: '1' },
  { label: 'Option 2', value: '2' },
  { label: 'Option 3', value: '3' }
]
</script>
```

### Example: Multiple Selection

```vue
<template>
  <lay-select 
    v-model="value" 
    :options="options"
    multiple
  ></lay-select>
</template>

<script setup>
import { ref } from 'vue'
import { LaySelect } from '@layui/layui-vue'

const value = ref([])
const options = [
  { label: 'Option 1', value: '1' },
  { label: 'Option 2', value: '2' }
]
</script>
```

### Example: Searchable Select

```vue
<template>
  <lay-select 
    v-model="value" 
    :options="options"
    searchable
  ></lay-select>
</template>
```

### Example: Select with Placeholder

```vue
<template>
  <lay-select 
    v-model="value" 
    :options="options"
    placeholder="Please select"
  ></lay-select>
</template>
```

### Key Points

- Use v-model for two-way binding
- Configure options array
- Enable multiple selection
- Enable searchable mode
- Support placeholder
