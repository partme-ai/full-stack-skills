# Methods API

## 方法 API

通过 `getChart()` 获取的 ECharts 实例支持的方法。

### setOption(option, notMerge, lazyUpdate)

设置图表配置项。

**参数**:
- `option`: 配置项对象
- `notMerge`: 是否不合并配置，默认 `false`
- `lazyUpdate`: 是否延迟更新，默认 `false`

```javascript
const chartInstance = this.$refs.chart.getChart()
chartInstance.setOption({
  series: [{
    data: [120, 200, 150]
  }]
}, false) // false 表示合并配置
```

### getOption()

获取当前配置项。

```javascript
const chartInstance = this.$refs.chart.getChart()
const option = chartInstance.getOption()
```

### resize(opts)

调整图表尺寸。

**参数**:
- `opts`: 可选的尺寸配置对象

```javascript
this.$refs.chart.resize()
// 或
const chartInstance = this.$refs.chart.getChart()
chartInstance.resize({
  width: 800,
  height: 600
})
```

### dispatchAction(payload)

触发图表行为。

```javascript
const chartInstance = this.$refs.chart.getChart()
// 高亮数据项
chartInstance.dispatchAction({
  type: 'highlight',
  seriesIndex: 0,
  dataIndex: 2
})
```

### on(eventName, handler, context)

绑定事件。

```javascript
const chartInstance = this.$refs.chart.getChart()
chartInstance.on('click', (params) => {
  console.log('点击事件', params)
})
```

### off(eventName, handler)

解绑事件。

```javascript
const chartInstance = this.$refs.chart.getChart()
chartInstance.off('click', handler)
```

### getDom()

获取图表容器 DOM 元素。

```javascript
const chartInstance = this.$refs.chart.getChart()
const dom = chartInstance.getDom()
```

### getWidth()

获取图表宽度。

```javascript
const chartInstance = this.$refs.chart.getChart()
const width = chartInstance.getWidth()
```

### getHeight()

获取图表高度。

```javascript
const chartInstance = this.$refs.chart.getChart()
const height = chartInstance.getHeight()
```

### getRenderedWidth()

获取渲染后的宽度。

```javascript
const chartInstance = this.$refs.chart.getChart()
const width = chartInstance.getRenderedWidth()
```

### getRenderedHeight()

获取渲染后的高度。

```javascript
const chartInstance = this.$refs.chart.getChart()
const height = chartInstance.getRenderedHeight()
```

### convertToPixel(finder, value)

将数据坐标转换为像素坐标。

```javascript
const chartInstance = this.$refs.chart.getChart()
const pixel = chartInstance.convertToPixel('grid', [100, 200])
```

### convertFromPixel(finder, pixel)

将像素坐标转换为数据坐标。

```javascript
const chartInstance = this.$refs.chart.getChart()
const data = chartInstance.convertFromPixel('grid', [100, 200])
```

### containPixel(finder, pixel)

判断给定的点是否在指定的坐标系或系列上。

```javascript
const chartInstance = this.$refs.chart.getChart()
const isContain = chartInstance.containPixel('grid', [100, 200])
```

### showLoading(type, opts)

显示加载动画。

```javascript
const chartInstance = this.$refs.chart.getChart()
chartInstance.showLoading('default', {
  text: '加载中...',
  color: '#409EFF'
})
```

### hideLoading()

隐藏加载动画。

```javascript
const chartInstance = this.$refs.chart.getChart()
chartInstance.hideLoading()
```

### getDataURL(opts)

导出图表为图片。

```javascript
const chartInstance = this.$refs.chart.getChart()
const dataURL = chartInstance.getDataURL({
  type: 'png',
  pixelRatio: 2,
  backgroundColor: '#fff'
})
```

### getConnectedDataURL(opts)

导出多个关联的图表为图片。

```javascript
const chartInstance = this.$refs.chart.getChart()
const dataURL = chartInstance.getConnectedDataURL({
  type: 'png',
  pixelRatio: 2
})
```

### appendData(opts)

增量添加数据。

```javascript
const chartInstance = this.$refs.chart.getChart()
chartInstance.appendData({
  seriesIndex: 0,
  data: [120, 200, 150]
})
```

### clear()

清空当前实例，会移除实例中所有的组件和图表。

```javascript
const chartInstance = this.$refs.chart.getChart()
chartInstance.clear()
```

### dispose()

销毁实例，销毁后实例无法再被使用。

```javascript
const chartInstance = this.$refs.chart.getChart()
chartInstance.dispose()
```

## 使用示例

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chart" :option="option" :echarts="echarts"></l-echart>
    <button @click="exportChart">导出图片</button>
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
  methods: {
    exportChart() {
      const chartInstance = this.$refs.chart.getChart()
      const dataURL = chartInstance.getDataURL({
        type: 'png',
        pixelRatio: 2
      })
      // 保存图片
      uni.saveFile({
        tempFilePath: dataURL,
        success: (res) => {
          console.log('保存成功', res.savedFilePath)
        }
      })
    }
  }
}
</script>
```
