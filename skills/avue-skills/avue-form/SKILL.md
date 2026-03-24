---
name: avue-form
description: Provides comprehensive guidance for Avue Form component including form configuration, validation, and dynamic forms. Use when the user asks about Avue Form, needs to create dynamic forms, implement form validation, or work with form configurations.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Install and set up Avue-form in a Vue project
- Use Avue-form components in Vue applications
- Configure form options and columns
- Handle form validation
- Use form events and methods
- Customize form components
- Understand Avue-form API and methods
- Troubleshoot Avue-form issues

## How to use this skill

This skill is organized to match the Avue-form official documentation structure (https://avuejs.com/form/form-doc.html). When working with Avue-form:

1. **Identify the topic** from the user's request:
   - Installation/安装 → `examples/components/installation.md`
   - Basic Usage/基础用法 → `examples/components/basic-usage.md`
   - Configuration/配置 → `examples/components/configuration.md`
   - Features/功能特性 → `examples/features/`
   - API/API 文档 → `api/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Components (组件)**:
   - `examples/components/intro.md` - Introduction to Avue-form
   - `examples/components/installation.md` - Installation guide
   - `examples/components/basic-usage.md` - Basic usage
   - `examples/components/configuration.md` - Configuration
   - `examples/components/options.md` - Form options
   - `examples/components/columns.md` - Form columns
   - `examples/components/validation.md` - Form validation
   - `examples/components/events.md` - Form events
   - `examples/components/methods.md` - Form methods

   **Features (功能特性)**:
   - `examples/features/dynamic-form.md` - Dynamic form
   - `examples/features/form-layout.md` - Form layout
   - `examples/features/form-rules.md` - Form rules
   - `examples/features/form-submit.md` - Form submit
   - `examples/features/form-reset.md` - Form reset
   - `examples/features/custom-components.md` - Custom components
   - `examples/features/form-group.md` - Form group
   - `examples/features/form-tabs.md` - Form tabs

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Avue-form is based on Vue
   - Components use Vue syntax
   - Examples include both Options API and Composition API
   - Each example file includes key concepts, code examples, and key points

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/form-api.md` - Form component API
   - `api/options-api.md` - Options API
   - `api/columns-api.md` - Columns API
   - `api/events-api.md` - Events API
   - `api/methods-api.md` - Methods API

5. **Use templates** from the `templates/` directory:
   - `templates/installation.md` - Installation templates
   - `templates/basic-form.md` - Basic form templates
   - `templates/configuration.md` - Configuration templates

### 1. Understanding Avue-form

Avue-form is a Vue form component library that provides rich form controls and configuration options.

**Key Concepts**:
- **Form Component**: Main form component
- **Options**: Form configuration options
- **Columns**: Form field definitions
- **Validation**: Form validation rules
- **Events**: Form events
- **Methods**: Form methods

### 2. Installation

**Using npm**:

```bash
npm install @avue/form
```

**Using yarn**:

```bash
yarn add @avue/form
```

**Using pnpm**:

```bash
pnpm add @avue/form
```

### 3. Basic Setup

```javascript
// main.js
import Vue from 'vue'
import Avue from '@avue/form'
import '@avue/form/lib/theme-default/index.css'

Vue.use(Avue)
```

```vue
<template>
  <avue-form :option="option" v-model="form"></avue-form>
</template>

<script>
export default {
  data() {
    return {
      form: {},
      option: {
        column: [
          {
            label: 'Name',
            prop: 'name',
            type: 'input'
          }
        ]
      }
    }
  }
}
</script>
```


### Doc mapping (one-to-one with official documentation)

- `examples/` → https://avuejs.com/form/form-doc.html

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

Detailed API documentation is available in the `api/` directory, organized to match the official Avue-form API documentation structure:

### Form Component API (`api/form-api.md`)
- Form component props
- Form component events
- Form component slots

### Options API (`api/options-api.md`)
- Form options configuration
- Option properties
- Option methods

### Columns API (`api/columns-api.md`)
- Column definitions
- Column properties
- Column types

### Events API (`api/events-api.md`)
- Form events
- Event handlers
- Event parameters

### Methods API (`api/methods-api.md`)
- Form methods
- Method parameters
- Method return values

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Configure options properly**: Set up form options correctly
2. **Define columns clearly**: Define form columns with proper types
3. **Handle validation**: Use validation rules appropriately
4. **Handle events**: Use form events for interactions
5. **Use methods**: Leverage form methods for operations
6. **Customize components**: Customize components when needed
7. **Follow Vue patterns**: Follow Vue.js best practices

## Resources

- **Official Documentation**: https://avuejs.com/form/form-doc.html
- **GitHub Repository**: https://github.com/avue/avue

## Keywords

Avue-form, avue-form, @avue/form, Vue form, form component, 表单组件, 表单配置, 表单验证, 表单事件, 表单方法, form options, form columns, form validation, form events, form methods, dynamic form, form layout, form rules, form submit, form reset, custom components, form group, form tabs
