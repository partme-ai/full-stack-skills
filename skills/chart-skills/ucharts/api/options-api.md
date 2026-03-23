# Options API

## API Reference

uCharts options configuration API.

### Common Options

**color**
- Type: `Array<String>`
- Default: `['#1890FF', '#2FC25B', '#FACC14', '#F04864', '#8543E0']`
- Description: Chart color palette

**padding**
- Type: `Array<Number>`
- Default: `[15, 15, 0, 15]`
- Description: Chart padding [top, right, bottom, left]

**dataLabel**
- Type: `Boolean`
- Default: `false`
- Description: Show data labels

**enableScroll**
- Type: `Boolean`
- Default: `false`
- Description: Enable horizontal scroll

**animation**
- Type: `Boolean`
- Default: `true`
- Description: Enable animation

**animationDuration**
- Type: `Number`
- Default: `1000`
- Description: Animation duration (ms)

### Legend Options

**legend.show**
- Type: `Boolean`
- Default: `true`
- Description: Show legend

**legend.position**
- Type: `String`
- Default: `'bottom'`
- Options: `'top' | 'bottom' | 'left' | 'right'`
- Description: Legend position

### Axis Options

**xAxis.disableGrid**
- Type: `Boolean`
- Default: `false`
- Description: Disable X-axis grid

**yAxis.disableGrid**
- Type: `Boolean`
- Default: `false`
- Description: Disable Y-axis grid

**yAxis.gridType**
- Type: `String`
- Default: `'solid'`
- Options: `'solid' | 'dash'`
- Description: Y-axis grid type

### Tooltip Options

**tooltip.show**
- Type: `Boolean`
- Default: `true`
- Description: Show tooltip

**tooltip.triggerOn**
- Type: `String`
- Default: `'mousemove'`
- Options: `'mousemove' | 'click'`
- Description: Tooltip trigger

**See also:** `examples/guide/configuration.md` for detailed examples
