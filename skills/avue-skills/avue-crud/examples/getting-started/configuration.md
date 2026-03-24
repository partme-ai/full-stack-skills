# Configuration | 配置

**官方文档**: https://avuejs.com/crud/crud-doc.html


## Instructions

This example demonstrates Avue CRUD configuration options.

### Key Concepts

- Option configuration
- Table options
- Form options
- Button options
- Display options

### Example: Basic Configuration

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
        // Table display options
        border: true,           // Show border
        index: true,            // Show index
        indexLabel: '序号',     // Index label
        stripe: true,           // Stripe style
        menuAlign: 'center',    // Menu alignment
        align: 'center',        // Column alignment
        
        // Button options
        addBtn: true,           // Show add button
        editBtn: true,          // Show edit button
        delBtn: true,           // Show delete button
        searchBtn: true,        // Show search button
        refreshBtn: true,       // Show refresh button
        columnBtn: true,        // Show column button
        
        // Form options
        dialogType: 'drawer',   // Dialog type: drawer or dialog
        dialogWidth: '50%',     // Dialog width
        dialogHeight: '50%',    // Dialog height
        formOption: {
          labelWidth: 100,
          labelPosition: 'right'
        },
        
        // Column configuration
        column: [
          {
            label: 'Name',
            prop: 'name'
          }
        ]
      }
    }
  }
}
</script>
```

### Example: Advanced Configuration

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
        // Display
        border: true,
        index: true,
        stripe: true,
        size: 'medium',
        height: 'auto',
        
        // Buttons
        addBtn: true,
        editBtn: true,
        delBtn: true,
        viewBtn: true,
        searchBtn: true,
        refreshBtn: true,
        columnBtn: true,
        excelBtn: true,
        printBtn: true,
        
        // Pagination
        page: true,
        pageSize: 10,
        pageSizes: [10, 20, 50, 100],
        
        // Search
        searchMenuSpan: 6,
        searchSize: 'medium',
        searchIcon: true,
        
        // Form
        dialogType: 'dialog',
        dialogWidth: '60%',
        dialogHeight: '70%',
        formOption: {
          labelWidth: 120,
          labelPosition: 'right',
          size: 'medium'
        },
        
        column: [
          {
            label: 'Name',
            prop: 'name',
            search: true,
            searchPlaceholder: 'Enter name'
          }
        ]
      }
    }
  },
  methods: {
    handleLoad(page) {
      console.log('Load page:', page)
    }
  }
}
</script>
```

### Key Points

- Configure via option object
- Use border, index, stripe for table display
- Use addBtn, editBtn, delBtn for CRUD buttons
- Use dialogType for form display type
- Use formOption for form configuration
- Use page options for pagination
- Use search options for search functionality
