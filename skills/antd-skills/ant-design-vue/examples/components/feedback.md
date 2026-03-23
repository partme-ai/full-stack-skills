# Feedback Components (反馈)

## Modal (对话框)
Modal dialogs.

```vue
<template>
  <a-button type="primary" @click="showModal">Open Modal</a-button>
  <a-modal v-model:open="open" title="Basic Modal" @ok="handleOk">
    <p>Some contents...</p>
  </a-modal>
</template>
<script setup lang="ts">
import { ref } from 'vue';
const open = ref(false);
const showModal = () => { open.value = true; };
const handleOk = e => { open.value = false; };
</script>
```

## Message (全局提示)
Display global messages as feedback in response to user operations.

```vue
<script setup lang="ts">
import { message } from 'ant-design-vue';
const info = () => {
  message.info('This is a normal message');
};
</script>
```

## Notification (通知提醒框)
Display a notification message globally.

```vue
<script setup lang="ts">
import { notification } from 'ant-design-vue';
const openNotification = () => {
  notification.open({
    message: 'Notification Title',
    description: 'This is the content of the notification.',
  });
};
</script>
```

## Spin (加载中)
A spinner for displaying loading state of a page or a section.

```vue
<a-spin />
<a-spin size="large" />
```

## Alert (警告提示)
Alert component for feedback.

```vue
<a-alert message="Success Text" type="success" />
<a-alert message="Info Text" type="info" />
<a-alert message="Warning Text" type="warning" />
<a-alert message="Error Text" type="error" />
```

## Drawer (抽屉)
A panel which slides in from the edge of the screen.

```vue
<a-drawer
  v-model:open="open"
  class="custom-class"
  root-class-name="root-class-name"
  :root-style="{ color: 'blue' }"
  style="color: red"
  title="Basic Drawer"
  placement="right"
  @after-open-change="afterOpenChange"
>
  <p>Some contents...</p>
</a-drawer>
```

## Popconfirm (气泡确认框)
A simple and compact confirmation dialog of an action.

```vue
<a-popconfirm
  title="Are you sure delete this task?"
  ok-text="Yes"
  cancel-text="No"
  @confirm="confirm"
  @cancel="cancel"
>
  <a href="#">Delete</a>
</a-popconfirm>
```

## Progress (进度条)
Display the current progress of an operation flow.

```vue
<a-progress :percent="30" />
<a-progress type="circle" :percent="75" />
```

## Result (结果)
Used to feed back the results of a series of operational tasks.

```vue
<a-result
  status="success"
  title="Successfully Purchased Cloud Server ECS!"
  sub-title="Order number: 2017182818828182881 Cloud server configuration takes 1-5 minutes, please wait."
>
  <template #extra>
    <a-button key="console" type="primary">Go Console</a-button>
    <a-button key="buy">Buy Again</a-button>
  </template>
</a-result>
```

## Skeleton (骨架屏)
Provide a placeholder while waiting for content to load.

```vue
<a-skeleton active />
<a-skeleton avatar :paragraph="{ rows: 4 }" />
```

## Watermark (水印)
Add specific text or patterns to the page.

```vue
<a-watermark content="Ant Design Vue">
  <div style="height: 500px" />
</a-watermark>
```
