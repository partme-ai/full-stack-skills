# DatePicker Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/date-picker


## Instructions

This example demonstrates the DatePicker component in Layui Vue.

### Key Concepts

- Date selection
- Date range
- Date formats
- Date picker types

### Example: Basic DatePicker

```vue
<template>
  <lay-date-picker v-model="date"></lay-date-picker>
</template>

<script setup>
import { ref } from 'vue'
import { LayDatePicker } from '@layui/layui-vue'

const date = ref('')
</script>
```

### Example: Date Range

```vue
<template>
  <lay-date-picker 
    v-model="dateRange" 
    type="daterange"
  ></lay-date-picker>
</template>

<script setup>
import { ref } from 'vue'
import { LayDatePicker } from '@layui/layui-vue'

const dateRange = ref([])
</script>
```

### Example: Date Format

```vue
<template>
  <lay-date-picker 
    v-model="date" 
    format="YYYY-MM-DD"
  ></lay-date-picker>
</template>
```

### Example: Date Picker Types

```vue
<template>
  <lay-date-picker type="date"></lay-date-picker>
  <lay-date-picker type="datetime"></lay-date-picker>
  <lay-date-picker type="year"></lay-date-picker>
  <lay-date-picker type="month"></lay-date-picker>
</template>
```

### Example: Date Picker with Options

```vue
<template>
  <lay-date-picker 
    v-model="date"
    :shortcuts="shortcuts"
  ></lay-date-picker>
</template>

<script setup>
import { ref } from 'vue'
import { LayDatePicker } from '@layui/layui-vue'

const date = ref('')
const shortcuts = [
  { text: 'Today', value: new Date() },
  { text: 'Yesterday', value: () => {
    const d = new Date()
    d.setDate(d.getDate() - 1)
    return d
  }}
]
</script>
```

### Key Points

- Use v-model for two-way binding
- Support date range selection
- Configure date format
- Multiple picker types
- Shortcuts support
