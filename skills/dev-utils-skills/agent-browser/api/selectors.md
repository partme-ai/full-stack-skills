# Selectors API | 选择器 API

## API Reference

Complete selector reference for agent-browser.

### Refs

Deterministic element identifiers from snapshot.

**Format:** `@e1`, `@e2`, `@e3`, etc.

**Example:**
```bash
agent-browser click @e1
agent-browser fill @e2 "text"
```

**Advantages:**
- Deterministic
- Fast
- AI-friendly
- Stable across page changes

### CSS Selectors

Standard CSS selector syntax.

**Examples:**
```bash
agent-browser click button
agent-browser click .submit-button
agent-browser click #login-btn
agent-browser click input[name="email"]
agent-browser click form .submit
```

### XPath Selectors

XPath expression syntax (must be quoted).

**Examples:**
```bash
agent-browser click "//button"
agent-browser click "//button[@type='submit']"
agent-browser click "//button[text()='Submit']"
agent-browser click "//form[@id='login']//button"
```

### Semantic Locators

Accessibility-focused selectors.

**Format:** `role=<role>`, `role=<role> name=<name>`

**Examples:**
```bash
agent-browser click role=button
agent-browser click role=button name="Submit"
agent-browser click role=textbox name="Email"
agent-browser click role=link name="Login"
agent-browser get text role=heading name="Welcome" level=1
```

### ID and Class Selectors

Simple ID and class selectors.

**Examples:**
```bash
agent-browser click #my-button
agent-browser click .my-class
agent-browser click .btn.primary
agent-browser click button.primary
```

### Selector Priority

1. **Refs** (preferred): Most reliable, deterministic
2. **Semantic Locators**: Accessibility-focused, stable
3. **CSS Selectors**: Simple, but can break
4. **XPath**: Powerful, but complex

### When to Use Each

- **Refs**: Always prefer for AI agents and deterministic automation
- **Semantic Locators**: When structure might change, accessibility-focused
- **CSS Selectors**: Simple, stable HTML structure
- **XPath**: Complex relationships, text-based selection

### Key Points

- Refs are the most reliable selector type
- Get refs from `snapshot` command
- Semantic locators are more maintainable
- CSS selectors are simple but fragile
- XPath is powerful but complex
- Always prefer refs when available
