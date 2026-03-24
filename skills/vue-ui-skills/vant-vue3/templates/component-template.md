# Component Template | 组件模板

**使用时机**：

- 用户要基于 Vant 快速搭一个新组件
- 已知要用 Vant 组件，但还没有明确的页面骨架
- 需要从通用结构开始，再替换成 Button / Cell / Form / Popup 等具体组件

**关联文件**：

- `api/components.md`
- `examples/components/button.md`
- `examples/components/cell.md`
- `examples/components/form.md`

## Basic Component Usage

```vue
<template>
  <van-component-name
    prop1="value1"
    prop2="value2"
    @event="handleEvent"
  />
</template>

<script setup>
import { ComponentName as VanComponentName } from 'vant'

const handleEvent = () => {
  console.log('Event handled')
}
</script>
```

## Component with v-model

```vue
<template>
  <van-field
    v-model="value"
    placeholder="Enter text"
  />
</template>

<script setup>
import { ref } from 'vue'
import { Field as VanField } from 'vant'

const value = ref('')
</script>
```

## Component in Form

```vue
<template>
  <van-form @submit="onSubmit">
    <van-field
      v-model="form.field"
      name="field"
      label="Field"
      :rules="[{ required: true, message: 'Please enter field' }]"
    />
    <van-button type="primary" native-type="submit">Submit</van-button>
  </van-form>
</template>

<script setup>
import { ref } from 'vue'
import { Form as VanForm, Field as VanField, Button as VanButton } from 'vant'

const form = ref({
  field: ''
})

const onSubmit = (values) => {
  console.log('Form submitted:', values)
}
</script>
```

## Usage notes

- 优先替换 `ComponentName` 为当前真实需要的 Vant 组件
- 如果需要校验、提交、重置，优先参考 `examples/components/form.md`
- 如果需要交互反馈，配合 `showToast()` 或 `showDialog()`
- 如果需要全局主题变量，配合 `api/config-provider.md`
