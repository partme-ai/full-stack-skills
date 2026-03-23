# Gantt Chart | 甘特图

**官方文档**: https://plantuml.com/zh/gantt-diagram

## Instructions

Gantt charts show project schedules and timelines. They are useful for project management and planning.

## Key Concepts

- Use `@startgantt` and `@endgantt` to wrap the diagram
- Use `project starts` to define project start date
- Use `sprint` to define sprints
- Use `[Task]` to define tasks
- Use `--` for task dependencies
- Use `starts`, `ends`, `happens` for date constraints
- Use `colors` for styling

## Example: Basic Gantt Chart

```plantuml
@startgantt
project starts 2024-01-01
[Task 1] lasts 5 days
[Task 2] lasts 3 days
[Task 3] lasts 4 days
[Task 1] -> [Task 2]
[Task 2] -> [Task 3]
@endgantt
```

## Example: With Dates

```plantuml
@startgantt
project starts 2024-01-01
[Design] lasts 10 days
[Development] lasts 20 days
[Testing] lasts 5 days
[Deployment] lasts 2 days

[Design] -> [Development]
[Development] -> [Testing]
[Testing] -> [Deployment]
@endgantt
```

## Example: With Sprints

```plantuml
@startgantt
project starts 2024-01-01
sprint starts 2024-01-01
sprint ends 2024-01-14

[User Stories] lasts 5 days
[Development] lasts 8 days
[Testing] lasts 3 days

sprint starts 2024-01-15
sprint ends 2024-01-28

[More Development] lasts 10 days
[More Testing] lasts 4 days

[User Stories] -> [Development]
[Development] -> [Testing]
[Testing] -> [More Development]
[More Development] -> [More Testing]
@endgantt
```

## Example: With Colors

```plantuml
@startgantt
project starts 2024-01-01
[Design] lasts 10 days
[Development] lasts 20 days
[Testing] lasts 5 days

[Design] is colored in LightBlue
[Development] is colored in LightGreen
[Testing] is colored in LightYellow
@endgantt
```

## Key Points

- Use `@startgantt` and `@endgantt` for Gantt charts
- Use `project starts` to define project start date
- Use `[Task]` to define tasks with durations
- Use `->` for task dependencies
- Use `sprint` to define sprints
- Use `is colored in` for styling
- Gantt charts are ideal for project management
