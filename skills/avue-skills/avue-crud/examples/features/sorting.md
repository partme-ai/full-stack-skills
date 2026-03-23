# Sorting | 排序

**官方文档**: https://avuejs.com/crud/crud-doc.html


## Instructions

This example demonstrates sorting functionality in Avue CRUD.

### Key Concepts

- Column sorting
- Sort configuration
- Sort events
- Custom sorting

### Example: Basic Sorting

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
        column: [
          {
            label: 'Name',
            prop: 'name',
            sortable: true
          },
          {
            label: 'Email',
            prop: 'email',
            sortable: true
          },
          {
            label: 'Age',
            prop: 'age',
            type: 'number',
            sortable: true
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Custom Sorting

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
    @sort-change="handleSortChange"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      option: {
        border: true,
        column: [
          {
            label: 'Name',
            prop: 'name',
            sortable: true,
            sortMethod: (a, b) => {
              return a.name.localeCompare(b.name)
            }
          }
        ]
      }
    }
  },
  methods: {
    handleSortChange({ column, prop, order }) {
      console.log('Sort:', column, prop, order)
      // Custom sort logic
    }
  }
}
</script>
```

### Key Points

- Use sortable: true for sortable columns
- Sorting works automatically for basic types
- Use sortMethod for custom sorting logic
- Handle @sort-change for sort events
- Sort order: ascending/descending/null
