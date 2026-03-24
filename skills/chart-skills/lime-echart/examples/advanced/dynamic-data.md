# Dynamic Data

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 动态数据更新

在 UniApp/UniAppX 中，图表数据通常需要动态更新。

### 响应式数据更新

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chart" :option="option" :echarts="echarts"></l-echart>
    <button @click="updateData">更新数据</button>
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
    updateData() {
      // 直接修改 option，组件会自动响应
      this.option.series[0].data = [
        Math.random() * 200,
        Math.random() * 200,
        Math.random() * 200,
        Math.random() * 200,
        Math.random() * 200,
        Math.random() * 200,
        Math.random() * 200
      ]
    }
  }
}
</script>
```

### 从接口获取数据

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chart" :option="option" :echarts="echarts" :loading="loading"></l-echart>
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
      loading: true,
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
          type: 'line'
        }]
      }
    }
  },
  onLoad() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      try {
        // 调用接口获取数据
        const res = await uni.request({
          url: 'https://api.example.com/chart-data',
          method: 'GET'
        })
        
        // 更新图表数据
        this.option.xAxis.data = res.data.categories
        this.option.series[0].data = res.data.values
        this.loading = false
      } catch (error) {
        console.error('获取数据失败', error)
        this.loading = false
      }
    }
  }
}
</script>
```

### 定时更新数据

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
      timer: null,
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
          type: 'line'
        }]
      }
    }
  },
  onLoad() {
    // 每5秒更新一次数据
    this.timer = setInterval(() => {
      this.updateData()
    }, 5000)
  },
  onUnload() {
    // 清除定时器
    if (this.timer) {
      clearInterval(this.timer)
    }
  },
  methods: {
    updateData() {
      // 生成随机数据
      const newData = Array.from({ length: 7 }, () => Math.random() * 200)
      this.option.series[0].data = newData
    }
  }
}
</script>
```

### 使用 setOption 方法更新

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chart" :option="option" :echarts="echarts"></l-echart>
    <button @click="updateChart">更新图表</button>
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
    updateChart() {
      // 获取图表实例
      const chartInstance = this.$refs.chart.getChart()
      
      // 使用 setOption 更新，notMerge: false 表示合并配置
      chartInstance.setOption({
        series: [{
          data: [
            Math.random() * 200,
            Math.random() * 200,
            Math.random() * 200,
            Math.random() * 200,
            Math.random() * 200,
            Math.random() * 200,
            Math.random() * 200
          ]
        }]
      }, false) // false 表示合并，true 表示不合并
    }
  }
}
</script>
```

## 注意事项

1. **响应式更新**：直接修改 `option` 对象，组件会自动检测变化并更新图表
2. **性能优化**：大量数据更新时，考虑使用 `setOption` 的 `notMerge` 参数控制合并策略
3. **内存管理**：定时更新时，记得在组件销毁时清除定时器
4. **异步数据**：从接口获取数据时，使用 `loading` 状态提升用户体验
