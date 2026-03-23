# Mutations API

## API Reference

Vuex mutations API.

### Mutation Handler

**mutationHandler(state, payload)**
- Mutation handler function
- Parameters:
  - `state`: Store state object
  - `payload`: Mutation payload (optional)

### Commit Method

**store.commit(type, payload, options)**
- Commit mutation
- Parameters:
  - `type`: `string` - Mutation type
  - `payload`: `any` - Mutation payload (optional)
  - `options`: `object` - Options (optional)
    - `silent`: `boolean` - Silent commit (no devtools)
    - `root`: `boolean` - Commit to root (for namespaced modules)

### Commit Examples

```javascript
// String type
store.commit('increment')

// With payload
store.commit('increment', 10)

// Object style
store.commit({
  type: 'increment',
  amount: 10
})

// In namespaced module
store.commit('user/setName', 'John', { root: false })
```

### Mutation Rules

- Mutations must be synchronous
- Mutations are the only way to change state
- Mutations are tracked by devtools
- Mutations should be pure functions

**See also:** `examples/core-concepts/mutations.md` for detailed examples
