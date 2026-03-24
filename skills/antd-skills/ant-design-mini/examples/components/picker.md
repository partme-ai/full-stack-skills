# Picker Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Picker component in Ant Design Mini.

### Key Concepts

- Picker options
- Picker selection
- Picker events
- Multi-column picker

### Example: Basic Picker

```xml
<ant-picker 
  value="{{selectedValue}}"
  options="{{options}}"
  onOk="handlePickerOk"
  onCancel="handlePickerCancel"
>
  <view>Select: {{selectedValue}}</view>
</ant-picker>
```

```javascript
// page.js
Page({
  data: {
    selectedValue: '',
    options: [
      { label: 'Option 1', value: '1' },
      { label: 'Option 2', value: '2' },
      { label: 'Option 3', value: '3' }
    ]
  },
  handlePickerOk(e) {
    this.setData({
      selectedValue: e.detail.value
    })
  }
})
```

### Example: Multi-column Picker

```xml
<ant-picker 
  value="{{selectedValues}}"
  columns="{{columns}}"
  onOk="handlePickerOk"
/>
```

```javascript
// page.js
Page({
  data: {
    selectedValues: [],
    columns: [
      [
        { label: 'A', value: 'a' },
        { label: 'B', value: 'b' }
      ],
      [
        { label: '1', value: '1' },
        { label: '2', value: '2' }
      ]
    ]
  }
})
```

### Key Points

- Configure options array
- Handle onOk event for selection
- Support single and multi-column
- Use value for controlled component
- Customize picker display
