---
name: lime-echart
description: "Integrates Apache ECharts into UniApp and UniAppX projects for cross-platform data visualization (H5, mini-programs, native App). Supports line, bar, pie, scatter, radar, gauge, funnel, heatmap, and more chart types. Use when the user needs to create ECharts charts in UniApp/UniAppX or configure interactive data visualizations for mobile and web."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Create ECharts charts (line, bar, pie, scatter, radar, gauge, etc.) in UniApp or UniAppX
- Display data visualizations in H5, mini-programs, or native App
- Handle chart events, dynamic data updates, or custom themes in UniApp
- Optimize chart performance for mobile environments

## How to use this skill

### Workflow

1. **Install** lime-echart - Load `examples/getting-started/installation.md`
2. **Choose chart type** - Match the requirement to the chart type below
3. **Load the example file** - Each chart type has a dedicated example in `examples/charts/`
4. **Customize** - Adjust options, theme, and data binding per the API docs

### Quick-Start Example: Line Chart in UniApp

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chartRef" @bindinit="onInit" />
  </view>
</template>

<script>
import * as echarts from '@nicefan/lime-echart/echarts';

export default {
  methods: {
    onInit(chart) {
      chart.setOption({
        xAxis: { type: 'category', data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] },
        yAxis: { type: 'value' },
        series: [{
          type: 'line',
          data: [120, 200, 150, 80, 270],
          smooth: true,
          lineStyle: { color: '#5470c6' }
        }]
      });
    }
  }
};
</script>

<style>
.chart-container { width: 100%; height: 300px; }
</style>
```

### Chart Type Reference

| Chart | File | Use Case |
|-------|------|----------|
| Line | `examples/charts/line-chart.md` | Trends over time |
| Bar | `examples/charts/bar-chart.md` | Category comparison |
| Pie | `examples/charts/pie-chart.md` | Proportions |
| Scatter | `examples/charts/scatter-chart.md` | Correlation |
| Radar | `examples/charts/radar-chart.md` | Multi-dimension comparison |
| Gauge | `examples/charts/gauge-chart.md` | Single metric display |

### API Reference

- `api/component-api.md` - Component properties and attributes
- `api/methods-api.md` - Chart manipulation methods
- `api/events-api.md` - Event handling (click, hover, zoom)
- `api/options-api.md` - Full ECharts options reference

## Best Practices

1. **Dispose on unmount** - Call `chart.dispose()` in `onUnload` to prevent memory leaks
2. **Lazy load charts** - Initialize charts only when they scroll into view
3. **Test cross-platform** - Verify on H5, WeChat mini-program, and native App
4. **Optimize data volume** - Downsample large datasets before rendering on mobile
5. **Use CSS sizing** - Set chart container dimensions via CSS, not inline styles

## Resources

- **Official Plugin**: https://ext.dcloud.net.cn/plugin?id=4899
- **ECharts Docs**: https://echarts.apache.org/

## Keywords

lime-echart, echarts, uniapp, uniappx, chart, visualization, 图表, 折线图, 柱状图, 饼图, data visualization, mobile chart
