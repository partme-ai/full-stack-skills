# Quick Start | 快速开始

**官方文档**: https://avuejs.com/


## Instructions

This example demonstrates basic Avue usage for forms and tables.

### Key Concepts

- Basic form usage
- Basic table usage
- Data-driven approach
- Configuration options

### Example: Basic Form

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
            label: 'Username',
            prop: 'username',
            rules: [{ required: true, message: 'Please enter username' }]
          },
          {
            label: 'Email',
            prop: 'email',
            type: 'input',
            rules: [
              { required: true, message: 'Please enter email' },
              { type: 'email', message: 'Invalid email' }
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

### Example: Basic Table

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
    @row-save="handleSave"
    @row-update="handleUpdate"
    @row-del="handleDelete"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      option: {
        border: true,
        index: true,
        indexLabel: '序号',
        stripe: true,
        menuAlign: 'center',
        align: 'center',
        column: [
          {
            label: 'Name',
            prop: 'name',
            rules: [{ required: true, message: 'Please enter name' }]
          },
          {
            label: 'Email',
            prop: 'email'
          }
        ]
      }
    }
  },
  methods: {
    handleSave(row, done) {
      console.log('Save:', row)
      done()
    },
    handleUpdate(row, index, done) {
      console.log('Update:', row, index)
      done()
    },
    handleDelete(row, index) {
      console.log('Delete:', row, index)
    }
  }
}
</script>
```

### Key Points

- Use avue-form for forms
- Use avue-crud for tables with CRUD
- Configure via option object
- Use column array for form/table fields
- Data-driven approach
- Handle events with @submit, @row-save, etc.
