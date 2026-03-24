# Columns | 列配置

**官方文档**: https://avuejs.com/crud/crud-doc.html


## Instructions

This example demonstrates how to configure columns in Avue CRUD.

### Key Concepts

- Column definition
- Column types
- Column properties
- Column validation
- Column display

### Example: Basic Columns

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
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
          },
          {
            label: 'Age',
            prop: 'age',
            type: 'number'
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Column Types

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
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
            label: 'DateTime',
            prop: 'datetime',
            type: 'datetime'
          },
          {
            label: 'Switch',
            prop: 'switch',
            type: 'switch'
          },
          {
            label: 'Checkbox',
            prop: 'checkbox',
            type: 'checkbox',
            dicData: [
              { label: 'Option 1', value: '1' },
              { label: 'Option 2', value: '2' }
            ]
          },
          {
            label: 'Radio',
            prop: 'radio',
            type: 'radio',
            dicData: [
              { label: 'Option 1', value: '1' },
              { label: 'Option 2', value: '2' }
            ]
          },
          {
            label: 'Upload',
            prop: 'upload',
            type: 'upload',
            action: '/api/upload'
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Column with Validation

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      option: {
        column: [
          {
            label: 'Email',
            prop: 'email',
            type: 'input',
            rules: [
              { required: true, message: 'Please enter email' },
              { type: 'email', message: 'Invalid email format' }
            ]
          },
          {
            label: 'Age',
            prop: 'age',
            type: 'number',
            rules: [
              { required: true, message: 'Please enter age' },
              { type: 'number', min: 18, max: 100, message: 'Age must be between 18 and 100' }
            ]
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Column Display Options

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      option: {
        column: [
          {
            label: 'Name',
            prop: 'name',
            width: 200,
            minWidth: 100,
            fixed: 'left',
            align: 'center',
            headerAlign: 'center',
            sortable: true,
            search: true,
            searchPlaceholder: 'Enter name',
            hide: false,
            disabled: false,
            readonly: false
          }
        ]
      }
    }
  }
}
</script>
```

### Key Points

- Define columns in option.column array
- Use type prop for different input types
- Use rules for validation
- Use width, minWidth for column width
- Use fixed for fixed columns
- Use sortable for sorting
- Use search for searchable columns
- Use hide, disabled, readonly for column state
