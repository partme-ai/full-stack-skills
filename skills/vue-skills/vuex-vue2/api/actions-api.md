# Actions API

## API Reference

Vuex actions API.

### Action Handler

**actionHandler(context, payload)**
- Action handler function
- Parameters:
  - `context`: Action context object
    - `state`: Local state
    - `getters`: Local getters
    - `commit`: Commit function
    - `dispatch`: Dispatch function
    - `rootState`: Root state
    - `rootGetters`: Root getters
  - `payload`: Action payload (optional)

### Dispatch Method

**store.dispatch(type, payload, options)**
- Dispatch action
- Parameters:
  - `type`: `string` - Action type
  - `payload`: `any` - Action payload (optional)
  - `options`: `object` - Options (optional)
    - `root`: `boolean` - Dispatch to root (for namespaced modules)

### Dispatch Examples

```javascript
// String type
store.dispatch('increment')

// With payload
store.dispatch('fetchUser', userId)

// Object style
store.dispatch({
  type: 'fetchUser',
  userId: 1
})

// In namespaced module
store.dispatch('user/fetchUser', userId, { root: false })
```

### Action Context Destructuring

```javascript
actions: {
  async fetchData({ commit, state, dispatch, rootState }) {
    // Use context properties
  }
}
```

### Action Rules

- Actions can be asynchronous
- Actions commit mutations
- Actions can dispatch other actions
- Actions can access root state/getters

**See also:** `examples/core-concepts/actions.md` for detailed examples
