# Form Template | 表单模板

## Basic Form Template

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
        labelWidth: 100,
        labelPosition: 'right',
        column: [
          {
            label: 'Field Name',
            prop: 'field',
            type: 'input',
            rules: [{ required: true, message: 'Please enter field' }]
          }
        ]
      }
    }
  },
  methods: {
    handleSubmit(form, done) {
      console.log('Form data:', form)
      // Submit logic here
      done()
    }
  }
}
</script>
```

## Form with Multiple Fields

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
            label: 'Text',
            prop: 'text',
            type: 'input'
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
