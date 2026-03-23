# Quick Start

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example provides a quick start guide for Ant Design Mini.

### Key Concepts

- Project setup
- First component
- Component registration
- Basic usage

### Example: Complete Setup

```json
// app.json
{
  "usingComponents": {
    "ant-button": "antd-mini/es/Button/index",
    "ant-input": "antd-mini/es/Input/index"
  }
}
```

```xml
<!-- index.axml -->
<view class="container">
  <ant-input 
    value="{{value}}" 
    placeholder="Enter text"
    onInput="handleInput"
  />
  <ant-button type="primary" onTap="handleTap">
    Submit
  </ant-button>
</view>
```

```javascript
// index.js
Page({
  data: {
    value: ''
  },
  handleInput(e) {
    this.setData({
      value: e.detail.value
    })
  },
  handleTap() {
    console.log('Value:', this.data.value)
  }
})
```

### Example: Using Multiple Components

```json
// app.json
{
  "usingComponents": {
    "ant-button": "antd-mini/es/Button/index",
    "ant-form": "antd-mini/es/Form/index",
    "ant-form-item": "antd-mini/es/FormItem/index",
    "ant-input": "antd-mini/es/Input/index"
  }
}
```

### Key Points

- Register all used components
- Use correct event names (onTap/bindtap)
- Handle events in page methods
- Use data binding for two-way binding
- Follow mini-program syntax
