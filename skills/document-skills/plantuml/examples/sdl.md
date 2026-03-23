# SDL Diagram | SDL 图

**官方文档**: https://plantuml.com/zh/sdl

## Instructions

SDL (Specification and Description Language) diagrams model system behavior and state machines. They are useful for telecommunications and real-time systems.

## Key Concepts

- Use `@startsdl` and `@endsdl` to wrap the diagram
- Use SDL syntax for state machines
- Define states, transitions, and actions
- Follow SDL notation standards

## Example: Basic SDL Diagram

```plantuml
@startsdl
state "Idle" as idle
state "Processing" as processing
state "Completed" as completed

idle --> processing : start
processing --> completed : finish
completed --> idle : reset
@endsdl
```

## Example: Communication Protocol

```plantuml
@startsdl
state "Waiting" as waiting
state "Sending" as sending
state "Receiving" as receiving
state "Acknowledged" as acknowledged

waiting --> sending : send_request
sending --> receiving : wait_response
receiving --> acknowledged : receive_ack
acknowledged --> waiting : reset
@endsdl
```

## Key Points

- Use `@startsdl` and `@endsdl` for SDL diagrams
- SDL diagrams model system behavior and protocols
- Use states and transitions to define behavior
- SDL diagrams are ideal for telecommunications and real-time systems
