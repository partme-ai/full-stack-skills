# Actions

**官方文档**: https://vuex.vuejs.org/zh/,


## Instructions

This example demonstrates actions usage in Vuex.

### Key Concepts

- Action definition
- Action dispatch
- Action context
- Asynchronous operations

### Example: Basic Action

```javascript
// store/index.js
const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++
    }
  },
  actions: {
    increment(context) {
      context.commit('increment')
    }
  }
})
```

### Example: Action with Payload

```javascript
actions: {
  incrementBy(context, payload) {
    context.commit('increment', payload)
  }
}
```

### Example: Async Action

```javascript
actions: {
  async fetchUser({ commit }, userId) {
    const response = await fetch(`/api/users/${userId}`)
    const user = await response.json()
    commit('setUser', user)
  }
}
```

### Example: Action Context Destructuring

```javascript
actions: {
  async fetchData({ commit, state, dispatch }) {
    const response = await fetch('/api/data')
    const data = await response.json()
    commit('setData', data)
    
    if (state.needsMore) {
      dispatch('fetchMore')
    }
  }
}
```

### Example: Dispatching Actions

```vue
<template>
  <div>
    <button @click="increment">Increment</button>
    <button @click="fetchUser(1)">Fetch User</button>
  </div>
</template>

<script>
export default {
  methods: {
    increment() {
      this.$store.dispatch('increment')
    },
    fetchUser(userId) {
      this.$store.dispatch('fetchUser', userId)
    }
  }
}
</script>
```

### Example: Using mapActions

```vue
<template>
  <div>
    <button @click="increment">Increment</button>
    <button @click="fetchUser(1)">Fetch User</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  methods: {
    ...mapActions(['increment', 'fetchUser'])
  }
}
</script>
```

### Example: Action Returning Promise

```javascript
actions: {
  fetchData({ commit }) {
    return new Promise((resolve, reject) => {
      fetch('/api/data')
        .then(response => response.json())
        .then(data => {
          commit('setData', data)
          resolve(data)
        })
        .catch(error => {
          reject(error)
        })
    })
  }
}
```

### Key Points

- Actions can be asynchronous
- Dispatch actions via $store.dispatch
- Use mapActions helper
- Actions receive context object
- Actions commit mutations
