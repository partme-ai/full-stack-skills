## Instructions

Gantt charts display project schedules, showing tasks, their durations, and dependencies over time. A Gantt chart is a type of bar chart that illustrates a project schedule and the amount of time it would take for any one project to finish. Gantt charts illustrate number of days between the start and finish dates of the terminal elements and summary elements of a project.

### Syntax

- Use `gantt` keyword
- Date format: `dateFormat YYYY-MM-DD` (required)
- Title: `title Project Title` (optional)
- Sections: `section Section Name` (required for grouping tasks)
- Tasks: `Task Name :[tags], [taskID], [startDate], [endDate|duration]`
- Tags: `active`, `done`, `crit`, `milestone` (optional, must be first)
- Task metadata syntax:
  - `Task Name :[tags], taskID, startDate, endDate`
  - `Task Name :[tags], taskID, startDate, duration`
  - `Task Name :[tags], taskID, after otherTaskID, endDate`
  - `Task Name :[tags], taskID, after otherTaskID, duration`
  - `Task Name :[tags], startDate, endDate` (no ID)
  - `Task Name :[tags], startDate, duration` (no ID)
  - `Task Name :[tags], after otherTaskID, endDate` (no ID)
  - `Task Name :[tags], endDate` (no ID, sequential)
  - `Task Name :[tags], duration` (no ID, sequential)
- Excludes: `excludes dates` (optional) - excludes specific dates, days, or weekends
- Weekend: `weekend friday` or `weekend saturday` (v11.0.0+, optional)
- Milestones: Use `milestone` tag
- Comments: `%% comment` (on separate line)
- Tick interval: `tickInterval 1day|1week|1month` (v10.3.0+)
- Weekday: `weekday sunday|monday|...` (for week-based intervals)

Reference: [Mermaid Gantt Chart Documentation](https://mermaid.ai/open-source/syntax/gantt.html)

### Example (Basic Gantt Chart)

```mermaid
gantt
    title A Gantt Diagram
    dateFormat YYYY-MM-DD
    section Section
        A task          :a1, 2014-01-01, 30d
        Another task    :after a1, 20d
    section Another
        Task in Another :2014-01-12, 12d
        another task    :24d
```

### Example (With Task IDs and Dependencies)

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title       Adding GANTT diagram functionality to mermaid
    excludes    weekends
    %% (`excludes` accepts specific dates in YYYY-MM-DD format, days of the week ("sunday") or "weekends", but not the word "weekdays".)

    section A section
    Completed task            :done,    des1, 2014-01-06,2014-01-08
    Active task               :active,  des2, 2014-01-09, 3d
    Future task               :         des3, after des2, 5d
    Future task2              :         des4, after des3, 5d

    section Critical tasks
    Completed task in the critical line :crit, done, 2014-01-06,24h
    Implement parser and jison          :crit, done, after des1, 2d
    Create tests for parser             :crit, active, 3d
    Future task in critical line        :crit, 5d
    Create tests for renderer           :2d
    Add to mermaid                      :until isadded
    Functionality added                 :milestone, isadded, 2014-01-25, 0d

    section Documentation
    Describe gantt syntax               :active, a1, after des1, 3d
    Add gantt diagram to demo page      :after a1  , 20h
    Add another diagram to demo page    :doc1, after a1  , 48h

    section Last section
    Describe gantt syntax               :after doc1, 3d
    Add gantt diagram to demo page      :20h
    Add another diagram to demo page    :48h
```

### Example (With Multiple Task Dependencies)

```mermaid
gantt
    apple :a, 2017-07-20, 1w
    banana :crit, b, 2017-07-23, 1d
    cherry :active, c, after b a, 1d
    kiwi   :d, 2017-07-20, until b c
```

### Example (With Excludes)

```mermaid
gantt
    title Project with Exclusions
    dateFormat YYYY-MM-DD
    excludes weekends
    section Development
    Task 1 :task1, 2024-01-01, 10d
    Task 2 :task2, after task1, 10d
```

### Example (With Weekend Configuration)

```mermaid
gantt
    title A Gantt Diagram Excluding Fri - Sat weekends
    dateFormat YYYY-MM-DD
    excludes weekends
    weekend friday
    section Section
        A task          :a1, 2024-01-01, 30d
        Another task    :after a1, 20d
```

### Example (With Milestones)

```mermaid
gantt
    dateFormat HH:mm
    axisFormat %H:%M
    Initial milestone : milestone, m1, 17:49, 2m
    Task A : 10m
    Task B : 5m
    Final milestone : milestone, m2, 18:08, 4m
```

### Example (With Vertical Markers)

**Note**: Vertical markers (`vert`) may not be supported in all Mermaid versions. If this example doesn't work, use milestones instead.

```mermaid
gantt
    dateFormat HH:mm
    axisFormat %H:%M
    Initial milestone : milestone, m1, 17:30, 0m
    Task A : 3m
    Task B : 8m
    Final milestone : milestone, m2, 17:58, 0m
```

### Example (With Tick Interval)

**Note**: `tickInterval` requires Mermaid v10.3.0+. This example includes tasks to demonstrate the tick interval.

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    tickInterval 1week
    weekday monday
    section Phase 1
    Design :des1, 2024-01-01, 2024-01-15
    Development :dev1, after des1, 20d
```

### Example (With Comments)

```mermaid
gantt
    title A Gantt Diagram
    %% This is a comment
    dateFormat YYYY-MM-DD
    section Section
        A task          :a1, 2014-01-01, 30d
        Another task    :after a1, 20d
    section Another
        Task in Another :2014-01-12, 12d
        another task    :24d
```

### Example (Compact Mode)

```mermaid
---
displayMode: compact
---
gantt
    title A Gantt Diagram
    dateFormat  YYYY-MM-DD

    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :a2, 2014-01-20, 25d
    Another one      :a3, 2014-02-10, 20d
```

### Example (Bar Chart using Gantt)

```mermaid
gantt
    title Git Issues - days since last update
    dateFormat X
    axisFormat %s
    section Issue19062
    71   : 0, 71
    section Issue19401
    36   : 0, 36
    section Issue193
    34   : 0, 34
    section Issue7441
    9    : 0, 9
    section Issue1300
    5    : 0, 5
```

### Example (Timeline with Comments, CSS, and Config in Frontmatter)

A comprehensive example demonstrating frontmatter configuration, custom CSS styling, milestones, and vertical markers:

```mermaid
---
# Frontmatter config, YAML comments
title: Ignored if specified in chart
displayMode: compact
config:
    themeCSS: |
        #item36 { fill: CadetBlue }
        rect[id^=workaround] {
            height: calc(100% - 50px);
            transform: translate(9px, 25px);
            y: 0;
            width: 1.5px;
            stroke: none;
            fill: red;
        }
        text[id^=workaround] {
            fill: red;
            y: 100%;
            font-size: 15px;
        }
    gantt:
        useWidth: 400
        rightPadding: 0
        topAxis: true
        numberSectionStyles: 2
---
gantt
    title Timeline - Gantt Sampler
    dateFormat YYYY
    axisFormat %y
    tickInterval 1decade
    section Issue19062
    71   : item71, 1900, 1930
    section Issue19401
    36   : item36, 1913, 1935
    section Issue1300
    94   : item94, 1910, 1915
    5    : item5, 1920, 1925
    0    : milestone, item0, 1918, 1s
    9    : vert, 1906, 1s
    64   : workaround, 1923, 1s
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If Gantt charts are not supported, use this flowchart alternative:

```mermaid
flowchart TD
    Start([Project Start]) --> PlanningPhase[Planning Phase]
    PlanningPhase --> DesignPhase[Design Phase]
    DesignPhase --> DevelopmentPhase[Development Phase]
    DevelopmentPhase --> TestingPhase[Testing Phase]
    TestingPhase --> Deployment([Deployment])
    
    subgraph Planning["Planning"]
        Req[Requirements<br/>Gathering]
        Sys[System Design]
        Req --> Sys
    end
    
    subgraph Development["Development"]
        Front[Frontend<br/>Development]
        Back[Backend<br/>Development]
        DB[Database<br/>Setup]
    end
    
    subgraph Testing["Testing"]
        Unit[Unit Testing]
        Integration[Integration<br/>Testing]
        Unit --> Integration
    end
    
    PlanningPhase --> Req
    DesignPhase --> Front
    DesignPhase --> Back
    DesignPhase --> DB
    Front --> Unit
    Back --> Unit
    DB --> Unit
    Integration --> Deployment
    
    style Start fill:#e1f5,stroke:#333
    style Deployment fill:#e1f5,stroke:#333
    style PlanningPhase fill:#bbf,stroke:#333
    style DevelopmentPhase fill:#bbf,stroke:#333
    style TestingPhase fill:#bbf,stroke:#333
```
