# Funnel Chart

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates the Funnel chart in uCharts.

### Key Concepts

- Funnel chart setup
- Data format
- Funnel configuration
- Customization

### Example: Basic Funnel Chart

```vue
<template>
  <qiun-data-chart type="funnel" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        series: [
          { name: 'Step 1', value: 100 },
          { name: 'Step 2', value: 80 },
          { name: 'Step 3', value: 60 },
          { name: 'Step 4', value: 40 },
          { name: 'Step 5', value: 20 }
        ]
      },
      opts: {}
    }
  }
}
</script>
```

### Example: Funnel Configuration

```javascript
opts: {
  color: ['#1890FF', '#2FC25B', '#FACC14', '#F04864', '#8543E0'],
  padding: [5, 5, 5, 5],
  dataLabel: true,
  legend: {
    show: true,
    position: 'bottom'
  },
  extra: {
    funnel: {
      activeOpacity: 0.5,
      activeRadius: 5,
      labelOffset: 10,
      labelLine: true
    }
  }
}
```

### Key Points

- Use type="funnel" for funnel chart
- Provide series data with name and value
- Configure funnel style in extra.funnel
- Support custom colors
- Customize appearance with opts
