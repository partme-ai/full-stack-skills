# Store Setup Templates

## Basic Store

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
    }
  }
})

export default store
```

## Store with All Features

```javascript
// store/index.js
import Vue from 'vue'
import Vuex from 'vuex'
import userModule from './modules/user'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    count: 0
  },
  getters: {
    doubleCount: state => state.count * 2
  },
  mutations: {
    increment(state) {
      state.count++
    }
  },
  actions: {
    incrementAsync({ commit }) {
      setTimeout(() => {
        commit('increment')
      }, 1000)
    }
  },
  modules: {
    user: userModule
  }
})

export default store
```

## Module Template

```javascript
// store/modules/user.js
const userModule = {
  namespaced: true,
  state: {
    name: '',
    email: ''
  },
  getters: {
    fullName: state => `${state.name} (${state.email})`
  },
  mutations: {
    setName(state, name) {
      state.name = name
    }
  },
  actions: {
    fetchUser({ commit }, userId) {
      // Async operation
      commit('setName', 'John')
    }
  }
}

export default userModule
```
