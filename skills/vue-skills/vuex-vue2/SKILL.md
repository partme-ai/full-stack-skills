---
name: vuex-vue2
description: Provides comprehensive guidance for Vuex 2.x state management in Vue 2 applications including state, mutations, actions, getters, modules, and plugins. Use when the user asks about Vuex for Vue 2, needs to manage state in Vue 2 applications, or implement Vuex patterns.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Install and set up Vuex in a Vue 2 project
- Manage application state with Vuex
- Use Vuex store in Vue components
- Understand Vuex core concepts (state, getters, mutations, actions)
- Use Vuex modules for large applications
- Handle Vuex plugins and devtools
- Understand Vuex API and methods
- Troubleshoot Vuex issues

## How to use this skill

This skill is organized to match the Vuex official documentation structure (https://vuex.vuejs.org/zh/, https://vuex.vuejs.org/zh/guide/, https://vuex.vuejs.org/zh/api/). When working with Vuex:

1. **Identify the topic** from the user's request:
   - Installation/安装 → `examples/guide/installation.md`
   - Quick Start/快速开始 → `examples/guide/quick-start.md`
   - Core Concepts/核心概念 → `examples/core-concepts/`
   - Advanced/高级 → `examples/advanced/`
   - API/API 文档 → `api/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Guide (使用指南)**:
   - `examples/guide/intro.md` - Introduction to Vuex
   - `examples/guide/installation.md` - Installation guide
   - `examples/guide/quick-start.md` - Quick start guide
   - `examples/guide/what-is-vuex.md` - What is Vuex

   **Core Concepts (核心概念)**:
   - `examples/core-concepts/state.md` - State
   - `examples/core-concepts/getters.md` - Getters
   - `examples/core-concepts/mutations.md` - Mutations
   - `examples/core-concepts/actions.md` - Actions
   - `examples/core-concepts/modules.md` - Modules

   **Advanced (高级)**:
   - `examples/advanced/plugins.md` - Plugins
   - `examples/advanced/strict-mode.md` - Strict mode
   - `examples/advanced/form-handling.md` - Form handling
   - `examples/advanced/testing.md` - Testing
   - `examples/advanced/hot-reload.md` - Hot reload

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Vuex is for Vue 2.x
   - Store is the central state management
   - State is reactive
   - Mutations are synchronous
   - Actions are asynchronous
   - Each example file includes key concepts, code examples, and key points

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/store-api.md` - Store API
   - `api/state-api.md` - State API
   - `api/getters-api.md` - Getters API
   - `api/mutations-api.md` - Mutations API
   - `api/actions-api.md` - Actions API
   - `api/modules-api.md` - Modules API
   - `api/plugins-api.md` - Plugins API

5. **Use templates** from the `templates/` directory:
   - `templates/installation.md` - Installation templates
   - `templates/store-setup.md` - Store setup templates
   - `templates/component-usage.md` - Component usage templates

### 1. Understanding Vuex

Vuex is a state management pattern and library for Vue.js applications. It serves as a centralized store for all the components in an application.

**Key Concepts**:
- **Store**: Centralized state container
- **State**: Application state (data)
- **Getters**: Computed properties for store
- **Mutations**: Synchronous state changes
- **Actions**: Asynchronous operations
- **Modules**: Store organization

### 2. Installation

**Using npm**:

```bash
npm install vuex@3
```

**Using yarn**:

```bash
yarn add vuex@3
```

**Using CDN**:

```html
<script src="https://unpkg.com/vuex@3"></script>
```

### 3. Basic Setup

```javascript
// store/index.js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++
    }
  }
})

export default store
```

```javascript
// main.js
import Vue from 'vue'
import store from './store'

new Vue({
  store,
  render: h => h(App)
}).$mount('#app')
```


### Doc mapping (one-to-one with official documentation)

- `examples/guide/` or `examples/getting-started/` → https://vuex.vuejs.org/zh/guide/
- `api/` → https://vuex.vuejs.org/zh/api/

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

Detailed API documentation is available in the `api/` directory, organized to match the official Vuex API documentation structure (https://vuex.vuejs.org/zh/api/):

### Store API (`api/store-api.md`)
- Store constructor options
- Store instance properties
- Store instance methods

### State API (`api/state-api.md`)
- State definition
- State access
- State reactivity

### Getters API (`api/getters-api.md`)
- Getter definition
- Getter access
- Getter arguments

### Mutations API (`api/mutations-api.md`)
- Mutation definition
- Mutation commit
- Mutation payload

### Actions API (`api/actions-api.md`)
- Action definition
- Action dispatch
- Action context

### Modules API (`api/modules-api.md`)
- Module definition
- Module namespacing
- Module registration

### Plugins API (`api/plugins-api.md`)
- Plugin definition
- Plugin usage
- Built-in plugins

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use mutations for synchronous changes**: Mutations must be synchronous
2. **Use actions for async operations**: Actions can contain async operations
3. **Keep state normalized**: Avoid nested state structures
4. **Use modules for large apps**: Organize store with modules
5. **Use getters for computed state**: Derive state with getters
6. **Follow naming conventions**: Use consistent naming patterns
7. **Use TypeScript**: Leverage TypeScript for type safety

## Resources

- **Official Documentation**: https://vuex.vuejs.org/zh/
- **Guide**: https://vuex.vuejs.org/zh/guide/
- **API Documentation**: https://vuex.vuejs.org/zh/api/
- **GitHub Repository**: https://github.com/vuejs/vuex

## Keywords

Vuex, vuex, Vue 2, state management, 状态管理, store, state, getters, mutations, actions, modules, 存储, 状态, 获取器, 变更, 动作, 模块, Vuex store, Vuex state, Vuex getters, Vuex mutations, Vuex actions, Vuex modules, Vuex plugins, centralized state, reactive state, synchronous mutations, asynchronous actions
