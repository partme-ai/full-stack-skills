# Sequence Diagram | 时序图

**官方文档**: https://plantuml.com/zh/sequence-diagram

## Instructions

Sequence diagrams show interactions between objects or components over time. They are ideal for visualizing the flow of messages between actors, systems, or components.

## Key Concepts

- Use `@startuml` and `@enduml` to wrap the diagram
- Declare participants with `participant` or `actor`
- Use arrows (`->`, `-->`, `->>`, `-->>`) to show messages
- Use `activate` and `deactivate` to show activation boxes
- Use `alt`, `opt`, `loop`, `par`, `break`, `critical`, `group` for control structures
- Use `note` for annotations
- Use `autonumber` for automatic message numbering

## Example: Basic Sequence Diagram

```plantuml
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response

Alice -> Bob: Another authentication Request
Alice <-- Bob: Another authentication Response
@enduml
```

## Example: With Participants

```plantuml
@startuml
participant "First Actor" as A
participant "Second Actor" as B
participant "Last Actor" as C

A -> B: DoWork
activate B

B -> C: CreateRequest
activate C
C --> B: RequestCreated
deactivate C

B --> A: WorkDone
deactivate B
@enduml
```

## Example: With Control Structures

```plantuml
@startuml
Alice -> Bob: Do you love me?

alt Yes
    Bob -> Alice: Yes, I do!
else No
    Bob -> Alice: No, I don't.
end

opt Extra response
    Bob -> Alice: But I like you!
end
@enduml
```

## Example: With Notes and Groups

```plantuml
@startuml
autonumber
Alice -> Bob: Hello
note right: This is a note
Bob -> Alice: Hi

group Group 1
    Alice -> Bob: Message 1
    Bob -> Alice: Response 1
end

group Group 2
    Alice -> Bob: Message 2
    Bob -> Alice: Response 2
end
@enduml
```

## Example: With Loops

```plantuml
@startuml
Alice -> Bob: Hello, how are you?
loop Every minute
    Alice -> Bob: Are you OK?
    Bob -> Alice: Yes, I'm OK
end
@enduml
```

## Key Points

- Use `participant` for regular participants, `actor` for actors
- Use `->` for synchronous messages, `-->` for return messages
- Use `->>` for asynchronous messages, `-->>` for asynchronous return
- Use `activate` and `deactivate` to show activation boxes
- Use control structures (`alt`, `opt`, `loop`, `par`, etc.) for complex flows
- Use `autonumber` to automatically number messages
- Use `note` for annotations on the left or right side
- Use `group` to organize related messages
