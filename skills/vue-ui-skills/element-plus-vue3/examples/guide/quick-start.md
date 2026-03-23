# Quick Start

## Instructions

This example provides a quick start guide for Element Plus.

### Key Concepts

- Basic setup
- First component
- Global configuration
- Component usage

### Example: Basic Setup

```vue
<template>
  <el-button type="primary">Button</el-button>
</template>

<script setup>
// Component is auto-imported if using unplugin-vue-components
</script>
```

### Example: With Options API

```vue
<template>
  <el-button type="primary" @click="handleClick">
    Click Me
  </el-button>
</template>

<script>
export default {
  methods: {
    handleClick() {
      console.log('Button clicked')
    }
  }
}
</script>
```

### Example: With Composition API

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

### Example: Global Configuration

```javascript
// main.js
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(ElementPlus, {
  size: 'large',
  zIndex: 3000
})
app.mount('#app')
```

### Example: Using ConfigProvider

```vue
<template>
  <el-config-provider :locale="locale" :size="size">
    <el-button>Button</el-button>
  </el-config-provider>
</template>

<script setup>
import { ref } from 'vue'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'

const locale = ref(zhCn)
const size = ref('default')
</script>
```

### Key Points

- Use el- prefix for components
- Support both Options API and Composition API
- Configure globally or per component
- Use ConfigProvider for locale and size
- Import styles for components
