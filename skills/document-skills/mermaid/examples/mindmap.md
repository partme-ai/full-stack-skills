## Instructions

Mindmaps visualize hierarchical information, showing relationships between concepts in a tree-like structure. A mind map is a diagram used to visually organize information into a hierarchy, showing relationships among pieces of the whole. It is often created around a single concept, drawn as an image in the center of a blank page, to which associated representations of ideas such as images, words and parts of words are added.

**Note**: This is an experimental diagram type. The syntax and properties can change in future releases. The syntax is stable except for the icon integration which is the experimental part.

### Syntax

- Use `mindmap` keyword
- Root: `root((Root Node))` or just `Root` (text at root level)
- Nodes: Defined by indentation (spaces or tabs determine hierarchy)
- Shapes: Similar to flowchart nodes:
  - Square: `id["Label"]`
  - Rounded square: `id("Label")`
  - Circle: `id(("Label"))`
  - Bang: `id))Label((`
  - Cloud: `id))Label(("
  - Hexagon: `id{{"Label"}}`
  - Default: Just text (no shape delimiters)
- Icons: `::icon(fa:fa-icon-name)` (experimental, requires icon fonts)
- Classes: `:::class1 class2` (triple colon followed by CSS classes)
- Markdown strings: Supports **bold** and *italics*, auto-wraps text
- Configuration: `layout: tidy-tree` for alternative layout

Reference: [Mermaid Mindmap Documentation](https://mermaid.js.org/syntax/mindmap.html)

### Example (Basic Mindmap with Icons)

A complete mindmap example with icons:

```mermaid
mindmap
  root((mindmap))
    Origins
      Long history
      ::icon(fa fa-book)
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectiveness<br/>and features
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      Pen and paper
      Mermaid
```

### Example (Basic Syntax)

A simple mindmap with hierarchical structure:

```mermaid
mindmap
    Root
        A
            B
            C
```

### Example (Square Shape)

Use square shape for a node:

```mermaid
mindmap
    id[I am a square]
```

### Example (Rounded Square Shape)

Use rounded square shape for a node:

```mermaid
mindmap
    id(I am a rounded square)
```

### Example (Circle Shape)

Use circle shape for a node:

```mermaid
mindmap
    id((I am a circle))
```

### Example (Bang Shape)

Use bang shape for a node:

```mermaid
mindmap
    id))I am a bang((
```

### Example (Cloud Shape)

Use cloud shape for a node:

```mermaid
mindmap
    id)I am a cloud(
```

### Example (Hexagon Shape)

Use hexagon shape for a node:

```mermaid
mindmap
    id{{I am a hexagon}}
```

### Example (Default Shape)

Default shape (no delimiters):

```mermaid
mindmap
    I am the default shape
```

### Example (With Icons)

Add icons to nodes (requires icon fonts to be loaded):

```mermaid
mindmap
    Root
        A
        ::icon(fa fa-book)
        B(B)
        ::icon(mdi mdi-skull-outline)
```

### Example (With CSS Classes)

Apply CSS classes to style nodes:

```mermaid
mindmap
    Root
        A[A]
        :::urgent large
        B(B)
        C
```

### Example (Unclear Indentation)

Mermaid handles unclear indentation by finding the nearest parent:

```mermaid
mindmap
    Root
        A
            B
          C
```

### Example (Markdown Strings)

Use markdown formatting in labels with automatic text wrapping:

```mermaid
mindmap
    id1["`**Root** with
a second line
Unicode works too: 🤓`"]
      id2["`The dog in **the** hog... a *very long text* that wraps to a new line`"]
      id3[Regular labels still works]
```

### Example (With Configuration - Tidy Tree Layout)

Configure alternative layout using tidy-tree:

```mermaid
---
config:
  layout: tidy-tree
---
mindmap
root((mindmap is a long thing))
  A
  B
  C
  D
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If mindmap diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    Root((Root))
    A[Node A]
    B[Node B]
    C[Node C]
    D[Node D]

    Root --> A
    Root --> B
    A --> C
    A --> D
```
