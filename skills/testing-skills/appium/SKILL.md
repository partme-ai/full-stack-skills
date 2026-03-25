---
name: appium
description: "Provides comprehensive guidance for Appium mobile testing including mobile app automation, element location, gestures, and cross-platform testing. Use when the user asks about Appium, needs to test mobile applications, automate mobile apps, or write Appium test scripts."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write automated tests for Android and iOS native or hybrid mobile applications
- Locate elements using accessibility ID, ID, XPath, or class name
- Perform gestures (tap, swipe, scroll) and handle device interactions
- Configure desired capabilities for different devices and platforms
- Integrate Appium tests into CI/CD pipelines (Jenkins, GitHub Actions)

## How to use this skill

### Workflow

1. **Set up the environment**: install Appium Server, drivers (UiAutomator2 for Android, XCUITest for iOS), and language bindings
2. **Define capabilities**: specify device name, platform, app path, and automation engine
3. **Write test scripts**: locate elements, perform actions, and assert results
4. **Run in CI**: execute on real devices or emulators with parallel execution and reporting

### 1. Desired Capabilities

```python
desired_caps = {
    "platformName": "Android",
    "deviceName": "Pixel_6",
    "app": "/path/to/app.apk",
    "automationName": "UiAutomator2",
    "noReset": True,
}
```

### 2. Test Example (Python)

```python
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
wait = WebDriverWait(driver, 10)

# Login flow
username = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "username")))
username.send_keys("testuser")

driver.find_element(AppiumBy.ACCESSIBILITY_ID, "password").send_keys("secret")
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "login-button").click()

# Assert
welcome = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "welcome")))
assert welcome.is_displayed()

driver.quit()
```

### 3. Test Example (Java)

```java
DesiredCapabilities caps = new DesiredCapabilities();
caps.setCapability("platformName", "Android");
caps.setCapability("deviceName", "Pixel_6");
caps.setCapability("app", "/path/to/app.apk");
caps.setCapability("automationName", "UiAutomator2");

AndroidDriver driver = new AndroidDriver(new URL("http://localhost:4723/wd/hub"), caps);
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

driver.findElement(AppiumBy.accessibilityId("username")).sendKeys("testuser");
driver.findElement(AppiumBy.accessibilityId("login-button")).click();
assertTrue(wait.until(ExpectedConditions.visibilityOfElementLocated(AppiumBy.accessibilityId("welcome"))).isDisplayed());

driver.quit();
```

## Best Practices

- Prefer accessibility ID or resource ID for element location; avoid fragile XPath expressions
- Use explicit waits and retry logic; capture screenshots and logs on failure
- Test across multiple devices and OS versions using a device matrix
- Store sensitive information (app paths, credentials) in environment variables
- Use Appium's built-in gesture APIs for swipe, scroll, and long-press actions

## Resources

- Official documentation: https://appium.io/docs/en/latest/
- GitHub: https://github.com/appium/appium

## Keywords

appium, mobile automation, Android, iOS, UiAutomator2, XCUITest, accessibility ID, desired capabilities, cross-platform, UI testing, mobile testing
