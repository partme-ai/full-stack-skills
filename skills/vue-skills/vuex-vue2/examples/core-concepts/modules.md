# Modules

**官方文档**: https://vuex.vuejs.org/zh/,


## Instructions

This example demonstrates modules usage in Vuex.

### Key Concepts

- Module definition
- Module namespacing
- Module state access
- Module mutations and actions

### Example: Basic Module

```javascript
// store/modules/user.js
const userModule = {
  state: {
    name: '',
    email: ''
  },
  mutations: {
    setName(state, name) {
      state.name = name
    }
  },
  actions: {
    fetchUser({ commit }) {
      // Fetch user data
      commit('setName', 'John')
    }
  }
}

export default userModule
```

### Example: Registering Module

```javascript
// store/index.js
import userModule from './modules/user'

const store = new Vuex.Store({
  modules: {
    user: userModule
  }
})
```

### Example: Namespaced Module

```javascript
// store/modules/user.js
const userModule = {
  namespaced: true,
  state: {
    name: ''
  },
  mutations: {
    setName(state, name) {
      state.name = name
    }
  },
  actions: {
    fetchUser({ commit }) {
      commit('setName', 'John')
    }
  }
}
```

### Example: Accessing Namespaced Module

```vue
<template>
  <div>
    <p>{{ userName }}</p>
    <button @click="fetchUser">Fetch User</button>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState('user', ['name']),
    userName() {
      return this.$store.state.user.name
    }
  },
  methods: {
    ...mapActions('user', ['fetchUser']),
    fetchUser() {
      this.$store.dispatch('user/fetchUser')
    }
  }
}
</script>
```

### Example: Accessing Root State

```javascript
// In namespaced module
actions: {
  someAction({ commit, state, rootState, rootGetters }) {
    // Access root state
    console.log(rootState.someRootState)
    
    // Access root getters
    console.log(rootGetters.someRootGetter)
    
    // Commit root mutation
    commit('someRootMutation', null, { root: true })
    
    // Dispatch root action
    dispatch('someRootAction', null, { root: true })
  }
}
```

### Key Points

- Organize store with modules
- Use namespaced modules
- Access module state via namespace
- Access root state in modules
- Register modules in store
