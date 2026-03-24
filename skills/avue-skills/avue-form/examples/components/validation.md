# Form Validation

**官方文档**: https://avuejs.com/form/form-doc.html


## Instructions

This example demonstrates form validation in Avue-form.

### Key Concepts

- Validation rules
- Rule types
- Custom validation
- Error messages

### Example: Basic Validation

```vue
<template>
  <avue-form :option="option" v-model="form"></avue-form>
</template>

<script>
export default {
  data() {
    return {
      form: {},
      option: {
        column: [
          {
            label: 'Name',
            prop: 'name',
            type: 'input',
            rules: [
              { required: true, message: 'Please input name' }
            ]
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Multiple Rules

```javascript
column: [
  {
    label: 'Email',
    prop: 'email',
    type: 'input',
    rules: [
      { required: true, message: 'Please input email' },
      { type: 'email', message: 'Please input valid email' }
    ]
  }
]
```

### Example: Custom Validation

```javascript
const validateAge = (rule, value, callback) => {
  if (value < 18) {
    callback(new Error('Age must be at least 18'))
  } else {
    callback()
  }
}

column: [
  {
    label: 'Age',
    prop: 'age',
    type: 'number',
    rules: [
      { required: true, message: 'Please input age' },
      { validator: validateAge, trigger: 'blur' }
    ]
  }
]
```

### Example: Validation Methods

```vue
<template>
  <avue-form 
    ref="form"
    :option="option" 
    v-model="form"
  ></avue-form>
  <el-button @click="validate">Validate</el-button>
</template>

<script>
export default {
  methods: {
    validate() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          console.log('Validation passed')
        } else {
          console.log('Validation failed')
        }
      })
    }
  }
}
</script>
```

### Key Points

- Define validation rules
- Use built-in rule types
- Create custom validators
- Handle validation errors
- Use validation methods
