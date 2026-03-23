# Event Handling

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 事件处理

lime-echart 支持 ECharts 的所有事件，可以通过事件监听实现交互功能。

### 基础事件监听

```vue
<template>
  <view class="chart-container">
    <l-echart 
      ref="chart" 
      :option="option" 
      :echarts="echarts"
      @click="handleClick"
      @dblclick="handleDblClick"
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
      option: {
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [120, 200, 150, 80, 70, 110, 130],
          type: 'bar'
        }]
      }
    }
  },
  methods: {
    handleClick(params) {
      console.log('点击事件', params)
      uni.showToast({
        title: `点击了 ${params.name}`,
        icon: 'none'
      })
    },
    handleDblClick(params) {
      console.log('双击事件', params)
    }
  }
}
</script>
```

### 图表事件

```vue
<template>
  <view class="chart-container">
    <l-echart 
      ref="chart" 
      :option="option" 
      :echarts="echarts"
      @legendselectchanged="handleLegendSelect"
      @datazoom="handleDataZoom"
      @brush="handleBrush"
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
      option: {
        legend: {
          data: ['系列1', '系列2']
        },
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        dataZoom: [{
          type: 'slider',
          start: 0,
          end: 100
        }],
        brush: {
          toolbox: ['rect', 'polygon', 'keep', 'clear']
        },
        series: [
          {
            name: '系列1',
            type: 'line',
            data: [120, 200, 150, 80, 70, 110, 130]
          },
          {
            name: '系列2',
            type: 'line',
            data: [220, 182, 191, 234, 290, 330, 310]
          }
        ]
      }
    }
  },
  methods: {
    handleLegendSelect(params) {
      console.log('图例选择变化', params)
    },
    handleDataZoom(params) {
      console.log('数据缩放', params)
    },
    handleBrush(params) {
      console.log('刷选', params)
    }
  }
}
</script>
```

### 鼠标事件

```vue
<template>
  <view class="chart-container">
    <l-echart 
      ref="chart" 
      :option="option" 
      :echarts="echarts"
      @mouseover="handleMouseOver"
      @mouseout="handleMouseOut"
      @mousemove="handleMouseMove"
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
      option: {
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [120, 200, 150, 80, 70, 110, 130],
          type: 'bar'
        }]
      }
    }
  },
  methods: {
    handleMouseOver(params) {
      console.log('鼠标移入', params)
    },
    handleMouseOut(params) {
      console.log('鼠标移出', params)
    },
    handleMouseMove(params) {
      // 鼠标移动事件，注意可能触发频繁
    }
  }
}
</script>
```

### 通过图表实例绑定事件

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
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [120, 200, 150, 80, 70, 110, 130],
          type: 'bar'
        }]
      }
    }
  },
  onReady() {
    // 获取图表实例
    const chartInstance = this.$refs.chart.getChart()
    
    // 绑定事件
    chartInstance.on('click', (params) => {
      console.log('点击事件', params)
      uni.showToast({
        title: `点击了 ${params.name}`,
        icon: 'none'
      })
    })
    
    chartInstance.on('legendselectchanged', (params) => {
      console.log('图例选择变化', params)
    })
  }
}
</script>
```

## 常用事件

- `click`: 点击事件
- `dblclick`: 双击事件
- `mouseover`: 鼠标移入
- `mouseout`: 鼠标移出
- `mousemove`: 鼠标移动
- `legendselectchanged`: 图例选择变化
- `datazoom`: 数据缩放
- `brush`: 刷选
- `selectchanged`: 选择变化

## 事件参数

事件回调函数的参数通常包含：

- `componentType`: 组件类型
- `seriesType`: 系列类型
- `seriesIndex`: 系列索引
- `seriesName`: 系列名称
- `name`: 数据名称
- `dataIndex`: 数据索引
- `data`: 数据值
- `value`: 数值

## 注意事项

1. **事件绑定时机**：在 `onReady` 生命周期中绑定事件，确保图表已初始化
2. **事件解绑**：组件销毁时记得解绑事件，避免内存泄漏
3. **性能考虑**：`mousemove` 事件触发频繁，注意性能影响
4. **小程序兼容**：部分事件在小程序环境可能不支持，需要测试验证
