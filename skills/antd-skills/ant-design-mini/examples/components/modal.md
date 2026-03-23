# Modal Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Modal component in Ant Design Mini.

### Key Concepts

- Modal display
- Modal content
- Modal actions
- Modal events

### Example: Basic Modal

```xml
<ant-modal 
  visible="{{visible}}"
  title="Title"
  onClose="handleClose"
>
  <view>Modal Content</view>
</ant-modal>
<ant-button onTap="showModal">Show Modal</ant-button>
```

```javascript
// page.js
Page({
  data: {
    visible: false
  },
  showModal() {
    this.setData({ visible: true })
  },
  handleClose() {
    this.setData({ visible: false })
  }
})
```

### Example: Modal with Actions

```xml
<ant-modal 
  visible="{{visible}}"
  title="Confirm"
  onOk="handleOk"
  onCancel="handleCancel"
>
  <view>Are you sure?</view>
</ant-modal>
```

### Example: Modal API

```javascript
// Using Modal API
import { Modal } from 'antd-mini'

Modal.confirm({
  title: 'Confirm',
  content: 'Are you sure?',
  onOk: () => {
    console.log('Confirmed')
  }
})
```

### Key Points

- Control visibility with visible prop
- Handle onClose event
- Support onOk and onCancel
- Use Modal API for programmatic control
- Customize modal content
