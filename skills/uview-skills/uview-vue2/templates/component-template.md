# Component Template | 组件模板

## Basic Component Usage

```vue
<template>
  <u-component-name
    prop1="value1"
    prop2="value2"
    @event="handleEvent"
  />
</template>

<script>
export default {
  methods: {
    handleEvent() {
      console.log('Event handled')
    }
  }
}
</script>
```

## Component with v-model

```vue
<template>
  <u-input
    v-model="value"
    placeholder="Enter text"
  />
</template>

<script>
export default {
  data() {
    return {
      value: ''
    }
  }
}
</script>
```

## Component in Form

```vue
<template>
  <u-form :model="form" :rules="rules" ref="form">
    <u-form-item label="Field" prop="field">
      <u-input v-model="form.field" />
    </u-form-item>
    <u-button type="primary" @click="submit">Submit</u-button>
  </u-form>
</template>

<script>
export default {
  data() {
    return {
      form: {
        field: ''
      },
      rules: {
        field: [
          { required: true, message: 'Please enter field', trigger: 'blur' }
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
