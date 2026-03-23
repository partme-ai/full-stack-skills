# Area Chart

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates the Area chart in uCharts.

### Key Concepts

- Area chart setup
- Data format
- Area configuration
- Multiple series

### Example: Basic Area Chart

```vue
<template>
  <qiun-data-chart type="area" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        series: [
          {
            name: 'Sales',
            data: [35, 36, 31, 33, 13]
          }
        ]
      },
      opts: {}
    }
  }
}
</script>
```

### Example: Multiple Series

```vue
<template>
  <qiun-data-chart type="area" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        series: [
          {
            name: 'Sales',
            data: [35, 36, 31, 33, 13]
          },
          {
            name: 'Orders',
            data: [18, 27, 21, 24, 6]
          }
        ]
      },
      opts: {
        color: ['#1890FF', '#2FC25B']
      }
    }
  }
}
</script>
```

### Example: Area Configuration

```javascript
opts: {
  color: ['#1890FF'],
  padding: [15, 15, 0, 15],
  dataLabel: true,
  enableScroll: false,
  legend: {
    show: true
  },
  extra: {
    area: {
      type: 'curve',
      opacity: 0.2,
      addLine: true,
      width: 2,
      gradient: false
    }
  }
}
```

### Key Points

- Use type="area" for area chart
- Provide categories and series data
- Configure area style in extra.area
- Support multiple series
- Customize appearance with opts
