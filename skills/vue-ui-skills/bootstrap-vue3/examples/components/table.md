# Table | 表格

**官方文档**: https://bootstrap-vue.org


## Instructions

This example demonstrates how to use the Table component in Bootstrap Vue 3.0.

### Key Concepts

- Basic Table
- Table with data
- Table with sorting
- Table with filtering
- Table with pagination
- Table with selection

### Example: Basic Table

```vue
<template>
  <BTable :items="items" :fields="fields" />
</template>

<script setup>
import { ref } from 'vue'
import { BTable } from 'bootstrap-vue-next'

const fields = [
  { key: 'name', label: 'Name' },
  { key: 'age', label: 'Age' },
  { key: 'address', label: 'Address' }
]

const items = ref([
  { name: 'John Brown', age: 32, address: 'New York' },
  { name: 'Jim Green', age: 42, address: 'London' },
  { name: 'Joe Black', age: 32, address: 'Sidney' }
])
</script>
```

### Example: Table with Sorting

```vue
<template>
  <BTable
    :items="items"
    :fields="fields"
    sortable
  />
</template>

<script setup>
import { ref } from 'vue'
import { BTable } from 'bootstrap-vue-next'

const fields = [
  { key: 'name', label: 'Name', sortable: true },
  { key: 'age', label: 'Age', sortable: true },
  { key: 'address', label: 'Address' }
]

const items = ref([
  { name: 'John Brown', age: 32, address: 'New York' },
  { name: 'Jim Green', age: 42, address: 'London' },
  { name: 'Joe Black', age: 32, address: 'Sidney' }
])
</script>
```

### Example: Table with Pagination

```vue
<template>
  <div>
    <BTable
      :items="items"
      :fields="fields"
      :per-page="perPage"
      :current-page="currentPage"
    />
    <BPagination
      v-model="currentPage"
      :total-rows="items.length"
      :per-page="perPage"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { BTable, BPagination } from 'bootstrap-vue-next'

const fields = [
  { key: 'name', label: 'Name' },
  { key: 'age', label: 'Age' },
  { key: 'address', label: 'Address' }
]

const items = ref([
  { name: 'John Brown', age: 32, address: 'New York' },
  { name: 'Jim Green', age: 42, address: 'London' },
  { name: 'Joe Black', age: 32, address: 'Sidney' }
])

const perPage = ref(10)
const currentPage = ref(1)
</script>
```

### Example: Table with Selection

```vue
<template>
  <BTable
    :items="items"
    :fields="fields"
    selectable
    select-mode="multi"
    v-model:selected="selected"
  />
</template>

<script setup>
import { ref } from 'vue'
import { BTable } from 'bootstrap-vue-next'

const fields = [
  { key: 'name', label: 'Name' },
  { key: 'age', label: 'Age' },
  { key: 'address', label: 'Address' }
]

const items = ref([
  { name: 'John Brown', age: 32, address: 'New York' },
  { name: 'Jim Green', age: 42, address: 'London' },
  { name: 'Joe Black', age: 32, address: 'Sidney' }
])

const selected = ref([])
</script>
```

### Key Points

- Use `BTable` component with `:items` and `:fields` props
- Use `:fields` to define table columns
- Use `:items` for table data
- Use `sortable` prop for sorting
- Use `BPagination` for pagination
- Use `selectable` and `select-mode` for row selection
- Use `v-model:selected` for selected rows
