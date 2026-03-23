# Props and Events

## API Reference

Common props and events in Ant Design Mini components.

### Common Props

#### className

**Type:** `string`

Custom CSS class name.

#### style

**Type:** `string | object`

Custom inline style.

#### disabled

**Type:** `boolean`

**Default:** `false`

Whether component is disabled.

### Common Events

#### onTap / bindtap

**Type:** `Function`

Tap/click event handler.

**Platform Differences:**
- Alipay: `onTap`
- WeChat: `bindtap`

**Example:**
```xml
<!-- Alipay -->
<ant-button onTap="handleTap">Button</ant-button>

<!-- WeChat -->
<ant-button bindtap="handleTap">Button</ant-button>
```

#### onChange / bindchange

**Type:** `Function`

Change event handler.

**Platform Differences:**
- Alipay: `onChange`
- WeChat: `bindchange`

**Example:**
```xml
<!-- Alipay -->
<ant-input onChange="handleChange" />

<!-- WeChat -->
<ant-input bindchange="handleChange" />
```

### Event Object

Event handlers receive an event object:

```javascript
handleEvent(e) {
  // e.detail.value - Value from component
  // e.currentTarget - Current target element
  // e.currentTarget.dataset - Data attributes
}
```

### Platform Compatibility

**Event Naming:**
- Alipay uses `on*` prefix (onTap, onChange, onInput)
- WeChat uses `bind*` prefix (bindtap, bindchange, bindinput)

**See also:** `examples/components/` for component-specific examples
