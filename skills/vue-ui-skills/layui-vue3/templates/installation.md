# Installation Templates

## Global Installation

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

## Import on Demand

```javascript
// main.js
import { createApp } from 'vue'
import { LayButton, LayTable, LayInput } from '@layui/layui-vue'
import '@layui/layui-vue/lib/index.css'
import App from './App.vue'

const app = createApp(App)
app.component('LayButton', LayButton)
app.component('LayTable', LayTable)
app.component('LayInput', LayInput)
app.mount('#app')
```

## TypeScript Setup

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

## Component Usage

```vue
<template>
  <lay-button type="primary">Button</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'
</script>
```
