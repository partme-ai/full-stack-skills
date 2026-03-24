# Configuration

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates how to configure uCharts.

### Key Concepts

- Options configuration
- Chart appearance
- Chart behavior
- Customization

### Example: Basic Options

```javascript
opts: {
  color: ['#1890FF', '#2FC25B', '#FACC14'],
  padding: [15, 15, 0, 15],
  enableScroll: false,
  legend: {
    show: true
  }
}
```

### Example: Axis Configuration

```javascript
opts: {
  xAxis: {
    disableGrid: false,
    gridType: 'solid',
    gridColor: '#CCCCCC',
    fontSize: 11,
    fontColor: '#666666'
  },
  yAxis: {
    disableGrid: false,
    gridType: 'dash',
    gridColor: '#CCCCCC',
    dashLength: 2,
    fontSize: 11,
    fontColor: '#666666'
  }
}
```

### Example: Legend Configuration

```javascript
opts: {
  legend: {
    show: true,
    position: 'bottom',
    lineHeight: 25,
    itemWidth: 25,
    itemGap: 5,
    fontSize: 11,
    fontColor: '#666666'
  }
}
```

### Example: Tooltip Configuration

```javascript
opts: {
  tooltip: {
    show: true,
    triggerOn: 'mousemove',
    showArrow: true,
    showCategory: true,
    showValue: true,
    fontSize: 11,
    fontColor: '#666666',
    bgColor: '#000000',
    bgOpacity: 0.7
  }
}
```

### Example: Animation Configuration

```javascript
opts: {
  animation: true,
  animationDuration: 1000,
  animationEasing: 'easeOutQuart'
}
```

### Key Points

- Configure chart appearance
- Set axis properties
- Customize legend
- Configure tooltip
- Control animation
