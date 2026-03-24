# Installation

## Instructions

This example demonstrates how to install Element Plus in a Vue 3 project.

### Key Concepts

- Package installation
- Full import
- On-demand import
- CDN import
- Compatibility

### Example: Package Installation

```bash
# Using npm
npm install element-plus

# Using yarn
yarn add element-plus

# Using pnpm
pnpm add element-plus
```

### Example: Full Import

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

### Example: On-Demand Import

```javascript
// main.js
import { createApp } from 'vue'
import { ElButton, ElInput } from 'element-plus'
import 'element-plus/es/components/button/style/css'
import 'element-plus/es/components/input/style/css'
import App from './App.vue'

const app = createApp(App)
app.component(ElButton.name, ElButton)
app.component(ElInput.name, ElInput)
app.mount('#app')
```

### Example: CDN Import

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://unpkg.com/element-plus/dist/index.css" />
</head>
<body>
  <div id="app"></div>
  <script src="https://unpkg.com/vue@next"></script>
  <script src="https://unpkg.com/element-plus"></script>
  <script>
    const { createApp } = Vue
    const app = createApp({})
    app.use(ElementPlus)
    app.mount('#app')
  </script>
</body>
</html>
```

### Example: Auto Import with unplugin-vue-components

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

### Key Points

- Install element-plus package
- Choose between full import or on-demand import
- Import CSS styles
- Use app.use() for full import
- Use auto-import plugins for better DX
- Element Plus requires Vue 3
