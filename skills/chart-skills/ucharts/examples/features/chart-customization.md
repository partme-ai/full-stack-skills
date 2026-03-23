# Chart Customization

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example demonstrates chart customization in uCharts.

### Key Concepts

- Appearance customization
- Color customization
- Style customization
- Theme customization

### Example: Color Customization

```javascript
opts: {
  color: ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
}
```

### Example: Padding Customization

```javascript
opts: {
  padding: [20, 20, 10, 20]  // [top, right, bottom, left]
}
```

### Example: Font Customization

```javascript
opts: {
  fontSize: 12,
  fontColor: '#333333',
  xAxis: {
    fontSize: 11,
    fontColor: '#666666'
  },
  yAxis: {
    fontSize: 11,
    fontColor: '#666666'
  }
}
```

### Example: Grid Customization

```javascript
opts: {
  xAxis: {
    gridType: 'solid',
    gridColor: '#E5E5E5'
  },
  yAxis: {
    gridType: 'dash',
    gridColor: '#E5E5E5',
    dashLength: 4
  }
}
```

### Example: Line Chart Customization

```javascript
opts: {
  extra: {
    line: {
      type: 'curve',        // 'straight' | 'curve'
      width: 3,
      activeType: 'hollow', // 'solid' | 'hollow'
      activeWidth: 4
    }
  }
}
```

### Example: Column Chart Customization

```javascript
opts: {
  extra: {
    column: {
      type: 'group',        // 'group' | 'stack'
      width: 30,
      activeWidth: 40,
      columnGap: 5
    }
  }
}
```

### Key Points

- Customize colors
- Adjust padding
- Configure fonts
- Customize grids
- Style chart elements
