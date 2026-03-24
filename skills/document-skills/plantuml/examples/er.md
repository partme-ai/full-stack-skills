# ER Diagram | 实体关系图

**官方文档**: https://plantuml.com/zh/ie-diagram

## Instructions

ER (Entity-Relationship) diagrams show entities and their relationships. They are useful for database design and data modeling.

## Key Concepts

- Use `@startuml` and `@enduml` to wrap the diagram
- Use `entity` to define entities
- Use relationships: `||--`, `}o--`, `}--`, etc.
- Use `(`, `)` for cardinality notation

## Example: Basic ER Diagram

```plantuml
@startuml
entity "User" as user {
  * id : INT <<PK>>
  --
  * username : VARCHAR
  * email : VARCHAR
}

entity "Order" as order {
  * id : INT <<PK>>
  --
  * user_id : INT <<FK>>
  * total : DECIMAL
  * date : DATE
}

user ||--o{ order
@enduml
```

## Example: Complex ER Diagram

```plantuml
@startuml
entity "Customer" as customer {
  * customer_id : INT <<PK>>
  --
  * name : VARCHAR
  * email : VARCHAR
  phone : VARCHAR
}

entity "Order" as order {
  * order_id : INT <<PK>>
  --
  * customer_id : INT <<FK>>
  * order_date : DATE
  * total_amount : DECIMAL
}

entity "Product" as product {
  * product_id : INT <<PK>>
  --
  * name : VARCHAR
  * price : DECIMAL
  description : TEXT
}

entity "OrderItem" as order_item {
  * order_id : INT <<PK>> <<FK>>
  * product_id : INT <<PK>> <<FK>>
  --
  * quantity : INT
  * price : DECIMAL
}

customer ||--o{ order
order ||--o{ order_item
product ||--o{ order_item
@enduml
```

## Example: With Attributes

```plantuml
@startuml
entity "Student" as student {
  * student_id : INT <<PK>>
  --
  * name : VARCHAR
  * email : VARCHAR
  date_of_birth : DATE
}

entity "Course" as course {
  * course_id : INT <<PK>>
  --
  * title : VARCHAR
  * credits : INT
  description : TEXT
}

entity "Enrollment" as enrollment {
  * student_id : INT <<PK>> <<FK>>
  * course_id : INT <<PK>> <<FK>>
  --
  * enrollment_date : DATE
  grade : VARCHAR
}

student ||--o{ enrollment
course ||--o{ enrollment
@enduml
```

## Key Points

- Use `entity` to define entities
- Use `*` for primary keys, `--` for separator
- Use `||--`, `}o--`, `}--` for relationships
- Use `(`, `)` for cardinality notation
- ER diagrams are ideal for database design
