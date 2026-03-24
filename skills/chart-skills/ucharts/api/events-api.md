# Events API

## API Reference

uCharts events API.

### Chart Events

**@complete**
- Parameters: `(chart)`
- Description: Chart render complete event
- `chart`: Chart instance

**@renderComplete**
- Parameters: `(chart)`
- Description: Chart render complete event (alias)

### Event Usage

```vue
<template>
  <qiun-data-chart 
    type="line" 
    :chartData="chartData" 
    :opts="opts"
    @complete="handleComplete"
  />
</template>

<script>
export default {
  methods: {
    handleComplete(chart) {
      console.log('Chart rendered:', chart)
    }
  }
}
</script>
```

### Chart Instance Methods

After chart renders, access chart instance:

```vue
<template>
  <qiun-data-chart 
    ref="chart"
    type="line" 
    :chartData="chartData" 
    :opts="opts"
    @complete="handleComplete"
  />
</template>

<script>
export default {
  methods: {
    handleComplete(chart) {
      // Access chart instance
      this.chartInstance = chart
      
      // Use chart methods
      chart.showTooltip(0, 0)
    }
  }
}
</script>
```

**See also:** `examples/features/chart-events.md` for detailed examples
