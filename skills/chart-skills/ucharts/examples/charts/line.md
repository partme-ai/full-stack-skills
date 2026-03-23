# Line Chart

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates the Line chart in uCharts.

### Key Concepts

- Line chart setup
- Data format
- Line configuration
- Multiple series

### Example: Basic Line Chart

```vue
<template>
  <qiun-data-chart type="line" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        series: [
          {
            name: 'Sales',
            data: [35, 36, 31, 33, 13, 34, 27]
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
  <qiun-data-chart type="line" :chartData="chartData" :opts="opts" />
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

### Example: Line Configuration

```javascript
opts: {
  color: ['#1890FF'],
  padding: [15, 15, 0, 15],
  dataLabel: true,
  dataPointShape: true,
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
    line: {
      type: 'curve',
      width: 2,
      activeType: 'hollow'
    }
  }
}
```

### Key Points

- Use type="line" for line chart
- Provide categories and series data
- Configure line style in extra.line
- Support multiple series
- Customize appearance with opts
