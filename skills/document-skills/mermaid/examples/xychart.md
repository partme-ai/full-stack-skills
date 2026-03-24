## Instructions

XY charts display data using X and Y axes, supporting bar charts and line charts. The XY chart module is designed to be dynamic and adaptable, with capacity for expansion to include additional chart types in the future.

### Syntax

- Use `xychart` keyword (not `xychart-beta`)
- Orientation: `xychart horizontal` (default is vertical)
- Title: `title "Chart Title"` (quotes needed if title has spaces)
- X-axis:
  - Numeric range: `x-axis title min --> max`
  - Categorical: `x-axis "title" [cat1, "cat2 with space", cat3]`
- Y-axis:
  - `y-axis title min --> max` (numeric range)
  - `y-axis title` (auto-generated range from data)
- Series:
  - `line [values]` - Line chart with numeric values
  - `bar [values]` - Bar chart with numeric values
- Multiple series can be defined
- Configuration: `width`, `height`, `titlePadding`, `titleFontSize`, `showTitle`, `xAxis`, `yAxis`, `chartOrientation`, `plotReservedSpacePercent`, `showDataLabel`
- Theme variables: `backgroundColor`, `titleColor`, `xAxisLabelColor`, `xAxisTitleColor`, `xAxisTickColor`, `xAxisLineColor`, `yAxisLabelColor`, `yAxisTitleColor`, `yAxisTickColor`, `yAxisLineColor`, `plotColorPalette`

Reference: [Mermaid XY Chart Documentation](https://mermaid.js.org/syntax/xyChart.html)

### Example (Simplest)

The simplest example with only chart name and one data set:

```mermaid
xychart
    line [+1.3, .6, 2.4, -.34]
```

### Example (Bar Chart)

A bar chart with categorical x-axis and numeric y-axis:

```mermaid
xychart
    title "Sales Performance"
    x-axis [Jan, Feb, Mar, Apr, May, Jun]
    y-axis "Sales" 0 --> 1000
    bar [500, 600, 750, 800, 950, 1000]
```

### Example (Line Chart)

A line chart with categorical x-axis:

```mermaid
xychart
    title "Revenue Trend"
    x-axis "Month" [Jan, Feb, Mar, Apr, May]
    y-axis "Revenue" 0 --> 5000
    line [1200, 1900, 3000, 5000, 4000]
```

### Example (Multiple Series)

Combine bar and line charts in one diagram:

```mermaid
xychart
    title "Sales Revenue"
    x-axis [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    y-axis "Revenue (in $)" 4000 --> 11000
    bar [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
    line [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
```

### Example (Horizontal Orientation)

Horizontal chart orientation with numeric x-axis:

```mermaid
xychart horizontal
    title "Product Comparison"
    x-axis "Score" 0 --> 100
    y-axis "Products"
    bar [85, 70, 90]
```

### Example (Numeric X-axis Range)

Use numeric range for x-axis:

```mermaid
xychart
    title "Function Plot"
    x-axis "X" 0 --> 10
    y-axis "Y" -5 --> 5
    line [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
```

### Example (With Color Palette)

Set custom colors for lines and bars using plotColorPalette:

```mermaid
---
config:
  themeVariables:
    xyChart:
      plotColorPalette: '#000000, #0000FF, #00FF00, #FF0000'
---
xychart
title "Different Colors in xyChart"
x-axis "categoriesX" ["Category 1", "Category 2", "Category 3", "Category 4"]
y-axis "valuesY" 0 --> 50
%% Black line
line [10,20,30,40]
%% Blue bar
bar [20,30,25,35]
%% Green bar
bar [15,25,20,30]
%% Red line
line [5,15,25,35]
```

### Example (With Configuration and Theme)

Full configuration example with width, height, showDataLabel, and theme variables:

```mermaid
---
config:
  xyChart:
    width: 900
    height: 600
    showDataLabel: true
  themeVariables:
    xyChart:
      titleColor: "#ff0000"
---
xychart
    title "Sales Revenue"
    x-axis [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    y-axis "Revenue (in $)" 4000 --> 11000
    bar [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
    line [5000, 6000, 7500, 8200, 9500, 10500, 11000, 10200, 9200, 8500, 7000, 6000]
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If XY charts are not supported, use this flowchart alternative:

```mermaid
flowchart LR
    Jan[Jan: 500] --> Feb[Feb: 600]
    Feb --> Mar[Mar: 750]
    Mar --> Apr[Apr: 800]
    Apr --> May[May: 950]
    May --> Jun[Jun: 1000]
```
