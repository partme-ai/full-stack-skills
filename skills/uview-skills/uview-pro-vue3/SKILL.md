---
name: uview-pro-vue3
description: "Builds Vue 3 mobile UIs in uni-app using the uView Pro component library (100+ components). Covers Button, Form, List, Modal, Tabs, NavBar, plus built-in HTTP, storage, router, and validator utilities. Use when the user needs to create uni-app interfaces with uView Pro, configure themes, or use uView Pro utility tools."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build Vue 3 / uni-app mobile interfaces with uView Pro components
- Use form, data display, feedback, or navigation components
- Configure uView Pro theme, internationalization, or global settings
- Use built-in tools (HTTP requests, storage, routing, validation, formatting)
- Set up uView Pro in a new uni-app project

## How to use this skill

### Workflow

1. **Install** - `npm install uview-pro` and register in main.js
2. **Choose component** - Match the UI need to component from reference below
3. **Load example file** - Each component has a detailed example in `examples/components/`
4. **Use tools** - Leverage built-in utilities from `examples/tools/`

### Quick-Start: Installation and Basic Usage

```javascript
// main.js
import { createSSRApp } from 'vue'
import uView from 'uview-pro'
import App from './App.vue'

export function createApp() {
  const app = createSSRApp(App)
  app.use(uView)
  return { app }
}
```

### Example: Form with Validation

```vue
<template>
  <u-form :model="form" :rules="rules" ref="formRef">
    <u-form-item label="Username" prop="name">
      <u-input v-model="form.name" placeholder="Enter username" />
    </u-form-item>
    <u-form-item label="Email" prop="email">
      <u-input v-model="form.email" placeholder="Enter email" />
    </u-form-item>
    <u-button type="primary" @click="submit">Submit</u-button>
  </u-form>
</template>

<script setup>
import { ref, reactive } from 'vue'

const formRef = ref(null)
const form = reactive({ name: '', email: '' })
const rules = {
  name: [{ required: true, message: 'Name is required' }],
  email: [{ required: true, message: 'Email is required' }, { type: 'email', message: 'Invalid email' }]
}

const submit = () => {
  formRef.value.validate(valid => {
    if (valid) uni.showToast({ title: 'Success!' })
  })
}
</script>
```

### Component Categories

| Category | Components | Example Files |
|----------|-----------|---------------|
| Form | Button, Input, Form, Select, Switch, Checkbox, Radio, Upload | `examples/components/form.md` |
| Display | List, Card, Avatar, Badge, Tag, Empty | `examples/components/list.md` |
| Feedback | Toast, Modal, Loading, Popup, Drawer | `examples/components/modal.md` |
| Navigation | Tabs, NavBar, Pagination, Dropdown | `examples/components/tabs.md` |

### Tools Reference

| Tool | File | Purpose |
|------|------|---------|
| HTTP | `examples/tools/http.md` | Request wrapper with interceptors |
| Storage | `examples/tools/storage.md` | Local storage utilities |
| Router | `examples/tools/router.md` | Navigation helpers |
| Validator | `examples/tools/validator.md` | Form validation |

### API Reference

- `api/component-api.md` - Component props, events, methods, and slots
- `api/tools-api.md` - Utility function signatures and parameters
- `api/config-api.md` - Global and theme configuration

## Best Practices

1. **On-demand import** - Import only used components to reduce bundle size
2. **Composition API** - Prefer `<script setup>` for cleaner Vue 3 code
3. **Theme variables** - Customize via uView theme config rather than overriding CSS
4. **Use built-in tools** - Leverage HTTP, storage, and router utilities instead of adding extra dependencies
5. **Test on device** - Verify uni-app behavior on actual mobile devices, not just H5

## Resources

- **Official Docs**: https://uviewpro.cn/

## Keywords

uView Pro, uview-pro, Vue 3, uni-app, component library, 组件库, Button, Form, List, Modal, Tabs, NavBar, mobile UI, 表单, 列表
