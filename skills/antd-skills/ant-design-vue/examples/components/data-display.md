# Data Display Components (数据展示)

## Table (表格)
A table displays rows of data.

```vue
<template>
  <a-table :dataSource="dataSource" :columns="columns" />
</template>
<script setup lang="ts">
const columns = [
  { title: 'Name', dataIndex: 'name', key: 'name' },
  { title: 'Age', dataIndex: 'age', key: 'age' },
  { title: 'Address', dataIndex: 'address', key: 'address' },
];
const dataSource = [
  { key: '1', name: 'Mike', age: 32, address: '10 Downing Street' },
];
</script>
```

## List (列表)
Simple List.

```vue
<a-list item-layout="horizontal" :data-source="data">
  <template #renderItem="{ item }">
    <a-list-item>
      <a-list-item-meta description="Ant Design, a design language">
        <template #title><a href="https://www.antdv.com/">{{ item.title }}</a></template>
        <template #avatar><a-avatar src="..." /></template>
      </a-list-item-meta>
    </a-list-item>
  </template>
</a-list>
```

## Card (卡片)
Simple rectangular container.

```vue
<a-card title="Default size card" style="width: 300px">
  <template #extra><a href="#">more</a></template>
  <p>card content</p>
</a-card>
```

## Image (图片)
Previewable image.

```vue
<a-image :width="200" src="https://aliyuncdn.antdv.com/logo.png" />
```

## Avatar (头像)
Avatars can be used to represent people or objects.

```vue
<a-avatar size="large">User</a-avatar>
<a-avatar-group>
  <a-avatar src="https://xsgames.co/randomusers/avatar.php?g=pixel&key=1" />
  <a-avatar style="background-color: #f56a00">K</a-avatar>
</a-avatar-group>
```

## Badge (徽标数)
Badge normally appears in proximity to another object or user interface element.

```vue
<a-badge :count="5">
  <a-avatar shape="square" size="large" />
</a-badge>
<a-badge dot>
  <NotificationOutlined />
</a-badge>
```

## Calendar (日历)
Container for displaying data in calendar form.

```vue
<a-calendar v-model:value="value" @panelChange="onPanelChange" />
```

## Carousel (走马灯)
A carousel component for displaying multiple images or cards.

```vue
<a-carousel autoplay>
  <div><h3>1</h3></div>
  <div><h3>2</h3></div>
  <div><h3>3</h3></div>
  <div><h3>4</h3></div>
</a-carousel>
```

## Collapse (折叠面板)
A content area which can be collapsed and expanded.

```vue
<a-collapse v-model:activeKey="activeKey">
  <a-collapse-panel key="1" header="This is panel header 1">
    <p>{{ text }}</p>
  </a-collapse-panel>
</a-collapse>
```

## Descriptions (描述列表)
Display multiple read-only fields in groups.

```vue
<a-descriptions title="User Info">
  <a-descriptions-item label="UserName">Zhou Maomao</a-descriptions-item>
  <a-descriptions-item label="Telephone">1810000000</a-descriptions-item>
  <a-descriptions-item label="Live">Hangzhou, Zhejiang</a-descriptions-item>
</a-descriptions>
```

## Empty (空状态)
Empty state placeholder.

```vue
<a-empty />
<a-empty description="No Data" />
```

## Popover (气泡卡片)
The floating card popped by clicking or hovering.

```vue
<a-popover title="Title">
  <template #content>
    <p>Content</p>
  </template>
  <a-button type="primary">Hover me</a-button>
</a-popover>
```

## QRCode (二维码)
QRCode component.

```vue
<a-qrcode value="https://www.antdv.com" />
```

## Segmented (分段控制器)
Segmented Controls.

```vue
<a-segmented v-model:value="value" :options="['Daily', 'Weekly', 'Monthly']" />
```

## Statistic (统计数值)
Display statistic numbers.

```vue
<a-statistic title="Active Users" :value="112893" />
<a-statistic-countdown title="Countdown" :value="deadline" format="HH:mm:ss" />
```

## Tabs (标签页)
Tabs make it easy to switch between different views.

```vue
<a-tabs v-model:activeKey="activeKey">
  <a-tab-pane key="1" tab="Tab 1">Content of Tab Pane 1</a-tab-pane>
  <a-tab-pane key="2" tab="Tab 2" force-render>Content of Tab Pane 2</a-tab-pane>
  <a-tab-pane key="3" tab="Tab 3">Content of Tab Pane 3</a-tab-pane>
</a-tabs>
```

## Tag (标签)
Tag for categorizing or markup.

```vue
<a-tag color="success">success</a-tag>
<a-tag color="processing">processing</a-tag>
<a-tag color="error">error</a-tag>
```

## Timeline (时间轴)
Vertical display timeline.

```vue
<a-timeline>
  <a-timeline-item>Create a services site 2015-09-01</a-timeline-item>
  <a-timeline-item>Solve initial network problems 2015-09-01</a-timeline-item>
</a-timeline>
```

## Tooltip (文字提示)
Simple text pop-up tip.

```vue
<a-tooltip title="prompt text">
  <span>Tooltip will show on mouse enter.</span>
</a-tooltip>
```

## Tour (漫游式引导)
A guide to introduce the application's functions.

```vue
<a-tour :open="open" :steps="steps" @close="handleClose" />
```

## Tree (树形控件)
A hierarchical list structure component.

```vue
<a-tree
  v-model:expandedKeys="expandedKeys"
  v-model:selectedKeys="selectedKeys"
  v-model:checkedKeys="checkedKeys"
  checkable
  :tree-data="treeData"
/>
```
