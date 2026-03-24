# Checkbox Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/checkbox


## Instructions

This example demonstrates the Checkbox component in Layui Vue.

### Key Concepts

- Single checkbox
- Checkbox group
- Checkbox states
- Checkbox events

### Example: Basic Checkbox

```vue
<template>
  <lay-checkbox v-model="checked">Checkbox</lay-checkbox>
</template>

<script setup>
import { ref } from 'vue'
import { LayCheckbox } from '@layui/layui-vue'

const checked = ref(false)
</script>
```

### Example: Checkbox Group

```vue
<template>
  <lay-checkbox-group v-model="checkedList">
    <lay-checkbox value="1">Option 1</lay-checkbox>
    <lay-checkbox value="2">Option 2</lay-checkbox>
    <lay-checkbox value="3">Option 3</lay-checkbox>
  </lay-checkbox-group>
</template>

<script setup>
import { ref } from 'vue'
import { LayCheckbox, LayCheckboxGroup } from '@layui/layui-vue'

const checkedList = ref([])
</script>
```

### Example: Checkbox States

```vue
<template>
  <lay-checkbox v-model="checked" disabled>Disabled</lay-checkbox>
  <lay-checkbox v-model="checked" :indeterminate="indeterminate">Indeterminate</lay-checkbox>
</template>

<script setup>
import { ref } from 'vue'
import { LayCheckbox } from '@layui/layui-vue'

const checked = ref(false)
const indeterminate = ref(true)
</script>
```

### Example: Checkbox Events

```vue
<template>
  <lay-checkbox 
    v-model="checked"
    @change="handleChange"
  >Checkbox</lay-checkbox>
</template>

<script setup>
import { ref } from 'vue'
import { LayCheckbox } from '@layui/layui-vue'

const checked = ref(false)

const handleChange = (val) => {
  console.log('Checked:', val)
}
</script>
```

### Key Points

- Use v-model for two-way binding
- Use lay-checkbox-group for multiple checkboxes
- Support disabled and indeterminate states
- Handle change events
- Configure checkbox values
