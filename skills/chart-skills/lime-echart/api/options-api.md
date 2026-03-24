# Options API

## 配置项 API

ECharts 的配置项参考，详细文档请参考 [ECharts 官方文档](https://echarts.apache.org/zh/option.html)。

### 基础配置

#### title
标题组件。

```javascript
title: {
  show: true,
  text: '图表标题',
  link: 'https://example.com',
  target: 'blank',
  textStyle: {
    color: '#333',
    fontSize: 18
  },
  left: 'center',
  top: 'top'
}
```

#### tooltip
提示框组件。

```javascript
tooltip: {
  trigger: 'item', // 'item' | 'axis' | 'none'
  formatter: '{a} <br/>{b}: {c} ({d}%)',
  axisPointer: {
    type: 'line' // 'line' | 'shadow' | 'none' | 'cross'
  }
}
```

#### legend
图例组件。

```javascript
legend: {
  show: true,
  type: 'plain', // 'plain' | 'scroll'
  orient: 'horizontal', // 'horizontal' | 'vertical'
  left: 'center',
  top: 'top',
  data: ['系列1', '系列2']
}
```

#### grid
直角坐标系内绘图网格。

```javascript
grid: {
  show: true,
  left: '3%',
  right: '4%',
  bottom: '3%',
  containLabel: true
}
```

### 坐标轴

#### xAxis
X 轴配置。

```javascript
xAxis: {
  type: 'category', // 'category' | 'value' | 'time' | 'log'
  data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  axisLabel: {
    show: true,
    rotate: 0
  },
  axisLine: {
    show: true,
    lineStyle: {
      color: '#333'
    }
  }
}
```

#### yAxis
Y 轴配置。

```javascript
yAxis: {
  type: 'value',
  axisLabel: {
    formatter: '{value} 元'
  },
  splitLine: {
    show: true,
    lineStyle: {
      type: 'dashed'
    }
  }
}
```

### 系列

#### series
系列列表。

```javascript
series: [
  {
    name: '系列名称',
    type: 'bar', // 'line' | 'bar' | 'pie' | 'scatter' | ...
    data: [120, 200, 150, 80, 70, 110, 130],
    itemStyle: {
      color: '#409EFF'
    },
    label: {
      show: true,
      position: 'top'
    }
  }
]
```

### 数据缩放

#### dataZoom
数据缩放组件。

```javascript
dataZoom: [
  {
    type: 'slider',
    start: 0,
    end: 100,
    xAxisIndex: 0
  },
  {
    type: 'inside',
    start: 0,
    end: 100
  }
]
```

### 视觉映射

#### visualMap
视觉映射组件。

```javascript
visualMap: {
  min: 0,
  max: 100,
  calculable: true,
  inRange: {
    color: ['#50a3ba', '#eac736', '#d94e5d']
  }
}
```

### 工具箱

#### toolbox
工具箱组件。

```javascript
toolbox: {
  show: true,
  feature: {
    saveAsImage: {
      show: true
    },
    dataView: {
      show: true,
      readOnly: false
    },
    restore: {
      show: true
    },
    dataZoom: {
      show: true
    }
  }
}
```

### 时间轴

#### timeline
时间轴组件。

```javascript
timeline: {
  axisType: 'time',
  currentIndex: 0,
  autoPlay: true,
  playInterval: 2000,
  data: ['2024-01-01', '2024-01-02', '2024-01-03']
}
```

### 图形元素

#### graphic
图形元素组件。

```javascript
graphic: [
  {
    type: 'text',
    left: 'center',
    top: 'middle',
    style: {
      text: '文字',
      fontSize: 30,
      fill: '#333'
    }
  }
]
```

### 其他配置

#### color
调色盘颜色列表。

```javascript
color: ['#409EFF', '#67C23A', '#E6A23C', '#F56C6C', '#909399']
```

#### backgroundColor
背景色。

```javascript
backgroundColor: '#fff'
```

#### textStyle
全局字体样式。

```javascript
textStyle: {
  fontFamily: 'Arial, Verdana, sans-serif',
  fontSize: 12,
  color: '#333'
}
```

#### animation
动画配置。

```javascript
animation: true,
animationDuration: 1000,
animationEasing: 'cubicOut'
```

## 完整配置示例

```javascript
{
  title: {
    text: '图表标题',
    left: 'center'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['系列1', '系列2'],
    top: '10%'
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      name: '系列1',
      type: 'bar',
      data: [120, 200, 150, 80, 70, 110, 130]
    },
    {
      name: '系列2',
      type: 'line',
      data: [220, 182, 191, 234, 290, 330, 310]
    }
  ]
}
```

## 参考文档

更多详细的配置项说明，请参考：
- [ECharts 配置项手册](https://echarts.apache.org/zh/option.html)
- [ECharts API 文档](https://echarts.apache.org/zh/api.html)
