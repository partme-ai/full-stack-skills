# Table Template | 表格模板

## Basic Table Template

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
        index: true,
        indexLabel: '序号',
        stripe: true,
        menuAlign: 'center',
        align: 'center',
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

## Table with CRUD

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
