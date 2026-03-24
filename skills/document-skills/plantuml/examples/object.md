# Object Diagram | 对象图

**官方文档**: https://plantuml.com/zh/object-diagram

## Instructions

Object diagrams show instances of classes and their relationships at a specific point in time. They are useful for modeling the runtime structure of a system.

## Key Concepts

- Use `@startuml` and `@enduml` to wrap the diagram
- Use `object` to define objects
- Use `map` for key-value pairs
- Use relationships: `--`, `-->`, etc.
- Use `note` for annotations

## Example: Basic Object Diagram

```plantuml
@startuml
object User1 {
  name = "Alice"
  age = 30
}

object Order1 {
  orderId = 12345
  total = 99.99
}

User1 --> Order1 : places
@enduml
```

## Example: With Multiple Objects

```plantuml
@startuml
object "Customer: Alice" as customer {
  name = "Alice"
  email = "alice@example.com"
}

object "Order: #12345" as order {
  orderId = 12345
  date = "2024-01-15"
  total = 199.99
}

object "Product: Laptop" as product {
  productId = "P001"
  name = "Laptop"
  price = 199.99
}

object "Product: Mouse" as product2 {
  productId = "P002"
  name = "Mouse"
  price = 29.99
}

customer --> order : places
order --> product : contains
order --> product2 : contains
@enduml
```

## Example: With Maps

```plantuml
@startuml
map "User Preferences" as prefs {
  theme => "dark"
  language => "en"
  notifications => true
}

object User {
  name = "Bob"
  preferences = prefs
}
@enduml
```

## Key Points

- Use `object` to define object instances
- Use `map` for key-value pairs
- Object diagrams show runtime instances, not classes
- Use relationships to show object connections
- Object diagrams are ideal for modeling specific system states
