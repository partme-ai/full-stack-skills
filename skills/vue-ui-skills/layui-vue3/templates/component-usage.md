# Component Usage Templates

## Button Usage

```vue
<template>
  <lay-button type="primary" @click="handleClick">
    Click Me
  </lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'

const handleClick = () => {
  console.log('Clicked')
}
</script>
```

## Table Usage

```vue
<template>
  <lay-table 
    :columns="columns" 
    :data-source="dataSource"
    :pagination="pagination"
  ></lay-table>
</template>

<script setup>
import { ref } from 'vue'
import { LayTable } from '@layui/layui-vue'

const columns = [
  { title: 'ID', key: 'id' },
  { title: 'Name', key: 'name' }
]

const dataSource = ref([
  { id: 1, name: 'John' },
  { id: 2, name: 'Jane' }
])

const pagination = ref({
  current: 1,
  pageSize: 10,
  total: 100
})
</script>
```

## Form Usage

```vue
<template>
  <lay-form :model="form" :rules="rules">
    <lay-form-item label="Name" prop="name">
      <lay-input v-model="form.name"></lay-input>
    </lay-form-item>
    <lay-form-item>
      <lay-button type="primary" @click="submit">Submit</lay-button>
    </lay-form-item>
  </lay-form>
</template>

<script setup>
import { ref } from 'vue'
import { LayForm, LayFormItem, LayInput, LayButton } from '@layui/layui-vue'

const form = ref({
  name: ''
})

const rules = {
  name: [{ required: true, message: 'Name is required' }]
}

const submit = () => {
  // Handle submission
}
</script>
```

## Layer Usage

```vue
<template>
  <lay-button @click="openLayer">Open</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'
import { layer } from '@layui/layui-vue'

const openLayer = () => {
  layer.open({
    title: 'Title',
    content: 'Content'
  })
}
</script>
```
