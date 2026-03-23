# Custom Theme

**官方文档**: https://ext.dcloud.net.cn/plugin?id=4899


## 自定义主题

可以通过自定义主题来统一图表的视觉风格。

### 使用内置主题

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chart" :option="option" :echarts="echarts" :theme="theme"></l-echart>
  </view>
</template>

<script>
import * as echarts from 'echarts'
// 引入主题
import 'echarts/theme/dark'
import 'echarts/theme/infographic'
import 'echarts/theme/macarons'
import 'echarts/theme/roma'
import 'echarts/theme/shine'
import 'echarts/theme/vintage'
import lEchart from '@/uni_modules/lime-echart/components/l-echart/l-echart.vue'

export default {
  components: {
    lEchart
  },
  data() {
    return {
      echarts,
      theme: 'dark', // 使用暗色主题
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

### 注册自定义主题

```vue
<template>
  <view class="chart-container">
    <l-echart ref="chart" :option="option" :echarts="echarts" :theme="theme"></l-echart>
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
      theme: 'myTheme',
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
    // 注册自定义主题
    echarts.registerTheme('myTheme', {
      color: [
        '#409EFF',
        '#67C23A',
        '#E6A23C',
        '#F56C6C',
        '#909399'
      ],
      backgroundColor: '#fff',
      textStyle: {
        fontFamily: 'Arial, Verdana, sans-serif'
      },
      title: {
        textStyle: {
          color: '#333'
        }
      },
      line: {
        itemStyle: {
          borderWidth: 2
        },
        lineStyle: {
          width: 3
        },
        symbolSize: 4,
        symbol: 'emptyCircle',
        smooth: false
      },
      radar: {
        itemStyle: {
          borderWidth: 2
        },
        lineStyle: {
          width: 2
        },
        symbolSize: 4,
        symbol: 'emptyCircle',
        smooth: false
      },
      bar: {
        itemStyle: {
          barBorderWidth: 0,
          barBorderColor: '#ccc'
        }
      },
      pie: {
        itemStyle: {
          borderWidth: 0,
          borderColor: '#ccc'
        }
      },
      scatter: {
        itemStyle: {
          borderWidth: 0,
          borderColor: '#ccc'
        }
      },
      boxplot: {
        itemStyle: {
          borderWidth: 0,
          borderColor: '#ccc'
        }
      },
      parallel: {
        itemStyle: {
          borderWidth: 0,
          borderColor: '#ccc'
        }
      },
      sankey: {
        itemStyle: {
          borderWidth: 0,
          borderColor: '#ccc'
        }
      },
      funnel: {
        itemStyle: {
          borderWidth: 0,
          borderColor: '#ccc'
        }
      },
      gauge: {
        itemStyle: {
          borderWidth: 0,
          borderColor: '#ccc'
        }
      },
      candlestick: {
        itemStyle: {
          color: '#e6a0d1',
          color0: 'transparent',
          borderColor: '#d680bc',
          borderColor0: '#8fd3e8',
          borderWidth: 1
        }
      },
      graph: {
        itemStyle: {
          borderWidth: 0,
          borderColor: '#ccc'
        },
        lineStyle: {
          width: 1,
          color: '#aaa'
        },
        symbolSize: 4,
        symbol: 'emptyCircle',
        smooth: false,
        color: [
          '#409EFF',
          '#67C23A',
          '#E6A23C',
          '#F56C6C',
          '#909399'
        ],
        label: {
          color: '#eee'
        }
      },
      map: {
        itemStyle: {
          areaColor: '#eee',
          borderColor: '#444',
          borderWidth: 0.5
        },
        label: {
          color: '#000'
        },
        emphasis: {
          itemStyle: {
            areaColor: 'rgba(255,215,0,0.8)',
            borderColor: '#444',
            borderWidth: 1
          },
          label: {
            color: 'rgb(100,0,0)'
          }
        }
      },
      geo: {
        itemStyle: {
          areaColor: '#eee',
          borderColor: '#444',
          borderWidth: 0.5
        },
        label: {
          color: '#000'
        },
        emphasis: {
          itemStyle: {
            areaColor: 'rgba(255,215,0,0.8)',
            borderColor: '#444',
            borderWidth: 1
          },
          label: {
            color: 'rgb(100,0,0)'
          }
        }
      },
      categoryAxis: {
        axisLine: {
          show: true,
          lineStyle: {
            color: '#333'
          }
        },
        axisTick: {
          show: true,
          lineStyle: {
            color: '#333'
          }
        },
        axisLabel: {
          show: true,
          color: '#333'
        },
        splitLine: {
          show: false,
          lineStyle: {
            color: ['#ccc']
          }
        },
        splitArea: {
          show: false,
          areaStyle: {
            color: ['rgba(250,250,250,0.3)', 'rgba(200,200,200,0.3)']
          }
        }
      },
      valueAxis: {
        axisLine: {
          show: true,
          lineStyle: {
            color: '#333'
          }
        },
        axisTick: {
          show: true,
          lineStyle: {
            color: '#333'
          }
        },
        axisLabel: {
          show: true,
          color: '#333'
        },
        splitLine: {
          show: true,
          lineStyle: {
            color: ['#ccc']
          }
        },
        splitArea: {
          show: false,
          areaStyle: {
            color: ['rgba(250,250,250,0.3)', 'rgba(200,200,200,0.3)']
          }
        }
      },
      logAxis: {
        axisLine: {
          show: true,
          lineStyle: {
            color: '#333'
          }
        },
        axisTick: {
          show: true,
          lineStyle: {
            color: '#333'
          }
        },
        axisLabel: {
          show: true,
          color: '#333'
        },
        splitLine: {
          show: true,
          lineStyle: {
            color: ['#ccc']
          }
        },
        splitArea: {
          show: false,
          areaStyle: {
            color: ['rgba(250,250,250,0.3)', 'rgba(200,200,200,0.3)']
          }
        }
      },
      timeAxis: {
        axisLine: {
          show: true,
          lineStyle: {
            color: '#333'
          }
        },
        axisTick: {
          show: true,
          lineStyle: {
            color: '#333'
          }
        },
        axisLabel: {
          show: true,
          color: '#333'
        },
        splitLine: {
          show: true,
          lineStyle: {
            color: ['#ccc']
          }
        },
        splitArea: {
          show: false,
          areaStyle: {
            color: ['rgba(250,250,250,0.3)', 'rgba(200,200,200,0.3)']
          }
        }
      },
      toolbox: {
        iconStyle: {
          borderColor: '#999'
        },
        emphasis: {
          iconStyle: {
            borderColor: '#666'
          }
        }
      },
      legend: {
        textStyle: {
          color: '#333'
        }
      },
      tooltip: {
        axisPointer: {
          lineStyle: {
            color: '#ccc',
            width: 1
          },
          crossStyle: {
            color: '#ccc',
            width: 1
          }
        }
      },
      timeline: {
        lineStyle: {
          color: '#DAE1F5',
          width: 2
        },
        itemStyle: {
          color: '#A4B1D7',
          borderWidth: 1
        },
        controlStyle: {
          color: '#A4B1D7',
          borderColor: '#A4B1D7',
          borderWidth: 1
        },
        checkpointStyle: {
          color: '#316bf3',
          borderColor: '#fff',
          borderWidth: 2
        },
        label: {
          color: '#A4B1D7'
        },
        emphasis: {
          itemStyle: {
            color: '#FDD805'
          },
          controlStyle: {
            color: '#FDD805',
            borderColor: '#FDD805',
            borderWidth: 1
          },
          label: {
            color: '#FDD805'
          }
        }
      },
      visualMap: {
        color: ['#bf444c', '#d88273', '#f6efa6']
      },
      dataZoom: {
        handleSize: 'undefined%',
        textStyle: {}
      },
      markPoint: {
        label: {
          color: '#eee'
        },
        emphasis: {
          label: {
            color: '#eee'
          }
        }
      }
    })
  }
}
</script>
```

### 在 option 中直接配置样式

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
        color: ['#409EFF', '#67C23A', '#E6A23C'], // 自定义颜色
        textStyle: {
          fontFamily: 'Arial, sans-serif',
          fontSize: 12,
          color: '#333'
        },
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          axisLine: {
            lineStyle: {
              color: '#409EFF'
            }
          }
        },
        yAxis: {
          type: 'value',
          axisLine: {
            lineStyle: {
              color: '#409EFF'
            }
          }
        },
        series: [{
          data: [120, 200, 150, 80, 70, 110, 130],
          type: 'bar',
          itemStyle: {
            color: '#409EFF',
            borderRadius: [4, 4, 0, 0]
          }
        }]
      }
    }
  }
}
</script>
```

## 主题配置说明

主题配置对象包含以下主要部分：

- `color`: 调色盘颜色列表
- `backgroundColor`: 背景色
- `textStyle`: 全局字体样式
- `title`: 标题样式
- `line`: 折线图样式
- `bar`: 柱状图样式
- `pie`: 饼图样式
- `scatter`: 散点图样式
- `categoryAxis`: 类目轴样式
- `valueAxis`: 数值轴样式
- `tooltip`: 提示框样式
- `legend`: 图例样式

## 最佳实践

1. **统一主题**：在应用中统一使用主题，保持视觉一致性
2. **主题切换**：支持明暗主题切换，提升用户体验
3. **自定义颜色**：根据品牌色自定义主题颜色
4. **性能考虑**：主题注册只需一次，避免重复注册
