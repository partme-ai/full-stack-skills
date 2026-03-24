# Cell | 单元格

**官方文档入口**: https://vant-ui.github.io/vant/#/zh-CN
**官方对应章节**: Cell / 单元格


## Instructions

This example demonstrates how to use the Cell component in Vant.

### Key Concepts

- Basic Cell
- Cell with value
- Cell with icon
- Cell with arrow
- Cell with click handler
- Cell groups

### Example: Basic Cell

```vue
<template>
  <van-cell title="Cell Title" />
  <van-cell title="Cell Title" value="Content" />
</template>

<script setup>
import { Cell as VanCell } from 'vant'
</script>
```

### Example: Cell with Icon

```vue
<template>
  <van-cell
    title="Cell Title"
    value="Content"
    icon="location-o"
  />
</template>

<script setup>
import { Cell as VanCell } from 'vant'
</script>
```

### Example: Cell with Arrow

```vue
<template>
  <van-cell title="Cell Title" is-link />
  <van-cell title="Cell Title" is-link arrow-direction="down" />
</template>

<script setup>
import { Cell as VanCell } from 'vant'
</script>
```

### Example: Cell with Click Handler

```vue
<template>
  <van-cell
    title="Cell Title"
    value="Content"
    is-link
    @click="handleClick"
  />
</template>

<script setup>
import { Cell as VanCell, showToast } from 'vant'

const handleClick = () => {
  showToast('Cell clicked')
}
</script>
```

### Example: Cell Groups

```vue
<template>
  <van-cell-group>
    <van-cell title="Cell 1" value="Content 1" />
    <van-cell title="Cell 2" value="Content 2" />
    <van-cell title="Cell 3" value="Content 3" />
  </van-cell-group>
</template>

<script setup>
import { Cell as VanCell, CellGroup as VanCellGroup } from 'vant'
</script>
```

### Key Points

- Use `van-cell` component for cell display
- Use `title` prop for cell title
- Use `value` prop for cell value
- Use `icon` prop for cell icon
- Use `is-link` prop for arrow indicator
- Use `@click` for click handlers
- Use `van-cell-group` to group cells

### Related local files

- API summary: `api/components.md`
- Nearby component pattern: `examples/components/button.md`
