# DatePicker Component

**官方文档**: https://element-plus.org/en-US/component/date-picker.html


## Instructions

This example demonstrates the DatePicker component in Element Plus.

### Key Concepts

- Date selection
- Date range
- Date format
- Date picker types

### Example: Basic DatePicker

```vue
<template>
  <el-date-picker v-model="date" type="date" placeholder="Select date" />
</template>

<script setup>
import { ref } from 'vue'

const date = ref('')
</script>
```

### Example: Date Range

```vue
<template>
  <el-date-picker
    v-model="dateRange"
    type="daterange"
    range-separator="To"
    start-placeholder="Start date"
    end-placeholder="End date"
  />
</template>

<script setup>
import { ref } from 'vue'

const dateRange = ref([])
</script>
```

### Example: Date Picker Types

```vue
<template>
  <el-date-picker v-model="date" type="date" />
  <el-date-picker v-model="datetime" type="datetime" />
  <el-date-picker v-model="daterange" type="daterange" />
  <el-date-picker v-model="datetimerange" type="datetimerange" />
  <el-date-picker v-model="month" type="month" />
  <el-date-picker v-model="year" type="year" />
</template>
```

### Example: Date Format

```vue
<template>
  <el-date-picker
    v-model="date"
    type="date"
    format="YYYY-MM-DD"
    value-format="YYYY-MM-DD"
  />
</template>
```

### Example: Date Picker with Shortcuts

```vue
<template>
  <el-date-picker
    v-model="date"
    type="date"
    :shortcuts="shortcuts"
  />
</template>

<script setup>
import { ref } from 'vue'

const date = ref('')
const shortcuts = [
  {
    text: 'Today',
    value: new Date()
  },
  {
    text: 'Yesterday',
    value: () => {
      const date = new Date()
      date.setTime(date.getTime() - 3600 * 1000 * 24)
      return date
    }
  }
]
</script>
```

### Key Points

- Use v-model for selected date
- Multiple types: date, datetime, daterange, etc.
- Configure format and value-format
- Support shortcuts
- Use Day.js for date handling
