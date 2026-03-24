# CRUD Operations | CRUD 操作

**官方文档**: https://avuejs.com/crud/crud-doc.html


## Instructions

This example demonstrates CRUD operations in Avue CRUD.

### Key Concepts

- Create operation
- Read operation
- Update operation
- Delete operation
- Operation events

### Example: Complete CRUD

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
      // Create new record
      console.log('Save:', row)
      // API call
      this.data.push({ ...row, id: Date.now() })
      this.$message.success('Created successfully')
      done()
    },
    handleUpdate(row, index, done) {
      // Update existing record
      console.log('Update:', row, index)
      // API call
      this.$set(this.data, index, row)
      this.$message.success('Updated successfully')
      done()
    },
    handleDelete(row, index) {
      // Delete record
      console.log('Delete:', row, index)
      this.$confirm('Are you sure to delete?', 'Confirm', {
        type: 'warning'
      }).then(() => {
        // API call
        this.data.splice(index, 1)
        this.$message.success('Deleted successfully')
      }).catch(() => {
        // Cancel
      })
    }
  }
}
</script>
```

### Example: CRUD with API

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
            rules: [{ required: true }]
          }
        ]
      }
    }
  },
  methods: {
    async handleSave(row, done) {
      try {
        const res = await this.$http.post('/api/users', row)
        this.data.push(res.data)
        this.$message.success('Created successfully')
        done()
      } catch (error) {
        this.$message.error('Create failed')
        done(false)
      }
    },
    async handleUpdate(row, index, done) {
      try {
        const res = await this.$http.put(`/api/users/${row.id}`, row)
        this.$set(this.data, index, res.data)
        this.$message.success('Updated successfully')
        done()
      } catch (error) {
        this.$message.error('Update failed')
        done(false)
      }
    },
    async handleDelete(row, index) {
      try {
        await this.$http.delete(`/api/users/${row.id}`)
        this.data.splice(index, 1)
        this.$message.success('Deleted successfully')
      } catch (error) {
        this.$message.error('Delete failed')
      }
    },
    async handleLoad(page) {
      try {
        const res = await this.$http.get('/api/users', {
          params: {
            page: page.currentPage,
            size: page.pageSize
          }
        })
        this.data = res.data.records
        this.page.total = res.data.total
      } catch (error) {
        this.$message.error('Load failed')
      }
    }
  }
}
</script>
```

### Key Points

- Enable addBtn, editBtn, delBtn for CRUD buttons
- Handle @row-save for create operation
- Handle @row-update for update operation
- Handle @row-del for delete operation
- Use done() callback to close dialog
- Use done(false) to prevent closing on error
- Show success/error messages
- Integrate with backend APIs
