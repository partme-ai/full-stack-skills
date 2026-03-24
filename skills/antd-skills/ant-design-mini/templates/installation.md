# Installation Templates

## Alipay Mini Program

```json
// app.json
{
  "usingComponents": {
    "ant-button": "antd-mini/es/Button/index",
    "ant-input": "antd-mini/es/Input/index",
    "ant-form": "antd-mini/es/Form/index"
  }
}
```

```xml
<!-- page.axml -->
<ant-button type="primary" onTap="handleTap">Button</ant-button>
```

```javascript
// page.js
Page({
  handleTap() {
    console.log('Tapped')
  }
})
```

## WeChat Mini Program

```json
// app.json
{
  "usingComponents": {
    "ant-button": "antd-mini/es/Button/index",
    "ant-input": "antd-mini/es/Input/index",
    "ant-form": "antd-mini/es/Form/index"
  }
}
```

```xml
<!-- page.wxml -->
<ant-button type="primary" bindtap="handleTap">Button</ant-button>
```

```javascript
// page.js
Page({
  handleTap() {
    console.log('Tapped')
  }
})
```

## Complete Setup

```bash
# Install
npm install antd-mini

# Register components in app.json
# Use components in pages
```
