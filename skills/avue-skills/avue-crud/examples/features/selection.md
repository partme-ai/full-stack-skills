# Selection | 选择

**官方文档**: https://avuejs.com/crud/crud-doc.html


## Instructions

This example demonstrates row selection in Avue CRUD.

### Key Concepts

- Row selection
- Multiple selection
- Selection events
- Batch operations

### Example: Basic Selection

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
    @selection-change="handleSelectionChange"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      selectedRows: [],
      option: {
        border: true,
        selection: true,
        column: [
          {
            label: 'Name',
            prop: 'name'
          }
        ]
      }
    }
  },
  methods: {
    handleSelectionChange(selection) {
      this.selectedRows = selection
      console.log('Selected:', selection)
    }
  }
}
</script>
```

### Example: Batch Operations

```vue
<template>
  <div>
    <avue-crud
      :option="option"
      :data="data"
      @selection-change="handleSelectionChange"
    />
    <el-button
      v-if="selectedRows.length > 0"
      type="danger"
      @click="handleBatchDelete"
    >
      Batch Delete ({{ selectedRows.length }})
    </el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: [],
      selectedRows: [],
      option: {
        border: true,
        selection: true,
        column: [
          {
            label: 'Name',
            prop: 'name'
          }
        ]
      }
    }
  },
  methods: {
    handleSelectionChange(selection) {
      this.selectedRows = selection
    },
    handleBatchDelete() {
      this.$confirm(`Delete ${this.selectedRows.length} items?`, 'Confirm', {
        type: 'warning'
      }).then(() => {
        const ids = this.selectedRows.map(row => row.id)
        this.data = this.data.filter(row => !ids.includes(row.id))
        this.selectedRows = []
        this.$message.success('Deleted successfully')
      })
    }
  }
}
</script>
```

### Key Points

- Use selection: true for row selection
- Handle @selection-change for selection events
- Selection returns array of selected rows
- Use for batch operations
- Clear selection after operations
