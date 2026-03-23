# Tools API | 工具 API

## API Reference

uView UI tools API ($u object methods).

### $u.toast

Show toast message.

**Usage:**
```javascript
this.$u.toast('Message')
this.$u.toast({
  type: 'success',
  message: 'Success',
  duration: 2000
})
```

**Options:**
- `type`: Toast type (success, error, warning, loading)
- `message`: Toast message
- `duration`: Toast duration (milliseconds)
- `position`: Toast position (top, center, bottom)

### $u.http

HTTP request tool.

**Methods:**
- `get(url, params)`: GET request
- `post(url, data)`: POST request
- `request(options)`: Custom request

**Usage:**
```javascript
// GET request
const res = await this.$u.http.get('/api/data', { page: 1 })

// POST request
const res = await this.$u.http.post('/api/submit', { name: 'John' })

// Custom request
const res = await this.$u.http.request({
  url: '/api/data',
  method: 'GET',
  header: { 'Authorization': 'Bearer token' }
})
```

### $u.storage

Storage tool.

**Methods:**
- `set(key, value)`: Set storage
- `get(key)`: Get storage
- `remove(key)`: Remove storage
- `clear()`: Clear all storage

**Usage:**
```javascript
// Set storage
this.$u.storage.set('token', 'abc123')

// Get storage
const token = this.$u.storage.get('token')

// Remove storage
this.$u.storage.remove('token')

// Clear all
this.$u.storage.clear()
```

### $u.route

Route navigation tool.

**Methods:**
- `navigateTo(url)`: Navigate to page
- `redirectTo(url)`: Redirect to page
- `switchTab(url)`: Switch tab
- `navigateBack(delta)`: Navigate back

**Usage:**
```javascript
// Navigate to page
this.$u.route.navigateTo('/pages/detail/index?id=1')

// Redirect to page
this.$u.route.redirectTo('/pages/login/index')

// Switch tab
this.$u.route.switchTab('/pages/index/index')

// Navigate back
this.$u.route.navigateBack()
```

### Key Points

- All tools are available via `this.$u` object
- Tools work in Vue 2 Options API
- Tools are available globally in all components
- Http tool supports async/await
- Storage tool works with uni-app storage
- Route tool works with uni-app navigation
