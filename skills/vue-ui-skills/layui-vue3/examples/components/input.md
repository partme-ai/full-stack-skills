# Input Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/input


## Instructions

This example demonstrates the Input component in Layui Vue.

### Key Concepts

- Input types
- Input sizes
- Input states
- Input events

### Example: Basic Input

```vue
<template>
  <lay-input v-model="value" placeholder="Enter text"></lay-input>
</template>

<script setup>
import { ref } from 'vue'
import { LayInput } from '@layui/layui-vue'

const value = ref('')
</script>
```

### Example: Input Sizes

```vue
<template>
  <lay-input size="lg" v-model="value1"></lay-input>
  <lay-input size="md" v-model="value2"></lay-input>
  <lay-input size="sm" v-model="value3"></lay-input>
</template>
```

### Example: Input States

```vue
<template>
  <lay-input disabled v-model="value"></lay-input>
  <lay-input readonly v-model="value"></lay-input>
</template>
```

### Example: Input with Icon

```vue
<template>
  <lay-input 
    v-model="value" 
    prefix-icon="layui-icon-search"
  ></lay-input>
  <lay-input 
    v-model="value" 
    suffix-icon="layui-icon-close"
  ></lay-input>
</template>
```

### Example: Input Events

```vue
<template>
  <lay-input 
    v-model="value"
    @input="handleInput"
    @change="handleChange"
    @blur="handleBlur"
    @focus="handleFocus"
  ></lay-input>
</template>

<script setup>
import { ref } from 'vue'
import { LayInput } from '@layui/layui-vue'

const value = ref('')

const handleInput = (val) => {
  console.log('Input:', val)
}

const handleChange = (val) => {
  console.log('Change:', val)
}
</script>
```

### Key Points

- Use v-model for two-way binding
- Multiple sizes: lg, md, sm
- Support disabled and readonly
- Icon support (prefix/suffix)
- Multiple events: input, change, blur, focus
