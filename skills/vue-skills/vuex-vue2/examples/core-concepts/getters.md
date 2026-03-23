# Getters

**官方文档**: https://vuex.vuejs.org/zh/,


## Instructions

This example demonstrates getters usage in Vuex.

### Key Concepts

- Getter definition
- Getter access
- Getter arguments
- Computed properties

### Example: Basic Getter

```javascript
// store/index.js
const store = new Vuex.Store({
  state: {
    todos: [
      { id: 1, text: 'Todo 1', done: true },
      { id: 2, text: 'Todo 2', done: false }
    ]
  },
  getters: {
    doneTodos: state => {
      return state.todos.filter(todo => todo.done)
    }
  }
})
```

### Example: Getter with Arguments

```javascript
getters: {
  getTodoById: state => id => {
    return state.todos.find(todo => todo.id === id)
  }
}
```

### Example: Getter Accessing Other Getters

```javascript
getters: {
  doneTodos: state => {
    return state.todos.filter(todo => todo.done)
  },
  doneTodosCount: (state, getters) => {
    return getters.doneTodos.length
  }
}
```

### Example: Accessing Getters in Components

```vue
<template>
  <div>
    <p>Done: {{ doneTodos.length }}</p>
  </div>
</template>

<script>
export default {
  computed: {
    doneTodos() {
      return this.$store.getters.doneTodos
    }
  }
}
</script>
```

### Example: Using mapGetters

```vue
<template>
  <div>
    <p>Done: {{ doneTodos.length }}</p>
    <p>Count: {{ doneTodosCount }}</p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters(['doneTodos', 'doneTodosCount'])
  }
}
</script>
```

### Key Points

- Getters are computed properties
- Access via $store.getters
- Use mapGetters helper
- Getters are cached
- Can access other getters
