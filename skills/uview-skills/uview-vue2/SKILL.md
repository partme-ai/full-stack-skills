---
name: uview-vue2
description: "Builds Vue 2 mobile UIs in uni-app using the uView UI component library with Button, Input, Form, Table, Modal, Tabs, and built-in $u tools (toast, http, storage, route). Use when the user needs to create uni-app interfaces with uView UI for Vue 2, customize themes via SCSS variables, or use $u utility methods."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build uni-app mobile applications with uView UI Vue 2 components
- Use uView components (Button, Input, Form, Table, Modal, Tabs, etc.)
- Use $u utility tools ($u.toast, $u.http, $u.storage, $u.route)
- Customize the uView UI theme via SCSS variables
- Set up uView UI in a Vue 2 uni-app project

## How to use this skill

### Workflow

1. **Install** - Install uView UI plugin and register with `Vue.use()` in main.js
2. **Configure easycom** - Set up easycom in pages.json for auto component registration
3. **Choose component** - Match the UI need to component from reference below
4. **Load example file** - Each component has detailed examples in `examples/components/`

### Quick-Start: Setup and Basic Usage

```javascript
// main.js
import Vue from 'vue'
import uView from 'uview-ui'
Vue.use(uView)
```

```vue
<!-- pages.json - add easycom config -->
{
  "easycom": {
    "^u-(.*)": "uview-ui/components/u-$1/u-$1.vue"
  }
}
```

### Example: Form with $u Tools

```vue
<template>
  <view>
    <u-form :model="form" :rules="rules" ref="uForm">
      <u-form-item label="Name" prop="name">
        <u-input v-model="form.name" placeholder="Enter name" />
      </u-form-item>
      <u-form-item label="Phone" prop="phone">
        <u-input v-model="form.phone" type="number" placeholder="Enter phone" />
      </u-form-item>
    </u-form>
    <u-button type="primary" @click="submit">Submit</u-button>
  </view>
</template>

<script>
export default {
  data() {
    return {
      form: { name: '', phone: '' },
      rules: {
        name: [{ required: true, message: 'Name is required', trigger: 'blur' }],
        phone: [{ required: true, message: 'Phone is required', trigger: 'blur' }]
      }
    }
  },
  methods: {
    submit() {
      this.$refs.uForm.validate(valid => {
        if (valid) this.$u.toast('Success!')
      })
    }
  }
}
</script>
```

### Component Categories

| Category | Components | Example Files |
|----------|-----------|---------------|
| Form | Button, Input, Form, Picker, Tabs | `examples/components/form.md`, `button.md` |
| Display | List, Card, Badge, Grid, Swiper, Table | `examples/components/list.md`, `table.md` |
| Feedback | Modal, Toast, Loading | `examples/components/modal.md` |
| Navigation | Navbar, Tabs | `examples/components/navbar.md` |

### $u Tools Reference

| Tool | Usage | Example File |
|------|-------|-------------|
| Toast | `this.$u.toast('message')` | `examples/tools/toast.md` |
| HTTP | `this.$u.http.get(url)` | `examples/tools/http.md` |
| Storage | `this.$u.storage.set(key, val)` | `examples/tools/storage.md` |
| Route | `this.$u.route('/pages/home')` | `examples/tools/route.md` |
| Debounce | `this.$u.debounce(fn, 300)` | `examples/tools/debounce.md` |

### API Reference

- `api/components.md` - Component props, events, and slots
- `api/tools.md` - $u utility method signatures
- `api/theme-variables.md` - SCSS theme variables

## Best Practices

1. **Use easycom** - Configure easycom in pages.json for automatic component registration
2. **SCSS theme variables** - Override uView SCSS variables for custom branding, not inline styles
3. **Use rpx units** - Ensure responsive layouts across screen sizes in uni-app
4. **Leverage $u tools** - Use built-in HTTP, storage, and route helpers instead of extra libraries
5. **Test cross-platform** - Verify on H5, WeChat mini-program, and native App

## Resources

- **Official Docs**: https://www.uviewui.com/
- **GitHub**: https://github.com/umicro/uView

## Keywords

uView UI, uView, Vue 2, uni-app, $u, component library, 组件库, Button, Form, Table, Modal, Toast, 按钮, 表单, 表格, 模态框, mobile UI
