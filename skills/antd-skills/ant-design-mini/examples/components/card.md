# Card Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Card component in Ant Design Mini.

### Key Concepts

- Card content
- Card header
- Card actions
- Card styling

### Example: Basic Card

```xml
<ant-card title="Card Title">
  <view>Card Content</view>
</ant-card>
```

### Example: Card with Actions

```xml
<ant-card 
  title="Card Title"
  extra="Extra"
>
  <view>Card Content</view>
  <view slot="actions">
    <ant-button size="small">Action</ant-button>
  </view>
</ant-card>
```

### Example: Card with Image

```xml
<ant-card>
  <image 
    slot="cover"
    src="{{imageUrl}}"
    mode="aspectFit"
  />
  <view>Card Content</view>
</ant-card>
```

### Key Points

- Use title for card title
- Use extra for header extra
- Support cover slot for image
- Support actions slot
- Customize card content
