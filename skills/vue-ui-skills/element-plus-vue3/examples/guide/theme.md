# Theme Customization

## Instructions

This example demonstrates how to customize Element Plus theme.

### Key Concepts

- CSS variables
- SCSS variables
- Theme builder
- Color customization

### Example: Using CSS Variables

```vue
<template>
  <el-button type="primary">Button</el-button>
</template>

<style>
:root {
  --el-color-primary: #409eff;
  --el-color-success: #67c23a;
  --el-color-warning: #e6a23c;
  --el-color-danger: #f56c6c;
  --el-color-info: #909399;
}
</style>
```

### Example: SCSS Variables

```scss
// variables.scss
$--color-primary: #409eff;
$--color-success: #67c23a;
$--color-warning: #e6a23c;
$--color-danger: #f56c6c;
$--color-info: #909399;
```

### Example: Import Custom Theme

```javascript
// main.js
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import './theme/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(ElementPlus)
app.mount('#app')
```

### Example: Component-Level Customization

```vue
<template>
  <el-button class="custom-button">Button</el-button>
</template>

<style scoped>
.custom-button {
  --el-button-bg-color: #409eff;
  --el-button-text-color: #fff;
}
</style>
```

### Key Points

- Use CSS variables for customization
- Override theme variables
- Use SCSS for advanced customization
- Component-level customization supported
- Use theme builder for visual customization
