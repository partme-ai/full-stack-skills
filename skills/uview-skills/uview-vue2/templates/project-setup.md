# Project Setup Template | 项目设置模板

## Basic uni-app + uView UI Setup

```json
// package.json
{
  "dependencies": {
    "uview-ui": "^2.0.0"
  }
}
```

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

Vue.config.productionTip = false

App.mpType = 'app'

const app = new Vue({
  ...App
})
app.$mount()
```

```vue
<!-- App.vue -->
<template>
  <view id="app">
    <router-view />
  </view>
</template>

<script>
export default {
  onLaunch: function() {
    console.log('App Launch')
  },
  onShow: function() {
    console.log('App Show')
  },
  onHide: function() {
    console.log('App Hide')
  }
}
</script>

<style lang="scss">
@import 'uview-ui/index.scss';
</style>
```

```json
// pages.json
{
  "easycom": {
    "autoscan": true,
    "custom": {
      "^u-(.*)": "uview-ui/components/u-$1/u-$1.vue"
    }
  },
  "pages": [
    {
      "path": "pages/index/index",
      "style": {
        "navigationBarTitleText": "首页"
      }
    }
  ]
}
```

## With TypeScript

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

## Configure Http Interceptors

```javascript
// main.js
import uView from 'uview-ui'

// Configure base URL
uView.http.setConfig({
  baseURL: 'https://api.example.com',
  timeout: 10000
})

// Request interceptor
uView.http.interceptors.request.use(config => {
  config.header = {
    ...config.header,
    'Authorization': 'Bearer ' + uni.getStorageSync('token')
  }
  return config
})

// Response interceptor
uView.http.interceptors.response.use(response => {
  if (response.statusCode === 200) {
    return response.data
  } else {
    return Promise.reject(response)
  }
}, error => {
  return Promise.reject(error)
})
```
