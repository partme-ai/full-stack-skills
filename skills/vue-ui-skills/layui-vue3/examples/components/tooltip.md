# Tooltip Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/tooltip


## Instructions

This example demonstrates the Tooltip component in Layui Vue.

### Key Concepts

- Tooltip placement
- Tooltip content
- Tooltip trigger
- Tooltip styling

### Example: Basic Tooltip

```vue
<template>
  <lay-tooltip content="This is a tooltip">
    <lay-button>Hover Me</lay-button>
  </lay-tooltip>
</template>

<script setup>
import { LayTooltip, LayButton } from '@layui/layui-vue'
</script>
```

### Example: Tooltip Placement

```vue
<template>
  <lay-tooltip content="Tooltip" placement="top">
    <lay-button>Top</lay-button>
  </lay-tooltip>
  <lay-tooltip content="Tooltip" placement="bottom">
    <lay-button>Bottom</lay-button>
  </lay-tooltip>
  <lay-tooltip content="Tooltip" placement="left">
    <lay-button>Left</lay-button>
  </lay-tooltip>
  <lay-tooltip content="Tooltip" placement="right">
    <lay-button>Right</lay-button>
  </lay-tooltip>
</template>
```

### Example: Tooltip Trigger

```vue
<template>
  <lay-tooltip content="Tooltip" trigger="click">
    <lay-button>Click Me</lay-button>
  </lay-tooltip>
</template>
```

### Example: Tooltip with HTML Content

```vue
<template>
  <lay-tooltip>
    <template #content>
      <div>
        <strong>Title</strong>
        <p>Description</p>
      </div>
    </template>
    <lay-button>Hover</lay-button>
  </lay-tooltip>
</template>
```

### Key Points

- Wrap content with lay-tooltip
- Configure placement (top, bottom, left, right)
- Set trigger (hover, click, focus)
- Support HTML content via slot
- Customize tooltip appearance
