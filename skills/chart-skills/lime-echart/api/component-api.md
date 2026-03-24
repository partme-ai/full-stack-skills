# Component API

## 组件 API

`l-echart` 组件的属性和方法。

### Props

#### option
- **类型**: `Object`
- **必填**: 是
- **说明**: ECharts 的配置项对象

```vue
<l-echart :option="chartOption" :echarts="echarts"></l-echart>
```

#### echarts
- **类型**: `Object`
- **必填**: 是
- **说明**: ECharts 实例，通过 `import * as echarts from 'echarts'` 或 `require()` 获取

```vue
<l-echart :option="option" :echarts="echarts"></l-echart>
```

#### initOptions
- **类型**: `Object`
- **必填**: 否
- **默认值**: `{}`
- **说明**: ECharts 初始化选项

```javascript
{
  renderer: 'canvas', // 'canvas' 或 'svg'
  width: 'auto',
  height: 'auto',
  devicePixelRatio: 2
}
```

#### loading
- **类型**: `Boolean`
- **必填**: 否
- **默认值**: `false`
- **说明**: 是否显示加载状态

```vue
<l-echart :loading="isLoading" :option="option" :echarts="echarts"></l-echart>
```

#### loadingOptions
- **类型**: `Object`
- **必填**: 否
- **说明**: 加载状态的配置选项

```javascript
{
  text: '加载中...',
  color: '#409EFF',
  textColor: '#000',
  maskColor: 'rgba(255, 255, 255, 0.8)',
  zlevel: 0
}
```

#### theme
- **类型**: `String`
- **必填**: 否
- **说明**: 主题名称，需要先引入对应的主题文件

```vue
<l-echart :theme="'dark'" :option="option" :echarts="echarts"></l-echart>
```

### Methods

#### getChart()
- **说明**: 获取 ECharts 实例
- **返回**: ECharts 实例对象

```javascript
const chartInstance = this.$refs.chart.getChart()
chartInstance.setOption(newOption)
```

#### resize()
- **说明**: 调整图表尺寸

```javascript
this.$refs.chart.resize()
```

#### setOption(option, notMerge, lazyUpdate)
- **说明**: 设置图表配置项
- **参数**:
  - `option`: 配置项对象
  - `notMerge`: 是否不合并配置，默认 `false`
  - `lazyUpdate`: 是否延迟更新，默认 `false`

```javascript
const chartInstance = this.$refs.chart.getChart()
chartInstance.setOption(newOption, false)
```

### Events

#### @click
- **说明**: 点击事件
- **参数**: 事件对象

```vue
<l-echart @click="handleClick" :option="option" :echarts="echarts"></l-echart>
```

#### @dblclick
- **说明**: 双击事件
- **参数**: 事件对象

#### @mouseover
- **说明**: 鼠标移入事件
- **参数**: 事件对象

#### @mouseout
- **说明**: 鼠标移出事件
- **参数**: 事件对象

#### @mousemove
- **说明**: 鼠标移动事件
- **参数**: 事件对象

#### @legendselectchanged
- **说明**: 图例选择变化事件
- **参数**: 事件对象

#### @datazoom
- **说明**: 数据缩放事件
- **参数**: 事件对象

#### @brush
- **说明**: 刷选事件
- **参数**: 事件对象

## 使用示例

```vue
<template>
  <view class="chart-container">
    <l-echart 
      ref="chart"
      :option="option"
      :echarts="echarts"
      :loading="loading"
      :init-options="initOptions"
      :theme="theme"
      @click="handleClick"
    ></l-echart>
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
      loading: false,
      theme: 'default',
      initOptions: {
        renderer: 'canvas'
      },
      option: {
        // ECharts 配置项
      }
    }
  },
  methods: {
    handleClick(params) {
      console.log('点击事件', params)
    },
    updateChart() {
      const chartInstance = this.$refs.chart.getChart()
      chartInstance.setOption(newOption)
    }
  }
}
</script>
```
