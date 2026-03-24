# Props and Events

## API Reference

Common props and events in Element Plus components.

### Common Props

#### size

**Type:** `'large' | 'default' | 'small'`

Component size.

#### disabled

**Type:** `boolean`

**Default:** `false`

Whether component is disabled.

#### className

**Type:** `string`

Custom CSS class name.

#### style

**Type:** `string | object`

Custom inline style.

### Common Events

#### @click

**Type:** `Function`

Click event handler.

**Example:**
```vue
<el-button @click="handleClick">Button</el-button>
```

#### @change

**Type:** `Function`

Change event handler.

**Example:**
```vue
<el-input v-model="value" @change="handleChange" />
```

#### @focus

**Type:** `Function`

Focus event handler.

**Example:**
```vue
<el-input @focus="handleFocus" />
```

#### @blur

**Type:** `Function`

Blur event handler.

**Example:**
```vue
<el-input @blur="handleBlur" />
```

### Event Object

Event handlers receive an event object:

```javascript
handleEvent(event) {
  // event.target - Target element
  // event.currentTarget - Current target element
  // event.detail - Event detail (component-specific)
}
```

### Component-Specific Events

Different components emit different events:
- **Input**: @input, @change, @focus, @blur
- **Select**: @change, @visible-change
- **Table**: @selection-change, @row-click, @sort-change
- **Form**: @validate

**See also:** `examples/components/` for component-specific examples
