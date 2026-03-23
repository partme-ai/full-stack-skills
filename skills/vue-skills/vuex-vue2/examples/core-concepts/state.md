# State

**官方文档**: https://vuex.vuejs.org/zh/,


## Instructions

This example demonstrates state usage in Vuex.

### Key Concepts

- State definition
- State access
- State reactivity
- Single source of truth

### Example: State Definition

```javascript
// store/index.js
const store = new Vuex.Store({
  state: {
    count: 0,
    todos: [],
    user: {
      name: '',
      email: ''
    }
  }
})
```

### Example: Accessing State in Components

```vue
<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>User: {{ user.name }}</p>
  </div>
</template>

<script>
export default {
  computed: {
    count() {
      return this.$store.state.count
    },
    user() {
      return this.$store.state.user
    }
  }
}
</script>
```

### Example: Using mapState

```vue
<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Todos: {{ todos.length }}</p>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState(['count', 'todos'])
  }
}
</script>
```

### Example: mapState with Object Syntax

```vue
<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState({
      count: state => state.count,
      todos: state => state.todos,
      user: 'user'
    })
  }
}
</script>
```

### Example: State as Function

```javascript
// For module reuse
const moduleA = {
  state: () => ({
    count: 0
  })
}
```

### Key Points

- State is reactive
- Access via $store.state
- Use mapState helper
- State can be object or function
- Single source of truth
