# Regex Diagram | 正则表达式图

**官方文档**: https://plantuml.com/zh/regex

## Instructions

Regex diagrams visualize regular expressions as state machines. They are useful for understanding and documenting complex regular expressions.

## Key Concepts

- Use `@startregex` and `@endregex` to wrap the diagram
- Regular expression syntax is automatically parsed
- Shows state transitions and matching paths
- Supports common regex patterns

## Example: Basic Regex Diagram

```plantuml
@startregex
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
@endregex
```

## Example: Phone Number Pattern

```plantuml
@startregex
^(\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})$
@endregex
```

## Example: URL Pattern

```plantuml
@startregex
^https?://([\da-z\.-]+)\.([a-z\.]{2,6})([/\w \.-]*)*/?$
@endregex
```

## Example: Date Pattern

```plantuml
@startregex
^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$
@endregex
```

## Key Points

- Use `@startregex` and `@endregex` for regex diagrams
- Regular expressions are automatically parsed and visualized
- Shows state machine representation of regex patterns
- Regex diagrams are ideal for understanding complex patterns
