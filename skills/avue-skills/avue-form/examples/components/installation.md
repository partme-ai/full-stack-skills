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
npm install @avue/form

# Using yarn
yarn add @avue/form

# Using pnpm
pnpm add @avue/form
```

### Example: Global Registration

```javascript
// main.js
import Vue from 'vue'
import Avue from '@avue/form'
import '@avue/form/lib/theme-default/index.css'

Vue.use(Avue)
```

### Example: Style Import

```javascript
// Import default theme
import '@avue/form/lib/theme-default/index.css'

// Or import custom theme
import '@avue/form/lib/theme-custom/index.css'
```

### Example: Complete Setup

```javascript
// main.js
import Vue from 'vue'
import App from './App.vue'
import Avue from '@avue/form'
import '@avue/form/lib/theme-default/index.css'

Vue.use(Avue)

new Vue({
  render: h => h(App)
}).$mount('#app')
```

### Key Points

- Install @avue/form package
- Register globally with Vue.use()
- Import CSS styles
- Ready to use in components
