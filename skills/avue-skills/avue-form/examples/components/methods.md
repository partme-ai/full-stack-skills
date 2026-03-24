# Form Methods

**官方文档**: https://avuejs.com/form/form-doc.html


## Instructions

This example demonstrates form methods in Avue-form.

### Key Concepts

- Method types
- Method usage
- Method parameters
- Method return values

### Example: Validate Method

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

### Example: ValidateField Method

```vue
<template>
  <avue-form 
    ref="form"
    :option="option" 
    v-model="form"
  ></avue-form>
  <el-button @click="validateField">Validate Field</el-button>
</template>

<script>
export default {
  methods: {
    validateField() {
      this.$refs.form.validateField('name', (errorMessage) => {
        if (errorMessage) {
          console.log('Validation error:', errorMessage)
        } else {
          console.log('Validation passed')
        }
      })
    }
  }
}
</script>
```

### Example: ResetFields Method

```vue
<template>
  <avue-form 
    ref="form"
    :option="option" 
    v-model="form"
  ></avue-form>
  <el-button @click="resetFields">Reset</el-button>
</template>

<script>
export default {
  methods: {
    resetFields() {
      this.$refs.form.resetFields()
    }
  }
}
</script>
```

### Example: ClearValidate Method

```vue
<template>
  <avue-form 
    ref="form"
    :option="option" 
    v-model="form"
  ></avue-form>
  <el-button @click="clearValidate">Clear Validate</el-button>
</template>

<script>
export default {
  methods: {
    clearValidate() {
      this.$refs.form.clearValidate()
    }
  }
}
</script>
```

### Key Points

- Use validate method
- Validate specific field
- Reset form fields
- Clear validation
- Access form via ref
