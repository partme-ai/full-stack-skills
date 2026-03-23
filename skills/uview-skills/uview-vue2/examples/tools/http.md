# Http | 请求

**官方文档**: https://www.uviewui.com


## Instructions

This example demonstrates how to use the Http tool ($u.http) in uView UI.

### Key Concepts

- Basic HTTP request
- GET request
- POST request
- Request interceptors
- Response interceptors
- Error handling

### Example: Basic GET Request

```vue
<template>
  <u-button @click="fetchData">Fetch Data</u-button>
</template>

<script>
export default {
  methods: {
    async fetchData() {
      try {
        const res = await this.$u.http.get('/api/data')
        console.log('Data:', res)
      } catch (error) {
        console.error('Error:', error)
      }
    }
  }
}
</script>
```

### Example: POST Request

```vue
<template>
  <u-button @click="submitData">Submit Data</u-button>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        name: 'John',
        email: 'john@example.com'
      }
    }
  },
  methods: {
    async submitData() {
      try {
        const res = await this.$u.http.post('/api/submit', this.formData)
        console.log('Response:', res)
        this.$u.toast('Success')
      } catch (error) {
        console.error('Error:', error)
        this.$u.toast('Failed')
      }
    }
  }
}
</script>
```

### Example: Request with Options

```vue
<template>
  <u-button @click="customRequest">Custom Request</u-button>
</template>

<script>
export default {
  methods: {
    async customRequest() {
      try {
        const res = await this.$u.http.request({
          url: '/api/data',
          method: 'GET',
          header: {
            'Authorization': 'Bearer token'
          },
          params: {
            page: 1,
            limit: 10
          }
        })
        console.log('Response:', res)
      } catch (error) {
        console.error('Error:', error)
      }
    }
  }
}
</script>
```

### Example: Configure Interceptors

```javascript
// main.js or http.js
import uView from 'uview-ui'

// Request interceptor
uView.http.setConfig({
  baseURL: 'https://api.example.com',
  timeout: 10000
})

// Request interceptor
uView.http.interceptors.request.use(config => {
  // Add token to header
  config.header = {
    ...config.header,
    'Authorization': 'Bearer ' + uni.getStorageSync('token')
  }
  return config
})

// Response interceptor
uView.http.interceptors.response.use(response => {
  // Handle response
  if (response.statusCode === 200) {
    return response.data
  } else {
    return Promise.reject(response)
  }
}, error => {
  // Handle error
  return Promise.reject(error)
})
```

### Key Points

- Use `this.$u.http.get()` for GET requests
- Use `this.$u.http.post()` for POST requests
- Use `this.$u.http.request()` for custom requests
- Configure interceptors in main.js
- Use async/await for async requests
- Handle errors with try/catch
- Http tool is available globally via $u object
