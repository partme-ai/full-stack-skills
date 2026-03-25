---
name: playwright
description: "Provides comprehensive guidance for Playwright testing including browser automation, test writing, page objects, and cross-browser testing. Use when the user asks about Playwright, needs to write E2E tests, automate browsers, or test web applications across browsers."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write end-to-end browser tests with Playwright (Chromium, Firefox, WebKit)
- Use auto-waiting locators and built-in assertions
- Handle multiple pages, tabs, and browser contexts
- Configure Playwright projects for CI execution with traces and screenshots
- Implement the Page Object Model pattern for maintainable tests

## How to use this skill

### Workflow

1. **Initialize Playwright**: `npm init playwright` to generate config and sample tests
2. **Write tests** using auto-wait locators (`getByRole`, `getByLabel`, `getByText`)
3. **Run tests**: `npx playwright test` in headless, headed, or UI mode
4. **Debug failures** using traces, screenshots, and the Playwright Inspector

### 1. Basic Test

```typescript
import { test, expect } from '@playwright/test';

test('homepage has title', async ({ page }) => {
  await page.goto('https://example.com');
  await expect(page).toHaveTitle(/Example/);
});

test('login flow', async ({ page }) => {
  await page.goto('https://example.com/login');
  await page.getByLabel('Username').fill('testuser');
  await page.getByLabel('Password').fill('secret');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await expect(page.getByText('Dashboard')).toBeVisible();
});
```

### 2. Page Object Model

```typescript
class LoginPage {
  constructor(private page: Page) {}

  async login(username: string, password: string) {
    await this.page.getByLabel('Username').fill(username);
    await this.page.getByLabel('Password').fill(password);
    await this.page.getByRole('button', { name: 'Sign in' }).click();
  }
}
```

### 3. Configuration

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  retries: 2,
  use: {
    baseURL: 'https://example.com',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    { name: 'chromium', use: { browserName: 'chromium' } },
    { name: 'firefox', use: { browserName: 'firefox' } },
    { name: 'webkit', use: { browserName: 'webkit' } },
  ],
});
```

### 4. Running Tests

```bash
npx playwright test                    # Run all tests headless
npx playwright test --headed           # Run with browser visible
npx playwright test --ui               # Interactive UI mode
npx playwright show-report             # View HTML report
```

## Best Practices

- Prefer role-based locators (`getByRole`, `getByLabel`) over fragile XPath or CSS selectors
- Keep tests independent and repeatable; use `beforeEach` or fixtures to prepare state
- Install browsers and dependencies in CI (`npx playwright install --with-deps`)
- Retain traces and screenshots on failure for debugging
- Use Playwright's built-in `expect` assertions — they auto-retry

## Resources

- Official documentation: https://playwright.dev/docs/intro
- API reference: https://playwright.dev/docs/api/class-playwright
- Best practices: https://playwright.dev/docs/best-practices

## Keywords

playwright, E2E, end-to-end testing, cross-browser, auto-wait, locators, getByRole, trace, Page Object Model, Chromium, Firefox, WebKit
