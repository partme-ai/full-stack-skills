# Installation | 安装

**官方文档入口**: https://vant-ui.github.io/vant/#/zh-CN
**官方对应章节**: Quickstart / 快速开始


## Instructions

This example demonstrates how to install Vant and set it up in a Vue 3 project.

### Key Concepts

- Installing Vant
- Importing styles
- Registering components
- Basic setup

### Example: Installation

```bash
# Using npm
npm install vant

# Using yarn
yarn add vant

# Using pnpm
pnpm add vant

# Using bun
bun add vant
```

### Example: Import Styles

```javascript
// Import CSS in your entry file (e.g., main.js or main.ts)
import 'vant/lib/index.css'
```

### Example: Full Import

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

### Example: Tree-shaking Import

```javascript
// main.js
import { createApp } from 'vue'
import App from './App.vue'
import { Button, Cell } from 'vant'
import 'vant/lib/index.css'

const app = createApp(App)
app.use(Button)
app.use(Cell)
app.mount('#app')
```

### Example: TypeScript Setup

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

### Example: Using unplugin-vue-components

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

### Key Points

- Install vant package
- Import Vant CSS in entry file
- Use app.use(Vant) for full import
- Or import components individually for tree-shaking
- Works with both JavaScript and TypeScript
- Use unplugin-vue-components for auto import
- Requires Vue 3
