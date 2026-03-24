# Basic Usage | 基本用法

**官方文档入口**: https://vant-ui.github.io/vant/#/zh-CN
**官方对应章节**: Quickstart / 快速开始


## Instructions

This example demonstrates basic Vant component usage in Vue 3.

### Key Concepts

- Using components
- Component props
- Component events
- Composition API

### Example: Button Component

```vue
<template>
  <van-button type="primary">Primary</van-button>
  <van-button type="success">Success</van-button>
  <van-button type="danger">Danger</van-button>
</template>

<script setup>
import { Button as VanButton } from 'vant'
</script>
```

### Example: Button with Events

```vue
<template>
  <van-button type="primary" @click="handleClick">
    Click Me
  </van-button>
</template>

<script setup>
import { Button as VanButton, showToast } from 'vant'

const handleClick = () => {
  showToast('Button clicked!')
}
</script>
```

### Example: Cell Component

```vue
<template>
  <van-cell title="Cell Title" value="Content" />
  <van-cell title="Cell Title" value="Content" is-link />
</template>

<script setup>
import { Cell as VanCell } from 'vant'
</script>
```

### Example: Multiple Components

```vue
<template>
  <van-card
    num="2"
    price="2.00"
    desc="Description"
    title="Title"
    thumb="https://img.yzcdn.cn/vant/cat.jpeg"
  />
  <van-button type="primary" class="mt-3">Submit</van-button>
</template>

<script setup>
import { Card as VanCard, Button as VanButton } from 'vant'
</script>
```

### Key Points

- Import components from 'vant'
- Use component props to configure behavior
- Use @click for event handling
- Use Composition API with script setup
- Components are optimized for mobile
- Use showToast, showDialog for programmatic APIs
