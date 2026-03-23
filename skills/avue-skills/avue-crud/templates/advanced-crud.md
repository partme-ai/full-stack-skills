# Advanced CRUD Template | 高级 CRUD 模板

## Advanced CRUD Template with All Features

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
    @search-change="handleSearch"
    @excel="handleExport"
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
        size: 'medium',
        menuAlign: 'center',
        align: 'center',
        addBtn: true,
        editBtn: true,
        delBtn: true,
        viewBtn: true,
        searchBtn: true,
        refreshBtn: true,
        columnBtn: true,
        excelBtn: true,
        printBtn: true,
        page: true,
        pageSize: 10,
        pageSizes: [10, 20, 50, 100],
        searchMenuSpan: 6,
        dialogType: 'dialog',
        dialogWidth: '60%',
        formOption: {
          labelWidth: 120,
          labelPosition: 'right'
        },
        column: [
          {
            label: 'Name',
            prop: 'name',
            search: true,
            sortable: true,
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
            search: true,
            searchType: 'select',
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
      this.data.push({ ...row, id: Date.now() })
      this.$message.success('Saved successfully')
      done()
    },
    handleUpdate(row, index, done) {
      this.$set(this.data, index, row)
      this.$message.success('Updated successfully')
      done()
    },
    handleDelete(row, index) {
      this.$confirm('Are you sure to delete?', 'Confirm', {
        type: 'warning'
      }).then(() => {
        this.data.splice(index, 1)
        this.$message.success('Deleted successfully')
      })
    },
    handleLoad(page) {
      console.log('Load page:', page)
      // Load data
    },
    handleSearch(params, done) {
      console.log('Search:', params)
      done()
    },
    handleExport() {
      this.$avue.$export.excel({
        title: 'Export',
        columns: this.option.column,
        data: this.data
      })
    }
  }
}
</script>
```
