# Mindmap | 思维导图

**官方文档**: https://plantuml.com/zh/mindmap-diagram

## Instructions

Mindmaps show hierarchical information in a tree structure. They are useful for brainstorming, note-taking, and organizing ideas.

## Key Concepts

- Use `@startmindmap` and `@endmindmap` to wrap the diagram
- Use `*` for root node
- Use `**` for second level nodes
- Use `***` for third level nodes, etc.
- Use `+` for left side, `-` for right side (optional)
- Use `:` for styling

## Example: Basic Mindmap

```plantuml
@startmindmap
* PlantUML
** Sequence Diagram
** Class Diagram
** Activity Diagram
** Component Diagram
** State Diagram
@endmindmap
```

## Example: With Multiple Levels

```plantuml
@startmindmap
* Software Development
** Frontend
*** React
*** Vue
*** Angular
** Backend
*** Spring Boot
*** Node.js
*** Django
** Database
*** PostgreSQL
*** MySQL
*** MongoDB
@endmindmap
```

## Example: With Styling

```plantuml
@startmindmap
* PlantUML Diagrams
** UML Diagrams
*** Sequence
*** Class
*** Activity
** Architecture
*** Component
*** Deployment
*** C4 Model
@endmindmap
```

## Key Points

- Use `@startmindmap` and `@endmindmap` for mindmaps
- Use `*` for root node
- Use `**`, `***`, etc. for nested levels
- Mindmaps are ideal for organizing hierarchical information
