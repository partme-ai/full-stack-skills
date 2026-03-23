## Instructions

Class diagrams represent the structure of a system by showing classes, their attributes, methods, and relationships. The class diagram is the main building block of object-oriented modeling.

### Syntax

- Use `classDiagram` keyword
- Class definition: `class ClassName` or via relationship `Vehicle <|-- Car`
- Members: `ClassName : +attribute` or `ClassName { +attribute +method() }`
- Visibility: `+` (Public), `-` (Private), `#` (Protected), `~` (Package/Internal)
- Methods: Identified by `()` parentheses
- Return types: `method() ReturnType` (space between `)` and return type)
- Generic types: `ClassName~Type~` (enclosed in `~` tilde)
- Classifiers: `*` (Abstract), `$` (Static)
- Relationships:
  - `<|--` - Inheritance
  - `*--` - Composition
  - `o--` - Aggregation
  - `-->` - Association
  - `--` - Link (Solid)
  - `..>` - Dependency
  - `..|>` - Realization
  - `..` - Link (Dashed)
- Labels: `ClassA --> ClassB : LabelText`
- Cardinality: `"1" ClassA --> "0..1" ClassB : LabelText`
- Annotations: `<<Interface>>`, `<<Abstract>>`, `<<Service>>`, `<<Enumeration>>`
- Interfaces: `ClassA ..|> InterfaceName` or lollipop syntax
- Namespaces: `namespace NamespaceName { Class1 Class2 }`
- Direction: `direction TB|BT|LR|RL` (default: TB)
- Comments: `%% comment` (on separate line)
- Notes: `note for ClassName "note text"`
- Styling: `style ClassName fill:#color,stroke:#color` or `classDef className fill:#color` and `cssClass "ClassName" className` or `ClassName:::className`

Reference: [Mermaid Class Diagram Documentation](https://mermaid.js.org/syntax/classDiagram.html)

### Example (Basic Class Diagram)

A simple class diagram showing classes with members and relationships:

```mermaid
---
title: Animal example
---
classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int sizeInFeet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
```

### Example (Define a class)

There are two ways to define a class: explicitly using `class` keyword or via a relationship:

```mermaid
classDiagram
    class Animal
    Vehicle <|-- Car
```

### Example (Class labels)

Provide a label for a class using square brackets:

```mermaid
classDiagram
    class Animal["Animal with a label"]
    class Car["Car with *! symbols"]
    Animal --> Car
```

### Example (Class labels with backticks)

Use backticks to escape special characters in class names:

```mermaid
classDiagram
    class `Animal Class!`
    class `Car Class`
    `Animal Class!` --> `Car Class`
```

### Example (Defining Members)

Define members using `:` (colon) or `{}` brackets. Methods are identified by `()`:

```mermaid
---
title: Bank example
---
classDiagram
    class BankAccount
    BankAccount : +String owner
    BankAccount : +Bigdecimal balance
    BankAccount : +deposit(amount)
    BankAccount : +withdrawal(amount)
```

Or using brackets:

```mermaid
classDiagram
class BankAccount{
    +String owner
    +BigDecimal balance
    +deposit(amount)
    +withdrawal(amount)
}
```

### Example (Return Type)

End a method definition with the data type that will be returned (space between `)` and return type):

```mermaid
classDiagram
class BankAccount{
    +String owner
    +BigDecimal balance
    +deposit(amount) bool
    +withdrawal(amount) int
}
```

### Example (Generic Types)

Enclose generic types within `~` (tilde):

```mermaid
classDiagram
class Square~Shape~{
    int id
    List~int~ position
    setPoints(List~int~ points)
    getPoints() List~int~
}

Square : -List~string~ messages
Square : +setMessages(List~string~ messages)
Square : +getMessages() List~string~
Square : +getDistanceMatrix() List~List~int~~
```

### Example (Visibility)

Use `+` (Public), `-` (Private), `#` (Protected), `~` (Package/Internal) before member names:

```mermaid
classDiagram
class BankAccount{
    +String owner
    -BigDecimal balance
    #String accountNumber
    ~String internalId
}
```

### Example (Relationships)

Eight types of relations are supported:

```mermaid
classDiagram
classA <|-- classB
classC *-- classD
classE o-- classF
classG <-- classH
classI -- classJ
classK <.. classL
classM <|.. classN
classO .. classP
```

### Example (Labels on Relations)

Add label text to a relation:

```mermaid
classDiagram
classA --|> classB : Inheritance
classC --* classD : Composition
classE --o classF : Aggregation
classG --> classH : Association
classI -- classJ : Link(Solid)
classK ..> classL : Dependency
classM ..|> classN : Realization
classO .. classP : Link(Dashed)
```

### Example (Two-way relations)

Represent N:M associations using two-way relations:

```mermaid
classDiagram
    Animal <|--|> Zebra
```

### Example (Lollipop Interfaces)

Define lollipop interfaces using `()--` or `--()`:

```mermaid
classDiagram
  bar ()-- foo
```

### Example (Namespaces)

Group classes using namespaces:

```mermaid
classDiagram
namespace BaseShapes {
    class Triangle
    class Rectangle {
      double width
      double height
    }
}
```

### Example (Cardinality)

Place cardinality notations near the end of an association:

```mermaid
classDiagram
    Customer "1" --> "*" Ticket
    Student "1" --> "1..*" Course
    Galaxy --> "many" Star : Contains
```

### Example (Annotations)

Annotate classes with markers like `<<Interface>>`, `<<Abstract>>`, `<<Service>>`, `<<Enumeration>>`:

```mermaid
classDiagram
class Shape{
    <<interface>>
    noOfVertices
    draw()
}
class Color{
    <<enumeration>>
    RED
    BLUE
    GREEN
    WHITE
    BLACK
}
```

### Example (Comments)

Comments need to be on their own line, prefaced with `%%`:

```mermaid
classDiagram
%% This whole line is a comment
classDiagram
class Shape <<interface>>
class Shape{
    <<interface>>
    noOfVertices
    draw()
}
```

### Example (Direction)

Set the direction using `direction` statement:

```mermaid
classDiagram
  direction RL
  class Student {
    -idCard : IdCard
  }
  class IdCard{
    -id : int
    -name : string
  }
  class Bike{
    -id : int
    -name : string
  }
  Student "1" --o "1" IdCard : carries
  Student "1" --o "1" Bike : rides
```

### Example (Notes)

Add notes using `note` or `note for ClassName`:

```mermaid
classDiagram
    note "This is a general note"
    note for MyClass "This is a note for a class"
    class MyClass{
    }
```

### Example (Interaction - Links)

Bind click events to nodes for links:

```mermaid
classDiagram
class Shape
link Shape "https://www.github.com" "This is a tooltip for a link"
class Shape2
click Shape2 href "https://www.github.com" "This is a tooltip for a link"
```

### Example (Interaction - Callbacks)

Bind click events to nodes for callbacks:

```mermaid
classDiagram
class Shape
callback Shape "callbackFunction" "This is a tooltip for a callback"
class Shape2
click Shape2 call callbackFunction() "This is a tooltip for a callback"
```

### Example (Styling a node)

Apply specific styles using `style` keyword:

```mermaid
classDiagram
  class Animal
  class Mineral
  style Animal fill:#f9f,stroke:#333,stroke-width:4px
  style Mineral fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
```

### Example (Classes)

Define reusable style classes using `classDef` and apply with `:::`:

```mermaid
classDiagram
    class Animal:::someclass
    classDef someclass fill:#f96
```

Or with class members:

```mermaid
classDiagram
    class Animal:::someclass {
        -int sizeInFeet
        -canEat()
    }
    classDef someclass fill:#f96
```

### Example (Default class)

A class named `default` will be applied to all nodes:

```mermaid
classDiagram
  class Animal:::pink
  class Mineral

  classDef default fill:#f96,color:red
  classDef pink color:#f9f
```

### Example (CSS Classes)

Predefine classes in CSS styles and apply from the graph definition:

```mermaid
classDiagram
    class Animal:::styleClass
```

### Example (Using cssClass)

Apply a class to a node using `cssClass`:

```mermaid
classDiagram
    class Animal
    class Mineral
    classDef someclass fill:#f96
    cssClass "Animal" someclass
```

### Example (Multiple Classes in classDef)

Define styles for multiple classes in one statement:

```mermaid
classDiagram
    class Animal
    class Mineral
    classDef firstClassName,secondClassName fill:#f9f,stroke:#333,stroke-width:2px;
    cssClass "Animal" firstClassName
    cssClass "Mineral" secondClassName
```

### Example (Configuration - Hide Empty Members Box)

Hide the empty members box using configuration:

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
  class Duck
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If class diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    Animal[Animal]
    Dog[Dog]
    Cat[Cat]

    Animal -->|inherits| Dog
    Animal -->|inherits| Cat
```
