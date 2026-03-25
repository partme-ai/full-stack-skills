---
name: detox
description: "Provides comprehensive guidance for Detox mobile testing framework including React Native testing, E2E testing, and test synchronization. Use when the user asks about Detox, needs to test React Native applications, write E2E tests for mobile apps, or configure Detox."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write end-to-end tests for React Native applications using Detox
- Configure Detox for iOS simulators and Android emulators
- Use element matchers, actions, and assertions in Detox tests
- Integrate Detox tests into CI/CD pipelines
- Debug synchronization and timing issues in mobile tests

## How to use this skill

### Workflow

1. **Set up the environment**: install Detox CLI, configure `.detoxrc.js`, ensure Xcode/Android SDK are ready
2. **Write test cases**: use `element(by.id(...))`, `tap()`, `typeText()`, and `expect()`
3. **Build and test**: `detox build` then `detox test`
4. **Run in CI**: save artifacts (logs, screenshots) on failure

### 1. Configuration (.detoxrc.js)

```javascript
module.exports = {
  testRunner: { args: { config: 'e2e/jest.config.js' } },
  apps: {
    'ios.debug': {
      type: 'ios.app',
      binaryPath: 'ios/build/MyApp.app',
      build: 'xcodebuild -workspace ios/MyApp.xcworkspace -scheme MyApp -configuration Debug -sdk iphonesimulator',
    },
    'android.debug': {
      type: 'android.apk',
      binaryPath: 'android/app/build/outputs/apk/debug/app-debug.apk',
      build: 'cd android && ./gradlew assembleDebug',
    },
  },
  devices: {
    simulator: { type: 'ios.simulator', device: { type: 'iPhone 15' } },
    emulator: { type: 'android.emulator', device: { avdName: 'Pixel_6' } },
  },
  configurations: {
    'ios.sim.debug': { device: 'simulator', app: 'ios.debug' },
    'android.emu.debug': { device: 'emulator', app: 'android.debug' },
  },
};
```

### 2. Test Example

```javascript
describe('Login Flow', () => {
  beforeAll(async () => {
    await device.launchApp();
  });

  it('should login successfully', async () => {
    await element(by.id('username-input')).typeText('testuser');
    await element(by.id('password-input')).typeText('secret');
    await element(by.id('login-button')).tap();
    await expect(element(by.id('welcome-message'))).toBeVisible();
  });
});
```

### 3. Running Tests

```bash
# Build the app
detox build --configuration ios.sim.debug

# Run tests
detox test --configuration ios.sim.debug

# With artifacts on failure
detox test --configuration ios.sim.debug --artifacts-location ./artifacts
```

## Best Practices

- Use `testID` props for stable element identification; avoid matching on text or animations
- Keep build and device configurations consistent between local development and CI
- Save artifacts (logs, screenshots, videos) on failure for debugging
- Use environment variables for sensitive operations; configure retry and parallelization strategies
- Disable animations in test builds to avoid synchronization issues

## Resources

- Official documentation: https://wix.github.io/Detox/
- GitHub: https://github.com/wix/Detox

## Keywords

detox, React Native, E2E, end-to-end testing, mobile testing, iOS simulator, Android emulator, testID, synchronization, Wix Detox
