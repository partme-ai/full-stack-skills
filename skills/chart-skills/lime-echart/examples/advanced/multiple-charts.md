# Multiple Charts

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 多个图表

在一个页面中展示多个图表。

### 基础多图表布局

```vue
<template>
  <view class="charts-container">
    <view class="chart-item">
      <l-echart ref="chart1" :option="option1" :echarts="echarts"></l-echart>
    </view>
    <view class="chart-item">
      <l-echart ref="chart2" :option="option2" :echarts="echarts"></l-echart>
    </view>
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
      option1: {
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
      },
      option2: {
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [120, 132, 101, 134, 90, 230, 210],
          type: 'line'
        }]
      }
    }
  }
}
</script>

<style scoped>
.charts-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.chart-item {
  width: 100%;
  height: 400px;
}
</style>
```

### 网格布局

```vue
<template>
  <view class="charts-grid">
    <view class="chart-box">
      <l-echart ref="chart1" :option="option1" :echarts="echarts"></l-echart>
    </view>
    <view class="chart-box">
      <l-echart ref="chart2" :option="option2" :echarts="echarts"></l-echart>
    </view>
    <view class="chart-box">
      <l-echart ref="chart3" :option="option3" :echarts="echarts"></l-echart>
    </view>
    <view class="chart-box">
      <l-echart ref="chart4" :option="option4" :echarts="echarts"></l-echart>
    </view>
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
      option1: {
        series: [{
          type: 'pie',
          data: [
            { value: 1048, name: '搜索引擎' },
            { value: 735, name: '直接访问' },
            { value: 580, name: '邮件营销' }
          ]
        }]
      },
      option2: {
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [120, 200, 150, 80, 70],
          type: 'bar'
        }]
      },
      option3: {
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [120, 132, 101, 134, 90],
          type: 'line'
        }]
      },
      option4: {
        radar: {
          indicator: [
            { name: '销售', max: 6500 },
            { name: '管理', max: 16000 },
            { name: '信息技术', max: 30000 }
          ]
        },
        series: [{
          type: 'radar',
          data: [{
            value: [4200, 3000, 20000],
            name: '预算分配'
          }]
        }]
      }
    }
  },
  onReady() {
    // 监听窗口尺寸变化，调整所有图表
    uni.onWindowResize(() => {
      this.$refs.chart1?.resize()
      this.$refs.chart2?.resize()
      this.$refs.chart3?.resize()
      this.$refs.chart4?.resize()
    })
  }
}
</script>

<style scoped>
.charts-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  padding: 20px;
}

.chart-box {
  width: 100%;
  height: 300px;
  background: #fff;
  border-radius: 8px;
  padding: 10px;
}
</style>
```

### 响应式多图表

```vue
<template>
  <view class="charts-responsive">
    <view 
      v-for="(chart, index) in charts" 
      :key="index" 
      class="chart-wrapper"
    >
      <l-echart 
        :ref="`chart${index}`" 
        :option="chart.option" 
        :echarts="echarts"
      ></l-echart>
    </view>
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
      charts: [
        {
          option: {
            xAxis: {
              type: 'category',
              data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
            },
            yAxis: {
              type: 'value'
            },
            series: [{
              data: [120, 200, 150, 80, 70],
              type: 'bar'
            }]
          }
        },
        {
          option: {
            xAxis: {
              type: 'category',
              data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
            },
            yAxis: {
              type: 'value'
            },
            series: [{
              data: [120, 132, 101, 134, 90],
              type: 'line'
            }]
          }
        }
      ]
    }
  },
  onReady() {
    // 响应式调整
    uni.onWindowResize(() => {
      this.charts.forEach((_, index) => {
        const ref = this.$refs[`chart${index}`]
        if (ref && ref[0]) {
          ref[0].resize()
        }
      })
    })
  }
}
</script>

<style scoped>
.charts-responsive {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.chart-wrapper {
  width: 100%;
  height: 400px;
}
</style>
```

## 注意事项

1. **性能优化**：多个图表时注意性能，考虑按需加载
2. **内存管理**：组件销毁时记得清理图表实例
3. **响应式调整**：监听窗口尺寸变化，及时调用 `resize()` 方法
4. **布局适配**：使用 flex 或 grid 布局，适配不同屏幕尺寸
