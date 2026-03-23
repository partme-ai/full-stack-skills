# Installation | 安装

**官方文档**: https://bootstrap-vue.org


## Instructions

This example demonstrates how to install Bootstrap Vue 3.0 and set it up in a Vue 3 project.

### Key Concepts

- Installing Bootstrap Vue
- Importing Bootstrap CSS
- Registering components
- Basic setup

### Example: Installation

```bash
# Using npm
npm install bootstrap-vue-next bootstrap

# Using yarn
yarn add bootstrap-vue-next bootstrap

# Using pnpm
pnpm add bootstrap-vue-next bootstrap
```

### Example: Import Bootstrap CSS

```javascript
// In main.js or main.ts
import 'bootstrap/dist/css/bootstrap.css'
```

### Example: Basic Setup

```javascript
// main.js
import { createApp } from 'vue'
import App from './App.vue'
import BootstrapVue3 from 'bootstrap-vue-next'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'

const app = createApp(App)
app.use(BootstrapVue3)
app.mount('#app')
```

### Example: Tree-shaking Setup

```javascript
// main.js
import { createApp } from 'vue'
import App from './App.vue'
import { BButton, BFormInput } from 'bootstrap-vue-next'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'

const app = createApp(App)
app.component('BButton', BButton)
app.component('BFormInput', BFormInput)
app.mount('#app')
```

### Example: TypeScript Setup

```typescript
// main.ts
import { createApp } from 'vue'
import App from './App.vue'
import BootstrapVue3 from 'bootstrap-vue-next'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'

const app = createApp(App)
app.use(BootstrapVue3)
app.mount('#app')
```

### Key Points

- Install bootstrap-vue-next and bootstrap packages
- Import Bootstrap CSS in entry file
- Use app.use(BootstrapVue3) for global registration
- Or register components individually for tree-shaking
- Works with both JavaScript and TypeScript
- Requires Vue 3 and Bootstrap 5
