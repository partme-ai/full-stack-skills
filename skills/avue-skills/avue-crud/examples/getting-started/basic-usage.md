# Basic Usage | 基本用法

**官方文档**: https://avuejs.com/crud/crud-doc.html


## Instructions

This example demonstrates basic Avue CRUD usage.

### Key Concepts

- Basic CRUD setup
- Column configuration
- Data binding
- CRUD operations

### Example: Basic CRUD

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
      data: [
        { id: 1, name: 'John', email: 'john@example.com' },
        { id: 2, name: 'Jane', email: 'jane@example.com' }
      ],
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
      console.log('Save:', row)
      this.data.push({ ...row, id: Date.now() })
      this.$message.success('Saved successfully')
      done()
    },
    handleUpdate(row, index, done) {
      console.log('Update:', row, index)
      this.$set(this.data, index, row)
      this.$message.success('Updated successfully')
      done()
    },
    handleDelete(row, index) {
      console.log('Delete:', row, index)
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

### Example: CRUD with Form Types

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
            label: 'Text',
            prop: 'text',
            type: 'input'
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
            label: 'Switch',
            prop: 'switch',
            type: 'switch'
          }
        ]
      }
    }
  },
  methods: {
    handleSave(row, done) {
      this.data.push({ ...row, id: Date.now() })
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

### Key Points

- Use avue-crud component
- Configure via option object
- Define columns in option.column array
- Use addBtn, editBtn, delBtn for CRUD buttons
- Handle @row-save, @row-update, @row-del events
- Use type prop for different input types
- Use rules for validation
