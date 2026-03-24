## Instructions

Quadrant charts display items in a 2x2 grid based on two criteria, useful for prioritization and analysis. A quadrant chart is a visual representation of data that is divided into four quadrants. It is used to plot data points on a two-dimensional grid, with one variable represented on the x-axis and another variable represented on the y-axis. The quadrants are determined by dividing the chart into four equal parts based on a set of criteria that is specific to the data being analyzed.

### Syntax

- Use `quadrantChart` keyword
- Title: `title Chart Title` (optional)
- X-axis: `x-axis Left Label --> Right Label` or `x-axis Left Label` (only left)
- Y-axis: `y-axis Bottom Label --> Top Label` or `y-axis Bottom Label` (only bottom)
- Quadrants: `quadrant-1 Label`, `quadrant-2 Label`, `quadrant-3 Label`, `quadrant-4 Label`
  - `quadrant-1`: Top right quadrant
  - `quadrant-2`: Top left quadrant
  - `quadrant-3`: Bottom left quadrant
  - `quadrant-4`: Bottom right quadrant
- Points: `Point Name: [x, y]` where x and y values are in the range 0-1
- Point styling: `Point Name: [x, y] radius: 12, color: #ff3300, stroke-color: #10f0f0, stroke-width: 5px`
- Class styling: `Point Name:::className: [x, y]` with `classDef className color: #109060, radius: 10`
- Configuration: `chartWidth`, `chartHeight`, `titlePadding`, `titleFontSize`, etc.
- Theme variables: `quadrant1Fill`, `quadrant1TextFill`, `quadrantPointFill`, etc.

Reference: [Mermaid Quadrant Chart Documentation](https://mermaid.js.org/syntax/quadrantChart.html)

### Example (Basic Quadrant Chart)

A complete quadrant chart example:

```mermaid
quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    Campaign A: [0.3, 0.6]
    Campaign B: [0.45, 0.23]
    Campaign C: [0.57, 0.69]
    Campaign D: [0.78, 0.34]
    Campaign E: [0.40, 0.34]
    Campaign F: [0.35, 0.78]
```

### Example (With Configuration and Theme)

Configure chart dimensions and theme variables:

```mermaid
---
config:
  quadrantChart:
    chartWidth: 400
    chartHeight: 400
  themeVariables:
    quadrant1TextFill: "ff0000"
---
quadrantChart
  x-axis Urgent --> Not Urgent
  y-axis Not Important --> "Important ❤"
  quadrant-1 Plan
  quadrant-2 Do
  quadrant-3 Delegate
  quadrant-4 Delete
```

### Example (With Point Styling)

Style points directly with radius, color, stroke-color, and stroke-width:

```mermaid
quadrantChart
  title Reach and engagement of campaigns
  x-axis Low Reach --> High Reach
  y-axis Low Engagement --> High Engagement
  quadrant-1 We should expand
  quadrant-2 Need to promote
  quadrant-3 Re-evaluate
  quadrant-4 May be improved
  Campaign A: [0.9, 0.0] radius: 12
  Campaign B:::class1: [0.8, 0.1] color: #ff3300, radius: 10
  Campaign C: [0.7, 0.2] radius: 25, color: #00ff33, stroke-color: #10f0f0
  Campaign D: [0.6, 0.3] radius: 15, stroke-color: #00ff0f, stroke-width: 5px ,color: #ff33f0
  Campaign E:::class2: [0.5, 0.4]
  Campaign F:::class3: [0.4, 0.5] color: #0000ff
  classDef class1 color: #109060
  classDef class2 color: #908342, radius : 10, stroke-color: #310085, stroke-width: 10px
  classDef class3 color: #f00fff, radius : 10
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If quadrant charts are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    subgraph Q1["Quadrant 1<br>High X, High Y"]
        A[Feature A]
    end
    subgraph Q2["Quadrant 2<br>Low X, High Y"]
        B[Feature B]
    end
    subgraph Q3["Quadrant 3<br>Low X, Low Y"]
        C[Feature C]
    end
    subgraph Q4["Quadrant 4<br>High X, Low Y"]
        D[Feature D]
    end
```
