# Search | 搜索

**官方文档**: https://avuejs.com/crud/crud-doc.html


## Instructions

This example demonstrates search functionality in Avue CRUD.

### Key Concepts

- Search configuration
- Column search
- Search events
- Search filters

### Example: Basic Search

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
    @search-change="handleSearch"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      option: {
        border: true,
        searchBtn: true,
        searchMenuSpan: 6,
        column: [
          {
            label: 'Name',
            prop: 'name',
            search: true,
            searchPlaceholder: 'Enter name'
          },
          {
            label: 'Email',
            prop: 'email',
            search: true
          }
        ]
      }
    }
  },
  methods: {
    handleSearch(params, done) {
      console.log('Search params:', params)
      // Filter data based on search params
      this.filterData(params)
      done()
    },
    filterData(params) {
      // Filter logic
    }
  }
}
</script>
```

### Example: Search with Different Types

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
    @search-change="handleSearch"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      option: {
        border: true,
        searchBtn: true,
        column: [
          {
            label: 'Name',
            prop: 'name',
            search: true,
            searchType: 'input'
          },
          {
            label: 'Status',
            prop: 'status',
            search: true,
            searchType: 'select',
            dicData: [
              { label: 'Active', value: '1' },
              { label: 'Inactive', value: '0' }
            ]
          },
          {
            label: 'Date',
            prop: 'date',
            search: true,
            searchType: 'date'
          }
        ]
      }
    }
  },
  methods: {
    handleSearch(params, done) {
      console.log('Search:', params)
      done()
    }
  }
}
</script>
```

### Key Points

- Use search: true in column for searchable fields
- Use searchBtn: true to show search button
- Use searchMenuSpan for search form layout
- Handle @search-change event
- Use searchType for different search input types
- Use searchPlaceholder for placeholder text
