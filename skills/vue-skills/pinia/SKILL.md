---
name: pinia
description: Provides comprehensive guidance for Pinia state management including stores, state, getters, actions, plugins, and TypeScript support. Use when the user asks about Pinia, needs to manage application state, create stores, implement state persistence, or migrate from Vuex.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Set up Pinia state management in Vue 3 applications
- Create stores with defineStore()
- Work with state, getters, and actions
- Use Pinia with Composition API
- Use Pinia with Options API
- Implement SSR (Server-Side Rendering) with Pinia
- Create and use Pinia plugins
- Access stores in components
- Share state between components
- Persist state with plugins
- Test Pinia stores
- Migrate from Vuex to Pinia

## How to use this skill

This skill is organized to match the Pinia official documentation structure (https://pinia.vuejs.org/introduction.html, https://pinia.vuejs.org/core-concepts/, https://pinia.vuejs.org/api/). When working with Pinia:

1. **Identify the topic** from the user's request:
   - Introduction/介绍 → `examples/introduction/`
   - Core Concepts/核心概念 → `examples/core-concepts/`
   - Cookbook/食谱 → `examples/cookbook/`
   - SSR/服务端渲染 → `examples/ssr/`
   - API Reference/API 参考 → `api/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Introduction (介绍)** - `examples/introduction/`:
   - `examples/introduction/introduction.md`

   **Core Concepts (核心概念)** - `examples/core-concepts/`:
   - `examples/core-concepts/actions.md`
   - `examples/core-concepts/defining-a-store.md`
   - `examples/core-concepts/getters.md`
   - `examples/core-concepts/index.md`
   - `examples/core-concepts/outside-component-usage.md`
   - `examples/core-concepts/plugins.md`
   - `examples/core-concepts/state.md`

   **Cookbook (食谱)** - `examples/cookbook/`:
   - `examples/cookbook/composables.md`
   - `examples/cookbook/composing-stores.md`
   - `examples/cookbook/hot-module-replacement.md`
   - `examples/cookbook/index.md`
   - `examples/cookbook/migration-v1-v2.md`
   - `examples/cookbook/migration-v2-v3.md`
   - `examples/cookbook/migration-vuex.md`
   - `examples/cookbook/options-api.md`
   - `examples/cookbook/testing.md`
   - `examples/cookbook/vscode-snippets.md`

   **SSR (服务端渲染)** - `examples/ssr/`:
   - `examples/ssr/index.md`
   - `examples/ssr/nuxt.md`

3. **Reference API documentation** in the `api/` directory when needed:

   **Pinia Core API** - `api/pinia/`:
   - `api/pinia/enumerations/MutationType.md`
   - `api/pinia/functions/acceptHMRUpdate.md`
   - `api/pinia/functions/createPinia.md`
   - `api/pinia/functions/defineStore.md`
   - `api/pinia/functions/disposePinia.md`
   - `api/pinia/functions/getActivePinia.md`
   - `api/pinia/functions/mapActions.md`
   - `api/pinia/functions/mapState.md`
   - `api/pinia/functions/mapStores.md`
   - `api/pinia/functions/mapWritableState.md`
   - `api/pinia/functions/setMapStoreSuffix.md`
   - `api/pinia/index.md`
   - `api/pinia/interfaces/Store.md`
   - `api/pinia/interfaces/StoreActions.md`
   - `api/pinia/interfaces/StoreDefinition.md`
   - `api/pinia/interfaces/StoreGetters.md`
   - `api/pinia/interfaces/StoreProperties.md`
   - `api/pinia/interfaces/StoreState.md`

   **@pinia/nuxt** - `api/@pinia/nuxt/`:
   - `api/@pinia/nuxt/index.md`
   - `api/@pinia/nuxt/interfaces/ModuleOptions.md`
   - `api/@pinia/nuxt/variables/default.md`

   **@pinia/testing** - `api/@pinia/testing/`:
   - `api/@pinia/testing/functions/createTestingPinia.md`
   - `api/@pinia/testing/index.md`
   - `api/@pinia/testing/interfaces/TestingOptions.md`
   - `api/@pinia/testing/interfaces/TestingPinia.md`

4. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow Pinia best practices
   - Examples include both JavaScript and TypeScript versions where applicable
   - Each example file includes parameters, returns, common errors, best practices, and scenarios
   - Always check the example file for best practices and common patterns

5. **Reference the official documentation** when needed:
   - Introduction: https://pinia.vuejs.org/introduction.html
   - Core Concepts: https://pinia.vuejs.org/core-concepts/
   - API Reference: https://pinia.vuejs.org/api/

## Best Practices

1. **Use defineStore()**: Always use defineStore() to create stores
2. **Store naming**: Use descriptive store IDs
3. **State structure**: Keep state flat and normalized when possible
4. **Getters**: Use getters for computed values derived from state
5. **Actions**: Use actions for async operations and mutations
6. **TypeScript**: Use TypeScript for type safety
7. **Store composition**: Split large stores into smaller, focused stores
8. **SSR**: Use proper SSR setup for server-side rendering
9. **Plugins**: Use plugins for cross-cutting concerns
10. **Testing**: Write tests for stores and actions

## Resources

- **Official Documentation**: https://pinia.vuejs.org/
- **Introduction**: https://pinia.vuejs.org/introduction.html
- **Core Concepts**: https://pinia.vuejs.org/core-concepts/
- **API Reference**: https://pinia.vuejs.org/api/
- **GitHub Repository**: https://github.com/vuejs/pinia

## Keywords

Pinia, state management, store, Vue 3, Composition API, Options API, defineStore, state, getters, actions, plugins, SSR, server-side rendering, TypeScript, Vuex migration, 状态管理, 存储, 组合式 API, 选项式 API, 插件, 服务端渲染, 类型支持
