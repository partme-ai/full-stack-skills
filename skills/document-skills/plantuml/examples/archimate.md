# Archimate Diagram | Archimate 架构图

**官方文档**: https://plantuml.com/zh/archimate-diagram

## Instructions

Archimate diagrams model enterprise architecture using the ArchiMate standard. They are useful for enterprise architecture documentation.

## Key Concepts

- Use `@startuml` and `@enduml` to wrap the diagram
- Use ArchiMate elements: Application, Business, Technology layers
- Use relationships to show dependencies
- Follow ArchiMate notation standards

## Example: Basic Archimate Diagram

```plantuml
@startuml
!include <archimate/Archimate>

archimate #Application "Order Management System" as OMS
archimate #Business "Order Process" as OP
archimate #Technology "Database Server" as DB

OP --> OMS
OMS --> DB
@enduml
```

## Example: Three-Layer Architecture

```plantuml
@startuml
!include <archimate/Archimate>

archimate #Business "Customer Service" as CS
archimate #Business "Order Processing" as OP
archimate #Application "CRM System" as CRM
archimate #Application "Order System" as OS
archimate #Technology "Application Server" as AS
archimate #Technology "Database" as DB

CS --> CRM
OP --> OS
CRM --> AS
OS --> AS
AS --> DB
@enduml
```

## Example: Enterprise Architecture

```plantuml
@startuml
!include <archimate/Archimate>

package "Business Layer" {
  archimate #Business "Customer Management" as CM
  archimate #Business "Order Management" as OM
}

package "Application Layer" {
  archimate #Application "CRM Application" as CRMA
  archimate #Application "Order Application" as OA
}

package "Technology Layer" {
  archimate #Technology "Web Server" as WS
  archimate #Technology "Database" as DB
}

CM --> CRMA
OM --> OA
CRMA --> WS
OA --> WS
WS --> DB
@enduml
```

## Key Points

- Use `!include <archimate/Archimate>` to include ArchiMate library
- Use `archimate` keyword for ArchiMate elements
- Use color codes: `#Business`, `#Application`, `#Technology`
- ArchiMate diagrams follow enterprise architecture standards
- ArchiMate diagrams are ideal for enterprise architecture documentation
