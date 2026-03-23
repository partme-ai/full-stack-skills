# Platform Support

**官方文档**: https://www.ucharts.cn/v2/#/,


## Instructions

This example explains platform support in uCharts.

### Key Concepts

- Supported platforms
- Platform-specific setup
- Platform differences
- Best practices

### Example: Supported Platforms

uCharts supports:
- **uni-app**: Full support
- **WeChat Mini Program**: Full support
- **Alipay Mini Program**: Full support
- **H5**: Full support
- **APP (iOS/Android)**: Full support
- **Other Mini Programs**: Support varies

### Example: uni-app Setup

```vue
<template>
  <qiun-data-chart type="line" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {},
      opts: {}
    }
  }
}
</script>
```

### Example: WeChat Mini Program Setup

```json
// app.json
{
  "usingComponents": {
    "qiun-data-chart": "@qiun/ucharts/components/qiun-data-chart/qiun-data-chart"
  }
}
```

```xml
<!-- page.wxml -->
<qiun-data-chart type="line" chartData="{{chartData}}" opts="{{opts}}" />
```

### Example: H5 Setup

```vue
<template>
  <qiun-data-chart type="line" :chartData="chartData" :opts="opts" />
</template>
```

### Key Points

- Support multiple platforms
- Use same API across platforms
- Platform-specific setup required
- Canvas rendering on all platforms
- Follow platform best practices
