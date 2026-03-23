# Select Component

**官方文档**: https://element-plus.org/en-US/component/select.html


## Instructions

This example demonstrates the Select component in Element Plus.

### Key Concepts

- Select options
- Select multiple
- Select filtering
- Select events

### Example: Basic Select

```vue
<template>
  <el-select v-model="value" placeholder="Select">
    <el-option label="Option 1" value="1" />
    <el-option label="Option 2" value="2" />
    <el-option label="Option 3" value="3" />
  </el-select>
</template>

<script setup>
import { ref } from 'vue'

const value = ref('')
</script>
```

### Example: Select with Options Array

```vue
<template>
  <el-select v-model="value" placeholder="Select">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value"
    />
  </el-select>
</template>

<script setup>
import { ref } from 'vue'

const value = ref('')
const options = ref([
  { label: 'Option 1', value: '1' },
  { label: 'Option 2', value: '2' },
  { label: 'Option 3', value: '3' }
])
</script>
```

### Example: Multiple Select

```vue
<template>
  <el-select v-model="value" multiple placeholder="Select multiple">
    <el-option label="Option 1" value="1" />
    <el-option label="Option 2" value="2" />
    <el-option label="Option 3" value="3" />
  </el-select>
</template>

<script setup>
import { ref } from 'vue'

const value = ref([])
</script>
```

### Example: Filterable Select

```vue
<template>
  <el-select
    v-model="value"
    filterable
    placeholder="Search and select"
  >
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value"
    />
  </el-select>
</template>
```

### Example: Select Events

```vue
<template>
  <el-select
    v-model="value"
    @change="handleChange"
    @visible-change="handleVisibleChange"
  >
    <el-option label="Option 1" value="1" />
    <el-option label="Option 2" value="2" />
  </el-select>
</template>

<script setup>
import { ref } from 'vue'

const value = ref('')

const handleChange = (val) => {
  console.log('Changed:', val)
}

const handleVisibleChange = (visible) => {
  console.log('Visible:', visible)
}
</script>
```

### Key Points

- Use v-model for selected value
- Use el-option for options
- Support multiple selection
- Enable filtering with filterable
- Handle change and visible-change events
