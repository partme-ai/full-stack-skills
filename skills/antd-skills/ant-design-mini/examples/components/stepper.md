# Stepper Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Stepper component in Ant Design Mini.

### Key Concepts

- Stepper value
- Stepper min/max
- Stepper step
- Stepper events

### Example: Basic Stepper

```xml
<!-- Alipay -->
<ant-stepper 
  value="{{value}}"
  onChange="handleChange"
/>
```

```xml
<!-- WeChat -->
<ant-stepper 
  value="{{value}}"
  bindchange="handleChange"
/>
```

```javascript
// page.js
Page({
  data: {
    value: 1
  },
  handleChange(e) {
    this.setData({
      value: e.detail.value
    })
  }
})
```

### Example: Stepper with Limits

```xml
<ant-stepper 
  value="{{value}}"
  min="0"
  max="10"
  step="1"
  onChange="handleChange"
/>
```

### Example: Stepper Disabled

```xml
<ant-stepper 
  value="{{value}}"
  disabled
/>
```

### Key Points

- Use value for current value
- Set min and max limits
- Configure step increment
- Handle onChange/bindchange event
- Support disabled state
