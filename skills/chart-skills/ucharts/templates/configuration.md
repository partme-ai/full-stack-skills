# Configuration Templates

## Basic Options

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

## Axis Configuration

```javascript
opts: {
  xAxis: {
    disableGrid: false,
    gridType: 'solid',
    gridColor: '#CCCCCC'
  },
  yAxis: {
    disableGrid: false,
    gridType: 'dash',
    gridColor: '#CCCCCC',
    dashLength: 2
  }
}
```

## Legend Configuration

```javascript
opts: {
  legend: {
    show: true,
    position: 'bottom',
    lineHeight: 25,
    itemWidth: 25,
    itemGap: 5
  }
}
```

## Tooltip Configuration

```javascript
opts: {
  tooltip: {
    show: true,
    triggerOn: 'mousemove',
    showArrow: true,
    showCategory: true,
    showValue: true
  }
}
```
