---
name: stitch-mcp-get-project
description: Retrieves the detailed metadata of a specific Stitch project.
allowed-tools:
  - "stitch*:*"
  - "Read"
  - "Write"
---


# Get Stitch Project Details

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Stitch".**

## Constraints

**Do NOT use this skill if:**
*   You already have both `projectId` and `screenId` and your goal is to get screen details or code. Use `stitch-mcp-get-screen` directly instead.

This skill retrieves the detailed metadata of a specific Stitch project.

## Use Case
Invoke this skill when you need to know the context of a project (e.g., its default theme, device type) before generating new screens, or to verify project existence.

## Input Parameters

The skill expects you to extract the following information from the user request:
*   `name` (required): The resource name of the project. Format: `projects/{project_id}`.

## Resource Path Parsing

If the user provides a resource path or URL, use the following rules to extract the project name:

1.  **Format**: `web application/stitch/projects/{projectId}`
    *   **Logic**: Extract `projectId` and construct the name as `projects/{projectId}`.

2.  **Format**: `projects/{projectId}`
    *   **Logic**: Use the string as is.

3.  **Format**: `https://stitch.withgoogle.com/projects/{projectId}`
    *   **Logic**: Extract `projectId` and construct the name as `projects/{projectId}`.

**Example**: Input "Describe web application/stitch/projects/12345", Call `get_project(name="projects/12345")`.

## Output Schema

Returns a `Project` object including:
*   `name`, `title`, `createTime`, `updateTime`
*   `designTheme`: Detailed theme settings.
*   `screenInstances`: List of screen instances currently in the project.

## Usage Example

User Input: "What is the theme of project 'projects/123'?"

Agent Action:
1.  Identify the user wants details of a specific project.
2.  Extract project name "projects/123".
3.  Call `get_project` tool with arguments `{"name": "projects/123"}`.

## References

- [Examples](examples/usage.md)
