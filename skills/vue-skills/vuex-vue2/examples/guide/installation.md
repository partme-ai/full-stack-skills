# Installation

**官方文档**: https://vuex.vuejs.org/zh/,


## Instructions

This example demonstrates how to install Vuex.

### Key Concepts

- Package installation
- CDN installation
- Vue plugin registration
- Version compatibility

### Example: Package Installation

```bash
# Using npm
npm install vuex@3

# Using yarn
yarn add vuex@3

# Using pnpm
pnpm add vuex@3
```

### Example: CDN Installation

```html
<script src="https://unpkg.com/vuex@3"></script>
```

### Example: Vue Plugin Registration

```javascript
// main.js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
```

### Example: Store Creation

```javascript
// store/index.js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++
    }
  }
})

export default store
```

### Example: Store Integration

```javascript
// main.js
import Vue from 'vue'
import store from './store'
import App from './App.vue'

new Vue({
  store,
  render: h => h(App)
}).$mount('#app')
```

### Key Points

- Install vuex@3 for Vue 2
- Register Vuex as Vue plugin
- Create store instance
- Inject store into Vue instance
- Use store in components
