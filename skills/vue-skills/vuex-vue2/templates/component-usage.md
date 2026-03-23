# Component Usage Templates

## Accessing State

```vue
<template>
  <div>{{ count }}</div>
</template>

<script>
export default {
  computed: {
    count() {
      return this.$store.state.count
    }
  }
}
</script>
```

## Using mapState

```vue
<template>
  <div>{{ count }}</div>
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

## Committing Mutations

```vue
<template>
  <button @click="increment">Increment</button>
</template>

<script>
export default {
  methods: {
    increment() {
      this.$store.commit('increment')
    }
  }
}
</script>
```

## Using mapMutations

```vue
<template>
  <button @click="increment">Increment</button>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  methods: {
    ...mapMutations(['increment'])
  }
}
</script>
```

## Dispatching Actions

```vue
<template>
  <button @click="fetchUser">Fetch User</button>
</template>

<script>
export default {
  methods: {
    fetchUser() {
      this.$store.dispatch('fetchUser', 1)
    }
  }
}
</script>
```

## Using mapActions

```vue
<template>
  <button @click="fetchUser(1)">Fetch User</button>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  methods: {
    ...mapActions(['fetchUser'])
  }
}
</script>
```
