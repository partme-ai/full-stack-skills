# Basic CRUD Template | 基础 CRUD 模板

## Basic CRUD Template

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
        indexLabel: '序号',
        stripe: true,
        menuAlign: 'center',
        align: 'center',
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
    }
  }
}
</script>
```
