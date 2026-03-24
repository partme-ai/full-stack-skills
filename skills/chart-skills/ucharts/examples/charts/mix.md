# Mixed Chart

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates the Mixed chart in uCharts.

### Key Concepts

- Mixed chart setup
- Data format
- Multiple chart types
- Configuration

### Example: Basic Mixed Chart

```vue
<template>
  <qiun-data-chart type="mix" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        series: [
          {
            name: 'Line',
            type: 'line',
            data: [35, 36, 31, 33, 13]
          },
          {
            name: 'Column',
            type: 'column',
            data: [18, 27, 21, 24, 6]
          }
        ]
      },
      opts: {}
    }
  }
}
</script>
```

### Example: Mixed Chart Configuration

```javascript
opts: {
  color: ['#1890FF', '#2FC25B'],
  padding: [15, 15, 0, 15],
  dataLabel: true,
  enableScroll: false,
  legend: {
    show: true
  },
  extra: {
    line: {
      type: 'curve',
      width: 2
    },
    column: {
      type: 'group',
      width: 30
    }
  }
}
```

### Example: Multiple Types

```vue
<template>
  <qiun-data-chart type="mix" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        series: [
          {
            name: 'Line',
            type: 'line',
            data: [35, 36, 31, 33, 13]
          },
          {
            name: 'Column',
            type: 'column',
            data: [18, 27, 21, 24, 6]
          },
          {
            name: 'Area',
            type: 'area',
            data: [25, 30, 26, 28, 10]
          }
        ]
      },
      opts: {
        color: ['#1890FF', '#2FC25B', '#FACC14']
      }
    }
  }
}
</script>
```

### Key Points

- Use type="mix" for mixed chart
- Specify type for each series
- Support multiple chart types
- Configure each type separately
- Customize appearance with opts
