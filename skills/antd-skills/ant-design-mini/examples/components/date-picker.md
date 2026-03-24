# DatePicker Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the DatePicker component in Ant Design Mini.

### Key Concepts

- Date selection
- Date range
- Date format
- Date picker types

### Example: Basic DatePicker

```xml
<ant-date-picker 
  value="{{date}}"
  onOk="handleDateOk"
/>
```

```javascript
// page.js
Page({
  data: {
    date: ''
  },
  handleDateOk(e) {
    this.setData({
      date: e.detail.value
    })
  }
})
```

### Example: Date Range

```xml
<ant-date-picker 
  value="{{dateRange}}"
  mode="range"
  onOk="handleRangeOk"
/>
```

```javascript
// page.js
Page({
  data: {
    dateRange: []
  },
  handleRangeOk(e) {
    this.setData({
      dateRange: e.detail.value
    })
  }
})
```

### Example: Date Picker Types

```xml
<ant-date-picker mode="date" />
<ant-date-picker mode="time" />
<ant-date-picker mode="datetime" />
```

### Key Points

- Use value for selected date
- Handle onOk event
- Support date range mode
- Multiple picker types
- Format date display
