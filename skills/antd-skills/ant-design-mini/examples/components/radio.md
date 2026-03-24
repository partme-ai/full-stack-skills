# Radio Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Radio component in Ant Design Mini.

### Key Concepts

- Single radio
- Radio group
- Radio states
- Radio events

### Example: Basic Radio

```xml
<ant-radio-group 
  value="{{value}}"
  onChange="handleChange"
>
  <ant-radio value="1">Option 1</ant-radio>
  <ant-radio value="2">Option 2</ant-radio>
  <ant-radio value="3">Option 3</ant-radio>
</ant-radio-group>
```

```javascript
// page.js
Page({
  data: {
    value: '1'
  },
  handleChange(e) {
    this.setData({
      value: e.detail.value
    })
  }
})
```

### Example: Radio States

```xml
<ant-radio value="1" disabled>Disabled</ant-radio>
```

### Key Points

- Use radio-group for radio groups
- Set value for each radio
- Handle onChange/bindchange event
- Support disabled state
- Single selection only
