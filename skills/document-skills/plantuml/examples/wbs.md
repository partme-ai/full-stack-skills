# WBS Diagram | 工作分解结构图

**官方文档**: https://plantuml.com/zh/wbs-diagram

## Instructions

WBS (Work Breakdown Structure) diagrams show hierarchical breakdown of work into smaller components. They are useful for project planning and management.

## Key Concepts

- Use `@startwbs` and `@endwbs` to wrap the diagram
- Use `*` for root level
- Use `**` for second level, `***` for third level, etc.
- Shows hierarchical work structure

## Example: Basic WBS Diagram

```plantuml
@startwbs
* Project
** Phase 1
*** Task 1.1
*** Task 1.2
** Phase 2
*** Task 2.1
*** Task 2.2
@endwbs
```

## Example: Software Development WBS

```plantuml
@startwbs
* Software Development Project
** Planning
*** Requirements Gathering
*** System Design
** Development
*** Frontend Development
**** UI Components
**** User Interface
*** Backend Development
**** API Development
**** Database Design
** Testing
*** Unit Testing
*** Integration Testing
*** System Testing
** Deployment
*** Environment Setup
*** Production Deployment
@endwbs
```

## Example: Product Launch WBS

```plantuml
@startwbs
* Product Launch
** Market Research
*** Competitor Analysis
*** Customer Surveys
** Product Development
*** Design
*** Development
*** Testing
** Marketing
*** Advertising
*** Social Media
*** Press Release
** Launch
*** Beta Testing
*** Official Launch
@endwbs
```

## Key Points

- Use `@startwbs` and `@endwbs` for WBS diagrams
- Use `*` for root level
- Use `**`, `***`, etc. for nested levels
- WBS diagrams show work breakdown structure
- WBS diagrams are ideal for project planning
