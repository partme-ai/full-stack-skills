---
name: stitch-mcp-create-project
description: Creates a new Stitch project container. Use this when starting a new design task, app idea, or fresh workspace.
license: Complete terms in LICENSE.txt
allowed-tools:
  - "stitch*:*"
  - "Read"
  - "Write"
---


## When to use this skill

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Stitch".**

**ALWAYS use this skill when:**
- The user wants to start a **new** design task or app idea **using Stitch**.
- The user asks to "create a Stitch project", "start a new app in Stitch".
- The user switches context to a completely different domain (e.g., from "Medical App" to "Gaming App") and needs a clean slate.
- You need to obtain a `projectId` before generating screens.

**Trigger phrases include:**
- "Create a new Stitch project" (创建新 Stitch 项目)
- "Start a new Stitch app" (开始一个新 Stitch 应用)
- "Initialize Stitch workspace" (初始化 Stitch 工作区)

## How to use this skill

1.  **Analyze the User Request**: Extract a meaningful `title` for the project.
    *   *User*: "Design a cyberpunk blog." -> *Title*: "Cyberpunk Blog"
    *   *User*: "Make a login page." -> *Title*: "Login Page Project" (Generic)

2.  **Call the MCP Tool**: Invoke `create_project` with the `title`.
    *   If your client namespaces MCP tools, call `mcp__<serverName>__create_project`.

3.  **Handle the Output (CRITICAL)**:
    *   The tool returns a `name` field (e.g., `projects/123456`).
    *   **YOU MUST EXTRACT THE NUMERIC ID**.
    *   *Example*: `projects/123456` -> `123456`.
    *   Store **BOTH** the full name (`projects/123...`) and the numeric ID (`123...`) in your context.
    *   **Usage Rule**:
    *   Use **Numeric ID** (`123...`) for `generate_screen_from_text` and `get_screen`.
    *   Use **Full Name** (`projects/123...`) for `list_screens` and `get_project`.

## Best Practices

1.  **Meaningful Titles**: Always try to infer a descriptive title. Avoid "Untitled Project".
2.  **One Project per Domain**: Encourage users to keep related screens (Login, Home, Settings) in the same project. Only create a new project if the domain changes.
3.  **Context Persistency**: Explicitly tell the user: "I've created project 'X' (ID: 123). I will use this for our design session."

## Keywords

**English keywords:**
create project, new project, start app, initialize, setup, workspace, container, new design, project id, stitch project

**Chinese keywords (中文关键词):**
创建项目, 新建项目, 开始设计, 初始化, 建立工程, 新应用, 项目ID, 启动项目

## References

- [Examples](examples/usage.md)
