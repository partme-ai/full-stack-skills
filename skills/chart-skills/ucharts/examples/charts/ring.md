# Ring Chart

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates the Ring chart in uCharts.

### Key Concepts

- Ring chart setup
- Data format
- Ring configuration
- Customization

### Example: Basic Ring Chart

```vue
<template>
  <qiun-data-chart type="ring" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        series: [
          { name: 'A', value: 50 },
          { name: 'B', value: 30 },
          { name: 'C', value: 20 }
        ]
      },
      opts: {}
    }
  }
}
</script>
```

### Example: Ring Configuration

```javascript
opts: {
  color: ['#1890FF', '#2FC25B', '#FACC14'],
  padding: [5, 5, 5, 5],
  dataLabel: true,
  legend: {
    show: true,
    position: 'bottom'
  },
  extra: {
    ring: {
      ringWidth: 30,
      activeOpacity: 0.5,
      activeRadius: 10,
      offsetAngle: 0,
      labelWidth: 15,
      border: true,
      borderWidth: 3,
      borderColor: '#FFFFFF'
    }
  }
}
```

### Key Points

- Use type="ring" for ring chart
- Provide series data with name and value
- Configure ring style in extra.ring
- Support custom colors
- Customize appearance with opts
