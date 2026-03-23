# Table Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/table


## Instructions

This example demonstrates the Table component in Layui Vue.

### Key Concepts

- Table data
- Columns configuration
- Sorting
- Pagination
- Selection

### Example: Basic Table

```vue
<template>
  <lay-table :columns="columns" :data-source="dataSource"></lay-table>
</template>

<script setup>
import { ref } from 'vue'
import { LayTable } from '@layui/layui-vue'

const columns = [
  { title: 'ID', key: 'id' },
  { title: 'Name', key: 'name' },
  { title: 'Email', key: 'email' }
]

const dataSource = ref([
  { id: 1, name: 'John', email: 'john@example.com' },
  { id: 2, name: 'Jane', email: 'jane@example.com' }
])
</script>
```

### Example: Table with Sorting

```vue
<template>
  <lay-table :columns="columns" :data-source="dataSource" :sortable="true"></lay-table>
</template>

<script setup>
import { ref } from 'vue'
import { LayTable } from '@layui/layui-vue'

const columns = [
  { title: 'ID', key: 'id', sort: true },
  { title: 'Name', key: 'name', sort: true }
]

const dataSource = ref([
  { id: 1, name: 'John' },
  { id: 2, name: 'Jane' }
])
</script>
```

### Example: Table with Pagination

```vue
<template>
  <lay-table 
    :columns="columns" 
    :data-source="dataSource"
    :pagination="pagination"
    @change="handleChange"
  ></lay-table>
</template>

<script setup>
import { ref } from 'vue'
import { LayTable } from '@layui/layui-vue'

const columns = [
  { title: 'ID', key: 'id' },
  { title: 'Name', key: 'name' }
]

const dataSource = ref([...])
const pagination = ref({
  current: 1,
  pageSize: 10,
  total: 100
})

const handleChange = (page, pageSize) => {
  // Handle pagination change
}
</script>
```

### Example: Table with Selection

```vue
<template>
  <lay-table 
    :columns="columns" 
    :data-source="dataSource"
    :checkbox="true"
    v-model:selectedKeys="selectedKeys"
  ></lay-table>
</template>

<script setup>
import { ref } from 'vue'
import { LayTable } from '@layui/layui-vue'

const selectedKeys = ref([])
</script>
```

### Key Points

- Configure columns and data source
- Enable sorting with sort: true
- Configure pagination
- Support row selection
- Handle table events
