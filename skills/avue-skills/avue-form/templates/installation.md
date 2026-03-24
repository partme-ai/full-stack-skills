# Installation Templates

## npm Installation

```bash
npm install @avue/form
```

## Global Registration

```javascript
// main.js
import Vue from 'vue'
import Avue from '@avue/form'
import '@avue/form/lib/theme-default/index.css'

Vue.use(Avue)
```

## Style Import

```javascript
// Import default theme
import '@avue/form/lib/theme-default/index.css'

// Or import custom theme
import '@avue/form/lib/theme-custom/index.css'
```

## Complete Setup

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
