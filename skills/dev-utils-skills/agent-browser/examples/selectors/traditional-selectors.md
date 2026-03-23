# Traditional Selectors | 传统选择器

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to use traditional selectors (CSS, XPath, semantic locators) in agent-browser.

### Key Concepts

- CSS selectors
- XPath selectors
- Semantic locators
- ID and class selectors
- When to use each type

### Example: CSS Selectors

```bash
# Element selector
agent-browser click button

# Class selector
agent-browser click .submit-button

# ID selector
agent-browser click #login-btn

# Attribute selector
agent-browser click input[name="email"]

# Descendant selector
agent-browser click form .submit

# Pseudo-selector
agent-browser click button:first-child
```

### Example: XPath Selectors

```bash
# Basic XPath
agent-browser click "//button"

# XPath with attribute
agent-browser click "//button[@type='submit']"

# XPath with text
agent-browser click "//button[text()='Submit']"

# XPath with contains
agent-browser click "//button[contains(@class, 'submit')]"

# Complex XPath
agent-browser click "//form[@id='login']//button[@type='submit']"
```

### Example: Semantic Locators

```bash
# Role-based selector
agent-browser click role=button

# Role with name
agent-browser click role=button name="Submit"

# Role with accessible name
agent-browser click role=textbox name="Email"

# Link by accessible name
agent-browser click role=link name="Login"

# Heading by level and name
agent-browser get text role=heading name="Welcome" level=1
```

### Example: ID and Class Selectors

```bash
# ID selector
agent-browser click #my-button

# Class selector
agent-browser click .my-class

# Multiple classes
agent-browser click .btn.primary

# Element with class
agent-browser click button.primary
```

### Example: Combining Selectors

```bash
# CSS selector in command
agent-browser fill input[name="email"] "user@example.com"

# XPath in command
agent-browser click "//form//button[@type='submit']"

# Semantic locator in command
agent-browser click role=button name="Submit"
```

### Example: When to Use Each Selector

```bash
# Use CSS selectors for:
# - Simple, stable selectors
# - Well-structured HTML
agent-browser click button.submit

# Use XPath for:
# - Complex element relationships
# - Text-based selection
agent-browser click "//button[text()='Submit']"

# Use semantic locators for:
# - Accessibility-focused selection
# - When structure might change
agent-browser click role=button name="Submit"

# Use refs for:
# - Deterministic selection (preferred)
# - AI agent workflows
agent-browser click @e1
```

### Key Points

- CSS selectors: Simple and fast, but can break with structure changes
- XPath: Powerful but complex, good for text-based selection
- Semantic locators: Accessibility-focused, more stable
- Refs: Most reliable, preferred for AI agents
- Choose selector type based on stability needs
- Semantic locators are more maintainable than CSS
- Always prefer refs when available
