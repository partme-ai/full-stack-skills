# Modules API

## API Reference

Vuex modules API.

### Module Definition

```typescript
interface Module {
  namespaced?: boolean
  state?: Object | Function
  getters?: Object
  mutations?: Object
  actions?: Object
  modules?: Object
}
```

### Module Registration

**Static Registration:**
```javascript
const store = new Vuex.Store({
  modules: {
    user: userModule,
    products: productsModule
  }
})
```

**Dynamic Registration:**
```javascript
store.registerModule('user', userModule)
```

### Module Namespacing

**Namespaced Module:**
```javascript
const module = {
  namespaced: true,
  state: {},
  getters: {},
  mutations: {},
  actions: {}
}
```

**Accessing Namespaced Module:**
```javascript
// State
store.state.moduleName.property

// Getters
store.getters['moduleName/getterName']

// Mutations
store.commit('moduleName/mutationName', payload)

// Actions
store.dispatch('moduleName/actionName', payload)
```

### Module Context

In namespaced modules, context provides:
- `state`: Local module state
- `getters`: Local module getters
- `commit`: Local commit (namespaced)
- `dispatch`: Local dispatch (namespaced)
- `rootState`: Root state
- `rootGetters`: Root getters

### Accessing Root

```javascript
// Commit root mutation
commit('someMutation', null, { root: true })

// Dispatch root action
dispatch('someAction', null, { root: true })
```

**See also:** `examples/core-concepts/modules.md` for detailed examples
