# Installation Templates

## npm Installation

```bash
npm install @smallwei/avue
```

## Global Registration

```javascript
// main.js
import Vue from 'vue'
import Avue from '@smallwei/avue'
import '@smallwei/avue/lib/theme-default/index.css'

Vue.use(Avue)
```

## Style Import

```javascript
// Import default theme
import '@smallwei/avue/lib/theme-default/index.css'

// Or import custom theme
import '@smallwei/avue/lib/theme-custom/index.css'
```

## Complete Setup

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
