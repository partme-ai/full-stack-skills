# Installation | 安装

**官方文档**: https://www.uviewui.com


## Instructions

This example demonstrates how to install uView UI and set it up in a uni-app project.

### Key Concepts

- Installing uView UI
- Importing styles
- Registering uView UI
- Configuring easycom
- Basic setup

### Example: Installation via npm

```bash
# Using npm
npm install uview-ui

# Using yarn
yarn add uview-ui
```

### Example: Installation via uni_modules

1. Download uView UI from DCloud plugin market
2. Import to project's `uni_modules` directory

### Example: Import and Register in main.js

```javascript
// main.js
import Vue from 'vue'
import App from './App'
import uView from 'uview-ui'

Vue.use(uView)

// #ifndef VUE3
import store from './store'
Vue.prototype.$store = store
// #endif

// #ifdef VUE3
import { createSSRApp } from 'vue'
export function createApp() {
  const app = createSSRApp(App)
  app.use(store)
  return {
    app
  }
}
// #endif
```

### Example: Import Styles in App.vue

```vue
<!-- App.vue -->
<style lang="scss">
@import 'uview-ui/index.scss';
</style>
```

### Example: Configure easycom in pages.json

```json
{
  "easycom": {
    "autoscan": true,
    "custom": {
      "^u-(.*)": "uview-ui/components/u-$1/u-$1.vue"
    }
  }
}
```

### Example: TypeScript Setup

```typescript
// main.ts
import Vue from 'vue'
import App from './App.vue'
import uView from 'uview-ui'

Vue.use(uView)

new Vue({
  render: h => h(App)
}).$mount('#app')
```

### Key Points

- Install uView UI via npm or uni_modules
- Import and register uView UI in main.js with Vue.use()
- Import styles in App.vue
- Configure easycom in pages.json for automatic component registration
- Works with Vue 2 and uni-app
- Supports H5, 小程序, and App platforms
