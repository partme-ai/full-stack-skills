<div align="center">

# Pencil Skills (Alpha)

**Pencil AI Design Partner - Your Senior UX/UI Design Partner**

![Version](https://img.shields.io/badge/Version-0.0.1-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Role](https://img.shields.io/badge/Role-UX%2FUI%20Partner-purple)

</div>

## 📖 Introduction

**Pencil Skills** is a collection of professional design skills based on the [Agent Skills Specification](https://agentskills.io/specification) and [Claude 自定义 Skills 指南](https://support.claude.com/zh-CN/articles/12512198-如何创建自定义-skills). It goes beyond simple tool wrapping, aiming to transform AI into a **"Pencil AI Design Partner"**.

- **Skill index (discovery)**：[docs/skills-index.md](docs/skills-index.md) — 所有技能的 name 与简短 description。
- **规范符合性**：[spec/agent-skills-spec.md](spec/agent-skills-spec.md) — 目录结构、SKILL.md 格式、渐进式披露。

With these skills, the Agent is no longer just a drawing command executor, but a design partner with the following traits:
- **Role**: Senior UX/UI Designer & Tool Expert.
- **Core Capabilities**: Understanding abstract design requirements, following design systems, precise canvas manipulation, and visual verification.
- **Interaction Style**: Professional, guided, and iterative.

## 🏗️ Architecture Overview

```mermaid
graph TD
    %% Styles
    classDef user fill:#e1f5fe,stroke:#01579b,stroke-width:2px,rx:10,ry:10;
    classDef orchestrator fill:#fff3e0,stroke:#ff6f00,stroke-width:2px,rx:5,ry:5;
    classDef ds fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,rx:5,ry:5;
    classDef atomic fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,rx:5,ry:5;
    classDef app fill:#212121,stroke:#000000,stroke-width:2px,color:#fff,rx:5,ry:5;

    %% Nodes
    User([User Input]):::user
    Orchestrator[Orchestrator<br/>pencil-ui-designer]:::orchestrator
    
    subgraph "Design System Layer"
        DS_uView[pencil-ui-design-system-uviewpro]:::ds
        DS_Element[pencil-ui-design-system-element-plus]:::ds
        DS_Vant[pencil-ui-design-system-vant]:::ds
        DS_More[...]:::ds
    end

    subgraph "Atomic Layer (Pencil MCP)"
        MCP_Design[pencil-mcp-batch-design]:::atomic
        MCP_Read[pencil-mcp-batch-get]:::atomic
        MCP_State[pencil-mcp-get-editor-state]:::atomic
        MCP_More[...]:::atomic
    end

    PencilApp[Pencil App<br/>MCP Server]:::app

    %% Edges
    User -->| "Use Pencil to design..." | Orchestrator
    Orchestrator -->| "Use uView Pro..." | DS_uView
    Orchestrator -->| "Use Element Plus..." | DS_Element
    Orchestrator -->| "Use Vant..." | DS_Vant
    
    DS_uView & DS_Element & DS_Vant -->| "JSON Operations" | MCP_Design
    DS_uView & DS_Element & DS_Vant -->| "Query Context" | MCP_State
    
    MCP_Design & MCP_Read & MCP_State -->| "MCP Protocol" | PencilApp
```

## 🧩 Atomic Skills Planning

We map Pencil MCP's atomic capabilities into four categories of independent Skills to build a complete Agent design capability matrix.

### A. Project Management
*   **`pencil-mcp-get-editor-state`** (Maps to `get_editor_state`)
    *   **Description**: Get current design environment context.
    *   **Usage**: Understand what is currently selected, canvas position, and environment state before any task.
*   **`pencil-mcp-open-document`** (Maps to `open_document`)
    *   **Description**: Open or create a design document.
    *   **Usage**: Initialize design tasks, create new files, or switch to specific designs.
*   **`pencil-mcp-snapshot-layout`** (Maps to `snapshot_layout`)
    *   **Description**: Get page layout structure snapshot.
    *   **Usage**: Understand the current page's DOM-like tree structure to prepare for layout adjustments.

### B. Design Execution
*   **`pencil-design-reader`** (Maps to `batch_design`)
    *   **Description**: Batch search and read node information.
    *   **Usage**: The Agent's "Eyes". Find specific components (e.g., all nodes named 'Button') or get child structure within a container.
*   **`pencil-design-writer`** (Maps to `batch_get`)
    *   **Description**: Batch execute design changes.
    *   **Usage**: The Agent's "Hands". Core capability for inserting, updating, moving, or deleting nodes.
*   **`pencil-canvas-space`** (Maps to `find_empty_space_on_canvas`)
    *   **Description**: Smartly find empty canvas space.
    *   **Usage**: Automatically plan artboard placement to avoid overlap and keep the canvas organized.
*   **`pencil-prop-search`** (Maps to `search_all_unique_properties`)
    *   **Description**: Global property search.
    *   **Usage**: Design audit, e.g., "Find all nodes using red background (#FF0000)".
*   **`pencil-prop-replace`** (Maps to `replace_all_matching_properties`)
    *   **Description**: Global property batch replace.
    *   **Usage**: Global style adjustment, e.g., "Replace all red backgrounds with brand blue".

### C. Visual Guidelines
*   **`pencil-mcp-get-guidelines`** (Maps to `get_guidelines`)
    *   **Description**: Get design system guidelines.
    *   **Usage**: Read and understand specifications (e.g., Material Design, iOS HIG, or custom specs) before designing.
*   **`pencil-mcp-get-style-guide-tags`** (Maps to `get_style_guide_tags`)
    *   **Description**: Explore design style tags.
    *   **Usage**: Get design inspiration, such as "Modern", "Dark Mode", "SaaS" directions.
*   **`pencil-mcp-get-style-guide`** (Maps to `get_style_guide`)
    *   **Description**: Get specific style detailed definitions.
    *   **Usage**: Get metadata for a specific style, including palettes, typography rules, etc.
*   **`pencil-mcp-get-variables`** (Maps to `get_variables`)
    *   **Description**: Read design variables (Tokens).
    *   **Usage**: Get Design Tokens (color, font variables) defined in the current document to ensure consistency.
*   **`pencil-mcp-set-variables`** (Maps to `set_variables`)
    *   **Description**: Set or update design variables.
    *   **Usage**: Establish or maintain a Design Token system.

### D. Canvas Insight
*   **`pencil-visual-check`** (Maps to `get_screenshot`)
    *   **Description**: Get node visual screenshot.
    *   **Usage**: **Visual Verification**. Capture screenshots after operations to verify if the design meets expectations (e.g., text overflow, alignment issues).

---

## 💡 UED Interaction Guidelines

To make the Agent work like a senior designer, we established the following interaction principles and workflows.

### 3.1 The Design Loop
1.  **Understand**: Ask for user intent, call `pencil-mcp-get-editor-state` to get context.
2.  **Explore**: Check existing component libraries via `pencil-mcp-batch-get` and consult guidelines via `pencil-mcp-get-guidelines`.
3.  **Propose**: Briefly outline the steps before executing complex operations (e.g., "I will create a login page Frame on the right side of the canvas...").
4.  **Execute**: Call `pencil-mcp-batch-design` for batch design operations.
5.  **Verify**: Call `pencil-mcp-get-screenshot` to capture results and self-evaluate design quality.
6.  **Feedback**: Show results to the user and ask for adjustments.

### 3.2 Key Principles
*   **Read Before Write**: Always read node state before modifying to avoid overwriting user data.
*   **Atomic Commits**: Break complex designs into steps (e.g., Frame -> Content -> Styling), ensuring each step succeeds before moving on.
*   **Visual Feedback First**: Proactively provide screenshot links or detailed visual descriptions after major changes.
*   **Design Token Priority**: Use variables (e.g., `var.primary`) instead of hardcoded values (e.g., `#FF0000`) for maintainability.

---

## 🛠️ UX Implementation Guide

How to translate abstract UX requirements into specific Pencil operations.

### Step 1: Wireframing
*   **Action**: Use `pencil-mcp-batch-design` to create basic containers (Frames).
*   **Strategy**: Use Auto Layout (Flexbox logic) instead of absolute positioning for flexibility.
*   **Skill Combo**:
    1.  `pencil-mcp-find-empty-space-on-canvas` (Find space)
    2.  `pencil-mcp-batch-design` (Create Frame with Layout props)

### Step 2: Component Assembly
*   **Action**: Reuse existing component libraries.
*   **Strategy**: Search (`pencil-mcp-batch-get` for Design System) then Instantiate (Instance).
*   **Skill Combo**:
    1.  `pencil-mcp-batch-get` (Find Component ID)
    2.  `pencil-mcp-batch-design` (Insert Instance)

### Step 3: Content Injection
*   **Action**: Fill real copy and images.
*   **Strategy**: Maintain semantic layer naming (e.g., "Title", "Avatar", "Submit Button") for easier lookup.

### Step 4: Responsiveness
*   **Action**: Set Constraints and Resizing properties.
*   **Strategy**: Ensure `horizontalResizing` and `verticalResizing` are set correctly (Fill/Hug/Fixed) for different screen sizes.

