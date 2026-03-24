# Composition API | 组合式 API

**官方文档**: https://router.vuejs.org/guide/advanced/composition-api.html


## Instructions

This example demonstrates how to use Vue Router with the Composition API in Vue 3.

### Key Concepts

- `useRouter()` - Access router instance
- `useRoute()` - Access current route
- Using router in `setup()` function
- Reactive route properties
- Navigation with Composition API

### Example: Basic Usage

```vue
<template>
  <div>
    <p>Current route: {{ route.path }}</p>
    <button @click="goHome">Go Home</button>
  </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

function goHome() {
  router.push('/')
}
</script>
```

### Example: Accessing Route Params

```vue
<template>
  <div>
    <h1>User {{ userId }}</h1>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()
const userId = computed(() => route.params.id)
</script>
```

### Example: Accessing Query and Hash

```vue
<template>
  <div>
    <p>Query: {{ route.query }}</p>
    <p>Hash: {{ route.hash }}</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>
```

### Example: Navigation Methods

```vue
<template>
  <div>
    <button @click="pushRoute">Push</button>
    <button @click="replaceRoute">Replace</button>
    <button @click="goBack">Back</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function pushRoute() {
  router.push('/home')
}

function replaceRoute() {
  router.replace('/home')
}

function goBack() {
  router.back()
}
</script>
```

### Example: Watching Route Changes

```vue
<template>
  <div>User {{ userId }}</div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { watch } from 'vue'

const route = useRoute()

watch(() => route.params.id, (newId, oldId) => {
  console.log(`User changed from ${oldId} to ${newId}`)
  // Fetch new user data
  fetchUserData(newId)
})
</script>
```

### Example: Using Route Meta

```vue
<template>
  <div>
    <h1>{{ route.meta.title }}</h1>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>
```

### Example: Programmatic Navigation with Params

```vue
<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function navigateToUser(id) {
  router.push({
    name: 'User',
    params: { id }
  })
}

function navigateWithQuery(query) {
  router.push({
    path: '/search',
    query: { q: query }
  })
}
</script>
```

### Example: TypeScript Support

```vue
<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router'
import type { RouteLocationNormalized } from 'vue-router'

const router = useRouter()
const route: RouteLocationNormalized = useRoute()

const userId = computed(() => route.params.id as string)
</script>
```

### Key Points

- `useRouter()` returns the router instance
- `useRoute()` returns the current route (reactive)
- Route properties are reactive and update automatically
- Can use `watch` to react to route changes
- Works seamlessly with Composition API
- TypeScript support available
- No need to access `this.$router` or `this.$route`
