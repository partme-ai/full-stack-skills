---
name: cypress
description: Provides comprehensive guidance for Cypress end-to-end testing including commands, assertions, component testing, CI/CD integration, and best practices. Use when the user asks about Cypress, needs to write E2E tests, component tests, or configure Cypress for testing.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Set up Cypress for end-to-end testing
- Write Cypress test cases
- Configure Cypress for component testing
- Integrate Cypress with CI/CD pipelines
- Use Cypress commands and assertions
- Debug Cypress tests
- Optimize Cypress test performance
- Migrate from other testing frameworks to Cypress
- Use Cypress with different frameworks (React, Vue, Angular, Svelte)
- Configure Cypress for different environments

## How to use this skill

This skill is organized to match the Cypress official documentation structure (https://docs.cypress.io/app/get-started/why-cypress, https://docs.cypress.io/api/table-of-contents). When working with Cypress:

1. **Identify the topic** from the user's request:
   - Getting Started/快速开始 → `examples/get-started/`
   - Core Concepts/核心概念 → `examples/core-concepts/`
   - Component Testing/组件测试 → `examples/component-testing/`
   - End-to-End Testing/E2E测试 → `examples/end-to-end-testing/`
   - Continuous Integration/持续集成 → `examples/continuous-integration/`
   - Guides/指南 → `examples/guides/`
   - References/参考 → `examples/references/`
   - API Reference/API 参考 → `api/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始)** - `examples/get-started/`:
   - `examples/get-started/install-cypress.md`
   - `examples/get-started/open-the-app.md`
   - `examples/get-started/why-cypress.md`

   **Core Concepts (核心概念)** - `examples/core-concepts/`:
   - `examples/core-concepts/best-practices.md`
   - `examples/core-concepts/interacting-with-elements.md`
   - `examples/core-concepts/introduction-to-cypress.md`
   - `examples/core-concepts/open-mode.md`
   - `examples/core-concepts/retry-ability.md`
   - `examples/core-concepts/test-isolation.md`
   - `examples/core-concepts/testing-types.md`
   - `examples/core-concepts/variables-and-aliases.md`
   - `examples/core-concepts/writing-and-organizing-tests.md`

   **Component Testing (组件测试)** - `examples/component-testing/`:
   - `examples/component-testing/angular/api.md`
   - `examples/component-testing/angular/examples.md`
   - `examples/component-testing/angular/overview.md`
   - `examples/component-testing/component-framework-configuration.md`
   - `examples/component-testing/custom-frameworks.md`
   - `examples/component-testing/get-started.md`
   - `examples/component-testing/react/api.md`
   - `examples/component-testing/react/examples.md`
   - `examples/component-testing/react/overview.md`
   - `examples/component-testing/styling-components.md`
   - `examples/component-testing/svelte/api.md`
   - `examples/component-testing/svelte/examples.md`
   - `examples/component-testing/svelte/overview.md`
   - `examples/component-testing/vue/api.md`
   - `examples/component-testing/vue/examples.md`
   - `examples/component-testing/vue/overview.md`

   **End-to-End Testing (E2E测试)** - `examples/end-to-end-testing/`:
   - `examples/end-to-end-testing/testing-your-app.md`
   - `examples/end-to-end-testing/writing-your-first-end-to-end-test.md`

   **Continuous Integration (持续集成)** - `examples/continuous-integration/`:
   - `examples/continuous-integration/aws-codebuild.md`
   - `examples/continuous-integration/bitbucket-pipelines.md`
   - `examples/continuous-integration/circleci.md`
   - `examples/continuous-integration/github-actions.md`
   - `examples/continuous-integration/gitlab-ci.md`
   - `examples/continuous-integration/overview.md`

   **Guides (指南)** - `examples/guides/`:
   - `examples/guides/accessibility-testing.md`
   - `examples/guides/authentication-testing/amazon-cognito-authentication.md`
   - `examples/guides/authentication-testing/auth0-authentication.md`
   - `examples/guides/authentication-testing/azure-active-directory-authentication.md`
   - `examples/guides/authentication-testing/google-authentication.md`
   - `examples/guides/authentication-testing/okta-authentication.md`
   - `examples/guides/authentication-testing/social-authentication.md`
   - `examples/guides/conditional-testing.md`
   - `examples/guides/cross-browser-testing.md`
   - `examples/guides/cross-origin-testing.md`
   - `examples/guides/cypress-studio.md`
   - `examples/guides/debugging.md`
   - `examples/guides/migration/protractor-to-cypress.md`
   - `examples/guides/migration/selenium-to-cypress.md`
   - `examples/guides/network-requests.md`
   - `examples/guides/screenshots-and-videos.md`
   - `examples/guides/stubs-spies-and-clocks.md`
   - `examples/guides/test-retries.md`

   **References (参考)** - `examples/references/`:
   - `examples/references/advanced-installation.md`
   - `examples/references/assertions.md`
   - `examples/references/bundled-libraries.md`
   - `examples/references/changelog.md`
   - `examples/references/client-certificates.md`
   - `examples/references/command-line.md`
   - `examples/references/configuration.md`
   - `examples/references/content-security-policy.md`
   - `examples/references/environment-variables.md`
   - `examples/references/error-messages.md`
   - `examples/references/experiments.md`
   - `examples/references/launching-browsers.md`
   - `examples/references/migration-guide.md`
   - `examples/references/module-api.md`
   - `examples/references/proxy-configuration.md`
   - `examples/references/recipes.md`
   - `examples/references/roadmap.md`
   - `examples/references/trade-offs.md`
   - `examples/references/troubleshooting.md`

   **Other Sections**:
   - `examples/faq.md`
   - `examples/plugins/plugins-guide.md`
   - `examples/plugins/plugins-list.md`
   - `examples/tooling/IDE-integration.md`
   - `examples/tooling/code-coverage.md`
   - `examples/tooling/reporters.md`
   - `examples/tooling/typescript-support.md`
   - `examples/tooling/visual-testing.md`

3. **Reference API documentation** in the `api/` directory when needed:

   **Commands API** - `api/commands/`:
   - `api/commands/and.md`
   - `api/commands/as.md`
   - `api/commands/blur.md`
   - `api/commands/check.md`
   - `api/commands/children.md`
   - `api/commands/clear.md`
   - `api/commands/clearallcookies.md`
   - `api/commands/clearalllocalstorage.md`
   - `api/commands/clearallsessionstorage.md`
   - `api/commands/clearcookie.md`
   - `api/commands/clearcookies.md`
   - `api/commands/clearlocalstorage.md`
   - `api/commands/click.md`
   - `api/commands/clock.md`
   - `api/commands/closest.md`
   - `api/commands/contains.md`
   - `api/commands/dblclick.md`
   - `api/commands/debug.md`
   - `api/commands/document.md`
   - `api/commands/each.md`
   - `api/commands/end.md`
   - `api/commands/eq.md`
   - `api/commands/exec.md`
   - `api/commands/filter.md`
   - `api/commands/find.md`
   - `api/commands/first.md`
   - `api/commands/fixture.md`
   - `api/commands/focus.md`
   - `api/commands/focused.md`
   - `api/commands/get.md`
   - `api/commands/getallcookies.md`
   - `api/commands/getalllocalstorage.md`
   - `api/commands/getallsessionstorage.md`
   - `api/commands/getcookie.md`
   - `api/commands/getcookies.md`
   - `api/commands/go.md`
   - `api/commands/hash.md`
   - `api/commands/hover.md`
   - `api/commands/intercept.md`
   - `api/commands/invoke.md`
   - `api/commands/its.md`
   - `api/commands/last.md`
   - `api/commands/location.md`
   - `api/commands/log.md`
   - `api/commands/mount.md`
   - `api/commands/next.md`
   - `api/commands/nextall.md`
   - `api/commands/nextuntil.md`
   - `api/commands/not.md`
   - `api/commands/origin.md`
   - ... and 43 more command files

   **Cypress API** - `api/cypress-api/`:
   - `api/cypress-api/arch.md`
   - `api/cypress-api/browser.md`
   - `api/cypress-api/catalog-of-events.md`
   - `api/cypress-api/config.md`
   - `api/cypress-api/cookies.md`
   - `api/cypress-api/currentretry.md`
   - `api/cypress-api/currenttest.md`
   - `api/cypress-api/custom-commands.md`
   - `api/cypress-api/custom-queries.md`
   - `api/cypress-api/cypress-log.md`
   - `api/cypress-api/dom.md`
   - `api/cypress-api/element-selector-api.md`
   - `api/cypress-api/ensure.md`
   - `api/cypress-api/env.md`
   - `api/cypress-api/isbrowser.md`
   - `api/cypress-api/iscy.md`
   - `api/cypress-api/keyboard-api.md`
   - `api/cypress-api/platform.md`
   - `api/cypress-api/require.md`
   - `api/cypress-api/screenshot-api.md`
   - `api/cypress-api/session.md`
   - `api/cypress-api/spec.md`
   - `api/cypress-api/stop.md`
   - `api/cypress-api/testing-type.md`
   - `api/cypress-api/version.md`

   **Node Events API** - `api/node-events/`:
   - `api/node-events/after-run-api.md`
   - `api/node-events/after-screenshot-api.md`
   - `api/node-events/after-spec-api.md`
   - `api/node-events/before-run-api.md`
   - `api/node-events/before-spec-api.md`
   - `api/node-events/browser-launch-api.md`
   - `api/node-events/configuration-api.md`
   - `api/node-events/overview.md`
   - `api/node-events/preprocessors-api.md`

   **Utilities API** - `api/utilities/`:
   - `api/utilities/$.md`
   - `api/utilities/_.md`
   - `api/utilities/blob.md`
   - `api/utilities/buffer.md`
   - `api/utilities/minimatch.md`
   - `api/utilities/promise.md`
   - `api/utilities/sinon.md`

   **Table of Contents** - `api/table-of-contents/`:

4. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow Cypress best practices
   - Examples include both JavaScript and TypeScript versions where applicable
   - Each example file includes parameters, returns, common errors, best practices, and scenarios
   - Always check the example file for best practices and common patterns

5. **Reference the official documentation** when needed:
   - Getting Started: https://docs.cypress.io/app/get-started/why-cypress
   - API Reference: https://docs.cypress.io/api/table-of-contents

## Best Practices

1. **Use data-cy attributes**: Use data-cy attributes for stable, test-friendly selectors
2. **Avoid hard-coded waits**: Leverage Cypress's built-in retry-ability instead of cy.wait()
3. **Keep tests isolated**: Each test should be independent and not rely on other tests
4. **Use custom commands**: Create custom commands for reusable test logic
5. **Follow assertion patterns**: Use Cypress's built-in assertions for better error messages
6. **Configure properly**: Set up cypress.config.js correctly for your project
7. **Use fixtures**: Use fixtures for test data instead of hard-coding values
8. **Component testing**: Use component testing for isolated component testing
9. **CI/CD integration**: Configure Cypress properly for CI/CD environments
10. **Debug effectively**: Use Cypress's debugging tools and commands

## Resources

- **Official Documentation**: https://docs.cypress.io/
- **Getting Started**: https://docs.cypress.io/app/get-started/why-cypress
- **API Reference**: https://docs.cypress.io/api/table-of-contents
- **GitHub Repository**: https://github.com/cypress-io/cypress

## Keywords

Cypress, end-to-end testing, E2E testing, component testing, test automation, browser testing, test framework, assertions, commands, fixtures, CI/CD, continuous integration, test runner, 端到端测试, E2E测试, 组件测试, 测试自动化, 浏览器测试, 测试框架, 断言, 命令, 固定数据, 持续集成, 测试运行器
