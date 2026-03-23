# Project Setup Templates

## Vite Project Setup

```bash
# Create Vite project
npm create vite@latest my-app -- --template vue

# Install dependencies
cd my-app
npm install
npm install element-plus

# Install auto-import plugins
npm install -D unplugin-vue-components unplugin-auto-import
```

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [ElementPlusResolver()],
    }),
  ],
})
```

## Vue CLI Project Setup

```bash
# Create Vue CLI project
vue create my-app

# Install Element Plus
cd my-app
npm install element-plus
```

```javascript
// main.js
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(ElementPlus)
app.mount('#app')
```

## Nuxt 3 Project Setup

```bash
# Create Nuxt 3 project
npx nuxi@latest init my-app

# Install Element Plus
cd my-app
npm install element-plus
```

```javascript
// nuxt.config.ts
import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  css: ['element-plus/dist/index.css'],
  build: {
    transpile: ['element-plus']
  }
})
```
