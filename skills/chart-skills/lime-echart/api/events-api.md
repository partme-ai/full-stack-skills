# Events API

## 事件 API

lime-echart 支持 ECharts 的所有事件。

### 鼠标事件

#### click
点击事件。

```vue
<l-echart @click="handleClick" :option="option" :echarts="echarts"></l-echart>
```

```javascript
handleClick(params) {
  console.log('点击事件', params)
  // params: { componentType, seriesType, seriesIndex, seriesName, name, dataIndex, data, value, ... }
}
```

#### dblclick
双击事件。

```vue
<l-echart @dblclick="handleDblClick" :option="option" :echarts="echarts"></l-echart>
```

#### mousedown
鼠标按下事件。

```vue
<l-echart @mousedown="handleMouseDown" :option="option" :echarts="echarts"></l-echart>
```

#### mousemove
鼠标移动事件。

```vue
<l-echart @mousemove="handleMouseMove" :option="option" :echarts="echarts"></l-echart>
```

#### mouseup
鼠标抬起事件。

```vue
<l-echart @mouseup="handleMouseUp" :option="option" :echarts="echarts"></l-echart>
```

#### mouseover
鼠标移入事件。

```vue
<l-echart @mouseover="handleMouseOver" :option="option" :echarts="echarts"></l-echart>
```

#### mouseout
鼠标移出事件。

```vue
<l-echart @mouseout="handleMouseOut" :option="option" :echarts="echarts"></l-echart>
```

#### globalout
鼠标移出图表区域事件。

```vue
<l-echart @globalout="handleGlobalOut" :option="option" :echarts="echarts"></l-echart>
```

### 交互事件

#### legendselectchanged
图例选择变化事件。

```vue
<l-echart @legendselectchanged="handleLegendSelect" :option="option" :echarts="echarts"></l-echart>
```

```javascript
handleLegendSelect(params) {
  console.log('图例选择变化', params)
  // params: { type: 'legendselectchanged', name, selected }
}
```

#### legendselected
图例选中事件。

```vue
<l-echart @legendselected="handleLegendSelected" :option="option" :echarts="echarts"></l-echart>
```

#### legendunselected
图例取消选中事件。

```vue
<l-echart @legendunselected="handleLegendUnselected" :option="option" :echarts="echarts"></l-echart>
```

#### datazoom
数据缩放事件。

```vue
<l-echart @datazoom="handleDataZoom" :option="option" :echarts="echarts"></l-echart>
```

```javascript
handleDataZoom(params) {
  console.log('数据缩放', params)
  // params: { type: 'datazoom', start, end, startValue, endValue }
}
```

#### datarangeselected
数据范围选择事件。

```vue
<l-echart @datarangeselected="handleDataRangeSelected" :option="option" :echarts="echarts"></l-echart>
```

#### brush
刷选事件。

```vue
<l-echart @brush="handleBrush" :option="option" :echarts="echarts"></l-echart>
```

```javascript
handleBrush(params) {
  console.log('刷选', params)
  // params: { type: 'brush', areas, isEnd }
}
```

#### brushEnd
刷选结束事件。

```vue
<l-echart @brushEnd="handleBrushEnd" :option="option" :echarts="echarts"></l-echart>
```

### 选择事件

#### selectchanged
选择变化事件。

```vue
<l-echart @selectchanged="handleSelectChanged" :option="option" :echarts="echarts"></l-echart>
```

```javascript
handleSelectChanged(params) {
  console.log('选择变化', params)
  // params: { type: 'selectchanged', fromAction, fromActionPayload, selected }
}
```

### 其他事件

#### finished
渲染完成事件。

```vue
<l-echart @finished="handleFinished" :option="option" :echarts="echarts"></l-echart>
```

#### resize
图表尺寸变化事件。

```vue
<l-echart @resize="handleResize" :option="option" :echarts="echarts"></l-echart>
```

## 事件参数说明

事件回调函数的参数通常包含以下字段：

- `type`: 事件类型
- `componentType`: 组件类型（如 'series', 'xAxis', 'yAxis'）
- `seriesType`: 系列类型（如 'line', 'bar', 'pie'）
- `seriesIndex`: 系列索引
- `seriesName`: 系列名称
- `name`: 数据名称
- `dataIndex`: 数据索引
- `data`: 数据值
- `value`: 数值（可能是单个值或数组）

## 通过图表实例绑定事件

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chart" :option="option" :echarts="echarts"></l-echart>
  </view>
</template>

<script>
import * as echarts from 'echarts'
import lEchart from '@/uni_modules/lime-echart/components/l-echart/l-echart.vue'

export default {
  components: {
    lEchart
  },
  data() {
    return {
      echarts,
      option: {
        // ECharts 配置项
      }
    }
  },
  onReady() {
    const chartInstance = this.$refs.chart.getChart()
    
    // 绑定事件
    chartInstance.on('click', (params) => {
      console.log('点击事件', params)
    })
    
    chartInstance.on('legendselectchanged', (params) => {
      console.log('图例选择变化', params)
    })
  },
  onUnload() {
    // 解绑事件
    const chartInstance = this.$refs.chart.getChart()
    if (chartInstance) {
      chartInstance.off('click')
      chartInstance.off('legendselectchanged')
    }
  }
}
</script>
```

## 注意事项

1. **事件绑定时机**：在 `onReady` 生命周期中绑定事件，确保图表已初始化
2. **事件解绑**：组件销毁时记得解绑事件，避免内存泄漏
3. **性能考虑**：`mousemove` 等事件触发频繁，注意性能影响
4. **小程序兼容**：部分事件在小程序环境可能不支持，需要测试验证
