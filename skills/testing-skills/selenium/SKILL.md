---
name: selenium
description: "Provides comprehensive guidance for Selenium WebDriver including browser automation, element location, waits, and test frameworks. Use when the user asks about Selenium, needs to automate web browsers, write Selenium tests, or work with Selenium WebDriver."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Write or maintain browser automation tests with Selenium WebDriver
- Locate elements using CSS selectors, IDs, or relative locators
- Implement explicit and implicit waits for robust test execution
- Run tests in headless mode or across browsers via Selenium Grid
- Integrate Selenium tests into CI/CD pipelines

## How to use this skill

### Workflow

1. **Set up the environment**: install browser drivers (ChromeDriver/GeckoDriver) or use Selenium 4 Manager
2. **Write test scripts**: navigate, find elements, interact, and assert
3. **Add waits and error handling**: use explicit waits instead of `sleep`
4. **Run in CI**: configure headless mode or Grid; generate reports

### 1. Basic Test (Python)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Explicit wait for element
wait = WebDriverWait(driver, 10)
username = wait.until(EC.presence_of_element_located((By.ID, "username")))
username.send_keys("testuser")

driver.find_element(By.ID, "password").send_keys("secret")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Assert login success
assert "Dashboard" in driver.title

driver.quit()
```

### 2. Basic Test (Java)

```java
WebDriver driver = new ChromeDriver();
driver.get("https://example.com/login");

WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
WebElement username = wait.until(ExpectedConditions.presenceOfElementLocated(By.id("username")));
username.sendKeys("testuser");

driver.findElement(By.id("password")).sendKeys("secret");
driver.findElement(By.cssSelector("button[type='submit']")).click();

assertTrue(driver.getTitle().contains("Dashboard"));
driver.quit();
```

### 3. Headless Mode

```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)
```

## Best Practices

- Use explicit waits (`WebDriverWait`) instead of `time.sleep` for reliable tests
- Prefer ID, CSS selector, or relative locators over fragile XPath expressions
- Keep test cases independent and repeatable; capture screenshots on failure
- Store sensitive data (URLs, credentials) in configuration files or environment variables
- Use Selenium Grid for parallel execution; ensure browser and driver versions match

## Resources

- Official documentation: https://www.selenium.dev/documentation/
- Selenium Grid: https://www.selenium.dev/documentation/grid/

## Keywords

selenium, WebDriver, browser automation, E2E, end-to-end testing, headless, Selenium Grid, ChromeDriver, explicit wait, CSS selector
