# Chronology Diagram | 时间线图

**官方文档**: https://plantuml.com/zh/chronology-diagram

## Instructions

Chronology diagrams show events and timelines. They are useful for documenting historical events, project timelines, and sequences of events.

## Key Concepts

- Use `@startuml` and `@enduml` to wrap the diagram
- Use timeline syntax to define events
- Show chronological order of events
- Support date and time annotations

## Example: Basic Chronology Diagram

```plantuml
@startuml
chronology "Project Timeline" {
  2024-01-01 : Project Start
  2024-02-01 : Phase 1 Complete
  2024-03-01 : Phase 2 Complete
  2024-04-01 : Project Complete
}
@enduml
```

## Example: Event Timeline

```plantuml
@startuml
chronology "System Events" {
  2024-01-01 09:00 : System Startup
  2024-01-01 10:30 : First User Login
  2024-01-01 12:00 : Peak Usage
  2024-01-01 18:00 : System Shutdown
}
@enduml
```

## Example: Project Milestones

```plantuml
@startuml
chronology "Project Milestones" {
  2024-01-15 : Requirements Complete
  2024-02-15 : Design Complete
  2024-03-15 : Development Complete
  2024-04-15 : Testing Complete
  2024-05-15 : Deployment Complete
}
@enduml
```

## Key Points

- Use `chronology` keyword for chronology diagrams
- Define events with dates and descriptions
- Chronology diagrams show temporal sequences
- Chronology diagrams are ideal for timelines and event sequences
