---
name: vue-router-v4
description: Provides comprehensive guidance for Vue Router v4 including route configuration, navigation, nested routes, route guards, and Vue 3 integration. Use when the user asks about Vue Router v4, needs to set up routing for Vue 3 applications, implement navigation guards, or work with Vue Router v4 features.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Set up routing in a Vue 3 application
- Configure routes, nested routes, and named routes
- Implement navigation guards (global, per-route, in-component)
- Use programmatic navigation with `router.push()`, `router.replace()`, etc.
- Handle dynamic route matching and route parameters
- Work with route meta fields and route records
- Implement lazy loading and code splitting for routes
- Use Vue Router with Composition API (`useRouter`, `useRoute`)
- Configure different history modes (hash, HTML5 history, memory)
- Handle scroll behavior and transitions
- Implement typed routes with TypeScript
- Migrate from Vue Router 3 to Vue Router 4
- Extend RouterLink component
- Handle navigation failures and errors
- Work with dynamic routing (adding/removing routes at runtime)

## How to use this skill

This skill is organized to match the Vue Router official documentation structure (https://router.vuejs.org/guide/, https://router.vuejs.org/api/). When working with Vue Router:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/essentials/getting-started.md`
   - Dynamic route matching/动态路由匹配 → `examples/essentials/dynamic-route-matching.md`
   - Routes matching syntax/路由匹配语法 → `examples/essentials/routes-matching-syntax.md`
   - Named routes/命名路由 → `examples/essentials/named-routes.md`
   - Nested routes/嵌套路由 → `examples/essentials/nested-routes.md`
   - Programmatic navigation/编程式导航 → `examples/essentials/programmatic-navigation.md`
   - Named views/命名视图 → `examples/essentials/named-views.md`
   - Redirect and alias/重定向和别名 → `examples/essentials/redirect-alias.md`
   - Passing props to route components/向路由组件传递 props → `examples/essentials/passing-props.md`
   - Different history modes/不同的历史模式 → `examples/essentials/different-history-modes.md`
   - Navigation guards/导航守卫 → `examples/advanced/navigation-guards.md`
   - Route meta fields/路由元信息 → `examples/advanced/route-meta-fields.md`
   - Data fetching/数据获取 → `examples/advanced/data-fetching.md`
   - Composition API/组合式 API → `examples/advanced/composition-api.md`
   - RouterView slot/RouterView 插槽 → `examples/advanced/routerview-slot.md`
   - Transitions/过渡效果 → `examples/advanced/transitions.md`
   - Scroll behavior/滚动行为 → `examples/advanced/scroll-behavior.md`
   - Lazy loading routes/懒加载路由 → `examples/advanced/lazy-loading-routes.md`
   - Typed routes/类型化路由 → `examples/advanced/typed-routes.md`
   - Extending RouterLink/扩展 RouterLink → `examples/advanced/extending-router-link.md`
   - Navigation failures/导航失败 → `examples/advanced/navigation-failures.md`
   - Dynamic routing/动态路由 → `examples/advanced/dynamic-routing.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Essentials (基础) - `examples/essentials/`**:
   - `examples/essentials/getting-started.md` - Creating a router and basic setup
   - `examples/essentials/dynamic-route-matching.md` - Dynamic route matching with params
   - `examples/essentials/routes-matching-syntax.md` - Route matching syntax and patterns
   - `examples/essentials/named-routes.md` - Named routes and navigation
   - `examples/essentials/nested-routes.md` - Nested routes and RouterView
   - `examples/essentials/programmatic-navigation.md` - Programmatic navigation with router methods
   - `examples/essentials/named-views.md` - Named views and multiple RouterView
   - `examples/essentials/redirect-alias.md` - Redirects and aliases
   - `examples/essentials/passing-props.md` - Passing props to route components
   - `examples/essentials/different-history-modes.md` - Hash, HTML5 history, and memory modes

   **Advanced (高级) - `examples/advanced/`**:
   - `examples/advanced/navigation-guards.md` - Global, per-route, and in-component guards
   - `examples/advanced/route-meta-fields.md` - Route meta fields and custom data
   - `examples/advanced/data-fetching.md` - Data fetching strategies
   - `examples/advanced/composition-api.md` - Using `useRouter()` and `useRoute()` with Composition API
   - `examples/advanced/routerview-slot.md` - RouterView slot props
   - `examples/advanced/transitions.md` - Route transitions and animations
   - `examples/advanced/scroll-behavior.md` - Scroll behavior configuration
   - `examples/advanced/lazy-loading-routes.md` - Lazy loading routes and code splitting
   - `examples/advanced/typed-routes.md` - TypeScript typed routes
   - `examples/advanced/extending-router-link.md` - Extending RouterLink component
   - `examples/advanced/navigation-failures.md` - Handling navigation failures
   - `examples/advanced/dynamic-routing.md` - Adding and removing routes dynamically

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow Vue Router 4 API
   - Examples include both JavaScript and TypeScript versions where applicable
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/router.md` - Router instance API (`createRouter`, `addRoute`, `removeRoute`, etc.)
   - `api/route-records.md` - Route record types and properties
   - `api/useRouter-useRoute.md` - Composition API functions (`useRouter`, `useRoute`)
   - `api/navigation-helpers.md` - Navigation helper functions
   - `api/router-link-router-view-components.md` - RouterLink and RouterView components
   - `api/history-modes-api.md` - History mode APIs
   - `api/error-and-failure-types.md` - Error and failure types

5. **Use templates** from the `templates/` directory:
   - `templates/router-setup.md` - Router setup templates
   - `templates/route-config.md` - Route configuration templates

## Examples and Templates

This skill includes detailed examples organized to match the Vue Router official documentation structure (https://router.vuejs.org/guide/, https://router.vuejs.org/api/). All examples are in the `examples/` directory, organized by topic:

### Essentials (基础) - `examples/essentials/`

- `examples/essentials/getting-started.md` - Creating a router, installing Vue Router, and basic setup
- `examples/essentials/dynamic-route-matching.md` - Dynamic route matching with params and query
- `examples/essentials/routes-matching-syntax.md` - Route matching syntax, catch-all routes, and regex
- `examples/essentials/named-routes.md` - Named routes and navigation with names
- `examples/essentials/nested-routes.md` - Nested routes and nested RouterView
- `examples/essentials/programmatic-navigation.md` - Programmatic navigation with `router.push()`, `router.replace()`, `router.go()`
- `examples/essentials/named-views.md` - Named views and multiple RouterView components
- `examples/essentials/redirect-alias.md` - Redirects and aliases configuration
- `examples/essentials/passing-props.md` - Passing props to route components
- `examples/essentials/different-history-modes.md` - Hash mode, HTML5 history mode, and memory mode

### Advanced (高级) - `examples/advanced/`

- `examples/advanced/navigation-guards.md` - Global guards, per-route guards, and in-component guards
- `examples/advanced/route-meta-fields.md` - Route meta fields and accessing meta in guards
- `examples/advanced/data-fetching.md` - Data fetching strategies (before navigation, after navigation)
- `examples/advanced/composition-api.md` - Using `useRouter()` and `useRoute()` with Composition API
- `examples/advanced/routerview-slot.md` - RouterView slot props and custom rendering
- `examples/advanced/transitions.md` - Route transitions and animations
- `examples/advanced/scroll-behavior.md` - Scroll behavior configuration
- `examples/advanced/lazy-loading-routes.md` - Lazy loading routes and code splitting
- `examples/advanced/typed-routes.md` - TypeScript typed routes and type safety
- `examples/advanced/extending-router-link.md` - Extending RouterLink component
- `examples/advanced/navigation-failures.md` - Handling navigation failures and errors
- `examples/advanced/dynamic-routing.md` - Adding and removing routes dynamically at runtime

### Templates Directory (`templates/`)

- `templates/router-setup.md` - Router setup templates for different scenarios
- `templates/route-config.md` - Route configuration templates

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the corresponding directory
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference `templates/router-setup.md` for router setup templates
- Use `templates/route-config.md` for route configuration templates
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Vue Router API documentation structure:

### Router API (`api/router.md`)
- `createRouter()` - Creating a router instance
- Router instance methods: `addRoute()`, `removeRoute()`, `hasRoute()`, `getRoutes()`, `push()`, `replace()`, `go()`, `back()`, `forward()`
- Router instance properties: `currentRoute`, `options`

### Route Records API (`api/route-records.md`)
- Route record types and properties
- Route configuration options

### Composition API (`api/useRouter-useRoute.md`)
- `useRouter()` - Access router instance in setup
- `useRoute()` - Access current route in setup

### Navigation Helpers (`api/navigation-helpers.md`)
- Navigation helper functions and utilities

### Components API (`api/router-link-router-view-components.md`)
- `RouterLink` component props and usage
- `RouterView` component props and usage

### History Modes API (`api/history-modes-api.md`)
- `createWebHistory()` - HTML5 history mode
- `createWebHashHistory()` - Hash mode
- `createMemoryHistory()` - Memory mode

### Error and Failure Types (`api/error-and-failure-types.md`)
- Navigation failure types
- Error handling

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use named routes**: Use named routes for better maintainability and refactoring
2. **Lazy load routes**: Use dynamic imports for route components to enable code splitting
3. **Type safety**: Use TypeScript with typed routes for better type safety
4. **Navigation guards**: Use navigation guards appropriately (global, per-route, in-component)
5. **Route meta**: Use route meta fields for custom data and permissions
6. **History mode**: Choose the appropriate history mode based on deployment environment
7. **Scroll behavior**: Configure scroll behavior for better UX
8. **Error handling**: Handle navigation failures gracefully

## Resources

- **Official Guide**: https://router.vuejs.org/guide/
- **API Reference**: https://router.vuejs.org/api/
- **Migration Guide**: https://router.vuejs.org/guide/migration/
- **GitHub Repository**: https://github.com/vuejs/router

## Keywords

Vue Router, router, routing, navigation, route, routes, nested routes, named routes, dynamic routes, route params, route query, navigation guards, route meta, programmatic navigation, RouterLink, RouterView, useRouter, useRoute, history mode, hash mode, HTML5 history, lazy loading, code splitting, typed routes, TypeScript, 路由, 导航, 路由守卫, 嵌套路由, 命名路由, 动态路由, 编程式导航, 懒加载, 类型化路由
