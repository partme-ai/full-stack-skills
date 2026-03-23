# Gauge Chart

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates the Gauge chart in uCharts.

### Key Concepts

- Gauge chart setup
- Data format
- Gauge configuration
- Customization

### Example: Basic Gauge Chart

```vue
<template>
  <qiun-data-chart type="gauge" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        series: [
          { name: 'Value', value: 75 }
        ]
      },
      opts: {}
    }
  }
}
</script>
```

### Example: Gauge Configuration

```javascript
opts: {
  color: ['#1890FF'],
  padding: [5, 5, 5, 5],
  dataLabel: true,
  extra: {
    gauge: {
      type: 'default',
      startAngle: 0,
      endAngle: 360,
      startNumber: 0,
      endNumber: 100,
      splitLine: 10,
      labelOffset: 5,
      labelShow: true
    }
  }
}
```

### Key Points

- Use type="gauge" for gauge chart
- Provide series data with name and value
- Configure gauge style in extra.gauge
- Support custom ranges
- Customize appearance with opts
