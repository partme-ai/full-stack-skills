# Column Types | 列类型

**官方文档**: https://avuejs.com/crud/crud-doc.html


## Instructions

This example demonstrates different column types in Avue CRUD.

### Key Concepts

- Various column types
- Type-specific configuration
- Type-specific properties
- Custom renderers

### Example: Common Column Types

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
            label: 'Number',
            prop: 'number',
            type: 'number'
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
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Upload Column

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
            label: 'File Upload',
            prop: 'file',
            type: 'upload',
            action: '/api/upload',
            propsHttp: {
              res: 'data',
              url: 'url'
            },
            listType: 'picture-card',
            limit: 5
          }
        ]
      }
    }
  }
}
</script>
```

### Key Points

- Use type prop for different column types
- Each type has specific configuration options
- Use dicData for select/checkbox/radio options
- Use action for upload type
- Configure type-specific properties
- Types determine form input and display
