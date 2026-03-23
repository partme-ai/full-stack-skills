# Pagination | 分页

**官方文档**: https://avuejs.com/crud/crud-doc.html


## Instructions

This example demonstrates pagination configuration in Avue CRUD.

### Key Concepts

- Pagination setup
- Page configuration
- Load data on page change
- Page events

### Example: Basic Pagination

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
        border: true,
        page: true,
        pageSize: 10,
        pageSizes: [10, 20, 50, 100],
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
    handleLoad(page) {
      console.log('Load page:', page)
      // Load data based on page
      this.loadData(page)
    },
    loadData(page) {
      // Simulate API call
      const start = (page.currentPage - 1) * page.pageSize
      const end = start + page.pageSize
      // Update data and total
      this.page.total = 100 // Total records
    }
  }
}
</script>
```

### Example: Pagination with API

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
        border: true,
        page: true,
        pageSize: 10,
        pageSizes: [10, 20, 50, 100],
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
        this.page.currentPage = res.data.current
      } catch (error) {
        this.$message.error('Load failed')
      }
    }
  }
}
</script>
```

### Key Points

- Use page prop for pagination object
- Set page: true in option
- Configure pageSize and pageSizes
- Handle @on-load event for page changes
- Update data and total on load
- Integrate with backend pagination API
