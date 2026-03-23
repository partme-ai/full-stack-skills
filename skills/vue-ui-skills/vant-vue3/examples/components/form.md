# Form | 表单

**官方文档入口**: https://vant-ui.github.io/vant/#/zh-CN
**官方对应章节**: Form / 表单


## Instructions

This example demonstrates how to use Form components in Vant.

### Key Concepts

- Form component setup
- Form validation
- Form fields
- Form submission
- Form layout

### Example: Basic Form

```vue
<template>
  <van-form @submit="onSubmit">
    <van-cell-group inset>
      <van-field
        v-model="form.username"
        name="username"
        label="Username"
        placeholder="Username"
        :rules="[{ required: true, message: 'Please enter username' }]"
      />
      <van-field
        v-model="form.password"
        type="password"
        name="password"
        label="Password"
        placeholder="Password"
        :rules="[{ required: true, message: 'Please enter password' }]"
      />
    </van-cell-group>
    <div style="margin: 16px;">
      <van-button round block type="primary" native-type="submit">
        Submit
      </van-button>
    </div>
  </van-form>
</template>

<script setup>
import { ref } from 'vue'
import { Form as VanForm, Field as VanField, CellGroup as VanCellGroup, Button as VanButton } from 'vant'

const form = ref({
  username: '',
  password: ''
})

const onSubmit = (values) => {
  console.log('Submit:', values)
}
</script>
```

### Example: Form with Validation

```vue
<template>
  <van-form @submit="onSubmit" @failed="onFailed">
    <van-cell-group inset>
      <van-field
        v-model="form.email"
        name="email"
        label="Email"
        placeholder="Email"
        :rules="emailRules"
      />
      <van-field
        v-model="form.password"
        type="password"
        name="password"
        label="Password"
        placeholder="Password"
        :rules="passwordRules"
      />
    </van-cell-group>
    <div style="margin: 16px;">
      <van-button round block type="primary" native-type="submit">
        Submit
      </van-button>
    </div>
  </van-form>
</template>

<script setup>
import { ref } from 'vue'
import { Form as VanForm, Field as VanField, CellGroup as VanCellGroup, Button as VanButton } from 'vant'

const form = ref({
  email: '',
  password: ''
})

const emailRules = [
  { required: true, message: 'Please enter email' },
  { pattern: /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/, message: 'Invalid email' }
]

const passwordRules = [
  { required: true, message: 'Please enter password' },
  { min: 6, message: 'Password must be at least 6 characters' }
]

const onSubmit = (values) => {
  console.log('Submit:', values)
}

const onFailed = (errorInfo) => {
  console.log('Failed:', errorInfo)
}
</script>
```

### Example: Form with Ref

```vue
<template>
  <van-form ref="formRef">
    <van-cell-group inset>
      <van-field
        v-model="form.username"
        name="username"
        label="Username"
        :rules="[{ required: true, message: 'Please enter username' }]"
      />
    </van-cell-group>
    <div style="margin: 16px;">
      <van-button type="primary" @click="submit">Submit</van-button>
      <van-button @click="reset">Reset</van-button>
    </div>
  </van-form>
</template>

<script setup>
import { ref } from 'vue'
import { Form as VanForm, Field as VanField, CellGroup as VanCellGroup, Button as VanButton } from 'vant'

const formRef = ref(null)
const form = ref({
  username: ''
})

const submit = async () => {
  try {
    await formRef.value.validate()
    console.log('Form valid:', form.value)
  } catch (error) {
    console.log('Validation failed')
  }
}

const reset = () => {
  formRef.value.resetValidation()
  form.value.username = ''
}
</script>
```

### Key Points

- Use `van-form` component to wrap form fields
- Use `van-field` for form inputs
- Use `:rules` prop for validation rules
- Use `@submit` for form submission
- Use `@failed` for validation failure
- Use `ref` and `validate()` method for programmatic validation
- Use `native-type="submit"` for submit button

### Related local files

- API summary: `api/components.md`
- Popup with form pattern: `examples/components/popup.md`
- Dialog with input pattern: `examples/components/dialog.md`
