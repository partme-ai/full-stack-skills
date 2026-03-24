# Getters API

## API Reference

Vuex getters API.

### Getter Definition

**getter(state, getters, rootState, rootGetters)**
- Getter function
- Parameters:
  - `state`: Local state (module state if in module)
  - `getters`: Local getters (module getters if in module)
  - `rootState`: Root state (only in modules)
  - `rootGetters`: Root getters (only in modules)

### Getter Access

**store.getters.getterName**
- Access getter value
- Returns: Getter return value

### Getter Examples

```javascript
// Basic getter
getters: {
  doneTodos: state => {
    return state.todos.filter(todo => todo.done)
  }
}

// Getter with arguments (returns function)
getters: {
  getTodoById: state => id => {
    return state.todos.find(todo => todo.id === id)
  }
}

// Getter accessing other getters
getters: {
  doneTodos: state => state.todos.filter(todo => todo.done),
  doneTodosCount: (state, getters) => getters.doneTodos.length
}
```

### Getter Access in Components

```javascript
// Direct access
this.$store.getters.doneTodos

// With arguments
this.$store.getters.getTodoById(1)

// Using mapGetters
import { mapGetters } from 'vuex'
computed: {
  ...mapGetters(['doneTodos', 'doneTodosCount'])
}
```

### Getter Rules

- Getters are cached
- Getters are computed properties
- Getters can access other getters
- Getters receive state and getters as arguments

**See also:** `examples/core-concepts/getters.md` for detailed examples
