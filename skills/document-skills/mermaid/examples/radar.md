## Instructions

Radar diagrams are a simple way to plot low-dimensional data in a circular format. They are also known as radar charts, spider charts, star charts, cobweb charts, polar charts, or Kiviat diagrams. This diagram type is particularly useful for developers, data scientists, and engineers who require a clear and concise way to represent data in a circular format. It is commonly used to graphically summarize and compare the performance of multiple entities across multiple dimensions.

### Syntax

- Use `radar-beta` keyword (requires Mermaid v11.6.0+)
- Title: `title Title of the Radar Diagram` or `--- title: "Title" ---` (optional)
- Axis: `axis id1["Label1"]` or `axis id1, id2, id3` (multiple axes in one line)
- Curve: `curve id1["Label1"]{1, 2, 3}` or `curve id1{ axis1: 20, axis2: 30, axis3: 10 }` (key-value pairs)
- Options:
  - `showLegend true/false` - Show or hide legend (default: true)
  - `max value` - Maximum value for scaling (auto-calculated if not provided)
  - `min value` - Minimum value for scaling (default: 0)
  - `graticule circle/polygon` - Type of graticule (default: circle)
  - `ticks number` - Number of concentric circles/polygons (default: 5)
- Configuration: `width`, `height`, `marginTop`, `marginBottom`, `marginLeft`, `marginRight`, `axisScaleFactor`, `axisLabelFactor`, `curveTension`
- Theme variables: `cScale0`, `cScale1`, etc. for curve colors, `radar.axisColor`, `radar.curveOpacity`, etc.

Reference: [Mermaid Radar Diagram Documentation](https://mermaid.js.org/syntax/radar.html)

### Example (Basic Radar Diagram with Configuration)

A radar diagram with title configuration and multiple axes:

```mermaid
---
title: "Grades"
---
radar-beta
  axis m["Math"], s["Science"], e["English"]
  axis h["History"], g["Geography"], a["Art"]
  curve a["Alice"]{85, 90, 80, 70, 75, 90}
  curve b["Bob"]{70, 75, 85, 80, 90, 85}

  max 100
  min 0
```

### Example (Restaurant Comparison with Polygon Graticule)

A radar diagram with polygon graticule and multiple curves:

```mermaid
radar-beta
  title Restaurant Comparison
  axis food["Food Quality"], service["Service"], price["Price"]
  axis ambiance["Ambiance"],

  curve a["Restaurant A"]{4, 3, 2, 4}
  curve b["Restaurant B"]{3, 4, 3, 3}
  curve c["Restaurant C"]{2, 3, 4, 2}
  curve d["Restaurant D"]{2, 2, 4, 3}

  graticule polygon
  max 5
```

### Example (With Configuration and Theme)

Configure radar diagram dimensions, scale factors, and theme variables:

```mermaid
---
config:
  radar:
    axisScaleFactor: 0.25
    curveTension: 0.1
  theme: base
  themeVariables:
    cScale0: "#FF0000"
    cScale1: "#00FF00"
    cScale2: "#0000FF"
    radar:
      curveOpacity: 0
---
radar-beta
  axis A, B, C, D, E
  curve c1{1,2,3,4,5}
  curve c2{5,4,3,2,1}
  curve c3{3,3,3,3,3}
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If radar diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    subgraph Performance["Performance Comparison"]
        A1[Product A: 80]
        A2[Product B: 70]
    end
    subgraph Quality["Quality"]
        B1[Product A: 90]
        B2[Product B: 85]
    end
    subgraph Speed["Speed"]
        C1[Product A: 70]
        C2[Product B: 90]
    end
    subgraph Cost["Cost"]
        D1[Product A: 60]
        D2[Product B: 75]
    end
```
