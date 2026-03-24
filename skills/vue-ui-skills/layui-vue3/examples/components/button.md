# Button Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/button


## Instructions

This example demonstrates the Button component in Layui Vue.

### Key Concepts

- Button types
- Button sizes
- Button states
- Button events

### Example: Basic Button

```vue
<template>
  <lay-button>Default</lay-button>
  <lay-button type="primary">Primary</lay-button>
  <lay-button type="normal">Normal</lay-button>
  <lay-button type="warm">Warm</lay-button>
  <lay-button type="danger">Danger</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'
</script>
```

### Example: Button Sizes

```vue
<template>
  <lay-button size="lg">Large</lay-button>
  <lay-button size="md">Medium</lay-button>
  <lay-button size="sm">Small</lay-button>
  <lay-button size="xs">Extra Small</lay-button>
</template>
```

### Example: Button States

```vue
<template>
  <lay-button disabled>Disabled</lay-button>
  <lay-button loading>Loading</lay-button>
</template>
```

### Example: Button with Icon

```vue
<template>
  <lay-button icon="layui-icon-search">Search</lay-button>
  <lay-button icon="layui-icon-add-circle">Add</lay-button>
</template>
```

### Example: Button Events

```vue
<template>
  <lay-button @click="handleClick">Click Me</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'

const handleClick = () => {
  console.log('Button clicked')
}
</script>
```

### Key Points

- Multiple types: primary, normal, warm, danger
- Multiple sizes: lg, md, sm, xs
- Support for disabled and loading states
- Icon support
- Click event handling
