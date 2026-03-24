# Introduction

**官方文档**: https://avuejs.com/form/form-doc.html


## Instructions

This example provides an introduction to Avue-form.

### Key Concepts

- What is Avue-form
- Basic usage
- Core concepts
- Features

### Example: What is Avue-form

Avue-form is a Vue form component library that provides rich form controls and configuration options, making form development easier and more efficient.

### Example: Basic Usage

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

### Example: Core Concepts

- **Form Component**: `avue-form` is the main component
- **Options**: Form configuration object
- **Columns**: Form field definitions array
- **v-model**: Two-way data binding
- **Validation**: Built-in validation support

### Key Points

- Based on Vue
- Rich form controls
- Flexible configuration
- Built-in validation
- Easy to use
