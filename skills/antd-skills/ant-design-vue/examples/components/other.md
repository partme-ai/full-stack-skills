# Other Components (其他)

## ConfigProvider (全局化配置)
Global configuration context, such as internationalization.

```vue
<a-config-provider :locale="locale">
  <App />
</a-config-provider>
```

## Affix (固钉)
Wrap Affix around another component to make it stick the viewport.

```vue
<a-affix :offset-top="top">
  <a-button type="primary" @click="top += 10">Affix top</a-button>
</a-affix>
```

## App (包裹组件)
Wrap components to provide global context (message/modal/notification).
Recommended in v4 to replace global static methods.

```vue
<template>
  <a-app>
    <MyPage />
  </a-app>
</template>

<!-- In child component -->
<script setup lang="ts">
import { App } from 'ant-design-vue';
const { message, modal, notification } = App.useApp();
const showMessage = () => {
  message.success('Success!');
};
</script>
```

## FloatButton (悬浮按钮)
Floating button, usually for global operations.

```vue
<a-float-button onClick={() => console.log('click')} />
<a-float-button-group trigger="hover" type="primary" :style="{ right: '24px' }">
  <template #icon><CustomerServiceOutlined /></template>
  <a-float-button />
  <a-float-button>
    <template #icon><CommentOutlined /></template>
  </a-float-button>
</a-float-button-group>
```

## BackTop (回到顶部)
Makes it easy to go back to the top of the page.

```vue
<a-back-top />
<!-- Or using FloatButton.BackTop in v4 -->
<a-float-button-back-top />
```
