# Navigation Components (导航)

## Anchor (锚点)
Hyperlinks to scroll on one page.

```vue
<template>
  <a-anchor :items="items" />
</template>
<script setup lang="ts">
const items = [
  {
    key: 'part-1',
    href: '#part-1',
    title: 'Part 1',
  },
  {
    key: 'part-2',
    href: '#part-2',
    title: 'Part 2',
  },
];
</script>
```

## Breadcrumb (面包屑)
Indicates the current page's location within a navigational hierarchy.

```vue
<a-breadcrumb>
  <a-breadcrumb-item>Home</a-breadcrumb-item>
  <a-breadcrumb-item><a href="">Application Center</a></a-breadcrumb-item>
  <a-breadcrumb-item>An Application</a-breadcrumb-item>
</a-breadcrumb>
```

## Dropdown (下拉菜单)
A dropdown list.

```vue
<a-dropdown>
  <a class="ant-dropdown-link" @click.prevent>
    Hover me <DownOutlined />
  </a>
  <template #overlay>
    <a-menu>
      <a-menu-item>
        <a href="javascript:;">1st menu item</a>
      </a-menu-item>
    </a-menu>
  </template>
</a-dropdown>
```

## Menu (导航菜单)
Navigation menu.

```vue
<template>
  <a-menu v-model:selectedKeys="current" mode="horizontal" :items="items" />
</template>
<script setup lang="ts">
import { ref, h } from 'vue';
import { MailOutlined } from '@ant-design/icons-vue';
const current = ref(['mail']);
const items = ref([
  {
    key: 'mail',
    icon: () => h(MailOutlined),
    label: 'Navigation One',
    title: 'Navigation One',
  },
]);
</script>
```

## Pagination (分页)
A long list can be divided into several pages.

```vue
<a-pagination v-model:current="current" :total="50" show-less-items />
```

## Steps (步骤条)
Navigation bar that guides the user through the steps of a task.

```vue
<a-steps :current="1">
  <a-step title="Finished" description="This is a description." />
  <a-step title="In Progress" sub-title="Left 00:00:08" description="This is a description." />
  <a-step title="Waiting" description="This is a description." />
</a-steps>
```
