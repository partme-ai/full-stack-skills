# Column Chart

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates the Column chart in uCharts.

### Key Concepts

- Column chart setup
- Data format
- Column configuration
- Multiple series

### Example: Basic Column Chart

```vue
<template>
  <qiun-data-chart type="column" :chartData="chartData" :opts="opts" />
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
  <qiun-data-chart type="column" :chartData="chartData" :opts="opts" />
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

### Example: Column Configuration

```javascript
opts: {
  color: ['#1890FF'],
  padding: [15, 15, 0, 15],
  dataLabel: true,
  enableScroll: false,
  legend: {
    show: true
  },
  xAxis: {
    disableGrid: false
  },
  yAxis: {
    gridType: 'dash',
    dashLength: 2
  },
  extra: {
    column: {
      type: 'group',
      width: 30,
      activeWidth: 40
    }
  }
}
```

### Key Points

- Use type="column" for column chart
- Provide categories and series data
- Configure column style in extra.column
- Support multiple series
- Customize appearance with opts
