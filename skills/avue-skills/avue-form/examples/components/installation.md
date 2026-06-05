# Installation

**官方文档**: https://avuejs.com/form/form-doc.html


## Instructions

This example demonstrates how to install Avue-form.

### Key Concepts

- Package installation
- Global registration
- Style import
- Basic setup

### Example: Package Installation

```bash
# Using npm
npm install @smallwei/avue

# Using yarn
yarn add @smallwei/avue

# Using pnpm
pnpm add @smallwei/avue
```

### Example: Global Registration

```javascript
// main.js
import Vue from 'vue'
import Avue from '@smallwei/avue'
import '@smallwei/avue/lib/theme-default/index.css'

Vue.use(Avue)
```

### Example: Style Import

```javascript
// Import default theme
import '@smallwei/avue/lib/theme-default/index.css'

// Or import custom theme
import '@smallwei/avue/lib/theme-custom/index.css'
```

### Example: Complete Setup

```javascript
// main.js
import Vue from 'vue'
import App from './App.vue'
import Avue from '@smallwei/avue'
import '@smallwei/avue/lib/theme-default/index.css'

Vue.use(Avue)

new Vue({
  render: h => h(App)
}).$mount('#app')
```

### Key Points

- Install @smallwei/avue package
- Register globally with Vue.use()
- Import CSS styles
- Ready to use in components
