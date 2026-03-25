---
name: avue
description: "Builds data-driven admin interfaces with the Avue framework (based on Vue 2 + Element UI). Covers CRUD tables, forms, global APIs ($DialogForm, $Clipboard, $ImagePreview, $Export), Tree, Upload, and Select components. Use when the user needs to build management systems, data-driven views, or configuration-based admin UIs with Avue."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build admin management systems with Avue
- Use Avue data-driven tables, forms, and CRUD components
- Use global APIs ($DialogForm, $Clipboard, $ImagePreview, $Export, $Print)
- Configure Avue components (Tree, Upload, Select, Input)
- Set up internationalization or custom plugins

## How to use this skill

### Quick-Start Example: Avue Form with Global API

```vue
<template>
  <div>
    <avue-form :option="option" v-model="form" @submit="handleSubmit" />
    <el-button @click="openDialog">Open Dialog Form</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {},
      option: {
        column: [
          { label: 'Name', prop: 'name', type: 'input', rules: [{ required: true }] },
          { label: 'Category', prop: 'category', type: 'tree', dicUrl: '/api/categories' }
        ]
      }
    }
  },
  methods: {
    handleSubmit(form, done) { console.log(form); done() },
    openDialog() {
      this.$DialogForm.show({ option: this.option, callback: (form) => console.log(form) })
    }
  }
}
</script>
```

This skill is organized to match the Avue official documentation structure (https://avuejs.com/). When working with Avue:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started/installation.md` or `examples/getting-started/quick-start.md`
   - Form/表单 → `examples/forms/basic-form.md` or `examples/forms/form-config.md`
   - Table/表格 → `examples/components/table.md`
   - Tree/树形 → `examples/components/tree.md`
   - Upload/上传 → `examples/components/upload.md`
   - Global API/全局 API → `api/global-api.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始) - `examples/getting-started/`**:
   - `examples/getting-started/installation.md` - Installing Avue and basic setup
   - `examples/getting-started/quick-start.md` - Quick start tutorial
   - `examples/getting-started/global-config.md` - Global configuration

   **Forms (表单) - `examples/forms/`**:
   - `examples/forms/basic-form.md` - Basic form usage
   - `examples/forms/form-config.md` - Form configuration
   - `examples/forms/form-validation.md` - Form validation
   - `examples/forms/form-table.md` - Form with table selector

   **Components (组件) - `examples/components/`**:
   - `examples/components/table.md` - Table component
   - `examples/components/tree.md` - Tree component
   - `examples/components/upload.md` - Upload component
   - `examples/components/select.md` - Select component
   - `examples/components/input.md` - Input component

   **Advanced (高级) - `examples/advanced/`**:
   - `examples/advanced/crud.md` - CRUD operations
   - `examples/advanced/internationalization.md` - Internationalization
   - `examples/advanced/plugins.md` - Plugins and extensions

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow Avue API
   - Examples use Vue 2.x syntax
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns
   - Avue is based on Vue and Element UI

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/global-api.md` - Global API reference
   - `api/components.md` - Component API reference

5. **Use templates** from the `templates/` directory:
   - `templates/form-template.md` - Form template
   - `templates/table-template.md` - Table template
   - `templates/crud-template.md` - CRUD template


### Doc mapping (one-to-one with official documentation)

- See examples and API files → https://avuejs.com

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

Detailed API documentation is available in the `api/` directory, organized to match the official Avue API documentation structure:

### Global API (`api/global-api.md`)
- $DialogForm - Dialog form
- $Clipboard - Clipboard operations
- $ImagePreview - Image preview
- $Print - Print functionality
- $Export - Export functionality
- $Log - Logging
- findObject, findArray, findNode - Utility functions
- watermark - Watermark
- downFile - File download
- randomId - Random ID generation
- loadScript - Script loading
- deepClone - Deep clone
- setPx - Pixel conversion
- validatenull - Validation
- vaildData - Data validation

### Components API (`api/components.md`)
- Component props and APIs
- Component events and methods
- Component configuration

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Install Avue**: Install @smallwei/avue package
2. **Import styles**: Import Avue CSS styles
3. **Use Vue.use()**: Register Avue with Vue.use(Avue)
4. **Data-driven**: Use data-driven approach for forms and tables
5. **Configuration**: Configure forms and tables via option objects
6. **Global API**: Use Avue global APIs for common operations
7. **Internationalization**: Configure i18n for multi-language support
8. **Plugins**: Use Avue plugins for extended functionality
9. **Component composition**: Compose components for complex UIs
10. **Performance**: Optimize for performance with large datasets

## Resources

- **Official Website**: https://avuejs.com/
- **GitHub Repository**: https://github.com/avue/avue

## Keywords

Avue, Vue, Element UI, data-driven, form, table, CRUD, $DialogForm, $Clipboard, $ImagePreview, $Print, $Export, tree, upload, select, 数据驱动, 表单, 表格, CRUD, 树形, 上传, 选择器
