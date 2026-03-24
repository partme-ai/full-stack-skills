# Methods API

## API Reference

uCharts chart methods API.

### updateData(data)

Update chart data.

**Parameters:**
- `data`: `Object` - New chart data

**Example:**
```javascript
this.$refs.chart.updateData({
  categories: ['New', 'Data'],
  series: [{ name: 'Test', data: [1, 2] }]
})
```

### updateOptions(opts)

Update chart options.

**Parameters:**
- `opts`: `Object` - New chart options

**Example:**
```javascript
this.$refs.chart.updateOptions({
  color: ['#FF0000', '#00FF00']
})
```

### showTooltip(index, seriesIndex)

Show tooltip programmatically.

**Parameters:**
- `index`: `Number` - Data point index
- `seriesIndex`: `Number` - Series index

**Example:**
```javascript
this.$refs.chart.showTooltip(0, 0)
```

### hideTooltip()

Hide tooltip.

**Example:**
```javascript
this.$refs.chart.hideTooltip()
```

### getChartData()

Get current chart data.

**Returns:** Current chart data object

**Example:**
```javascript
const data = this.$refs.chart.getChartData()
console.log(data)
```

**See also:** `examples/features/chart-methods.md` for detailed examples
