# Popup Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Popup component in Ant Design Mini.

### Key Concepts

- Popup display
- Popup position
- Popup mask
- Popup events

### Example: Basic Popup

```xml
<ant-popup 
  visible="{{popupVisible}}"
  onClose="handleClose"
>
  <view>Popup Content</view>
</ant-popup>
<ant-button onTap="showPopup">Show Popup</ant-button>
```

```javascript
// page.js
Page({
  data: {
    popupVisible: false
  },
  showPopup() {
    this.setData({ popupVisible: true })
  },
  handleClose() {
    this.setData({ popupVisible: false })
  }
})
```

### Example: Popup Position

```xml
<ant-popup 
  visible="{{visible}}"
  position="bottom"
  onClose="handleClose"
>
  <view>Bottom Popup</view>
</ant-popup>
```

### Example: Popup without Mask

```xml
<ant-popup 
  visible="{{visible}}"
  mask="{{false}}"
  onClose="handleClose"
>
  <view>Popup</view>
</ant-popup>
```

### Key Points

- Control visibility with visible prop
- Configure position (top, bottom, left, right, center)
- Show/hide mask
- Handle onClose event
- Customize popup content
