# Project Setup Template | 项目设置模板

## Basic Vue 3 + Bootstrap Vue Setup

```javascript
// package.json
{
  "dependencies": {
    "vue": "^3.0.0",
    "bootstrap-vue-next": "^0.0.0",
    "bootstrap": "^5.0.0"
  }
}
```

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

```vue
<!-- App.vue -->
<template>
  <BContainer>
    <BRow>
      <BCol>
        <h1>Bootstrap Vue App</h1>
      </BCol>
    </BRow>
  </BContainer>
</template>

<script setup>
import { BContainer, BRow, BCol } from 'bootstrap-vue-next'
</script>
```

## With TypeScript

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

```vue
<!-- App.vue -->
<template>
  <BContainer>
    <BRow>
      <BCol>
        <h1>Bootstrap Vue App</h1>
      </BCol>
    </BRow>
  </BContainer>
</template>

<script setup lang="ts">
import { BContainer, BRow, BCol } from 'bootstrap-vue-next'
</script>
```

## With Tree-shaking

```javascript
// main.js
import { createApp } from 'vue'
import App from './App.vue'
import { BButton, BFormInput, BContainer, BRow, BCol } from 'bootstrap-vue-next'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'

const app = createApp(App)
app.component('BButton', BButton)
app.component('BFormInput', BFormInput)
app.component('BContainer', BContainer)
app.component('BRow', BRow)
app.component('BCol', BCol)
app.mount('#app')
```
