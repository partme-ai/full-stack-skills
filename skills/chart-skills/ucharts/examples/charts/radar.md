# Radar Chart

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates the Radar chart in uCharts.

### Key Concepts

- Radar chart setup
- Data format
- Radar configuration
- Multiple series

### Example: Basic Radar Chart

```vue
<template>
  <qiun-data-chart type="radar" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['A', 'B', 'C', 'D', 'E'],
        series: [
          {
            name: 'Series 1',
            data: [80, 90, 70, 85, 75]
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
  <qiun-data-chart type="radar" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['A', 'B', 'C', 'D', 'E'],
        series: [
          {
            name: 'Series 1',
            data: [80, 90, 70, 85, 75]
          },
          {
            name: 'Series 2',
            data: [60, 70, 80, 65, 70]
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

### Example: Radar Configuration

```javascript
opts: {
  color: ['#1890FF'],
  padding: [15, 15, 0, 15],
  dataLabel: true,
  legend: {
    show: true
  },
  extra: {
    radar: {
      gridType: 'radar',
      gridCount: 5,
      opacity: 0.2,
      labelOffset: 5
    }
  }
}
```

### Key Points

- Use type="radar" for radar chart
- Provide categories and series data
- Configure radar style in extra.radar
- Support multiple series
- Customize appearance with opts
