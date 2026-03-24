# Form | 表单

**官方文档**: https://www.uviewui.com


## Instructions

This example demonstrates how to use Form components in uView UI.

### Key Concepts

- Form component setup
- Form validation
- Form inputs
- Form submission
- Form layout

### Example: Basic Form

```vue
<template>
  <u-form :model="form" ref="form">
    <u-form-item label="Username" prop="username">
      <u-input v-model="form.username" />
    </u-form-item>
    <u-form-item label="Email" prop="email">
      <u-input v-model="form.email" type="email" />
    </u-form-item>
    <u-button type="primary" @click="submit">Submit</u-button>
  </u-form>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: '',
        email: ''
      }
    }
  },
  methods: {
    submit() {
      this.$refs.form.validate().then(valid => {
        if (valid) {
          console.log('Form submitted:', this.form)
        }
      })
    }
  }
}
</script>
```

### Example: Form with Validation

```vue
<template>
  <u-form :model="form" :rules="rules" ref="form">
    <u-form-item label="Email" prop="email">
      <u-input v-model="form.email" />
    </u-form-item>
    <u-form-item label="Password" prop="password">
      <u-input v-model="form.password" type="password" />
    </u-form-item>
    <u-button type="primary" @click="submit">Submit</u-button>
  </u-form>
</template>

<script>
export default {
  data() {
    return {
      form: {
        email: '',
        password: ''
      },
      rules: {
        email: [
          { required: true, message: 'Please enter email', trigger: 'blur' },
          { type: 'email', message: 'Please enter valid email', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Please enter password', trigger: 'blur' },
          { min: 6, message: 'Password must be at least 6 characters', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submit() {
      this.$refs.form.validate().then(valid => {
        if (valid) {
          console.log('Form submitted:', this.form)
        }
      })
    }
  }
}
</script>
```

### Example: Form with Select

```vue
<template>
  <u-form :model="form" ref="form">
    <u-form-item label="Select" prop="select">
      <u-input
        v-model="form.select"
        type="select"
        :select-open="selectOpen"
        @click="selectOpen = true"
      />
      <u-picker
        :show="selectOpen"
        :columns="columns"
        @confirm="handleSelect"
        @cancel="selectOpen = false"
      />
    </u-form-item>
  </u-form>
</template>

<script>
export default {
  data() {
    return {
      form: {
        select: ''
      },
      selectOpen: false,
      columns: [
        ['Option 1', 'Option 2', 'Option 3']
      ]
    }
  },
  methods: {
    handleSelect(e) {
      this.form.select = e.value[0]
      this.selectOpen = false
    }
  }
}
</script>
```

### Key Points

- Use `u-form` component to wrap form fields
- Use `u-form-item` for form field groups
- Use `:model` prop for form data
- Use `:rules` prop for validation rules
- Use `ref` and `validate()` method for form validation
- Use `prop` prop to link form item with form data
- Form works in uni-app pages
