---
name: avue-crud
description: "Builds configuration-driven CRUD tables with the Avue framework, including column definition, pagination, search, sorting, row operations (add/edit/delete), data export, and form validation. Use when the user needs to create data management interfaces with Avue CRUD tables in Vue 2 applications."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build CRUD tables with Avue (create, read, update, delete)
- Configure table columns, pagination, search, and sorting
- Handle row events (@row-save, @row-update, @row-del)
- Export table data or implement batch operations
- Add form validation inside CRUD table dialogs

## How to use this skill

### Workflow

1. **Define the option object** - Configure columns, table behavior, and form rules
2. **Bind data and page** - Connect data array and pagination to the component
3. **Handle events** - Implement save, update, and delete event handlers
4. **Load detailed examples** - Each feature has a file in `examples/`

### Quick-Start Example: CRUD Table with Pagination

```vue
<template>
  <avue-crud
    :option="option"
    :data="data"
    :page.sync="page"
    @row-save="handleSave"
    @row-update="handleUpdate"
    @row-del="handleDel"
    @on-load="loadData"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [],
      page: { currentPage: 1, pageSize: 10, total: 0 },
      option: {
        border: true,
        index: true,
        selection: true,
        column: [
          { label: 'Name', prop: 'name', search: true, rules: [{ required: true, message: 'Name is required' }] },
          { label: 'Email', prop: 'email', search: true },
          { label: 'Status', prop: 'status', type: 'select', dicData: [
            { label: 'Active', value: 1 }, { label: 'Inactive', value: 0 }
          ]}
        ]
      }
    }
  },
  methods: {
    loadData() {
      // Fetch data from API using this.page.currentPage and this.page.pageSize
    },
    handleSave(row, done) { /* POST to API, then call done() */ done() },
    handleUpdate(row, index, done) { /* PUT to API, then call done() */ done() },
    handleDel(row, index) { /* DELETE from API, then remove from this.data */ }
  }
}
</script>
```

### Feature Reference

| Feature | File |
|---------|------|
| Column config | `examples/features/columns.md` |
| CRUD operations | `examples/features/crud-operations.md` |
| Pagination | `examples/features/pagination.md` |
| Search | `examples/features/search.md` |
| Export | `examples/features/export.md` |
| Form validation | `examples/advanced/validation.md` |

### API Reference

- `api/crud-api.md` - Component props, events, methods
- `api/column-api.md` - Column types, renderers, formatters
- `api/option-api.md` - Table, form, and button options

## Best Practices

1. **Configuration-driven** - Define all table behavior in the `option` object, not in template markup
2. **Call done() in event handlers** - Always call `done()` after save/update to close the dialog
3. **Use column types** - Set `type: 'select'`, `type: 'date'`, etc. for automatic form controls
4. **Paginate server-side** - Use `@on-load` with page params for large datasets
5. **Add search columns** - Set `search: true` on columns to enable the search bar

## Resources

- **Official Docs**: https://avuejs.com/crud/crud-doc.html

## Keywords

Avue CRUD, avue-crud, table, CRUD, 增删改查, pagination, search, column, form, 表格, 分页, data management
