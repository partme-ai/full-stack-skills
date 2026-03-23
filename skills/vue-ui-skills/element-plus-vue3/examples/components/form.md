# Form Component

**官方文档**: https://element-plus.org/en-US/component/form.html


## Instructions

This example demonstrates the Form component in Element Plus.

### Key Concepts

- Form structure
- Form validation
- Form rules
- Form submission
- Form fields

### Example: Basic Form

```vue
<template>
  <el-form :model="form" label-width="120px">
    <el-form-item label="Name">
      <el-input v-model="form.name" />
    </el-form-item>
    <el-form-item label="Email">
      <el-input v-model="form.email" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="handleSubmit">Submit</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import { ref } from 'vue'

const form = ref({
  name: '',
  email: ''
})

const handleSubmit = () => {
  console.log('Form:', form.value)
}
</script>
```

### Example: Form Validation

```vue
<template>
  <el-form
    ref="formRef"
    :model="form"
    :rules="rules"
    label-width="120px"
  >
    <el-form-item label="Name" prop="name">
      <el-input v-model="form.name" />
    </el-form-item>
    <el-form-item label="Email" prop="email">
      <el-input v-model="form.email" />
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
  name: '',
  email: ''
})

const rules = {
  name: [
    { required: true, message: 'Please input name', trigger: 'blur' }
  ],
  email: [
    { required: true, message: 'Please input email', trigger: 'blur' },
    { type: 'email', message: 'Please input valid email', trigger: 'blur' }
  ]
}

const handleSubmit = async () => {
  await formRef.value.validate((valid) => {
    if (valid) {
      console.log('Form valid:', form.value)
    }
  })
}
</script>
```

### Example: Form Layout

```vue
<template>
  <el-form :model="form" label-position="top">
    <el-row :gutter="20">
      <el-col :span="12">
        <el-form-item label="Name">
          <el-input v-model="form.name" />
        </el-form-item>
      </el-col>
      <el-col :span="12">
        <el-form-item label="Email">
          <el-input v-model="form.email" />
        </el-form-item>
      </el-col>
    </el-row>
  </el-form>
</template>
```

### Key Points

- Use :model for form data
- Configure :rules for validation
- Use prop for form-item validation
- Handle form submission
- Support multiple layouts
