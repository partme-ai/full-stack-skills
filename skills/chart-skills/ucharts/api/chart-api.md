# Chart Component API

## API Reference

uCharts chart component props, events, and methods.

### Props

**type**
- Type: `String`
- Required: `true`
- Description: Chart type (line, column, area, pie, ring, radar, funnel, gauge, candle, mix)

**chartData**
- Type: `Object`
- Required: `true`
- Description: Chart data object

**opts**
- Type: `Object`
- Default: `{}`
- Description: Chart options object

**canvasId**
- Type: `String`
- Description: Canvas ID (auto-generated if not provided)

**canvas2d**
- Type: `Boolean`
- Default: `false`
- Description: Use canvas2d mode

**ontouch**
- Type: `Boolean`
- Default: `true`
- Description: Enable touch events

### Events

**@complete**
- Parameters: `(chart)`
- Description: Chart render complete event

**@renderComplete**
- Parameters: `(chart)`
- Description: Chart render complete event (alias)

### Methods

Access chart methods via component ref:

```vue
<template>
  <qiun-data-chart ref="chart" type="line" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  methods: {
    updateChart() {
      this.$refs.chart.updateData({
        categories: ['New', 'Data'],
        series: [{ name: 'Test', data: [1, 2] }]
      })
    }
  }
}
</script>
```

**See also:** `examples/charts/` for detailed chart examples
