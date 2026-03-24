# Store Template | Store 模板

## Options API Store Template

```javascript
import { defineStore } from 'pinia'

export const useResourceStore = defineStore('resource', {
  state: () => ({
    items: [],
    loading: false,
    error: null
  }),
  getters: {
    itemCount: (state) => state.items.length,
    getItemById: (state) => {
      return (id) => state.items.find(item => item.id === id)
    }
  },
  actions: {
    async fetchItems() {
      this.loading = true
      this.error = null
      try {
        const response = await fetch('/api/items')
        const data = await response.json()
        this.items = data
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

## Composition API Store Template

```javascript
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useResourceStore = defineStore('resource', () => {
  const items = ref([])
  const loading = ref(false)
  const error = ref(null)
  
  const itemCount = computed(() => items.value.length)
  
  const getItemById = computed(() => {
    return (id) => items.value.find(item => item.id === id)
  })
  
  async function fetchItems() {
    loading.value = true
    error.value = null
    try {
      const response = await fetch('/api/items')
      const data = await response.json()
      items.value = data
    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }
  
  function addItem(item) {
    items.value.push(item)
  }
  
  function removeItem(id) {
    items.value = items.value.filter(item => item.id !== id)
  }
  
  return {
    items,
    loading,
    error,
    itemCount,
    getItemById,
    fetchItems,
    addItem,
    removeItem
  }
})
```
