# Component Usage Templates

## Button Usage

```vue
<template>
  <el-button type="primary" @click="handleClick">
    Click Me
  </el-button>
</template>

<script setup>
const handleClick = () => {
  console.log('Clicked')
}
</script>
```

## Form Usage

```vue
<template>
  <el-form :model="form" :rules="rules" ref="formRef">
    <el-form-item label="Name" prop="name">
      <el-input v-model="form.name" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="handleSubmit">Submit</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { ref } from 'vue'

const formRef = ref()
const form = ref({
  name: ''
})

const rules = {
  name: [
    { required: true, message: 'Please input name', trigger: 'blur' }
  ]
}

const handleSubmit = async () => {
  await formRef.value.validate((valid) => {
    if (valid) {
      console.log('Form:', form.value)
    }
  })
}
</script>
```

## Table Usage

```vue
<template>
  <el-table :data="tableData">
    <el-table-column prop="name" label="Name" />
    <el-table-column prop="email" label="Email" />
  </el-table>
</template>

<script setup>
import { ref } from 'vue'

const tableData = ref([
  { name: 'John', email: 'john@example.com' },
  { name: 'Jane', email: 'jane@example.com' }
])
</script>
```

## Dialog Usage

```vue
<template>
  <el-button @click="dialogVisible = true">Open Dialog</el-button>
  <el-dialog v-model="dialogVisible" title="Dialog">
    <span>Dialog Content</span>
  </el-dialog>
</template>

<script setup>
import { ref } from 'vue'

const dialogVisible = ref(false)
</script>
```
