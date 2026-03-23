# Candle Chart

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates the Candle chart in uCharts.

### Key Concepts

- Candle chart setup
- Data format
- Candle configuration
- OHLC data

### Example: Basic Candle Chart

```vue
<template>
  <qiun-data-chart type="candle" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        series: [
          {
            name: 'K Line',
            data: [
              [20, 30, 10, 35],  // [open, close, low, high]
              [25, 35, 15, 40],
              [30, 28, 20, 35],
              [28, 32, 25, 38],
              [32, 30, 28, 35]
            ]
          }
        ]
      },
      opts: {}
    }
  }
}
</script>
```

### Example: Candle Configuration

```javascript
opts: {
  color: ['#1890FF', '#2FC25B'],
  padding: [15, 15, 0, 15],
  dataLabel: false,
  enableScroll: false,
  legend: {
    show: true
  },
  extra: {
    candle: {
      type: 'candle',
      barWidth: 8,
      barGap: 2,
      color: {
        up: '#F04864',
        down: '#2FC25B',
        same: '#CCCCCC'
      }
    }
  }
}
```

### Key Points

- Use type="candle" for candle chart
- Provide OHLC data format [open, close, low, high]
- Configure candle style in extra.candle
- Support up/down colors
- Customize appearance with opts
