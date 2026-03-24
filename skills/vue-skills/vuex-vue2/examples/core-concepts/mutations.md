# Mutations

**官方文档**: https://vuex.vuejs.org/zh/,


## Instructions

This example demonstrates mutations usage in Vuex.

### Key Concepts

- Mutation definition
- Mutation commit
- Mutation payload
- Synchronous mutations

### Example: Basic Mutation

```javascript
// store/index.js
const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++
    },
    decrement(state) {
      state.count--
    }
  }
})
```

### Example: Mutation with Payload

```javascript
mutations: {
  increment(state, payload) {
    state.count += payload.amount
  },
  setUser(state, user) {
    state.user = user
  }
}
```

### Example: Committing Mutations

```vue
<template>
  <div>
    <button @click="increment">Increment</button>
    <button @click="incrementBy(10)">Increment by 10</button>
  </div>
</template>

<script>
export default {
  methods: {
    increment() {
      this.$store.commit('increment')
    },
    incrementBy(amount) {
      this.$store.commit('increment', { amount })
    }
  }
}
</script>
```

### Example: Using mapMutations

```vue
<template>
  <div>
    <button @click="increment">Increment</button>
    <button @click="decrement">Decrement</button>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  methods: {
    ...mapMutations(['increment', 'decrement'])
  }
}
</script>
```

### Example: Object-Style Commit

```javascript
this.$store.commit({
  type: 'increment',
  amount: 10
})
```

### Key Points

- Mutations must be synchronous
- Commit mutations via $store.commit
- Use mapMutations helper
- Mutations receive state and payload
- Only way to change state
