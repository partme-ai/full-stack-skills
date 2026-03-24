# Plugins

**官方文档**: https://vuex.vuejs.org/zh/,


## Instructions

This example demonstrates plugins usage in Vuex.

### Key Concepts

- Plugin definition
- Plugin registration
- Plugin usage
- Built-in plugins

### Example: Basic Plugin

```javascript
// plugins/logger.js
const logger = store => {
  store.subscribe((mutation, state) => {
    console.log(mutation.type, mutation.payload)
    console.log('New state:', state)
  })
}

export default logger
```

### Example: Registering Plugin

```javascript
// store/index.js
import logger from './plugins/logger'

const store = new Vuex.Store({
  plugins: [logger],
  state: {
    count: 0
  }
})
```

### Example: Plugin with Options

```javascript
// plugins/logger.js
const logger = (store) => {
  store.subscribe((mutation, state) => {
    if (mutation.type.startsWith('user/')) {
      console.log('User mutation:', mutation.type)
    }
  })
}

export default logger
```

### Example: State Persistence Plugin

```javascript
// plugins/persist.js
const persist = (store) => {
  // Load state from localStorage
  const savedState = localStorage.getItem('vuex-state')
  if (savedState) {
    store.replaceState(JSON.parse(savedState))
  }
  
  // Save state to localStorage on mutation
  store.subscribe((mutation, state) => {
    localStorage.setItem('vuex-state', JSON.stringify(state))
  })
}

export default persist
```

### Key Points

- Plugins are functions
- Plugins receive store instance
- Use subscribe for mutations
- Use replaceState for state replacement
- Register plugins in store options
