---
name: stitch-mcp-list-screens
description: "List all screens within a specific Stitch project, returning screen names, titles, thumbnails, and device types. Use when the user wants to browse generated designs, find a specific screen to iterate on, or select a screenId for export via get_screen. Requires projectId in projects/{id} format."
allowed-tools: "stitch*:*, Read, Write"
---


# List Screens

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Stitch".**

Lists all screens contained within a specific project.

## Use Case
Invoke this skill to browse the history of generated designs in a project or to find a specific screen to reference or iterate upon.

## Input Parameters

The skill expects you to extract the following information from the user request:
*   `projectId` (required): The ID of the project. **Format**: `projects/{project_id}`.

## Output Schema

Returns an object with `screens` array:
*   **`screens`**:
    *   `name`: Resource identifier (e.g., `projects/123/screens/abc`).
    *   `title`: Auto-generated title.
    *   `screenshot`: Thumbnail URL.
    *   `deviceType`: The device type of the screen.

## Usage Example

User Input: "Show me all screens in this project."

Agent Action:
1.  Extract project ID.
2.  Call `list_screens` tool with arguments `{"projectId": "projects/123456"}`.

## References

- [Examples](examples/usage.md)
