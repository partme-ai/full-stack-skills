---
name: tauri-app-planning
description: Comprehensive project planning, requirements analysis, and architectural orchestration for Tauri 2.0 applications.
license: Complete terms in LICENSE.txt
---


# Tauri App Planning

This skill acts as a Senior Architect for Tauri projects. It guides the user from vague requirements to a concrete implementation plan, integrating technical orchestration patterns.

## When to use this skill

**ALWAYS use this skill when the user:**
- Wants to start a new Tauri project.
- Asks for a "plan", "roadmap", or "architecture" for a Tauri app.
- Needs to analyze requirements and map them to specific Tauri features/plugins.
- Asks about "orchestrating" windows, state, or events in Tauri.

## Workflow

1.  **Requirement Analysis**: Clarify what the user wants to build (Platforms, Core Features, UI Framework).
2.  **Technical Planning**:
    -   Select necessary `tauri-app-*` skills/plugins.
    -   Define Architecture (Monolith vs Sidecar, Multi-window topology).
    -   Define Security Scope (Capabilities).
3.  **Orchestration Design**:
    -   State Management Strategy (Rust vs Frontend).
    -   Event Communication Patterns.
4.  **Execution Plan**:
    -   Generate a step-by-step Todo List using the `TodoWrite` tool.

## Outputs

- **Technical Design Document**: A Markdown document outlining the stack, plugins, and architecture.
- **Todo List**: A structured list of tasks to build the project.
