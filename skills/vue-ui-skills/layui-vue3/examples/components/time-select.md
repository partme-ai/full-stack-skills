# TimeSelect Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/time-select


## Instructions

This example demonstrates the TimeSelect component in Layui Vue.

### Key Concepts

- Time selection
- Time format
- Time range
- Time picker options

### Example: Basic TimeSelect

```vue
<template>
  <lay-time-select v-model="time"></lay-time-select>
</template>

<script setup>
import { ref } from 'vue'
import { LayTimeSelect } from '@layui/layui-vue'

const time = ref('')
</script>
```

### Example: TimeSelect with Format

```vue
<template>
  <lay-time-select 
    v-model="time"
    format="HH:mm:ss"
  ></lay-time-select>
</template>
```

### Example: TimeSelect with Steps

```vue
<template>
  <lay-time-select 
    v-model="time"
    :step="30"
  ></lay-time-select>
</template>
```

### Example: TimeSelect Range

```vue
<template>
  <lay-time-select 
    v-model="timeRange"
    range
  ></lay-time-select>
</template>

<script setup>
import { ref } from 'vue'
import { LayTimeSelect } from '@layui/layui-vue'

const timeRange = ref([])
</script>
```

### Key Points

- Use v-model for two-way binding
- Configure time format
- Set time step interval
- Support time range selection
- Customize picker options
