## Instructions

- Create the Vue app instance with createApp().
- Mount to a root element in the DOM.
- Register plugins or global components before mount.

### Example

```ts
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)
app.mount('#app')
```

Reference: https://cn.vuejs.org/guide/essentials/application.html
