# Checkbox Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Checkbox component in Ant Design Mini.

### Key Concepts

- Single checkbox
- Checkbox group
- Checkbox states
- Checkbox events

### Example: Basic Checkbox

```xml
<!-- Alipay -->
<ant-checkbox 
  checked="{{checked}}"
  onChange="handleChange"
>
  Checkbox
</ant-checkbox>
```

```xml
<!-- WeChat -->
<ant-checkbox 
  checked="{{checked}}"
  bindchange="handleChange"
>
  Checkbox
</ant-checkbox>
```

```javascript
// page.js
Page({
  data: {
    checked: false
  },
  handleChange(e) {
    this.setData({
      checked: e.detail.value
    })
  }
})
```

### Example: Checkbox Group

```xml
<ant-checkbox-group 
  value="{{checkedList}}"
  onChange="handleGroupChange"
>
  <ant-checkbox value="1">Option 1</ant-checkbox>
  <ant-checkbox value="2">Option 2</ant-checkbox>
  <ant-checkbox value="3">Option 3</ant-checkbox>
</ant-checkbox-group>
```

```javascript
// page.js
Page({
  data: {
    checkedList: []
  },
  handleGroupChange(e) {
    this.setData({
      checkedList: e.detail.value
    })
  }
})
```

### Example: Checkbox States

```xml
<ant-checkbox checked="{{checked}}" disabled>
  Disabled
</ant-checkbox>
```

### Key Points

- Use checked prop for state
- Handle onChange/bindchange event
- Use checkbox-group for multiple checkboxes
- Support disabled state
- Value array for group
