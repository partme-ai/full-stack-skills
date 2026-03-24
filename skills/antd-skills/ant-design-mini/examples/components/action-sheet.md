# ActionSheet Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the ActionSheet component in Ant Design Mini.

### Key Concepts

- Action sheet display
- Action items
- Action sheet events
- Action sheet styling

### Example: Basic ActionSheet

```xml
<ant-action-sheet 
  visible="{{visible}}"
  actions="{{actions}}"
  onClose="handleClose"
  onAction="handleAction"
/>
```

```javascript
// page.js
Page({
  data: {
    visible: false,
    actions: [
      { text: 'Option 1', value: '1' },
      { text: 'Option 2', value: '2' },
      { text: 'Cancel', value: 'cancel', type: 'cancel' }
    ]
  },
  showActionSheet() {
    this.setData({ visible: true })
  },
  handleClose() {
    this.setData({ visible: false })
  },
  handleAction(e) {
    console.log('Action:', e.detail.value)
    this.setData({ visible: false })
  }
})
```

### Example: ActionSheet API

```javascript
// Using ActionSheet API
import { ActionSheet } from 'antd-mini'

ActionSheet.show({
  actions: [
    { text: 'Option 1', value: '1' },
    { text: 'Option 2', value: '2' }
  ],
  onAction: (value) => {
    console.log('Selected:', value)
  }
})
```

### Key Points

- Configure actions array
- Handle onAction event
- Support cancel action
- Use ActionSheet API for programmatic control
- Control visibility with visible prop
