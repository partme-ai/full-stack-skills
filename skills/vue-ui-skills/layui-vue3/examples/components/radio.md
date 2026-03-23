# Radio Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/radio


## Instructions

This example demonstrates the Radio component in Layui Vue.

### Key Concepts

- Single radio
- Radio group
- Radio states
- Radio events

### Example: Basic Radio

```vue
<template>
  <lay-radio v-model="value" value="1">Option 1</lay-radio>
  <lay-radio v-model="value" value="2">Option 2</lay-radio>
</template>

<script setup>
import { ref } from 'vue'
import { LayRadio } from '@layui/layui-vue'

const value = ref('1')
</script>
```

### Example: Radio Group

```vue
<template>
  <lay-radio-group v-model="value">
    <lay-radio value="1">Option 1</lay-radio>
    <lay-radio value="2">Option 2</lay-radio>
    <lay-radio value="3">Option 3</lay-radio>
  </lay-radio-group>
</template>

<script setup>
import { ref } from 'vue'
import { LayRadio, LayRadioGroup } from '@layui/layui-vue'

const value = ref('1')
</script>
```

### Example: Radio States

```vue
<template>
  <lay-radio v-model="value" value="1" disabled>Disabled</lay-radio>
</template>
```

### Example: Radio Events

```vue
<template>
  <lay-radio-group v-model="value" @change="handleChange">
    <lay-radio value="1">Option 1</lay-radio>
    <lay-radio value="2">Option 2</lay-radio>
  </lay-radio-group>
</template>

<script setup>
import { ref } from 'vue'
import { LayRadio, LayRadioGroup } from '@layui/layui-vue'

const value = ref('1')

const handleChange = (val) => {
  console.log('Selected:', val)
}
</script>
```

### Key Points

- Use v-model for two-way binding
- Use lay-radio-group for radio groups
- Set value for each radio
- Support disabled state
- Handle change events
