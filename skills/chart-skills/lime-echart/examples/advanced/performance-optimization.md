# Performance Optimization

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 性能优化

在 UniApp/UniAppX 中使用图表时，需要注意性能优化。

### 按需引入

```javascript
// 按需引入 ECharts 模块，减小打包体积
import * as echarts from 'echarts/core'
import { BarChart, LineChart, PieChart } from 'echarts/charts'
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
} from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'

// 注册必要的组件
echarts.use([
  BarChart,
  LineChart,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  CanvasRenderer
])
```

### 懒加载图表

```vue
<template>
  <view class="chart-container">
    <l-echart 
      v-if="showChart" 
      ref="chart" 
      :option="option" 
      :echarts="echarts"
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
      showChart: false,
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
  onLoad() {
    // 延迟加载图表
    setTimeout(() => {
      this.showChart = true
    }, 100)
  }
}
</script>
```

### 数据采样

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
      rawData: [], // 原始数据
      option: {
        xAxis: {
          type: 'category',
          data: []
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [],
          type: 'line',
          sampling: 'lttb', // 使用 LTTB 算法采样
          large: true, // 启用大数据量优化
          largeThreshold: 2000 // 数据量超过 2000 时启用优化
        }]
      }
    }
  },
  methods: {
    processData(data) {
      // 如果数据量过大，进行采样
      if (data.length > 1000) {
        const step = Math.ceil(data.length / 500)
        return data.filter((_, index) => index % step === 0)
      }
      return data
    }
  }
}
</script>
```

### 禁用动画

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
        animation: false, // 禁用动画
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
  }
}
</script>
```

### 使用 Canvas 渲染

```vue
<template>
  <view class="chart-container">
    <l-echart 
      ref="chart" 
      :option="option" 
      :echarts="echarts"
      :init-options="initOptions"
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
      initOptions: {
        renderer: 'canvas', // 使用 Canvas 渲染，性能更好
        devicePixelRatio: 2 // 根据设备调整
      },
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
  }
}
</script>
```

### 防抖 resize

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
      resizeTimer: null,
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
    uni.onWindowResize(() => {
      // 防抖处理
      if (this.resizeTimer) {
        clearTimeout(this.resizeTimer)
      }
      this.resizeTimer = setTimeout(() => {
        this.$refs.chart.resize()
      }, 300)
    })
  },
  onUnload() {
    if (this.resizeTimer) {
      clearTimeout(this.resizeTimer)
    }
  }
}
</script>
```

## 优化建议

1. **按需引入**：只引入需要的图表类型和组件，减小打包体积
2. **懒加载**：非首屏图表延迟加载
3. **数据采样**：大数据量时使用采样算法
4. **禁用动画**：性能敏感场景禁用动画
5. **使用 Canvas**：优先使用 Canvas 渲染
6. **防抖优化**：resize 等操作使用防抖
7. **内存管理**：及时销毁图表实例，避免内存泄漏
