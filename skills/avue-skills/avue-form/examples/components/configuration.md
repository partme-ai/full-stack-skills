# Configuration

**官方文档**: https://avuejs.com/form/form-doc.html


## Instructions

This example demonstrates how to configure Avue-form.

### Key Concepts

- Options configuration
- Column configuration
- Form layout
- Button configuration

### Example: Options Configuration

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
        labelWidth: 120,
        labelPosition: 'right',
        size: 'medium',
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
  }
}
</script>
```

### Example: Column Configuration

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
            span: 12,
            disabled: false,
            display: true,
            rules: [
              { required: true, message: 'Please input name' }
            ]
          },
          {
            label: 'Email',
            prop: 'email',
            type: 'input',
            span: 12
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Form Layout

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
        gutter: 20,
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
          }
        ]
      }
    }
  }
}
</script>
```

### Key Points

- Configure form options
- Set column properties
- Control form layout
- Configure buttons
- Set validation rules
