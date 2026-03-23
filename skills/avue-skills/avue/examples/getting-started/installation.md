# Installation | 安装

**官方文档**: https://avuejs.com/


## Instructions

This example demonstrates how to install Avue and set it up in a Vue project.

### Key Concepts

- Installing Avue
- Importing styles
- Registering Avue
- Basic setup

### Example: Installation

```bash
# Using npm
npm install @smallwei/avue

# Using yarn
yarn add @smallwei/avue

# Using pnpm
pnpm add @smallwei/avue
```

### Example: Import and Register

```javascript
// main.js
import Vue from 'vue'
import App from './App.vue'
import Avue from '@smallwei/avue'
import '@smallwei/avue/lib/index.css'

Vue.use(Avue)

new Vue({
  render: h => h(App)
}).$mount('#app')
```

### Example: Partial Import

```javascript
// main.js
import Vue from 'vue'
import { AvueForm, AvueTable } from '@smallwei/avue'
import '@smallwei/avue/lib/index.css'

Vue.component('AvueForm', AvueForm)
Vue.component('AvueTable', AvueTable)
```

### Example: With Element UI

```javascript
// main.js
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Avue from '@smallwei/avue'
import '@smallwei/avue/lib/index.css'

Vue.use(ElementUI)
Vue.use(Avue)
```

### Key Points

- Install @smallwei/avue package
- Import Avue CSS styles
- Use Vue.use(Avue) to register
- Avue requires Element UI
- Works with Vue 2.x
- Can import components individually
