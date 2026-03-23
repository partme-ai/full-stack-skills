# Quick Start

**官方文档**: https://vuex.vuejs.org/zh/,


## Instructions

This example provides a quick start guide for Vuex.

### Key Concepts

- Basic store setup
- State access
- Mutations
- Component usage

### Example: Basic Store

```javascript
// store/index.js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

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

export default store
```

### Example: Component Usage

```vue
<template>
  <div>
    <p>{{ count }}</p>
    <button @click="increment">+</button>
    <button @click="decrement">-</button>
  </div>
</template>

<script>
export default {
  computed: {
    count() {
      return this.$store.state.count
    }
  },
  methods: {
    increment() {
      this.$store.commit('increment')
    },
    decrement() {
      this.$store.commit('decrement')
    }
  }
}
</script>
```

### Example: Using mapState

```vue
<template>
  <div>
    <p>{{ count }}</p>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState(['count'])
  }
}
</script>
```

### Example: Using mapMutations

```vue
<template>
  <div>
    <button @click="increment">+</button>
    <button @click="decrement">-</button>
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

### Key Points

- Create store with state and mutations
- Access state via $store.state
- Commit mutations via $store.commit
- Use mapState and mapMutations helpers
- Inject store in Vue instance
