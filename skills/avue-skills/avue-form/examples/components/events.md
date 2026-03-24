# Form Events

**官方文档**: https://avuejs.com/form/form-doc.html


## Instructions

This example demonstrates form events in Avue-form.

### Key Concepts

- Event types
- Event handlers
- Event parameters
- Event usage

### Example: Submit Event

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
            type: 'input'
          }
        ]
      }
    }
  },
  methods: {
    handleSubmit(form, done) {
      console.log('Form data:', form)
      // Call done() to close loading
      done()
    }
  }
}
</script>
```

### Example: Reset Event

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
  methods: {
    handleReset() {
      console.log('Form reset')
    }
  }
}
</script>
```

### Example: Change Event

```vue
<template>
  <avue-form 
    :option="option" 
    v-model="form"
    @change="handleChange"
  ></avue-form>
</template>

<script>
export default {
  methods: {
    handleChange(value, column) {
      console.log('Value changed:', value)
      console.log('Column:', column)
    }
  }
}
</script>
```

### Example: Column Change Event

```javascript
column: [
  {
    label: 'Select',
    prop: 'select',
    type: 'select',
    change: (value) => {
      console.log('Select changed:', value)
    }
  }
]
```

### Key Points

- Handle form submit
- Handle form reset
- Listen to value changes
- Handle column-specific events
- Use event parameters
