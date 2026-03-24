# Switch Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Switch component in Ant Design Mini.

### Key Concepts

- Switch state
- Switch events
- Switch styling
- Switch sizes

### Example: Basic Switch

```xml
<!-- Alipay -->
<ant-switch 
  checked="{{checked}}"
  onChange="handleSwitchChange"
/>
```

```xml
<!-- WeChat -->
<ant-switch 
  checked="{{checked}}"
  bindchange="handleSwitchChange"
/>
```

```javascript
// page.js
Page({
  data: {
    checked: false
  },
  handleSwitchChange(e) {
    this.setData({
      checked: e.detail.value
    })
  }
})
```

### Example: Switch with Label

```xml
<ant-switch 
  checked="{{checked}}"
  onChange="handleSwitchChange"
>
  Enable Feature
</ant-switch>
```

### Example: Switch States

```xml
<ant-switch checked="{{checked}}" disabled />
```

### Key Points

- Use checked prop for state
- Handle onChange/bindchange event
- Support disabled state
- Can include label text
- Simple toggle control
