# Export | 导出

**官方文档**: https://avuejs.com/crud/crud-doc.html


## Instructions

This example demonstrates data export functionality in Avue CRUD.

### Key Concepts

- Export configuration
- Excel export
- Export events
- Custom export

### Example: Basic Export

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
    @excel="handleExport"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      option: {
        border: true,
        excelBtn: true,
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
    handleExport() {
      // Export data to Excel
      this.$avue.$export.excel({
        title: 'User List',
        columns: this.option.column,
        data: this.data
      })
    }
  }
}
</script>
```

### Example: Export with Custom Columns

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
    @excel="handleExport"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      option: {
        border: true,
        excelBtn: true,
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
    handleExport() {
      const exportColumns = [
        { label: 'Name', prop: 'name' },
        { label: 'Email', prop: 'email' }
      ]
      
      this.$avue.$export.excel({
        title: 'User Export',
        columns: exportColumns,
        data: this.data
      })
    }
  }
}
</script>
```

### Key Points

- Use excelBtn: true to show export button
- Handle @excel event for export
- Use $avue.$export.excel() for Excel export
- Configure export columns
- Export current data or filtered data
