## Instructions

Kanban diagrams visualize workflow using a board with columns representing different stages of work.

### Syntax

- Use `kanban` keyword (requires Mermaid v11.4.0+, experimental feature 🔥)
- Columns: `columnId[Column Title]` - Each column has a unique identifier and title
- Tasks: `taskId[Task Description]` - Tasks are indented under their column
- Metadata: `@{assigned: "name", ticket: "TICKET-123", priority: "High"}` (optional)
- Supported priority values: `'Very High'`, `'High'`, `'Low'`, `'Very Low'`
- Tasks must be indented under their column (proper indentation is crucial)
- Configuration: `ticketBaseUrl` for linking tickets to external systems

Reference: [Mermaid Kanban Documentation](https://mermaid.js.org/syntax/kanban.html)

### Example (Basic Kanban)

A simple kanban board with columns and tasks:

```mermaid
kanban
  column1[Column Title]
    task1[Task Description]
```

### Example (With Metadata)

Add metadata to tasks using `@{ ... }` syntax:

```mermaid
kanban
todo[Todo]
  id3[Update Database Function]@{ ticket: MC-2037, assigned: 'knsv', priority: 'High' }
```

### Example (With Configuration)

Configure ticket base URL for linking tickets:

```mermaid
---
config:
  kanban:
    ticketBaseUrl: 'https://yourproject.atlassian.net/browse/#TICKET#'
---
kanban
  todo[Todo]
    task1[Task 1]@{ ticket: MC-123 }
```

### Example (Full Example)

A complete kanban board with multiple columns, tasks, and metadata:

```mermaid
---
config:
  kanban:
    ticketBaseUrl: 'https://mermaidchart.atlassian.net/browse/#TICKET#'
---
kanban
  Todo
    [Create Documentation]
    docs[Create Blog about the new diagram]
  [In progress]
    id6[Create renderer so that it works in all cases. We also add some extra text here for testing purposes. And some more just for the extra flare.]
  id9[Ready for deploy]
    id8[Design grammar]@{ assigned: 'knsv' }
  id10[Ready for test]
    id4[Create parsing tests]@{ ticket: MC-2038, assigned: 'K.Sveidqvist', priority: 'High' }
    id66[last item]@{ priority: 'Very Low', assigned: 'knsv' }
  id11[Done]
    id5[define getData]
    id2[Title of diagram is more than 100 chars when user duplicates diagram with 100 char]@{ ticket: MC-2036, priority: 'Very High'}
    id3[Update DB function]@{ ticket: MC-2037, assigned: knsv, priority: 'High' }
  id12[Can't reproduce]
    id3[Weird flickering in Firefox]
```

### Alternative (Flowchart - compatible with all Mermaid versions)

If kanban is not supported, use this flowchart alternative:

```mermaid
flowchart LR
    subgraph ToDo["To Do"]
        T1[Task 1]
        T2[Task 2]
    end
    subgraph InProgress["In Progress"]
        T3[Task 3]
        T4[Task 4]
    end
    subgraph Done["Done"]
        T5[Task 5]
        T6[Task 6]
    end

    ToDo --> InProgress
    InProgress --> Done
```
