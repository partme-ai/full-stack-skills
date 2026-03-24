---
name: stitch-mcp-get-screen
description: Retrieves the full details of a specific screen, including HTML code.
allowed-tools:
  - "stitch*:*"
  - "Read"
  - "Write"
---


# Get Screen Details

**CRITICAL PREREQUISITE:**
**You must ONLY use this skill when the user EXPLICITLY mentions "Stitch".**

Retrieves the full details of a specific screen, including its HTML code and high-res screenshot.

## Use Case
Invoke this skill when the user wants to "export" the code, view the full design details, or when the Agent needs to analyze the generated HTML structure.

## Input Parameters

The skill expects you to extract the following information from the user request:
*   `projectId` (required): The project ID. **Format**: Pure ID (e.g., `37803...`), no `projects/` prefix.
*   `screenId` (required): The screen ID. **Format**: Pure ID (e.g., `88805...`), no `screens/` prefix.

**CRITICAL:** When `projectId` and `screenId` are both available, call `stitch-mcp-get-screen` directly. Do NOT call `stitch-mcp-get-project`.

## Resource Path Parsing

If the user provides a resource path or URL, use the following rules to extract `projectId` and `screenId`:

1.  **Format**: `web application/stitch/projects/{projectId}/screens/{screenId}`
    *   **Logic**: Extract `projectId` and `screenId` directly from the path segments.
    *   **Example**: `web application/stitch/projects/3492931393329678076/screens/2e22a9fb99ba49ddb6ce8907a1e74d60` -> `projectId="3492931393329678076"`, `screenId="2e22a9fb99ba49ddb6ce8907a1e74d60"`.

2.  **Format**: `projects/{projectId}/screens/{screenId}`
    *   **Logic**: Extract `projectId` and `screenId` from the path segments.

**Agent flow:**
1.  Recognize the user input matches one of the above formats.
2.  Extract `projectId` and `screenId`.
3.  Call `get_screen` with `{"projectId": "<extracted projectId>", "screenId": "<extracted screenId>"}`.
4.  Use the returned `htmlCode.downloadUrl`, `screenshot.downloadUrl`, and metadata for design-to-code (e.g. stitch-design-md or a framework conversion skill).

## Output Schema

Returns a `Screen` object:
*   **`htmlCode`**: The actual HTML/CSS code of the UI.
*   **`screenshot`**: High-resolution image URL.
*   **`figmaExport`**: Figma file asset.
*   `width`, `height`, `deviceType`.

## Intent Recognition & Framework Conversion

After retrieving the screen details (HTML code), check if the user's request implies converting the design to a specific frontend framework.

**Logic:**
1.  **Identify Framework**: Look for specific keywords in user input (e.g., "uView", "uViewPro", "Vue", "React", "Flutter").
2.  **Locate Skill**: Search for and read the corresponding skill definition file to understand the "Design Contract" or conversion rules.
    *   **uViewPro / uni-app**: If user mentions "uView", "uViewPro" or "UniApp", you **MUST** load and reference the complete context from the `stitch-uviewpro-components` skill to ensure accurate code generation.
        *   **References**: Read `skills/stitch-uviewpro-components/references/` (especially `contract.md` and `tailwind-to-uviewpro.md`) for core mapping rules.
        *   **API**: Read `skills/stitch-uviewpro-components/api/component-api.md` for component props and event definitions.
        *   **Examples**: Read `skills/stitch-uviewpro-components/examples/usage.md` for correct implementation patterns.
        *   **Resources**: Read `skills/stitch-uviewpro-components/resources/architecture-checklist.md` for design compliance.

    *   **uView (Standard)**: If user mentions "uView" (without "Pro") or "uView 2.0", load `stitch-uview-components`.
        *   **Context**: Read `references/` (contract, tailwind-to-uview), `api/component-api.md`, `examples/usage.md`, `resources/architecture-checklist.md` from `stitch-uview-components`.

    *   **Element Plus**: If user mentions "Element Plus", "Element", "Vue Desktop", load `stitch-vue-element-components`.
        *   **Context**: Read `references/` (contract, tailwind-to-element-plus), `api/component-api.md`, `examples/usage.md`, `resources/architecture-checklist.md` from `stitch-vue-element-components`.

    *   **Vant UI**: If user mentions "Vant", "Vue Mobile", load `stitch-vue-vant-components`.
        *   **Context**: Read `references/` (contract, tailwind-to-vant), `api/component-api.md`, `examples/usage.md`, `resources/architecture-checklist.md` from `stitch-vue-vant-components`.

    *   **Layui Vue**: If user mentions "Layui", load `stitch-vue-layui-components`.
        *   **Context**: Read `references/` (contract, tailwind-to-layui), `api/component-api.md`, `examples/usage.md`, `resources/architecture-checklist.md` from `stitch-vue-layui-components`.

    *   **Bootstrap Vue**: If user mentions "Bootstrap", load `stitch-vue-bootstrap-components`.
        *   **Context**: Read `references/` (contract, tailwind-to-bootstrap), `api/component-api.md`, `examples/usage.md`, `resources/architecture-checklist.md` from `stitch-vue-bootstrap-components`.

    *   **React / Tailwind**: If user mentions "React" (standard), load `stitch-react-components`.
        *   **Context**: Read `references/tailwind-to-react.md`, `examples/usage.md`, `resources/architecture-checklist.md` from `stitch-react-components`.

    *   **Shadcn UI**: If user mentions "Shadcn", "Next.js", "Radix", load `stitch-shadcn-ui`.
        *   **Context**: Read `references/tailwind-to-shadcn.md`, `examples/usage.md` from `stitch-shadcn-ui`.

    *   **Other Frameworks**: Search for matching `stitch-*-components` skills and load their respective `api`, `examples`, and `references` directories.
3.  **Apply Constraints**: Use the rules defined in that framework's skill (e.g., component mappings, slot usage, unit conversion) to transform the raw HTML from Stitch into the target framework code.

**Example Flow:**
*   User: "Get screen X and convert to uViewPro code."
*   Agent:
    1.  Call `get_screen` to get HTML.
    2.  Detect intent: "uViewPro".
    3.  **Load Context**: Read `contract.md`, `component-api.md`, `usage.md`, and `architecture-checklist.md` from `stitch-uviewpro-components`.
    4.  Generate code by applying uViewPro rules to the Stitch HTML.

## Usage Example

User Input: "Give me the code for the login screen we just made."

Agent Action:
1.  Identify target screen.
2.  Call `get_screen` tool with arguments `{"projectId": "37803...", "screenId": "88805..."}`.

## References

- [Examples](examples/usage.md)
