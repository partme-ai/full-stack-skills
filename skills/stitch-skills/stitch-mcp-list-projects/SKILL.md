---
name: stitch-mcp-list-projects
description: Lists all Stitch projects accessible to the user.
allowed-tools:
  - "stitch*:*"
  - "Read"
  - "Write"
---


# List Stitch Projects

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Stitch".**

This skill lists all Stitch projects accessible to the user.

## Use Case
Invoke this skill when the user wants to resume work on an existing project, or needs to check what projects are currently available.

## Input Parameters

The skill expects you to extract the following information from the user request:
*   `filter` (optional): Filter for projects to list. Defaults to `"view=owned"`.
    *   `"view=owned"`: Projects owned by user.
    *   `"view=shared"`: Projects shared with user.

## Output Schema

Returns an object containing a list of projects:
*   **`projects`**: (Array of Project)
    *   `name`: Resource ID (e.g., `projects/123...`).
    *   `title`: Project title.
    *   `updateTime`: Last modification time.
    *   `thumbnailScreenshot`: Preview image of the project.

## Usage Example

User Input: "Show me my existing projects."

Agent Action:
1.  Identify the user wants to list projects.
2.  Call `list_projects` tool with arguments `{"filter": "view=owned"}`.

## References

- [Examples](examples/usage.md)
