# Tree | 树形

**官方文档**: https://avuejs.com/


## Instructions

This example demonstrates how to use Avue tree component.

### Key Concepts

- Tree configuration
- Tree data structure
- Tree selection
- Tree events

### Example: Basic Tree

```vue
<template>
  <avue-tree
    :option="option"
    :data="data"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [
        {
          label: 'Node 1',
          children: [
            { label: 'Node 1-1' },
            { label: 'Node 1-2' }
          ]
        },
        {
          label: 'Node 2',
          children: [
            { label: 'Node 2-1' }
          ]
        }
      ],
      option: {
        props: {
          label: 'label',
          children: 'children'
        }
      }
    }
  }
}
</script>
```

### Example: Tree with Selection

```vue
<template>
  <avue-tree
    :option="option"
    :data="data"
    @node-click="handleNodeClick"
  />
</template>

<script>
export default {
  data() {
    return {
      data: [
        {
          label: 'Node 1',
          children: [
            { label: 'Node 1-1' },
            { label: 'Node 1-2' }
          ]
        }
      ],
      option: {
        props: {
          label: 'label',
          children: 'children'
        },
        defaultExpandAll: true,
        showCheckbox: true
      }
    }
  },
  methods: {
    handleNodeClick(data) {
      console.log('Node clicked:', data)
    }
  }
}
</script>
```

### Key Points

- Use avue-tree component
- Configure via option.props
- Use defaultExpandAll for expanded tree
- Use showCheckbox for selection
- Handle @node-click for node events
- Data structure with label and children
