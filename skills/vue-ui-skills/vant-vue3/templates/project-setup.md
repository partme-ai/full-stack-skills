# Project Setup Template | 项目设置模板

## Basic Vue 3 + Vant Setup

```json
// package.json
{
  "dependencies": {
    "vue": "^3.0.0",
    "vant": "^4.0.0"
  }
}
```

```javascript
// main.js
import { createApp } from 'vue'
import App from './App.vue'
import Vant from 'vant'
import 'vant/lib/index.css'

const app = createApp(App)
app.use(Vant)
app.mount('#app')
```

```vue
<!-- App.vue -->
<template>
  <van-config-provider :theme-vars="themeVars">
    <router-view />
  </van-config-provider>
</template>

<script setup>
import { ConfigProvider as VanConfigProvider } from 'vant'

const themeVars = {
  primaryColor: '#07c160'
}
</script>
```

## With TypeScript

```typescript
// main.ts
import { createApp } from 'vue'
import App from './App.vue'
import Vant from 'vant'
import 'vant/lib/index.css'

const app = createApp(App)
app.use(Vant)
app.mount('#app')
```

```vue
<!-- App.vue -->
<template>
  <van-config-provider :theme-vars="themeVars">
    <router-view />
  </van-config-provider>
</template>

<script setup lang="ts">
import { ConfigProvider as VanConfigProvider } from 'vant'

const themeVars = {
  primaryColor: '#07c160'
}
</script>
```

## With Tree-shaking

```javascript
// main.js
import { createApp } from 'vue'
import App from './App.vue'
import { Button, Cell, ConfigProvider } from 'vant'
import 'vant/lib/index.css'

const app = createApp(App)
app.use(Button)
app.use(Cell)
app.use(ConfigProvider)
app.mount('#app')
```

## With unplugin-vue-components

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite'
import { VantResolver } from 'unplugin-vue-components/resolvers'

export default defineConfig({
  plugins: [
    vue(),
    Components({
      resolvers: [VantResolver()],
    }),
  ],
})
```
