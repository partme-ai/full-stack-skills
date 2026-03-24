# Use Case Diagram | 用例图

**官方文档**: https://plantuml.com/zh/use-case-diagram

## Instructions

Use case diagrams show the interactions between actors and the system. They are useful for requirements analysis and system design.

## Key Concepts

- Use `@startuml` and `@enduml` to wrap the diagram
- Use `actor` to define actors
- Use `usecase` or `(Use Case)` to define use cases
- Use `package` to group use cases
- Use relationships: `-->`, `<|--`, `..>`, etc.
- Use `note` for annotations

## Example: Basic Use Case Diagram

```plantuml
@startuml
actor User
actor Admin

(User Login) as Login
(User Registration) as Register
(View Dashboard) as Dashboard
(Manage Users) as Manage

User --> Login
User --> Register
User --> Dashboard
Admin --> Login
Admin --> Dashboard
Admin --> Manage
@enduml
```

## Example: With Relationships

```plantuml
@startuml
actor Customer
actor "Sales Staff" as Sales

(Create Order) as CreateOrder
(Process Payment) as ProcessPayment
(Generate Invoice) as GenerateInvoice
(View Order Status) as ViewStatus

Customer --> CreateOrder
CreateOrder ..> ProcessPayment : <<include>>
ProcessPayment ..> GenerateInvoice : <<include>>
Customer --> ViewStatus
Sales --> CreateOrder
Sales --> ViewStatus
@enduml
```

## Example: With Extends and Includes

```plantuml
@startuml
actor User

(Login) as Login
(Logout) as Logout
(View Profile) as ViewProfile
(Edit Profile) as EditProfile
(Change Password) as ChangePassword
(Search) as Search
(Advanced Search) as AdvancedSearch

User --> Login
User --> Logout
User --> ViewProfile
User --> EditProfile
User --> Search

EditProfile <|-- ChangePassword : <<extend>>
Search <|-- AdvancedSearch : <<extend>>

ViewProfile ..> Login : <<include>>
EditProfile ..> Login : <<include>>
@enduml
```

## Key Points

- Use `actor` to define actors
- Use `usecase` or `(Use Case)` to define use cases
- Use `-->` for associations
- Use `..>` for include relationships
- Use `<|--` for extend relationships
- Use `package` to group related use cases
- Use `note` for additional documentation
