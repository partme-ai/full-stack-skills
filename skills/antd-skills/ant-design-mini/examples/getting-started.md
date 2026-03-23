# Getting Started

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates how to get started with Ant Design Mini.

### Key Concepts

- Installation
- Component registration
- Basic usage
- Platform differences

### Example: Installation

```bash
# Using npm
npm install antd-mini

# Using yarn
yarn add antd-mini

# Using pnpm
pnpm add antd-mini
```

### Example: Component Registration (Alipay)

```json
// app.json
{
  "usingComponents": {
    "ant-button": "antd-mini/es/Button/index"
  }
}
```

### Example: Component Usage (Alipay)

```xml
<!-- page.axml -->
<ant-button type="primary" onTap="handleTap">Button</ant-button>
```

```javascript
// page.js
Page({
  handleTap() {
    console.log('Button tapped')
  }
})
```

### Example: Component Registration (WeChat)

```json
// app.json
{
  "usingComponents": {
    "ant-button": "antd-mini/es/Button/index"
  }
}
```

### Example: Component Usage (WeChat)

```xml
<!-- page.wxml -->
<ant-button type="primary" bindtap="handleTap">Button</ant-button>
```

```javascript
// page.js
Page({
  handleTap() {
    console.log('Button tapped')
  }
})
```

### Key Points

- Install antd-mini package
- Register components in app.json
- Use axml for Alipay, wxml for WeChat
- Use onTap for Alipay, bindtap for WeChat
- Import component styles if needed
