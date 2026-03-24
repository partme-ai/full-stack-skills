# Validation | 验证

**官方文档**: https://avuejs.com/crud/crud-doc.html


## Instructions

This example demonstrates form validation in Avue CRUD.

### Key Concepts

- Validation rules
- Required fields
- Type validation
- Custom validation
- Error messages

### Example: Basic Validation

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
    @row-save="handleSave"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      option: {
        column: [
          {
            label: 'Name',
            prop: 'name',
            rules: [
              { required: true, message: 'Please enter name', trigger: 'blur' }
            ]
          },
          {
            label: 'Email',
            prop: 'email',
            rules: [
              { required: true, message: 'Please enter email', trigger: 'blur' },
              { type: 'email', message: 'Invalid email format', trigger: 'blur' }
            ]
          }
        ]
      }
    }
  },
  methods: {
    handleSave(row, done) {
      console.log('Valid data:', row)
      done()
    }
  }
}
</script>
```

### Example: Advanced Validation

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      option: {
        column: [
          {
            label: 'Age',
            prop: 'age',
            type: 'number',
            rules: [
              { required: true, message: 'Please enter age' },
              { type: 'number', min: 18, max: 100, message: 'Age must be between 18 and 100' }
            ]
          },
          {
            label: 'Password',
            prop: 'password',
            type: 'password',
            rules: [
              { required: true, message: 'Please enter password' },
              { min: 6, max: 20, message: 'Password must be 6-20 characters' }
            ]
          },
          {
            label: 'Confirm Password',
            prop: 'confirmPassword',
            type: 'password',
            rules: [
              { required: true, message: 'Please confirm password' },
              {
                validator: (rule, value, callback) => {
                  if (value !== this.form.password) {
                    callback(new Error('Passwords do not match'))
                  } else {
                    callback()
                  }
                },
                trigger: 'blur'
              }
            ]
          }
        ]
      }
    }
  }
}
</script>
```

### Key Points

- Use rules array for validation
- Use required for required fields
- Use type for type validation
- Use min/max for range validation
- Use validator for custom validation
- Use trigger for validation trigger
- Validation runs on form submit
