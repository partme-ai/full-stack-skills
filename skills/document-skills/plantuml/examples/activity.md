# Activity Diagram | 活动图

**官方文档**: https://plantuml.com/zh/activity-diagram-legacy

## Instructions

Activity diagrams show workflows and business processes. They are useful for modeling the flow of control from activity to activity.

## Key Concepts

- Use `@startuml` and `@enduml` to wrap the diagram
- Use `start` and `stop` for start and end nodes
- Use `:` for activities
- Use `if`, `then`, `else`, `endif` for decisions
- Use `while`, `endwhile` for loops
- Use `fork`, `fork again`, `end fork` for parallel activities
- Use `partition` to group activities
- Use `note` for annotations

## Example: Basic Activity Diagram

```plantuml
@startuml
start
:Login;
if (Authentication successful?) then (yes)
  :Show dashboard;
else (no)
  :Show error message;
  stop
endif
stop
@enduml
```

## Example: With Decisions and Loops

```plantuml
@startuml
start
:Initialize;
while (More items?) is (yes)
  :Process item;
  if (Item valid?) then (yes)
    :Save item;
  else (no)
    :Log error;
  endif
endwhile (no)
:Finalize;
stop
@enduml
```

## Example: With Parallel Activities

```plantuml
@startuml
start
:Start process;
fork
  :Task 1;
fork again
  :Task 2;
fork again
  :Task 3;
end fork
:Combine results;
stop
@enduml
```

## Example: With Partitions

```plantuml
@startuml
start
partition "User" {
  :Login;
  :Enter data;
}
partition "System" {
  :Validate data;
  :Process data;
  :Save data;
}
partition "User" {
  :View results;
}
stop
@enduml
```

## Example: Complex Workflow

```plantuml
@startuml
start
:Receive order;
if (Order valid?) then (yes)
  :Check inventory;
  if (In stock?) then (yes)
    :Reserve items;
    :Process payment;
    if (Payment successful?) then (yes)
      :Ship order;
      :Send confirmation;
      stop
    else (no)
      :Release reservation;
      :Notify customer;
      stop
    endif
  else (no)
    :Backorder;
    :Notify customer;
    stop
  endif
else (no)
  :Reject order;
  stop
endif
@enduml
```

## Key Points

- Use `start` and `stop` for start and end nodes
- Use `:` for activity labels
- Use `if`, `then`, `else`, `endif` for decision nodes
- Use `while`, `endwhile` for loops
- Use `fork`, `fork again`, `end fork` for parallel execution
- Use `partition` to group related activities
- Use `note` for annotations
- Activities are connected automatically in sequence
