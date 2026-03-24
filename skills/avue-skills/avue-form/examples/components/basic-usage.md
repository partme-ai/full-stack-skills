# Basic Usage

**官方文档**: https://avuejs.com/form/form-doc.html


## Instructions

This example demonstrates basic usage of Avue-form.

### Key Concepts

- Form component
- Options configuration
- Columns definition
- v-model binding

### Example: Basic Form

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
            type: 'input'
          },
          {
            label: 'Email',
            prop: 'email',
            type: 'input'
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Form with Submit

```vue
<template>
  <avue-form 
    :option="option" 
    v-model="form"
    @submit="handleSubmit"
  ></avue-form>
</template>

<script>
export default {
  data() {
    return {
      form: {},
      option: {
        submitBtn: true,
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
  },
  methods: {
    handleSubmit(form, done) {
      console.log('Form data:', form)
      done()
    }
  }
}
</script>
```

### Example: Form with Reset

```vue
<template>
  <avue-form 
    :option="option" 
    v-model="form"
    @reset-change="handleReset"
  ></avue-form>
</template>

<script>
export default {
  data() {
    return {
      form: {},
      option: {
        submitBtn: true,
        emptyBtn: true,
        column: [
          {
            label: 'Name',
            prop: 'name',
            type: 'input'
          }
        ]
      }
    }
  },
  methods: {
    handleReset() {
      console.log('Form reset')
    }
  }
}
</script>
```

### Key Points

- Use avue-form component
- Configure option object
- Define columns array
- Use v-model for data binding
- Handle submit and reset events
