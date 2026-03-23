# Button Component

**官方文档**: https://element-plus.org/en-US/component/button.html


## Instructions

This example demonstrates the Button component in Element Plus.

### Key Concepts

- Button types
- Button sizes
- Button states
- Button groups
- Button events

### Example: Basic Button

```vue
<template>
  <el-button>Default</el-button>
  <el-button type="primary">Primary</el-button>
  <el-button type="success">Success</el-button>
  <el-button type="info">Info</el-button>
  <el-button type="warning">Warning</el-button>
  <el-button type="danger">Danger</el-button>
</template>
```

### Example: Button Sizes

```vue
<template>
  <el-button size="large">Large</el-button>
  <el-button size="default">Default</el-button>
  <el-button size="small">Small</el-button>
</template>
```

### Example: Button States

```vue
<template>
  <el-button disabled>Disabled</el-button>
  <el-button loading>Loading</el-button>
  <el-button plain>Plain</el-button>
  <el-button round>Round</el-button>
  <el-button circle>Circle</el-button>
</template>
```

### Example: Button Events

```vue
<template>
  <el-button type="primary" @click="handleClick">
    Click Me
  </el-button>
</template>

<script setup>
const handleClick = () => {
  console.log('Button clicked')
}
</script>
```

### Example: Button Group

```vue
<template>
  <el-button-group>
    <el-button type="primary" icon="ArrowLeft">Previous</el-button>
    <el-button type="primary" icon="ArrowRight">Next</el-button>
  </el-button-group>
</template>
```

### Example: Button with Icon

```vue
<template>
  <el-button type="primary" icon="Search">Search</el-button>
  <el-button type="primary" :icon="Search">Search</el-button>
</template>

<script setup>
import { Search } from '@element-plus/icons-vue'
</script>
```

### Key Points

- Multiple types: primary, success, info, warning, danger
- Multiple sizes: large, default, small
- Support disabled, loading, plain, round, circle
- Icon support
- Button group support
