# Form Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/form


## Instructions

This example demonstrates the Form component in Layui Vue.

### Key Concepts

- Form structure
- Form validation
- Form submission
- Form fields

### Example: Basic Form

```vue
<template>
  <lay-form :model="form" :rules="rules">
    <lay-form-item label="Name" prop="name">
      <lay-input v-model="form.name"></lay-input>
    </lay-form-item>
    <lay-form-item label="Email" prop="email">
      <lay-input v-model="form.email"></lay-input>
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
  name: '',
  email: ''
})

const rules = {
  name: [{ required: true, message: 'Name is required' }],
  email: [{ required: true, message: 'Email is required' }]
}

const submit = () => {
  // Handle form submission
}
</script>
```

### Example: Form Validation

```vue
<template>
  <lay-form ref="formRef" :model="form" :rules="rules">
    <lay-form-item label="Name" prop="name">
      <lay-input v-model="form.name"></lay-input>
    </lay-form-item>
    <lay-form-item>
      <lay-button type="primary" @click="validate">Validate</lay-button>
    </lay-form-item>
  </lay-form>
</template>

<script setup>
import { ref } from 'vue'
import { LayForm, LayFormItem, LayInput, LayButton } from '@layui/layui-vue'

const formRef = ref()
const form = ref({ name: '' })
const rules = {
  name: [{ required: true, message: 'Name is required' }]
}

const validate = async () => {
  await formRef.value.validate()
}
</script>
```

### Key Points

- Use lay-form for form container
- Use lay-form-item for form fields
- Configure validation rules
- Use ref to access form methods
- Handle form submission
