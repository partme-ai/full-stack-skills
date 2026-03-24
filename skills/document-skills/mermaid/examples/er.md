## Instructions

Entity Relationship (ER) diagrams represent the structure of a database, showing entities, their attributes, and relationships between them. Mermaid uses the popular crow's foot notation to represent cardinality.

### Syntax

- Use `erDiagram` keyword
- Entities: `ENTITY_NAME { }` or `ENTITY_NAME { type name }` (with attributes)
- Relationships: `<first-entity> [<relationship> <second-entity> : <relationship-label>]`
- Cardinality markers:
  - `||` - Exactly one
  - `|o` - Zero or one
  - `}|` - One or more
  - `}o` - Zero or more
- Relationship types:
  - `--` - Identifying relationship (solid line)
  - `..` - Non-identifying relationship (dashed line)
- Aliases: `one or zero`, `zero or one`, `one or more`, `one or many`, `many(1)`, `1+`, `zero or more`, `zero or many`, `many(0)`, `0+`, `only one`, `1`, `to`, `optionally to`
- Attributes: `type name` or `*type name` (asterisk for primary key)
- Attribute keys: `PK` (Primary Key), `FK` (Foreign Key), `UK` (Unique Key)
- Comments: Double quotes at the end of attribute: `type name "comment"`
- Entity aliases: `ENTITY_NAME[alias]` (alias shown instead of entity name)
- Direction: `direction TB|BT|LR|RL` (default: TB)
- Styling: `style entityId fill:#color,stroke:#color` or `classDef className fill:#color`
- Unicode and Markdown: Supported in entity names, relationships, and attributes

Reference: [Mermaid Entity Relationship Diagram Documentation](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)

### Example (Basic ER Diagram)

A simple ER diagram showing relationships between entities:

```mermaid
---
title: Order example
---
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
```

### Example (With Attributes)

Include attribute definitions to show entity properties:

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        string name
        string custNumber
        string sector
    }
    ORDER ||--|{ LINE-ITEM : contains
    ORDER {
        int orderNumber
        string deliveryAddress
    }
    LINE-ITEM {
        string productCode
        int quantity
        float pricePerUnit
    }
```

### Example (Unicode text)

Entity names, relationships, and attributes all support unicode text:

```mermaid
erDiagram
    "This ❤ Unicode"
```

### Example (Markdown formatting)

Markdown formatting and text is also supported:

```mermaid
erDiagram
    "This **is** _Markdown_"
```

### Example (Identifying vs Non-identifying Relationships)

Identifying relationships use `--` (solid line), non-identifying use `..` (dashed line):

```mermaid
erDiagram
    CAR ||--o{ NAMED-DRIVER : allows
    PERSON }o..o{ NAMED-DRIVER : is
```

### Example (Using Aliases for Cardinality)

Cardinality markers can be specified using aliases:

```mermaid
erDiagram
    CAR 1 to zero or more NAMED-DRIVER : allows
    PERSON many(0) optionally to 0+ NAMED-DRIVER : is
```

### Example (With Attributes on Entities)

Define attributes using `type name` pairs within entity blocks:

```mermaid
erDiagram
    CAR ||--o{ NAMED-DRIVER : allows
    CAR {
        string registrationNumber
        string make
        string model
    }
    PERSON ||--o{ NAMED-DRIVER : is
    PERSON {
        string firstName
        string lastName
        int age
    }
```

### Example (Entity Name Aliases)

Add an alias using square brackets to display a different name:

```mermaid
erDiagram
    p[Person] {
        string firstName
        string lastName
    }
    a["Customer Account"] {
        string email
    }
    p ||--o| a : has
```

### Example (Attribute Keys and Comments)

Use `PK`, `FK`, `UK` for keys and double quotes for comments:

```mermaid
erDiagram
    CAR ||--o{ NAMED-DRIVER : allows
    CAR {
        string registrationNumber PK
        string make
        string model
        string[] parts
    }
    PERSON ||--o{ NAMED-DRIVER : is
    PERSON {
        string driversLicense PK "The license #"
        string(99) firstName "Only 99 characters are allowed"
        string lastName
        string phone UK
        int age
    }
    NAMED-DRIVER {
        string carRegistrationNumber PK, FK
        string driverLicence PK, FK
    }
    MANUFACTURER only one to zero or more CAR : makes
```

### Example (Direction - Top to Bottom)

Set diagram orientation using `direction TB` (top to bottom):

```mermaid
erDiagram
    direction TB
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        string name
        string custNumber
        string sector
    }
    ORDER ||--|{ LINE-ITEM : contains
    ORDER {
        int orderNumber
        string deliveryAddress
    }
    LINE-ITEM {
        string productCode
        int quantity
        float pricePerUnit
    }
```

### Example (Direction - Left to Right)

Set diagram orientation using `direction LR` (left to right):

```mermaid
erDiagram
    direction LR
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        string name
        string custNumber
        string sector
    }
    ORDER ||--|{ LINE-ITEM : contains
    ORDER {
        int orderNumber
        string deliveryAddress
    }
    LINE-ITEM {
        string productCode
        int quantity
        float pricePerUnit
    }
```

### Example (Styling a node)

Apply specific styles using `style` statement:

```mermaid
erDiagram
    id1||--||id2 : label
    style id1 fill:#f9f,stroke:#333,stroke-width:4px
    style id2 fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
```

### Example (Classes)

Define reusable style classes using `classDef` and apply with `class` or `:::`:

```mermaid
erDiagram
    direction TB
    CAR:::someclass {
        string registrationNumber
        string make
        string model
    }
    PERSON:::someclass {
        string firstName
        string lastName
        int age
    }
    HOUSE:::someclass

    classDef someclass fill:#f96
```

### Example (Classes with Relationships)

Apply classes when declaring relationships:

```mermaid
erDiagram
    CAR {
        string registrationNumber
        string make
        string model
    }
    PERSON {
        string firstName
        string lastName
        int age
    }
    PERSON:::foo ||--|| CAR : owns
    PERSON o{--|| HOUSE:::bar : has

    classDef foo stroke:#f00
    classDef bar stroke:#0f0
    classDef foobar stroke:#00f
```

### Example (Default class)

A class named `default` is assigned to all nodes without specific class definitions:

```mermaid
erDiagram
    CAR {
        string registrationNumber
        string make
        string model
    }
    PERSON {
        string firstName
        string lastName
        int age
    }
    PERSON:::foo ||--|| CAR : owns
    PERSON o{--|| HOUSE:::bar : has

    classDef default fill:#f9f,stroke-width:4px
    classDef foo stroke:#f00
    classDef bar stroke:#0f0
    classDef foobar stroke:#00f
```

### Example (ELK Layout)

Use ELK layout for larger or more-complex diagrams (requires Mermaid v9.4+):

```mermaid
---
title: Order example
config:
    layout: elk
---
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If ER diagrams are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    CUSTOMER[Customer]
    ORDER[Order]
    PRODUCT[Product]
    LINE_ITEM[Line Item]

    CUSTOMER -->|places| ORDER
    ORDER -->|contains| LINE_ITEM
    PRODUCT -->|ordered in| LINE_ITEM
```
