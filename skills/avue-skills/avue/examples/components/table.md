# Table | 表格

**官方文档**: https://avuejs.com/


## Instructions

This example demonstrates how to use Avue table (avue-crud) component.

### Key Concepts

- Table configuration
- Column definition
- CRUD operations
- Table events
- Pagination and search

### Example: Basic Table

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
      data: [
        { name: 'John', email: 'john@example.com' },
        { name: 'Jane', email: 'jane@example.com' }
      ],
      option: {
        border: true,
        index: true,
        column: [
          {
            label: 'Name',
            prop: 'name'
          },
          {
            label: 'Email',
            prop: 'email'
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Table with CRUD

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
    @row-save="handleSave"
    @row-update="handleUpdate"
    @row-del="handleDelete"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      option: {
        border: true,
        index: true,
        addBtn: true,
        editBtn: true,
        delBtn: true,
        column: [
          {
            label: 'Name',
            prop: 'name',
            rules: [{ required: true, message: 'Please enter name' }]
          },
          {
            label: 'Email',
            prop: 'email',
            rules: [
              { required: true, message: 'Please enter email' },
              { type: 'email', message: 'Invalid email' }
            ]
          }
        ]
      }
    }
  },
  methods: {
    handleSave(row, done) {
      this.data.push(row)
      done()
    },
    handleUpdate(row, index, done) {
      this.$set(this.data, index, row)
      done()
    },
    handleDelete(row, index) {
      this.data.splice(index, 1)
    }
  }
}
</script>
```

### Example: Table with Pagination

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
    :page="page"
    @on-load="handleLoad"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      page: {
        pageSize: 10,
        currentPage: 1,
        total: 0
      },
      option: {
        border: true,
        index: true,
        column: [
          {
            label: 'Name',
            prop: 'name'
          },
          {
            label: 'Email',
            prop: 'email'
          }
        ]
      }
    }
  },
  methods: {
    handleLoad(page) {
      // Load data based on page
      console.log('Load page:', page)
    }
  }
}
</script>
```

### Key Points

- Use avue-crud for tables with CRUD
- Configure via option.column array
- Use addBtn, editBtn, delBtn for CRUD buttons
- Handle @row-save, @row-update, @row-del events
- Use @on-load for pagination
- Data-driven configuration
