---
name: avue-crud
description: Provides comprehensive guidance for Avue CRUD component including table operations, form handling, and data management. Use when the user asks about Avue CRUD, needs to implement table CRUD operations, or build data management interfaces.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build CRUD (Create, Read, Update, Delete) tables with Avue
- Configure Avue CRUD tables
- Implement data management interfaces
- Add pagination, search, and sorting to tables
- Customize table columns and operations
- Handle table events (save, update, delete)
- Export table data
- Implement table selection and batch operations
- Configure table forms for add/edit
- Use advanced CRUD features

## How to use this skill

This skill is organized to match the Avue CRUD official documentation structure (https://avuejs.com/crud/crud-doc.html). When working with Avue CRUD:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started/basic-usage.md` or `examples/getting-started/configuration.md`
   - Column configuration/列配置 → `examples/features/columns.md`
   - CRUD operations/CRUD 操作 → `examples/features/crud-operations.md`
   - Pagination/分页 → `examples/features/pagination.md`
   - Search/搜索 → `examples/features/search.md`
   - Export/导出 → `examples/features/export.md`
   - Advanced features/高级功能 → `examples/advanced/` directory

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始) - `examples/getting-started/`**:
   - `examples/getting-started/basic-usage.md` - Basic CRUD usage
   - `examples/getting-started/configuration.md` - CRUD configuration options

   **Features (功能特性) - `examples/features/`**:
   - `examples/features/columns.md` - Column configuration
   - `examples/features/crud-operations.md` - CRUD operations (add, edit, delete)
   - `examples/features/pagination.md` - Pagination configuration
   - `examples/features/search.md` - Search functionality
   - `examples/features/sorting.md` - Sorting configuration
   - `examples/features/selection.md` - Row selection
   - `examples/features/export.md` - Data export
   - `examples/features/form-config.md` - Form configuration in CRUD

   **Advanced (高级) - `examples/advanced/`**:
   - `examples/advanced/custom-operations.md` - Custom operations
   - `examples/advanced/column-types.md` - Different column types
   - `examples/advanced/validation.md` - Form validation in CRUD
   - `examples/advanced/events.md` - Event handling

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow Avue CRUD API
   - Examples use Vue 2.x syntax
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns
   - Avue CRUD is data-driven and configuration-based

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/crud-api.md` - CRUD component API reference
   - `api/column-api.md` - Column configuration API
   - `api/option-api.md` - Option configuration API

5. **Use templates** from the `templates/` directory:
   - `templates/basic-crud.md` - Basic CRUD template
   - `templates/advanced-crud.md` - Advanced CRUD template
   - `templates/crud-with-api.md` - CRUD with API integration


### Doc mapping (one-to-one with official documentation)

- `examples/` → https://avuejs.com/crud/crud-doc.html

## Examples and Templates

This skill includes detailed examples organized to match the official documentation structure. All examples are in the `examples/` directory (see mapping above).

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the mapping above
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference templates in `templates/` directory for common scaffolding
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Avue CRUD API documentation structure:

### CRUD API (`api/crud-api.md`)
- Component props and APIs
- Component events and methods
- Component configuration

### Column API (`api/column-api.md`)
- Column configuration options
- Column types and properties
- Column renderers and formatters

### Option API (`api/option-api.md`)
- Option configuration object
- Table options
- Form options
- Button options

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Configuration-driven**: Use option object for all configuration
2. **Column definition**: Define columns in option.column array
3. **Event handling**: Handle @row-save, @row-update, @row-del events
4. **Data management**: Manage data array and pagination object
5. **Validation**: Use rules in column configuration for validation
6. **Performance**: Optimize for large datasets with pagination
7. **User experience**: Provide loading states and error handling
8. **API integration**: Integrate with backend APIs properly
9. **Form configuration**: Configure forms in column definitions
10. **Customization**: Use slots and custom renderers when needed

## Resources

- **Official Website**: https://avuejs.com/
- **CRUD Documentation**: https://avuejs.com/crud/crud-doc.html
- **GitHub Repository**: https://github.com/avue/avue

## Keywords

Avue CRUD, avue-crud, table, CRUD, Create Read Update Delete, pagination, search, sort, export, column, form, validation, 表格, CRUD, 增删改查, 分页, 搜索, 排序, 导出, 列配置, 表单, 验证
