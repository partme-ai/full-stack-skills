# IE Diagram | 信息工程图

**官方文档**: https://plantuml.com/zh/ie-diagram

## Instructions

IE (Information Engineering) diagrams use Crow's Foot notation for entity relationships. They are useful for database design with standard IE notation.

## Key Concepts

- Use `@startuml` and `@enduml` to wrap the diagram
- Use `entity` to define entities
- Use IE notation for relationships
- Follow Information Engineering standards

## Example: Basic IE Diagram

```plantuml
@startuml
entity "User" {
  * id : INT
  --
  * username : VARCHAR
  * email : VARCHAR
}

entity "Order" {
  * id : INT
  --
  * user_id : INT
  * total : DECIMAL
}

User ||--o{ Order
@enduml
```

## Example: With Cardinality

```plantuml
@startuml
entity "Customer" {
  * customer_id : INT
  --
  * name : VARCHAR
  email : VARCHAR
}

entity "Order" {
  * order_id : INT
  --
  * customer_id : INT
  order_date : DATE
}

entity "Product" {
  * product_id : INT
  --
  * name : VARCHAR
  price : DECIMAL
}

Customer ||--o{ Order
Order }o--|| Product
@enduml
```

## Key Points

- Use `entity` for entities
- IE diagrams use Crow's Foot notation
- Use `||--`, `}o--`, etc. for relationships
- IE diagrams follow Information Engineering standards
