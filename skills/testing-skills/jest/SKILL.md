---
name: jest
description: Provides comprehensive guidance for Jest testing framework including test writing, matchers, async testing, mocking, snapshots, configuration, and CLI. Use when the user asks about Jest, needs to write JavaScript/TypeScript tests, mock dependencies, or configure Jest for projects.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write unit tests and integration tests with Jest
- Set up Jest in a project
- Use Jest matchers and assertions
- Test asynchronous code
- Mock functions, modules, and dependencies
- Create snapshot tests
- Configure Jest for different environments
- Use Jest with TypeScript, React, Vue, or other frameworks
- Run tests and generate coverage reports
- Use Jest CLI commands
- Set up test environments (jsdom, node)
- Use Jest with Vite (via vite-jest, though Vitest is recommended for new Vite projects)

## How to use this skill

This skill is organized to match the Jest official documentation structure (https://jestjs.io/docs/getting-started, https://jestjs.io/docs/api). When working with Jest:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started/installation.md` or `examples/getting-started/using-matchers.md`
   - Testing/测试 → `examples/testing/asynchronous.md` or `examples/testing/setup-teardown.md`
   - Mock functions/Mock 函数 → `examples/testing/mock-functions.md`
   - Mock modules/Mock 模块 → `examples/testing/manual-mocks.md`
   - Snapshots/快照 → `examples/testing/snapshot-testing.md`
   - Configuration/配置 → `examples/configuration/jest-config.md`
   - CLI/命令行 → `examples/configuration/cli-options.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始) - `examples/getting-started/`**:
   - `examples/getting-started/installation.md` - Installing Jest and basic setup
   - `examples/getting-started/using-matchers.md` - Using Jest matchers and assertions

   **Testing (测试) - `examples/testing/`**:
   - `examples/testing/asynchronous.md` - Testing asynchronous code
   - `examples/testing/setup-teardown.md` - Setup and teardown functions
   - `examples/testing/mock-functions.md` - Mocking functions
   - `examples/testing/manual-mocks.md` - Manual mocks
   - `examples/testing/snapshot-testing.md` - Snapshot testing
   - `examples/testing/timer-mocks.md` - Mocking timers
   - `examples/testing/es6-class-mocks.md` - Mocking ES6 classes

   **Configuration (配置) - `examples/configuration/`**:
   - `examples/configuration/jest-config.md` - Jest configuration options
   - `examples/configuration/cli-options.md` - CLI options and flags
   - `examples/configuration/babel.md` - Using Jest with Babel
   - `examples/configuration/typescript.md` - Using Jest with TypeScript

   **Guides (指南) - `examples/guides/`**:
   - `examples/guides/migrating-to-jest.md` - Migrating to Jest
   - `examples/guides/testing-react-apps.md` - Testing React applications
   - `examples/guides/testing-vue-apps.md` - Testing Vue applications

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow Jest best practices
   - Examples include both JavaScript and TypeScript versions where applicable
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/expect.md` - expect() API and matchers
   - `api/mock-functions.md` - Mock functions API
   - `api/jest-object.md` - Jest object API
   - `api/test.md` - test() and describe() API
   - `api/cli.md` - CLI commands and options

5. **Use templates** from the `templates/` directory:
   - `templates/jest-config.md` - Jest configuration templates
   - `templates/test-template.md` - Test file templates
   - `templates/setup-file.md` - Setup file templates

### Doc mapping (one-to-one with https://jestjs.io/docs/getting-started, https://jestjs.io/docs/api)

**Getting Started (快速开始)**:
- `examples/getting-started/installation.md` → https://jestjs.io/docs/getting-started
- `examples/getting-started/using-matchers.md` → https://jestjs.io/docs/using-matchers

**Testing (测试)**:
- `examples/testing/asynchronous.md` → https://jestjs.io/docs/asynchronous
- `examples/testing/setup-teardown.md` → https://jestjs.io/docs/setup-teardown
- `examples/testing/mock-functions.md` → https://jestjs.io/docs/mock-functions
- `examples/testing/manual-mocks.md` → https://jestjs.io/docs/manual-mocks
- `examples/testing/snapshot-testing.md` → https://jestjs.io/docs/snapshot-testing
- `examples/testing/timer-mocks.md` → https://jestjs.io/docs/timer-mocks
- `examples/testing/es6-class-mocks.md` → https://jestjs.io/docs/es6-class-mocks

**Configuration (配置)**:
- `examples/configuration/jest-config.md` → https://jestjs.io/docs/configuration
- `examples/configuration/cli-options.md` → https://jestjs.io/docs/cli

**API Reference**:
- `api/expect.md` → https://jestjs.io/docs/expect
- `api/mock-functions.md` → https://jestjs.io/docs/mock-functions
- `api/jest-object.md` → https://jestjs.io/docs/jest-object
- `api/test.md` → https://jestjs.io/docs/api#testname-fn-timeout
- `api/cli.md` → https://jestjs.io/docs/cli

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

1. **Write descriptive test names**: Use clear, descriptive test names
2. **Use appropriate matchers**: Choose the right matcher for each assertion
3. **Mock external dependencies**: Mock external APIs, databases, and services
4. **Test edge cases**: Test both happy paths and error cases
5. **Keep tests isolated**: Each test should be independent
6. **Use setup and teardown**: Clean up resources properly
7. **Snapshot testing**: Use snapshots for UI components, but review changes
8. **Coverage goals**: Aim for meaningful coverage, not just high percentages
9. **Organize tests**: Group related tests using describe blocks
10. **Async testing**: Properly handle async code with async/await or promises

## Resources

- **Official Documentation**: https://jestjs.io/
- **Getting Started**: https://jestjs.io/docs/getting-started
- **API Reference**: https://jestjs.io/docs/api
- **GitHub Repository**: https://github.com/jestjs/jest

## Keywords

Jest, testing, unit test, integration test, mock, spy, snapshot, matcher, assertion, async test, setup, teardown, coverage, CLI, configuration, TypeScript, React, Vue, Babel, 测试, 单元测试, 集成测试, Mock, 快照, 匹配器, 断言, 异步测试, 覆盖率, 配置
