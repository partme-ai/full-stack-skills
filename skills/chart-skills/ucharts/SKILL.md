---
name: ucharts
description: Provides comprehensive guidance for uCharts chart library including chart types, data formats, chart configuration, and platform support. Use when the user asks about uCharts, needs to create charts, configure chart options, or work with uCharts in applications.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Install and set up uCharts in a project
- Create charts in uni-app applications
- Use uCharts in WeChat Mini Program
- Use uCharts in H5 applications
- Configure chart options
- Use different chart types
- Handle chart events
- Customize chart appearance
- Understand uCharts API and methods
- Troubleshoot uCharts issues

## How to use this skill

This skill is organized to match the uCharts official documentation structure (https://www.ucharts.cn/v2/#/, https://www.ucharts.cn/v2/#/guide/index, https://www.ucharts.cn/v2/#/document/index). When working with uCharts:

1. **Identify the topic** from the user's request:
   - Installation/安装 → `examples/guide/installation.md`
   - Quick Start/快速开始 → `examples/guide/quick-start.md`
   - Chart Types/图表类型 → `examples/charts/`
   - Features/功能特性 → `examples/features/`
   - API/API 文档 → `api/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Guide (使用指南)**:
   - `examples/guide/intro.md` - Introduction to uCharts
   - `examples/guide/installation.md` - Installation guide
   - `examples/guide/quick-start.md` - Quick start guide
   - `examples/guide/configuration.md` - Configuration
   - `examples/guide/platform-support.md` - Platform support

   **Charts (图表类型)**:
   - `examples/charts/line.md` - Line chart
   - `examples/charts/column.md` - Column chart
   - `examples/charts/area.md` - Area chart
   - `examples/charts/pie.md` - Pie chart
   - `examples/charts/ring.md` - Ring chart
   - `examples/charts/radar.md` - Radar chart
   - `examples/charts/funnel.md` - Funnel chart
   - `examples/charts/gauge.md` - Gauge chart
   - `examples/charts/candle.md` - Candle chart
   - `examples/charts/mix.md` - Mixed chart

   **Features (功能特性)**:
   - `examples/features/data-format.md` - Data format
   - `examples/features/chart-events.md` - Chart events
   - `examples/features/chart-methods.md` - Chart methods
   - `examples/features/chart-update.md` - Chart update
   - `examples/features/chart-customization.md` - Chart customization

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - uCharts supports multiple platforms (uni-app, WeChat Mini Program, H5, APP)
   - Charts use canvas for rendering
   - Configuration through options object
   - Each example file includes key concepts, code examples, and key points

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/chart-api.md` - Chart component API
   - `api/options-api.md` - Options API
   - `api/data-api.md` - Data API
   - `api/events-api.md` - Events API
   - `api/methods-api.md` - Methods API

5. **Use templates** from the `templates/` directory:
   - `templates/installation.md` - Installation templates
   - `templates/basic-chart.md` - Basic chart templates
   - `templates/configuration.md` - Configuration templates

### 1. Understanding uCharts

uCharts is a high-performance cross-platform charting library that supports uni-app, WeChat Mini Program, H5, APP and more.

**Key Concepts**:
- **Chart Component**: Main chart component
- **Options**: Chart configuration options
- **Data**: Chart data format
- **Events**: Chart events
- **Methods**: Chart methods
- **Platform Support**: Multi-platform compatibility

### 2. Installation

**Using npm**:

```bash
npm install @qiun/ucharts
```

**Using yarn**:

```bash
yarn add @qiun/ucharts
```

**Using pnpm**:

```bash
pnpm add @qiun/ucharts
```

### 3. Basic Setup

```vue
<template>
  <qiun-data-chart type="line" :chartData="chartData" :opts="opts" />
</template>

<script>
export default {
  data() {
    return {
      chartData: {
        categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        series: [
          {
            name: 'Sales',
            data: [35, 36, 31, 33, 13]
          }
        ]
      },
      opts: {}
    }
  }
}
</script>
```


### Doc mapping (one-to-one with official documentation)

- `examples/guide/` or `examples/getting-started/` → https://www.ucharts.cn/v2/#/guide/index
- `examples/` → https://www.ucharts.cn/v2/#/document/index

## Examples and Templates

This skill includes detailed examples organized to match the official documentation structure. All examples are in the `examples/` directory (see mapping above).

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the mapping above
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference templates in `templates/` directory for common scaffolding
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official uCharts API documentation structure (https://www.ucharts.cn/v2/#/document/index):

### Chart Component API (`api/chart-api.md`)
- Chart component props
- Chart component events
- Chart component methods

### Options API (`api/options-api.md`)
- Chart options configuration
- Option properties
- Option methods

### Data API (`api/data-api.md`)
- Data format
- Data structure
- Data transformation

### Events API (`api/events-api.md`)
- Chart events
- Event handlers
- Event parameters

### Methods API (`api/methods-api.md`)
- Chart methods
- Method parameters
- Method return values

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Configure options properly**: Set up chart options correctly
2. **Format data correctly**: Use proper data format
3. **Handle events**: Use chart events for interactions
4. **Use methods**: Leverage chart methods for operations
5. **Optimize performance**: Optimize chart rendering performance
6. **Customize appearance**: Customize chart appearance when needed
7. **Follow platform patterns**: Follow platform-specific best practices

## Resources

- **Official Documentation**: https://www.ucharts.cn/v2/#/
- **Guide**: https://www.ucharts.cn/v2/#/guide/index
- **Documentation**: https://www.ucharts.cn/v2/#/document/index

## Keywords

uCharts, @qiun/ucharts, chart, 图表, 折线图, 柱状图, 饼图, 环形图, 雷达图, 漏斗图, 仪表盘, K线图, 混合图, line chart, column chart, area chart, pie chart, ring chart, radar chart, funnel chart, gauge chart, candle chart, mixed chart, uni-app, WeChat Mini Program, H5, APP, canvas, chart options, chart data, chart events, chart methods
