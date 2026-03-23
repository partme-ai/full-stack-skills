# Form Configuration | 表单配置

**官方文档**: https://avuejs.com/crud/crud-doc.html


## Instructions

This example demonstrates form configuration in Avue CRUD dialogs.

### Key Concepts

- Form options
- Form layout
- Form validation
- Form events

### Example: Basic Form Config

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
        border: true,
        addBtn: true,
        editBtn: true,
        formOption: {
          labelWidth: 120,
          labelPosition: 'right',
          size: 'medium'
        },
        column: [
          {
            label: 'Name',
            prop: 'name',
            span: 12
          },
          {
            label: 'Email',
            prop: 'email',
            span: 12
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Advanced Form Config

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
        border: true,
        addBtn: true,
        editBtn: true,
        dialogType: 'drawer',
        dialogWidth: '50%',
        formOption: {
          labelWidth: 100,
          labelPosition: 'top',
          size: 'small',
          menuBtn: true,
          submitBtn: true,
          emptyBtn: true
        },
        column: [
          {
            label: 'Name',
            prop: 'name',
            span: 24,
            rules: [{ required: true }]
          },
          {
            label: 'Description',
            prop: 'description',
            type: 'textarea',
            span: 24,
            minRows: 3,
            maxRows: 6
          }
        ]
      }
    }
  }
}
</script>
```

### Key Points

- Use formOption for form configuration
- Configure labelWidth and labelPosition
- Use span for column layout
- Use dialogType for drawer or dialog
- Configure form size and buttons
- Form validation uses column rules
