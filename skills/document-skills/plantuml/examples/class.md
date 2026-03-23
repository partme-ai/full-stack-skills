# Class Diagram | 类图

**官方文档**: https://plantuml.com/zh/class-diagram

## Instructions

Class diagrams show the structure of a system by modeling classes, their attributes, methods, and relationships. They are essential for object-oriented design and documentation.

## Key Concepts

- Use `@startuml` and `@enduml` to wrap the diagram
- Define classes with `class` keyword
- Use visibility modifiers: `+` (public), `-` (private), `#` (protected), `~` (package)
- Define relationships: `--`, `-->`, `<|--`, `*--`, `o--`, etc.
- Use `abstract`, `interface`, `enum` for special class types
- Use `package` to group related classes
- Use `note` for annotations

## Example: Basic Class Diagram

```plantuml
@startuml
class Car {
  - String brand
  - String model
  - int year
  + start()
  + stop()
  + accelerate()
}

class Engine {
  - int horsepower
  + start()
  + stop()
}

Car *-- Engine
@enduml
```

## Example: With Relationships

```plantuml
@startuml
class Animal {
  + String name
  + int age
  + makeSound()
}

class Dog {
  + String breed
  + bark()
}

class Cat {
  + String color
  + meow()
}

Animal <|-- Dog
Animal <|-- Cat
@enduml
```

## Example: With Interfaces and Abstract Classes

```plantuml
@startuml
abstract class Shape {
  {abstract} + draw()
  + getArea()
}

interface Drawable {
  + draw()
}

class Circle {
  - double radius
  + draw()
  + getArea()
}

class Rectangle {
  - double width
  - double height
  + draw()
  + getArea()
}

Shape <|-- Circle
Shape <|-- Rectangle
Drawable <|.. Circle
Drawable <|.. Rectangle
@enduml
```

## Example: With Packages

```plantuml
@startuml
package "com.example.model" {
  class User {
    - String username
    - String email
    + login()
    + logout()
  }
  
  class Order {
    - int orderId
    - Date orderDate
    + create()
    + cancel()
  }
}

package "com.example.service" {
  class UserService {
    + register(User)
    + authenticate(String, String)
  }
  
  class OrderService {
    + createOrder(Order)
    + processOrder(int)
  }
}

UserService --> User
OrderService --> Order
User "1" --> "*" Order
@enduml
```

## Example: With Enums

```plantuml
@startuml
enum OrderStatus {
  PENDING
  PROCESSING
  SHIPPED
  DELIVERED
  CANCELLED
}

class Order {
  - int orderId
  - OrderStatus status
  + updateStatus(OrderStatus)
}

Order --> OrderStatus
@enduml
```

## Relationship Types

- `--` : Association
- `-->` : Directed association
- `<|--` : Inheritance (extends)
- `*--` : Composition
- `o--` : Aggregation
- `..>` : Dependency
- `<|..` : Implementation (implements)

## Key Points

- Use visibility modifiers: `+` (public), `-` (private), `#` (protected), `~` (package)
- Use `abstract` for abstract classes, `interface` for interfaces
- Use `{abstract}` for abstract methods
- Use `package` to organize classes
- Use relationship arrows to show class relationships
- Use `note` for additional documentation
- Use `enum` for enumeration types
