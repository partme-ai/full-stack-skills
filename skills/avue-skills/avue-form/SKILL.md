---
name: avue-form
description: "Builds configuration-driven dynamic forms with Avue Form, including field types (input, select, date, upload), validation rules, form groups, tabbed layouts, and event handling. Use when the user needs to create forms with Avue in Vue applications, implement form validation, or build dynamic multi-step forms."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create configuration-driven forms with Avue Form
- Define form fields with types (input, select, date, checkbox, upload, etc.)
- Implement form validation rules
- Build dynamic forms, form groups, or tabbed form layouts
- Handle form submit, reset, and field change events

## How to use this skill

### Workflow

1. **Install** - `npm install @avue/form` and register with `Vue.use(Avue)`
2. **Define option** - Configure columns with labels, props, types, and rules
3. **Bind v-model** - Two-way bind the form data object
4. **Handle events** - Listen for @submit, @reset-change, and field-level events

### Quick-Start Example: Form with Validation

```vue
<template>
  <avue-form :option="option" v-model="form" @submit="handleSubmit" @reset-change="handleReset">
  </avue-form>
</template>

<script>
export default {
  data() {
    return {
      form: {},
      option: {
        submitText: 'Save',
        column: [
          {
            label: 'Name',
            prop: 'name',
            type: 'input',
            span: 12,
            rules: [{ required: true, message: 'Name is required', trigger: 'blur' }]
          },
          {
            label: 'Role',
            prop: 'role',
            type: 'select',
            span: 12,
            dicData: [
              { label: 'Admin', value: 'admin' },
              { label: 'User', value: 'user' }
            ]
          },
          {
            label: 'Start Date',
            prop: 'startDate',
            type: 'date',
            format: 'yyyy-MM-dd'
          }
        ]
      }
    }
  },
  methods: {
    handleSubmit(form, done) {
      console.log('Form data:', form)
      // Call API, then done() to re-enable button
      done()
    },
    handleReset() {
      console.log('Form reset')
    }
  }
}
</script>
```

### Feature Reference

| Feature | File |
|---------|------|
| Dynamic form | `examples/features/dynamic-form.md` |
| Form layout | `examples/features/form-layout.md` |
| Validation rules | `examples/features/form-rules.md` |
| Form groups | `examples/features/form-group.md` |
| Tabbed forms | `examples/features/form-tabs.md` |
| Custom components | `examples/features/custom-components.md` |

### API Reference

- `api/form-api.md` - Component props, events, and slots
- `api/columns-api.md` - Column types and properties
- `api/options-api.md` - Form option configuration

## Best Practices

1. **Use column types** - Set `type: 'select'`, `type: 'date'`, `type: 'upload'` for automatic controls
2. **Call done() after submit** - Always call `done()` in the submit handler to re-enable the button
3. **Use span for layout** - Set `span: 12` for half-width fields (24 = full width grid)
4. **Group related fields** - Use `group` option to organize complex forms into sections
5. **Validate on blur** - Set `trigger: 'blur'` for a less intrusive validation experience

## Resources

- **Official Docs**: https://avuejs.com/form/form-doc.html

## Keywords

Avue Form, avue-form, Vue form, dynamic form, 表单组件, 表单验证, form validation, form configuration, form columns, form rules
