# Responsive Charts

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 响应式图表

图表需要适配不同屏幕尺寸和设备。

### 基础响应式

```vue
<template>
  <view class="chart-container" :style="{ height: chartHeight + 'px' }">
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
      chartHeight: 400,
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
    // 获取系统信息
    const systemInfo = uni.getSystemInfoSync()
    this.chartHeight = systemInfo.windowHeight * 0.4
  },
  onReady() {
    // 监听窗口尺寸变化
    uni.onWindowResize(() => {
      this.$refs.chart.resize()
    })
  }
}
</script>
```

### 使用 rpx 单位

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
    uni.onWindowResize(() => {
      this.$refs.chart.resize()
    })
  }
}
</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 750rpx; /* 使用 rpx 单位 */
}
</style>
```

### 动态调整配置

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
      option: {}
    }
  },
  onLoad() {
    this.initChart()
  },
  onReady() {
    uni.onWindowResize(() => {
      this.$refs.chart.resize()
      // 根据屏幕尺寸调整配置
      this.adjustOption()
    })
  },
  methods: {
    initChart() {
      const systemInfo = uni.getSystemInfoSync()
      const isSmallScreen = systemInfo.windowWidth < 375
      
      this.option = {
        grid: {
          left: isSmallScreen ? '10%' : '3%',
          right: isSmallScreen ? '10%' : '4%',
          bottom: isSmallScreen ? '15%' : '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          axisLabel: {
            fontSize: isSmallScreen ? 10 : 12
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            fontSize: isSmallScreen ? 10 : 12
          }
        },
        series: [{
          data: [120, 200, 150, 80, 70, 110, 130],
          type: 'bar'
        }]
      }
    },
    adjustOption() {
      const systemInfo = uni.getSystemInfoSync()
      const isSmallScreen = systemInfo.windowWidth < 375
      
      this.option.grid.left = isSmallScreen ? '10%' : '3%'
      this.option.grid.right = isSmallScreen ? '10%' : '4%'
      this.option.xAxis.axisLabel.fontSize = isSmallScreen ? 10 : 12
      this.option.yAxis.axisLabel.fontSize = isSmallScreen ? 10 : 12
    }
  }
}
</script>
```

## 最佳实践

1. **使用 rpx 单位**：在小程序中优先使用 rpx 单位，自动适配不同屏幕
2. **监听尺寸变化**：使用 `uni.onWindowResize` 监听窗口尺寸变化
3. **及时调用 resize**：窗口尺寸变化时及时调用图表的 `resize()` 方法
4. **动态调整配置**：根据屏幕尺寸动态调整图表配置，如字体大小、边距等
5. **性能考虑**：避免频繁调用 `resize()`，可以使用防抖优化
