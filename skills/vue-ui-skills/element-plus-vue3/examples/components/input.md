# Input Component

**官方文档**: https://element-plus.org/en-US/component/input.html


## Instructions

This example demonstrates the Input component in Element Plus.

### Key Concepts

- Input types
- Input sizes
- Input states
- Input events
- Input validation

### Example: Basic Input

```vue
<template>
  <el-input v-model="input" placeholder="Please input" />
</template>

<script setup>
import { ref } from 'vue'
const input = ref('')
</script>
```

### Example: Input Types

```vue
<template>
  <el-input v-model="text" type="text" />
  <el-input v-model="password" type="password" show-password />
  <el-input v-model="textarea" type="textarea" :rows="4" />
</template>

<script setup>
import { ref } from 'vue'
const text = ref('')
const password = ref('')
const textarea = ref('')
</script>
```

### Example: Input Sizes

```vue
<template>
  <el-input v-model="input1" size="large" />
  <el-input v-model="input2" size="default" />
  <el-input v-model="input3" size="small" />
</template>
```

### Example: Input States

```vue
<template>
  <el-input v-model="input" disabled />
  <el-input v-model="input" readonly />
  <el-input v-model="input" clearable />
</template>
```

### Example: Input with Prefix/Suffix

```vue
<template>
  <el-input v-model="input1">
    <template #prefix>
      <el-icon><Search /></el-icon>
    </template>
  </el-input>
  <el-input v-model="input2">
    <template #suffix>
      <el-icon><Calendar /></el-icon>
    </template>
  </el-input>
</template>
```

### Example: Input Events

```vue
<template>
  <el-input
    v-model="input"
    @input="handleInput"
    @change="handleChange"
    @focus="handleFocus"
    @blur="handleBlur"
  />
</template>

<script setup>
import { ref } from 'vue'
const input = ref('')

const handleInput = (value) => {
  console.log('Input:', value)
}
const handleChange = (value) => {
  console.log('Change:', value)
}
const handleFocus = () => {
  console.log('Focus')
}
const handleBlur = () => {
  console.log('Blur')
}
</script>
```

### Key Points

- Use v-model for two-way binding
- Support multiple input types
- Support disabled, readonly, clearable
- Prefix and suffix slots
- Multiple event handlers
