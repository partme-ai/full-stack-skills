---
name: vitest
description: Provides comprehensive guidance for Vitest testing framework including fast test execution, Vite integration, component testing, mocking, and configuration. Use when the user asks about Vitest, needs to write fast unit tests, test Vue/React components, or configure Vitest with Vite projects.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Set up Vitest in a Vite project
- Write unit tests and component tests
- Configure Vitest for different environments
- Use Vitest API and utilities
- Test Vue, React, or Svelte components
- Use browser mode for testing
- Set up visual regression testing
- Mock functions and modules
- Use snapshots for testing
- Configure test coverage
- Use Vitest UI
- Optimize test performance
- Debug tests
- Understand Vitest best practices
- Troubleshoot Vitest issues

## How to use this skill

This skill is organized to match the Vitest official documentation structure (https://vitest.dev/guide/, https://vitest.dev/api/, https://vitest.dev/config/). When working with Vitest:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started.md`
   - Features/功能特性 → `examples/features.md`
   - Component testing/组件测试 → `examples/component-testing.md`
   - Browser mode/浏览器模式 → `examples/browser-mode.md`
   - API/API 文档 → `api/`
   - Configuration/配置 → `examples/config/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始)**:
   - `examples/getting-started.md` - Installation and first test

   **Features (功能特性)**:
   - `examples/features.md` - Key features and capabilities
   - `examples/ui.md` - Vitest UI
   - `examples/component-testing.md` - Component testing
   - `examples/browser-mode.md` - Browser mode testing
   - `examples/visual-regression-testing.md` - Visual regression testing
   - `examples/trace-view.md` - Trace view

   **Testing (测试)**:
   - `examples/test-api.md` - Test API (test, it, describe, etc.)
   - `examples/mocking.md` - Mocking functions and modules
   - `examples/snapshots.md` - Snapshot testing
   - `examples/coverage.md` - Code coverage

   **Configuration (配置)**:
   - `examples/config/basic-config.md` - Basic configuration
   - `examples/config/environment.md` - Environment configuration
   - `examples/config/browser-config.md` - Browser mode configuration

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Vitest is designed for Vite projects
   - Supports TypeScript, JSX, ESM out of the box
   - Fast watch mode with HMR-like experience
   - Compatible with Jest API
   - Examples include both JavaScript and TypeScript versions
   - Each example file includes key concepts, code examples, and key points

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/test-api.md` - Test API reference
   - `api/vi-utility.md` - vi utility functions
   - `api/expect.md` - Expect assertions
   - `api/mocking.md` - Mocking API

5. **Use templates** from the `templates/` directory:
   - `templates/vitest-config.md` - Vitest configuration templates
   - `templates/test-examples.md` - Test example templates

### Doc mapping (one-to-one with https://vitest.dev/guide/, https://vitest.dev/api/, https://vitest.dev/config/)

**Guide (指南)**:
- `examples/getting-started.md` → https://vitest.dev/guide/getting-started.html
- `examples/features.md` → https://vitest.dev/guide/features.html
- `examples/ui.md` → https://vitest.dev/guide/ui.html
- `examples/component-testing.md` → https://vitest.dev/guide/testing-components.html
- `examples/browser-mode.md` → https://vitest.dev/guide/browser.html
- `examples/visual-regression-testing.md` → https://vitest.dev/guide/visual-regression.html
- `examples/trace-view.md` → https://vitest.dev/guide/trace-view.html
- `examples/mocking.md` → https://vitest.dev/guide/mocking.html
- `examples/snapshots.md` → https://vitest.dev/guide/snapshot.html
- `examples/coverage.md` → https://vitest.dev/guide/coverage.html

**Configuration (配置)**:
- `examples/config/basic-config.md` → https://vitest.dev/config/
- `examples/config/environment.md` → https://vitest.dev/config/#environment
- `examples/config/browser-config.md` → https://vitest.dev/config/#browser

**API Reference**:
- `api/test-api.md` → https://vitest.dev/api/
- `api/vi-utility.md` → https://vitest.dev/api/vi.html
- `api/expect.md` → https://vitest.dev/api/expect.html
- `api/mocking.md` → https://vitest.dev/api/vi.html

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

## Best Practices

1. **Use watch mode**: Leverage Vitest's smart watch mode for faster feedback
2. **Organize tests**: Group related tests with describe blocks
3. **Use TypeScript**: Take advantage of native TypeScript support
4. **Mock effectively**: Use vi.mock() for module mocking
5. **Test components**: Use component testing for Vue/React components
6. **Use UI mode**: Use `--ui` flag for better test debugging experience
7. **Optimize performance**: Use test.only() during development

## Resources

- **Official Documentation**: https://vitest.dev/
- **Getting Started**: https://vitest.dev/guide/
- **API Reference**: https://vitest.dev/api/
- **Configuration**: https://vitest.dev/config/
- **GitHub Repository**: https://github.com/vitest-dev/vitest

## Keywords

Vitest, vitest, test framework, unit testing, component testing, Vite, Jest compatible, watch mode, HMR, TypeScript, ESM, mocking, snapshots, coverage, browser mode, visual regression testing, 测试框架, 单元测试, 组件测试, 监视模式, 热模块替换, 模拟, 快照, 覆盖率, 浏览器模式, 视觉回归测试
