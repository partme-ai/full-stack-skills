## Instructions

Treemap diagrams display hierarchical data as a set of nested rectangles. Each branch of the tree is represented by a rectangle, which is then tiled with smaller rectangles representing sub-branches. The size of each rectangle is proportional to the value it represents, making it easy to compare different parts of a hierarchy.

**Note**: This is a new diagram type in Mermaid. Its syntax may evolve in future versions.

### Syntax

- Use `treemap-beta` keyword (requires Mermaid v11.0.0+, experimental feature 🔥)
- Section/Parent nodes: `"Section Name"` (quoted text)
- Leaf nodes with values: `"Leaf Name": value` (quoted text followed by colon and value)
- Hierarchy: Created using indentation (spaces or tabs)
- Styling: Nodes can be styled using `:::class` syntax
- Root node: The first node is the root of the tree
- Configuration: `useMaxWidth`, `padding`, `diagramPadding`, `showValues`, `nodeWidth`, `nodeHeight`, `borderWidth`, `valueFontSize`, `labelFontSize`, `valueFormat`

Reference: [Mermaid Treemap Diagram Documentation](https://mermaid.js.org/syntax/treemap.html)

### Example (Basic Treemap)

A simple treemap with categories and items:

```mermaid
treemap-beta
"Category A"
    "Item A1": 10
    "Item A2": 20
"Category B"
    "Item B1": 15
    "Item B2": 25
```

### Example (Hierarchical Treemap)

A treemap with multiple levels of hierarchy:

```mermaid
treemap-beta
"Products"
    "Electronics"
        "Phones": 50
        "Computers": 30
        "Accessories": 20
    "Clothing"
        "Men's": 40
        "Women's": 40
```

### Example (With Styling)

Style nodes using classDef:

```mermaid
treemap-beta
"Section 1"
    "Leaf 1.1": 12
    "Section 1.2":::class1
      "Leaf 1.2.1": 12
"Section 2"
    "Leaf 2.1": 20:::class1
    "Leaf 2.2": 25
    "Leaf 2.3": 12

classDef class1 fill:red,color:blue,stroke:#FFD600;
```

### Example (Using classDef for Styling)

Another example of styling with classDef:

```mermaid
treemap-beta
"Main"
    "A": 20
    "B":::important
        "B1": 10
        "B2": 15
    "C": 5

classDef important fill:#f96,stroke:#333,stroke-width:2px;
```

### Example (With Theme Configuration)

Configure treemap theme:

```mermaid
---
config:
  theme: 'forest'
---
treemap-beta
"Category A"
    "Item A1": 10
    "Item A2": 20
"Category B"
    "Item B1": 15
    "Item B2": 25
```

### Example (With Diagram Padding)

Adjust padding around the treemap:

```mermaid
---
config:
  treemap:
    diagramPadding: 200
---
treemap-beta
"Category A"
    "Item A1": 10
    "Item A2": 20
"Category B"
    "Item B1": 15
    "Item B2": 25
```

### Example (With Currency Formatting)

Format values as currency:

```mermaid
---
config:
  treemap:
    valueFormat: '$0,0'
---
treemap-beta
"Budget"
    "Operations"
        "Salaries": 700000
        "Equipment": 200000
        "Supplies": 100000
    "Marketing"
        "Advertising": 400000
        "Events": 100000
```

### Example (With Percentage Formatting)

Format values as percentages:

```mermaid
---
config:
  treemap:
    valueFormat: '$.1%'
---
treemap-beta
"Market Share"
    "Company A": 0.35
    "Company B": 0.25
    "Company C": 0.15
    "Others": 0.25
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If treemap diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    Root["Sales: 1000"]
    A["Region A: 500"]
    B["Region B: 300"]
    C["Region C: 200"]

    Root --> A
    Root --> B
    Root --> C

    A1["Product A1: 200"]
    A2["Product A2: 150"]
    A3["Product A3: 150"]

    A --> A1
    A --> A2
    A --> A3
```
