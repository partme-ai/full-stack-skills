# Basic Form | 基础表单

**官方文档**: https://avuejs.com/


## Instructions

This example demonstrates how to use Avue form component.

### Key Concepts

- Form configuration
- Column definition
- Form validation
- Form submission
- Form events

### Example: Basic Form

```vue
<template>
  <avue-form
    :option="option"
    v-model="form"
  />
</template>

<script>
export default {
  data() {
    return {
      form: {},
      option: {
        column: [
          {
            label: 'Username',
            prop: 'username',
            type: 'input'
          },
          {
            label: 'Password',
            prop: 'password',
            type: 'password'
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Form with Validation

```vue
<template>
  <avue-form
    :option="option"
    v-model="form"
    @submit="handleSubmit"
  />
</template>

<script>
export default {
  data() {
    return {
      form: {},
      option: {
        column: [
          {
            label: 'Email',
            prop: 'email',
            type: 'input',
            rules: [
              { required: true, message: 'Please enter email' },
              { type: 'email', message: 'Invalid email format' }
            ]
          },
          {
            label: 'Age',
            prop: 'age',
            type: 'number',
            rules: [
              { required: true, message: 'Please enter age' },
              { type: 'number', min: 18, max: 100, message: 'Age must be between 18 and 100' }
            ]
          }
        ]
      }
    }
  },
  methods: {
    handleSubmit(form, done) {
      console.log('Form submitted:', form)
      done()
    }
  }
}
</script>
```

### Example: Form with Different Input Types

```vue
<template>
  <avue-form
    :option="option"
    v-model="form"
  />
</template>

<script>
export default {
  data() {
    return {
      form: {},
      option: {
        column: [
          {
            label: 'Text',
            prop: 'text',
            type: 'input'
          },
          {
            label: 'Number',
            prop: 'number',
            type: 'number'
          },
          {
            label: 'Select',
            prop: 'select',
            type: 'select',
            dicData: [
              { label: 'Option 1', value: '1' },
              { label: 'Option 2', value: '2' }
            ]
          },
          {
            label: 'Date',
            prop: 'date',
            type: 'date'
          },
          {
            label: 'Switch',
            prop: 'switch',
            type: 'switch'
          }
        ]
      }
    }
  }
}
</script>
```

### Key Points

- Use avue-form component
- Configure via option.column array
- Use type prop for input types
- Use rules for validation
- Use @submit for form submission
- v-model binds form data
- Data-driven configuration
