## Instructions

Block diagrams are an intuitive way to represent complex systems, processes, or architectures visually. They are composed of blocks and connectors, where blocks represent fundamental components or functions, and connectors show relationships or flow between components. Unlike flowcharts, block diagrams give the author full control over where shapes are positioned.

### Syntax

- Use `block` keyword
- Basic blocks: `block BlockName` or just `BlockName`
- Columns: `columns N` to specify number of columns to organize blocks
- Block width: `BlockName:N` where N is the number of columns to span
- Composite blocks: `block:ID ... end` for nested blocks within parent blocks
- Connections: `Block1 --> Block2` or `Block1 --- Block2`
- Labels: `Block1 -- "Label" --> Block2`
- Block shapes: rectangle (default), `("Round")`, `(["Stadium"])`, `[["Subroutine"]]`, `[("Cylindrical")]`, `(("Circle"))`, `{"Diamond"}`, `{{"Hexagon"}}`, `>"Asymmetric"]`, `[/"Parallelogram"/]`, `[\"Trapezoid"\`, `((("Double Circle")))`
- Block arrows: `blockArrowId<["Label"]>(direction)` where direction is `right`, `left`, `up`, `down`, `x`, `y`, or combinations
- Space blocks: `space` or `space:N` for intentional spacing (N is number of columns)
- Styling: `style BlockName fill:#color,stroke:#color,stroke-width:2px`
- Class styling: `classDef className fill:#color` and `class BlockName className`

Reference: [Mermaid Block Diagram Documentation](https://mermaid.js.org/syntax/block.html)

### Example (Simple Block Diagram)

A simple block diagram with three blocks:

```mermaid
block
  a b c
```

### Example (Multi-Column Layout)

Specify the number of columns to organize blocks:

```mermaid
block
  columns 3
  a b c d
```

### Example (Block Spanning Multiple Columns)

Blocks can span multiple columns using `:N` notation:

```mermaid
block
  columns 3
  a["A label"] b:2 c:2 d
```

### Example (Composite Blocks)

Create nested blocks using `block:ID ... end`:

```mermaid
block
    block
      D
    end
    A["A: I am a wide one"]
```

### Example (Composite Blocks with Columns)

Create composite blocks with column configuration:

```mermaid
block
  columns 3
  a:3
  block:group1:2
    columns 2
    h i j k
  end
  g
  block:group2:3
    l m n o p q r
  end
```

### Example (Vertical Stacking)

Stack blocks vertically using single column:

```mermaid
block
  block
    columns 1
    a["A label"] b c d
  end
```

### Example (Block Shapes)

Use different shapes for blocks:

```mermaid
block
    id1("Round")
    id2(["Stadium"])
    id3[["Subroutine"]]
    id4[("Cylindrical")]
    id5(("Circle"))
    id6{"Diamond"}
    id7{{"Hexagon"}}
    id8>"Asymmetric"]
    id9[/"Parallelogram"/]
    id10[\"Trapezoid"\]
    id11((("Double Circle")))
```

### Example (Individual Shape Examples)

Examples of each shape type:

```mermaid
block
    id1("This is the text in the box")
```

```mermaid
block
    id1(["This is the text in the box"])
```

```mermaid
block
    id1[["This is the text in the box"]]
```

```mermaid
block
    id1[("Database")]
```

```mermaid
block
    id1(("This is the text in the circle"))
```

```mermaid
block
    id1>"This is the text in the box"]
```

```mermaid
block
    id1{"This is the text in the box"}
```

```mermaid
block
    id1{{"This is the text in the box"}}
```

```mermaid
block
    id1[/"This is the text in the box"/]
    id2[\"This is the text in the box"\]
```

```mermaid
block
    id1((("This is the text in the circle")))
```

### Example (Block Arrows)

Use block arrows to indicate direction or flow:

```mermaid
block
  blockArrowId<["Label"]>(right)
  blockArrowId2<["Label"]>(left)
  blockArrowId3<["Label"]>(up)
  blockArrowId4<["Label"]>(down)
  blockArrowId5<["Label"]>(x)
  blockArrowId6<["Label"]>(y)
  blockArrowId7<["Label"]>(x, down)
```

### Example (Space Blocks)

Create intentional empty spaces using `space` or `space:N`:

```mermaid
block
  columns 3
  a space b
  c   d   e
```

Or specify column width:

```mermaid
block
  ida space:3 idb idc
```

### Example (Basic Connections)

Connect blocks using arrows:

```mermaid
block
  A space B
  A-->B
```

### Example (Connections with Labels)

Add text to links:

```mermaid
block
  A space:2 B
  A-- "X" -->B
```

### Example (Styling)

Apply styles to individual blocks:

```mermaid
block
  id1 space id2
  id1("Start")-->id2("Stop")
  style id1 fill:#636,stroke:#333,stroke-width:4px
  style id2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
```

### Example (Class Styling)

Define reusable style classes:

```mermaid
block
  A space B
  A-->B
  classDef blue fill:#6e6ce6,stroke:#333,stroke-width:4px;
  class A blue
  style B fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
```

### Example (System Architecture)

A system architecture example with styling:

```mermaid
block
  columns 3
  Frontend blockArrowId6<[" "]>(right) Backend
  space:2 down<[" "]>(down)
  Disk left<[" "]>(left) Database[("Database")]

  classDef front fill:#696,stroke:#333;
  classDef back fill:#969,stroke:#333;
  class Frontend front
  class Backend,Database back
```

### Example (Business Process Flow)

A business process flow with decision points:

```mermaid
block
  columns 3
  Start(("Start")) space:2
  down<[" "]>(down) space:2
  Decision{{"Make Decision"}} right<["Yes"]>(right) Process1["Process A"]
  downAgain<["No"]>(down) space r3<["Done"]>(down)
  Process2["Process B"] r2<["Done"]>(right) End(("End"))

  style Start fill:#969;
  style End fill:#696;
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If block diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    A[Component A]
    B[Component B]
    C[Component C]
    
    A -->|Data| B
    B -->|Result| C
```
