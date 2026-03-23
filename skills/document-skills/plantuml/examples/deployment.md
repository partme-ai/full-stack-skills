# Deployment Diagram | 部署图

**官方文档**: https://plantuml.com/zh/deployment-diagram

## Instructions

Deployment diagrams show the physical architecture of a system, including nodes, artifacts, and their relationships. They are useful for infrastructure documentation.

## Key Concepts

- Use `@startuml` and `@enduml` to wrap the diagram
- Use `node` to define deployment nodes
- Use `database` for database nodes
- Use `cloud` for cloud nodes
- Use `package` to group nodes
- Use relationships: `--`, `-->`, etc.
- Use `note` for annotations

## Example: Basic Deployment Diagram

```plantuml
@startuml
node "Web Server" {
  artifact "Web Application"
}

node "Application Server" {
  artifact "API Service"
}

database "Database Server" {
  database "PostgreSQL"
}

"Web Server" --> "Application Server"
"Application Server" --> "Database Server"
@enduml
```

## Example: Cloud Deployment

```plantuml
@startuml
cloud "AWS" {
  node "EC2 Instance 1" {
    artifact "Web Application"
  }
  
  node "EC2 Instance 2" {
    artifact "API Service"
  }
  
  database "RDS" {
    database "PostgreSQL"
  }
}

node "Load Balancer" as LB

LB --> "EC2 Instance 1"
LB --> "EC2 Instance 2"
"EC2 Instance 1" --> "RDS"
"EC2 Instance 2" --> "RDS"
@enduml
```

## Example: Microservices Deployment

```plantuml
@startuml
node "Kubernetes Cluster" {
  node "User Service Pod" {
    artifact "User Service"
  }
  
  node "Order Service Pod" {
    artifact "Order Service"
  }
  
  node "Payment Service Pod" {
    artifact "Payment Service"
  }
}

database "PostgreSQL" {
  database "User DB"
  database "Order DB"
  database "Payment DB"
}

"User Service Pod" --> "User DB"
"Order Service Pod" --> "Order DB"
"Payment Service Pod" --> "Payment DB"
@enduml
```

## Key Points

- Use `node` to define deployment nodes
- Use `artifact` to define software artifacts
- Use `database` for database nodes
- Use `cloud` for cloud infrastructure
- Use `package` to group related nodes
- Use `-->` for dependencies between nodes
- Deployment diagrams are ideal for infrastructure documentation
