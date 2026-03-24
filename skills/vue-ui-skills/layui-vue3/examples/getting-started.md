# Getting Started

**官方文档**: https://www.layui-vue.com/zh-CN/index


## Instructions

This example demonstrates how to get started with Layui Vue.

### Key Concepts

- Installation
- Basic setup
- Import components
- Global registration

### Example: Installation

```bash
# Using npm
npm install @layui/layui-vue

# Using yarn
yarn add @layui/layui-vue

# Using pnpm
pnpm add @layui/layui-vue
```

### Example: Global Registration

```javascript
// main.js
import { createApp } from 'vue'
import LayuiVue from '@layui/layui-vue'
import '@layui/layui-vue/lib/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(LayuiVue)
app.mount('#app')
```

### Example: Import on Demand

```javascript
// main.js
import { createApp } from 'vue'
import { LayButton, LayTable } from '@layui/layui-vue'
import '@layui/layui-vue/lib/index.css'
import App from './App.vue'

const app = createApp(App)
app.component('LayButton', LayButton)
app.component('LayTable', LayTable)
app.mount('#app')
```

### Example: Component Usage

```vue
<template>
  <lay-button type="primary">Primary Button</lay-button>
  <lay-button type="normal">Normal Button</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'
</script>
```

### Example: TypeScript Setup

```typescript
// main.ts
import { createApp } from 'vue'
import LayuiVue from '@layui/layui-vue'
import '@layui/layui-vue/lib/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(LayuiVue)
app.mount('#app')
```

### Key Points

- Install @layui/layui-vue package
- Import CSS file
- Register globally or import on demand
- Use components in templates
- Supports TypeScript
