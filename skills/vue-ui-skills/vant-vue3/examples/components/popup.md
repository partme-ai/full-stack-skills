# Popup | 弹出层

**官方文档入口**: https://vant-ui.github.io/vant/#/zh-CN
**官方对应章节**: Popup / 弹出层


## Instructions

This example demonstrates how to use the Popup component in Vant.

### Key Concepts

- Basic Popup
- Popup positions (top, bottom, left, right, center)
- Popup with close button
- Popup with round corners
- Popup with overlay

### Example: Basic Popup

```vue
<template>
  <van-button @click="show = true">Show Popup</van-button>
  <van-popup v-model:show="show" position="bottom">
    <div style="padding: 20px;">Popup content</div>
  </van-popup>
</template>

<script setup>
import { ref } from 'vue'
import { Button as VanButton, Popup as VanPopup } from 'vant'

const show = ref(false)
</script>
```

### Example: Popup Positions

```vue
<template>
  <van-button @click="showTop = true">Top</van-button>
  <van-button @click="showBottom = true">Bottom</van-button>
  <van-button @click="showLeft = true">Left</van-button>
  <van-button @click="showRight = true">Right</van-button>
  <van-button @click="showCenter = true">Center</van-button>

  <van-popup v-model:show="showTop" position="top">
    <div style="padding: 20px;">Top popup</div>
  </van-popup>
  <van-popup v-model:show="showBottom" position="bottom">
    <div style="padding: 20px;">Bottom popup</div>
  </van-popup>
  <van-popup v-model:show="showLeft" position="left">
    <div style="padding: 20px;">Left popup</div>
  </van-popup>
  <van-popup v-model:show="showRight" position="right">
    <div style="padding: 20px;">Right popup</div>
  </van-popup>
  <van-popup v-model:show="showCenter" position="center">
    <div style="padding: 20px;">Center popup</div>
  </van-popup>
</template>

<script setup>
import { ref } from 'vue'
import { Button as VanButton, Popup as VanPopup } from 'vant'

const showTop = ref(false)
const showBottom = ref(false)
const showLeft = ref(false)
const showRight = ref(false)
const showCenter = ref(false)
</script>
```

### Example: Popup with Round Corners

```vue
<template>
  <van-button @click="show = true">Show Popup</van-button>
  <van-popup
    v-model:show="show"
    position="bottom"
    round
  >
    <div style="padding: 20px;">Popup with round corners</div>
  </van-popup>
</template>

<script setup>
import { ref } from 'vue'
import { Button as VanButton, Popup as VanPopup } from 'vant'

const show = ref(false)
</script>
```

### Example: Popup with Close Button

```vue
<template>
  <van-button @click="show = true">Show Popup</van-button>
  <van-popup
    v-model:show="show"
    position="bottom"
    closeable
    close-icon-position="top-right"
  >
    <div style="padding: 20px;">Popup with close button</div>
  </van-popup>
</template>

<script setup>
import { ref } from 'vue'
import { Button as VanButton, Popup as VanPopup } from 'vant'

const show = ref(false)
</script>
```

### Key Points

- Use `van-popup` component for popup display
- Use `v-model:show` for popup visibility
- Use `position` prop for popup position (top, bottom, left, right, center)
- Use `round` prop for round corners
- Use `closeable` prop for close button
- Use `close-icon-position` for close button position
- Popup supports overlay and click-to-close

### Related local files

- API summary: `api/components.md`
- Dialog comparison: `examples/components/dialog.md`
