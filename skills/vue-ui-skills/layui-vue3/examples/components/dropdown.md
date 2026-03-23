# Dropdown Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/dropdown


## Instructions

This example demonstrates the Dropdown component in Layui Vue.

### Key Concepts

- Dropdown menu
- Dropdown items
- Dropdown trigger
- Dropdown events

### Example: Basic Dropdown

```vue
<template>
  <lay-dropdown>
    <lay-button>Dropdown</lay-button>
    <template #content>
      <lay-dropdown-item>Option 1</lay-dropdown-item>
      <lay-dropdown-item>Option 2</lay-dropdown-item>
      <lay-dropdown-item>Option 3</lay-dropdown-item>
    </template>
  </lay-dropdown>
</template>

<script setup>
import { LayDropdown, LayDropdownItem, LayButton } from '@layui/layui-vue'
</script>
```

### Example: Dropdown with Click Event

```vue
<template>
  <lay-dropdown>
    <lay-button>Actions</lay-button>
    <template #content>
      <lay-dropdown-item @click="handleClick1">Edit</lay-dropdown-item>
      <lay-dropdown-item @click="handleClick2">Delete</lay-dropdown-item>
    </template>
  </lay-dropdown>
</template>

<script setup>
import { LayDropdown, LayDropdownItem, LayButton } from '@layui/layui-vue'

const handleClick1 = () => {
  console.log('Edit clicked')
}

const handleClick2 = () => {
  console.log('Delete clicked')
}
</script>
```

### Example: Dropdown Trigger

```vue
<template>
  <lay-dropdown trigger="hover">
    <lay-button>Hover Me</lay-button>
    <template #content>
      <lay-dropdown-item>Option 1</lay-dropdown-item>
      <lay-dropdown-item>Option 2</lay-dropdown-item>
    </template>
  </lay-dropdown>
</template>
```

### Key Points

- Use lay-dropdown for container
- Use lay-dropdown-item for menu items
- Support click and hover triggers
- Handle item click events
- Customize dropdown content
