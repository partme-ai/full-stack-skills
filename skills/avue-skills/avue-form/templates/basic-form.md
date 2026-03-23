# Basic Form Templates

## Simple Form

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
          }
        ]
      }
    }
  }
}
</script>
```

## Form with Submit

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
      console.log('Form:', form)
      done()
    }
  }
}
</script>
```

## Form with Multiple Fields

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
            span: 12
          },
          {
            label: 'Email',
            prop: 'email',
            type: 'input',
            span: 12
          },
          {
            label: 'Select',
            prop: 'select',
            type: 'select',
            dicData: [
              { label: 'Option 1', value: '1' },
              { label: 'Option 2', value: '2' }
            ]
          }
        ]
      }
    }
  }
}
</script>
```
