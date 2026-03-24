# CRUD Operations | CRUD 操作

**官方文档**: https://avuejs.com/


## Instructions

This example demonstrates how to implement CRUD operations with Avue.

### Key Concepts

- Create operation
- Read operation
- Update operation
- Delete operation
- Data management

### Example: Complete CRUD

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
    :page="page"
    @row-save="handleSave"
    @row-update="handleUpdate"
    @row-del="handleDelete"
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
          },
          {
            label: 'Status',
            prop: 'status',
            type: 'select',
            dicData: [
              { label: 'Active', value: '1' },
              { label: 'Inactive', value: '0' }
            ]
          }
        ]
      }
    }
  },
  methods: {
    handleSave(row, done) {
      // Create new record
      this.data.push({ ...row, id: Date.now() })
      this.$message.success('Created successfully')
      done()
    },
    handleUpdate(row, index, done) {
      // Update existing record
      this.$set(this.data, index, row)
      this.$message.success('Updated successfully')
      done()
    },
    handleDelete(row, index) {
      // Delete record
      this.$confirm('Are you sure to delete?', 'Confirm', {
        type: 'warning'
      }).then(() => {
        this.data.splice(index, 1)
        this.$message.success('Deleted successfully')
      })
    },
    handleLoad(page) {
      // Load data with pagination
      console.log('Load page:', page)
      // Fetch data from API
    }
  }
}
</script>
```

### Key Points

- Use avue-crud for CRUD operations
- Enable addBtn, editBtn, delBtn for operations
- Handle @row-save, @row-update, @row-del events
- Use @on-load for pagination
- Implement data management logic
- Show success/error messages
