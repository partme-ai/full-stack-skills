# CRUD Template | CRUD 模板

## Complete CRUD Template

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
        indexLabel: '序号',
        stripe: true,
        menuAlign: 'center',
        align: 'center',
        addBtn: true,
        editBtn: true,
        delBtn: true,
        searchBtn: true,
        refreshBtn: true,
        column: [
          {
            label: 'Name',
            prop: 'name',
            search: true,
            rules: [{ required: true, message: 'Please enter name' }]
          },
          {
            label: 'Email',
            prop: 'email',
            search: true,
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
      // API call to create
      this.data.push({ ...row, id: Date.now() })
      this.$message.success('Created successfully')
      done()
    },
    handleUpdate(row, index, done) {
      // API call to update
      this.$set(this.data, index, row)
      this.$message.success('Updated successfully')
      done()
    },
    handleDelete(row, index) {
      this.$confirm('Are you sure to delete?', 'Confirm', {
        type: 'warning'
      }).then(() => {
        // API call to delete
        this.data.splice(index, 1)
        this.$message.success('Deleted successfully')
      })
    },
    handleLoad(page) {
      // API call to load data
      console.log('Load page:', page)
    }
  }
}
</script>
```
