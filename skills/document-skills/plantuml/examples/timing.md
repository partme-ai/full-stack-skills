# Timing Diagram | 时序图

**官方文档**: https://plantuml.com/zh/timing-diagram

## Instructions

Timing diagrams show the state of objects or interactions over time. They are useful for modeling real-time systems and timing constraints.

## Key Concepts

- Use `@startuml` and `@enduml` to wrap the diagram
- Use `concise` for concise timing diagrams
- Use `robust` for robust timing diagrams
- Define states and transitions
- Show timing constraints

## Example: Concise Timing Diagram

```plantuml
@startuml
concise "User" as U
0 is Idle
100 is Active
200 is Idle

@U
0 is Idle
50 is Active
150 is Idle
200 is Active
@enduml
```

## Example: Robust Timing Diagram

```plantuml
@startuml
robust "Web Browser" as WB
concise "Web Server" as WS

WB is Idle
WB is Processing
WB is Idle

WS is Waiting
WS is Processing
WS is Waiting

@WB
0 is Idle
100 is Processing
200 is Idle

@WS
0 is Waiting
150 is Processing
250 is Waiting
@enduml
```

## Example: With Multiple Participants

```plantuml
@startuml
robust "Client" as C
robust "Server" as S
robust "Database" as D

C is Idle
C is Requesting
C is Waiting
C is Processing

S is Idle
S is Processing
S is Querying
S is Responding

D is Idle
D is Processing
D is Idle

@C
0 is Idle
50 is Requesting
100 is Waiting
200 is Processing
250 is Idle

@S
0 is Idle
100 is Processing
150 is Querying
200 is Responding
250 is Idle

@D
0 is Idle
150 is Processing
200 is Idle
@enduml
```

## Key Points

- Use `concise` for simple timing diagrams
- Use `robust` for complex timing diagrams with multiple states
- Timing diagrams show state changes over time
- Use `@` to define state sequences for each participant
- Timing diagrams are ideal for real-time system modeling
