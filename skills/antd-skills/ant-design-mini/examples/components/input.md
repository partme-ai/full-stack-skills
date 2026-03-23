# Input Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Input component in Ant Design Mini.

### Key Concepts

- Input types
- Input states
- Input events
- Input validation

### Example: Basic Input

```xml
<!-- Alipay -->
<ant-input 
  value="{{value}}" 
  placeholder="Enter text"
  onInput="handleInput"
/>
```

```xml
<!-- WeChat -->
<ant-input 
  value="{{value}}" 
  placeholder="Enter text"
  bindinput="handleInput"
/>
```

```javascript
// page.js
Page({
  data: {
    value: ''
  },
  handleInput(e) {
    this.setData({
      value: e.detail.value
    })
  }
})
```

### Example: Input Types

```xml
<ant-input type="text" placeholder="Text" />
<ant-input type="number" placeholder="Number" />
<ant-input type="password" placeholder="Password" />
```

### Example: Input States

```xml
<ant-input disabled placeholder="Disabled" />
<ant-input readonly value="Readonly" />
```

### Example: Input with Clear

```xml
<ant-input 
  value="{{value}}"
  allowClear
  onInput="handleInput"
/>
```

### Example: Input Validation

```xml
<ant-input 
  value="{{value}}"
  maxlength="10"
  onInput="handleInput"
/>
```

### Key Points

- Use value and onInput/bindinput for two-way binding
- Support multiple input types
- Support disabled and readonly states
- Allow clear button
- Support maxlength validation
