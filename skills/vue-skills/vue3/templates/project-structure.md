# Vue 3 Project Structure Template

## Standard Project Structure

```
my-vue-app/
├── public/                 # Static assets
│   ├── favicon.ico
│   └── index.html
├── src/
│   ├── assets/            # Imported assets (images, styles)
│   │   ├── logo.png
│   │   └── main.css
│   ├── components/        # Reusable components
│   │   ├── common/        # Common UI components
│   │   │   ├── Button.vue
│   │   │   ├── Input.vue
│   │   │   └── Modal.vue
│   │   └── layout/        # Layout components
│   │       ├── Header.vue
│   │       ├── Footer.vue
│   │       └── Sidebar.vue
│   ├── views/            # Page components
│   │   ├── Home.vue
│   │   ├── About.vue
│   │   └── User/
│   │       ├── UserList.vue
│   │       └── UserDetail.vue
│   ├── router/            # Vue Router configuration
│   │   └── index.js
│   ├── stores/            # Pinia stores
│   │   ├── index.js
│   │   ├── user.js
│   │   └── counter.js
│   ├── composables/       # Composition functions
│   │   ├── useCounter.js
│   │   ├── useFetch.js
│   │   └── useLocalStorage.js
│   ├── utils/             # Utility functions
│   │   ├── helpers.js
│   │   └── constants.js
│   ├── api/               # API calls
│   │   ├── index.js
│   │   ├── user.js
│   │   └── product.js
│   ├── App.vue            # Root component
│   └── main.js            # Application entry point
├── .env                   # Environment variables
├── .env.local            # Local environment variables
├── .gitignore
├── package.json
├── vite.config.js        # Vite configuration
└── README.md
```

## Component Template

```vue
<script setup>
// 1. Imports
import { ref, computed, watch, onMounted } from 'vue'
import MyComponent from './MyComponent.vue'

// 2. Props & Emits
const props = defineProps({
  title: {
    type: String,
    required: true
  }
})

const emit = defineEmits(['update', 'delete'])

// 3. Reactive state
const count = ref(0)
const message = ref('Hello')

// 4. Computed properties
const doubleCount = computed(() => count.value * 2)

// 5. Watchers
watch(count, (newVal, oldVal) => {
  console.log(`Count changed: ${oldVal} -> ${newVal}`)
})

// 6. Lifecycle hooks
onMounted(() => {
  console.log('Component mounted')
})

// 7. Methods
function handleClick() {
  count.value++
  emit('update', count.value)
}
</script>

<template>
  <div class="component">
    <h2>{{ props.title }}</h2>
    <p>{{ message }}</p>
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubleCount }}</p>
    <button @click="handleClick">Click me</button>
  </div>
</template>

<style scoped>
.component {
  padding: 20px;
}
</style>
```

## TypeScript Component Template

```vue
<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'

interface Props {
  title: string
  count?: number
}

const props = withDefaults(defineProps<Props>(), {
  count: 0
})

interface Emits {
  (e: 'update', value: number): void
}

const emit = defineEmits<Emits>()

const localCount = ref(props.count)

function increment() {
  localCount.value++
  emit('update', localCount.value)
}
</script>

<template>
  <div>
    <h2>{{ props.title }}</h2>
    <p>Count: {{ localCount }}</p>
    <button @click="increment">+</button>
  </div>
</template>
```

## Composable Template

```javascript
// composables/useExample.js
import { ref, computed, onMounted, onUnmounted } from 'vue'

export function useExample(initialValue = 0) {
  // State
  const value = ref(initialValue)
  
  // Computed
  const doubleValue = computed(() => value.value * 2)
  
  // Methods
  function increment() {
    value.value++
  }
  
  function decrement() {
    value.value--
  }
  
  function reset() {
    value.value = initialValue
  }
  
  // Lifecycle
  onMounted(() => {
    console.log('Composable mounted')
  })
  
  onUnmounted(() => {
    console.log('Composable unmounted')
    // Cleanup logic here
  })
  
  // Return public API
  return {
    value,
    doubleValue,
    increment,
    decrement,
    reset
  }
}
```

## Store Template

```javascript
// stores/example.js
import { defineStore } from 'pinia'

export const useExampleStore = defineStore('example', {
  state: () => ({
    items: [],
    loading: false,
    error: null
  }),
  
  getters: {
    itemCount: (state) => state.items.length,
    hasItems: (state) => state.items.length > 0
  },
  
  actions: {
    async fetchItems() {
      this.loading = true
      this.error = null
      try {
        const response = await fetch('/api/items')
        this.items = await response.json()
      } catch (error) {
        this.error = error.message
      } finally {
        this.loading = false
      }
    },
    
    addItem(item) {
      this.items.push(item)
    },
    
    removeItem(id) {
      this.items = this.items.filter(item => item.id !== id)
    }
  }
})
```

## Router Template

```javascript
// router/index.js
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
```

## Main.js Template

```javascript
// main.js
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)
app.mount('#app')
```

## Vite Config Template

```javascript
// vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    port: 3000,
    open: true
  }
})
```
