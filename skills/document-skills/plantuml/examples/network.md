# Network Diagram | 网络图

**官方文档**: https://plantuml.com/zh/nwdiag

## Instructions

Network diagrams show network topology and infrastructure. They are useful for documenting network architecture and configurations.

## Key Concepts

- Use `@startuml` and `@enduml` to wrap the diagram
- Use `network` to define networks
- Use `group` to group network elements
- Use `node` for network nodes
- Use relationships to show connections

## Example: Basic Network Diagram

```plantuml
@startuml
network "Corporate Network" {
  node "Web Server" as web
  node "Database Server" as db
  node "Application Server" as app
}

network "DMZ" {
  node "Firewall" as fw
}

network "Internet" {
  node "Client" as client
}

client --> fw
fw --> web
web --> app
app --> db
@enduml
```

## Example: Cloud Network Architecture

```plantuml
@startuml
cloud "AWS" {
  network "VPC" {
    network "Public Subnet" {
      node "Load Balancer" as lb
      node "Web Server 1" as web1
      node "Web Server 2" as web2
    }
    
    network "Private Subnet" {
      node "App Server 1" as app1
      node "App Server 2" as app2
      node "Database" as db
    }
  }
}

network "Internet" {
  node "Users" as users
}

users --> lb
lb --> web1
lb --> web2
web1 --> app1
web2 --> app2
app1 --> db
app2 --> db
@enduml
```

## Example: Multi-Site Network

```plantuml
@startuml
network "Site A" {
  node "Router A" as routerA
  node "Switch A" as switchA
  node "Server A" as serverA
}

network "Site B" {
  node "Router B" as routerB
  node "Switch B" as switchB
  node "Server B" as serverB
}

network "WAN" {
  routerA <--> routerB
}

routerA --> switchA
switchA --> serverA

routerB --> switchB
switchB --> serverB
@enduml
```

## Key Points

- Use `network` to define network segments
- Use `node` for network devices
- Use `group` to organize network elements
- Use `-->` and `<-->` for connections
- Network diagrams are ideal for infrastructure documentation
