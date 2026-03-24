# Component API

## API Reference

Ant Design Mini component props, events, and methods.

### Common Props

Most components support:
- `className` - Custom class name
- `style` - Custom style
- `disabled` - Disabled state

### Common Events

Most components emit:
- `onTap` / `bindtap` - Tap event (Alipay/WeChat)
- `onChange` / `bindchange` - Change event

### Button Component

**Props:**
- `type` - Button type (primary, default, text)
- `size` - Button size (large, medium, small)
- `disabled` - Disabled state
- `loading` - Loading state
- `icon` - Icon name

**Events:**
- `onTap` / `bindtap` - Click event

### Input Component

**Props:**
- `value` - Input value
- `placeholder` - Placeholder text
- `type` - Input type (text, number, password)
- `disabled` - Disabled state
- `readonly` - Readonly state
- `maxlength` - Max length
- `allowClear` - Show clear button

**Events:**
- `onInput` / `bindinput` - Input event
- `onFocus` / `bindfocus` - Focus event
- `onBlur` / `bindblur` - Blur event

### Form Component

**Props:**
- `onFinish` - Submit handler
- `onFinishFailed` - Validation failed handler

**Events:**
- `onFinish` - Form submit event
- `onFinishFailed` - Validation failed event

### Modal Component

**Props:**
- `visible` - Modal visibility
- `title` - Modal title
- `onClose` - Close handler
- `onOk` - OK handler
- `onCancel` - Cancel handler

**Events:**
- `onClose` - Close event
- `onOk` - OK event
- `onCancel` - Cancel event

**See also:** `examples/components/` for detailed component examples
