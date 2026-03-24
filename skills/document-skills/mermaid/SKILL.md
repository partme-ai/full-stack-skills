---
name: mermaid
description: Provides comprehensive guidance for creating Mermaid diagrams. Mermaid is a JavaScript-based diagramming and charting tool that uses Markdown-inspired text definitions and a renderer to create and modify complex diagrams. The main purpose of Mermaid is to help documentation catch up with development. Mermaid is particularly well-suited for use in Markdown documents, GitHub, GitLab, wikis, blogs, and other Markdown-based platforms. Use when the user wants to draw, create, generate, make, build, or visualize any diagram, chart, graph, flowchart, architecture diagram, sequence diagram, class diagram, state diagram, Gantt chart, mindmap, timeline, or any other visual diagram in Markdown-friendly format. This skill covers all 23+ Mermaid diagram types including flowcharts, sequence diagrams, class diagrams, state diagrams, ER diagrams, Gantt charts, pie charts, quadrant charts, Git graphs, C4 diagrams, mindmaps, timelines, and more. Always use this skill when the user mentions Mermaid, needs diagrams for Markdown documentation, or wants quick diagrams that render directly in Markdown renderers.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Drawing, creating, generating, making, or building any diagram, chart, or graph
- Visualizing processes, workflows, systems, architectures, or data
- Any request to "画图" (draw diagram), "绘图" (draw chart), "生成图" (generate diagram), "创建图" (create diagram)
- Flowcharts, sequence diagrams, class diagrams, state diagrams, or any diagram type
- Architecture diagrams, system diagrams, or design diagrams
- Data visualization, charts, or graphs
- Process flows, workflows, or business processes
- Project timelines, schedules, or Gantt charts
- User journeys, mindmaps, or hierarchical structures
- Database schemas, ER diagrams, or entity relationships
- Git branching structures or version control diagrams
- Any visual representation or diagrammatic content

**Trigger phrases include:**
- "画一个图" (draw a diagram), "画流程图" (draw flowchart), "画架构图" (draw architecture diagram)
- "创建一个图表" (create a chart), "生成一个图" (generate a diagram)
- "帮我画" (help me draw), "给我画" (draw for me), "画出来" (draw it out)
- "用图表示" (represent with diagram), "可视化" (visualize), "画个图说明" (draw a diagram to explain)
- "流程图" (flowchart), "时序图" (sequence diagram), "类图" (class diagram), "状态图" (state diagram)
- "架构图" (architecture diagram), "系统图" (system diagram), "设计图" (design diagram)
- "甘特图" (Gantt chart), "思维导图" (mindmap), "时间线" (timeline)
- "用 Mermaid" (use Mermaid), "Mermaid 画图" (draw with Mermaid), "Mermaid 语法" (Mermaid syntax)
- Any mention of "diagram", "chart", "graph", "flowchart", "visualization", "drawing", "Mermaid"

**IMPORTANT: Mermaid vs PlantUML - Two Different Diagramming Tools:**

Mermaid and PlantUML are two different diagramming tools with different purposes:

- **Mermaid**: A JavaScript-based diagramming tool designed for Markdown documentation. It uses Markdown-inspired syntax and renders directly in Markdown renderers (GitHub, GitLab, wikis, blogs). Best for quick diagrams, Markdown documentation, and simple visualizations. Output format is fenced Markdown code blocks with the `mermaid` language tag.

- **PlantUML**: A component that allows you to create various UML diagrams through simple textual descriptions. It focuses on UML standards and complex system architecture. Best for UML diagrams, enterprise architecture, C4 models, and diagrams requiring precise UML notation. Output format is `@startuml`/`@enduml` blocks or `.puml` files.

**When both PlantUML and Mermaid skills are matched:**
- If the user explicitly mentions "Mermaid" or "Markdown diagram", use this skill (Mermaid)
- If the user explicitly mentions "PlantUML", "UML diagram", or "C4 model", use the PlantUML skill instead
- If the user references Markdown contexts (README, wiki, GitHub/GitLab, blog), default to Mermaid
- If the user references UML standards or `.puml`, default to PlantUML
- If the user mentions both or neither, **ALWAYS ask the user to choose**: "I can create this diagram using either Mermaid (Markdown code block) or PlantUML (@startuml). Which output format do you prefer?"

## How to use this skill

**CRITICAL: Mermaid is a Markdown-focused diagramming tool. This skill should be triggered when the user explicitly mentions "Mermaid", needs diagrams for Markdown documentation, or wants diagrams that render directly in Markdown renderers (GitHub, GitLab, wikis, blogs).**

**Trigger this skill when you see:**
- User says "用 Mermaid" (use Mermaid), "Mermaid 画图" (draw with Mermaid), "Markdown 图" (Markdown diagram)
- User needs diagrams for Markdown documentation, GitHub, GitLab, wikis, or blogs
- User wants quick diagrams that render directly in Markdown renderers
- User mentions any diagram type for Markdown: flowchart, sequence diagram, class diagram, etc.
- User wants to visualize, represent, or illustrate something with a diagram in Markdown format

**When both PlantUML and Mermaid are matched, ALWAYS ask the user to choose the output format or tool, as they are two different diagramming tools with different purposes.**

To create a Mermaid diagram:

1. **Identify the diagram type** from the user's request:
   - Flowchart/flow chart/流程图 → `flowchart` or `graph`
   - Sequence diagram/时序图 → `sequenceDiagram`
   - Class diagram/类图 → `classDiagram`
   - State diagram/状态图 → `stateDiagram` or `stateDiagram-v2`
   - Entity relationship diagram/实体关系图 → `erDiagram`
   - User journey/用户旅程图 → `journey`
   - Gantt chart/甘特图 → `gantt`
   - Pie chart/饼图 → `pie`
   - Quadrant chart/象限图 → `quadrantChart`
   - Requirement diagram/需求图 → `requirementDiagram`
   - Git graph/Git图 → `gitGraph`
   - C4 diagram/C4图 → `C4Context`, `C4Container`, `C4Component`, `C4Deployment`, or `C4Dynamic`
   - Mindmap/思维导图 → `mindmap`
   - Timeline/时间线图 → `timeline`
   - ZenUML/禅UML → `zenuml`
   - Sankey diagram/桑基图 → `sankey`
   - XY chart/XY图 → `xychart`
   - Block diagram/方块图 → `block`
   - Packet diagram/数据包图 → `packet`
   - Kanban/看板图 → `kanban`
   - Architecture diagram/架构图 → `architecture-beta` (requires Mermaid v11.1.0+)
   - Radar chart/雷达图 → `radar-beta` (requires Mermaid v11.1.0+)
   - Treemap/树状图 → `treemap-beta` (requires Mermaid v11.1.0+)

2. **Load the appropriate example file** from the `examples/` directory:
   - `examples/flowchart.md` - For flowcharts and process diagrams
   - `examples/sequence.md` - For sequence diagrams showing interactions
   - `examples/class.md` - For class diagrams and object-oriented designs
   - `examples/state.md` - For state diagrams and state machines
   - `examples/er.md` - For entity relationship diagrams
   - `examples/journey.md` - For user journey maps
   - `examples/gantt.md` - For Gantt charts and project timelines
   - `examples/pie.md` - For pie charts
   - `examples/quadrant.md` - For quadrant charts
   - `examples/requirement.md` - For requirement diagrams
   - `examples/gitgraph.md` - For Git branching diagrams
   - `examples/c4.md` - For C4 architecture diagrams
   - `examples/mindmap.md` - For mindmaps
   - `examples/timeline.md` - For timeline diagrams
   - `examples/zenuml.md` - For ZenUML diagrams
   - `examples/sankey.md` - For Sankey flow diagrams
   - `examples/xychart.md` - For XY charts (bar/line charts)
   - `examples/block.md` - For block diagrams
   - `examples/packet.md` - For packet diagrams
   - `examples/kanban.md` - For Kanban boards
   - `examples/architecture.md` - For architecture diagrams
   - `examples/radar.md` - For radar charts
   - `examples/treemap.md` - For treemap diagrams

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Beta diagram types (`architecture-beta`, `radar-beta`, `treemap-beta`) require Mermaid v11.1.0 or higher
   - If the rendering environment doesn't support beta diagram types, use the flowchart alternatives provided in the example files
   - Always check the example file for version compatibility notes and alternative syntax options

4. **Generate the Mermaid code** wrapped in a Markdown code block with proper syntax highlighting:
   
   **IMPORTANT**: Always wrap the Mermaid code in a Markdown code block with `mermaid` language tag. This ensures the format is preserved when users copy the content.
   
   **Example format** (use actual Mermaid syntax, not placeholders):
   ```mermaid
   flowchart TD
       A[Start] --> B[Process]
       B --> C[End]
   ```
   
   **Output Format Requirements**:
   - Always use triple backticks (```) with `mermaid` language tag
   - Never output raw Mermaid code without code block markers
   - The code block must be complete and properly formatted
   - Use actual valid Mermaid syntax, not placeholders like `<diagram-type>` or `...diagram content...`
   - This ensures users can copy the code without losing formatting

5. **Include styling and configuration** when needed:
   - Use `%%{ init: { theme: 'base' } }%%` for theme configuration
   - Apply `style` directives for node styling
   - Use `classDef` for reusable style classes

6. **Validate the syntax**:
   - Ensure all required elements are present
   - Check that relationships and connections are properly defined
   - Verify date formats for Gantt charts (YYYY-MM-DD)
   - Confirm data formats for charts (pie, quadrant, etc.)
   - For ER diagrams: Use underscores instead of hyphens in entity names (e.g., `LINE_ITEM` not `LINE-ITEM`)
   - For flowcharts: Avoid using "end" as a node label (use "End" or "END" instead)
   - For class diagrams: Escape special characters in labels using backticks
   - Check version compatibility for beta diagram types

7. **Save the diagram to project directory**:
   - **Default behavior**: When generating a Mermaid diagram, save it to the current project directory
   - **Recommended locations**:
     - `docs/diagrams/` - For documentation diagrams
     - `docs/` - For general documentation
     - `diagrams/` - For standalone diagram files
     - Current directory (`.`) - If no specific directory structure exists
   - **File naming**: Use descriptive names like `system-architecture.md`, `user-flow.md`, `database-schema.md`, etc.
   - **File format**: Save as `.md` file with the Mermaid code block inside
   - **Example**: If user requests a system architecture diagram, save it as `docs/diagrams/system-architecture.md` or `diagrams/system-architecture.md`
   - **Ask if needed**: If the project structure is unclear, ask the user where they'd like the diagram saved, but default to creating a `docs/` or `diagrams/` directory if it doesn't exist

**Output Format and File Saving**:

When generating a diagram, follow this response structure:

1. **Save the file first**: Create the diagram file in the project directory (e.g., `docs/diagrams/system-architecture.md`)

2. **Inform the user**: Tell them where the file was saved

3. **Display the diagram**: Show the Mermaid code in a properly formatted Markdown code block with `mermaid` language tag

**Example Response Structure**:
- First line: "I've created the Mermaid diagram and saved it to `docs/diagrams/system-architecture.md`."
- Then show the diagram wrapped in a code block:
  - Start with: three backticks + `mermaid` + newline
  - Then the Mermaid code
  - End with: three backticks + newline

**Critical Requirements**:
- The Mermaid code block MUST ALWAYS be properly formatted with triple backticks (```) and `mermaid` language tag
- NEVER output raw Mermaid code without code block markers
- The code block must be complete (opening and closing backticks)
- This ensures users can copy the code without losing formatting
- Always save the diagram file to the current project directory (default: `docs/diagrams/` or `diagrams/`)

If the diagram type doesn't match any existing example, refer to the Mermaid documentation or ask the user for clarification about the desired visualization.

## Version Compatibility

Some diagram types have specific version requirements:

- **Beta diagram types** (require Mermaid v11.1.0+):
  - `architecture-beta` - Architecture diagrams
  - `radar-beta` - Radar charts
  - `treemap-beta` - Treemap diagrams

- **Advanced features** (require specific versions):
  - Participant types with JSON configuration: Mermaid v10.0.0+
  - Actor creation/destruction: Mermaid v10.3.0+
  - Edge IDs and curve styles: Mermaid v11.10.0+
  - New shapes with `@{}` syntax: Mermaid v11.3.0+

If a beta diagram type is not supported, the example files provide flowchart alternatives that work with all Mermaid versions.

## Best Practices

1. **Always use code blocks**: Wrap all Mermaid code in Markdown code blocks with `mermaid` language tag
2. **Check compatibility**: Verify version requirements before using beta diagram types
3. **Use alternatives**: When beta types aren't supported, use the provided flowchart alternatives
4. **Follow naming conventions**: Avoid reserved keywords and special characters in node labels
5. **Test syntax**: Validate diagram syntax before saving to ensure proper rendering
6. **Organize files**: Save diagrams in appropriate directories (`docs/diagrams/` or `diagrams/`)
7. **Use descriptive names**: Name diagram files clearly (e.g., `system-architecture.md`, `user-flow.md`)

## Mermaid vs PlantUML - Key Differences

**Mermaid (This Skill):**
- **Purpose**: JavaScript-based diagramming tool designed for Markdown documentation
- **Main Use Case**: Help documentation catch up with development
- **Best For**: 
  - Markdown documents, GitHub, GitLab, wikis, blogs
  - Quick diagrams that render directly in Markdown renderers
  - Simple flowcharts, sequence diagrams, basic charts
  - Rapid prototyping and iteration
  - When the user explicitly requests Mermaid or needs Markdown-compatible diagrams

**PlantUML (Different Skill):**
- **Purpose**: Component for creating various UML diagrams through textual descriptions
- **Main Use Case**: UML-focused diagramming with emphasis on standard UML notation
- **Best For**:
  - Complex UML diagrams requiring precise notation (class, component, deployment diagrams)
  - Enterprise architecture diagrams and C4 model diagrams
  - Standard UML compliance requirements
  - Diagrams requiring advanced customization, styling, or layout control
  - When the user explicitly requests PlantUML or UML diagrams

**When Both Skills Are Matched:**
- **ALWAYS ask the user to choose**: "I can create this diagram using either Mermaid or PlantUML. Mermaid is a JavaScript-based tool designed for Markdown documentation and renders directly in GitHub/GitLab. PlantUML is focused on UML diagrams and enterprise architecture. Which would you prefer?"
- These are two different diagramming tools with different purposes - do not automatically choose one
- If the user explicitly mentions one tool, use that tool
- If the user mentions both or neither, ask the user to choose based on their needs

## Keywords

**English keywords:**
mermaid, diagram, chart, graph, flowchart, flow chart, sequence diagram, class diagram, state diagram, entity relationship, ER diagram, user journey, Gantt chart, pie chart, quadrant chart, requirement diagram, Git graph, C4 diagram, mindmap, timeline, ZenUML, Sankey diagram, XY chart, block diagram, packet diagram, Kanban, architecture diagram, radar chart, treemap, draw, create, generate, make, build, visualize, visualization, drawing, plotting, mapping, schematics, blueprint, design diagram, system diagram, process flow, workflow, data visualization, visual representation

**Chinese keywords (中文关键词):**
流程图, 时序图, 类图, 状态图, 实体关系图, 用户旅程图, 甘特图, 饼图, 象限图, 需求图, Git图, C4图, 思维导图, 时间线图, 桑基图, XY图, 方块图, 数据包图, 看板图, 架构图, 雷达图, 树状图, 画图, 绘图, 生成图, 创建图, 制作图, 画流程图, 画架构图, 画时序图, 画类图, 画状态图, 画甘特图, 画思维导图, 画时间线, 可视化, 图表, 图形, 示意图, 设计图, 系统图, 流程图, 架构图, 时序图, 类图, 状态图, 甘特图, 思维导图, 时间线, 用图表示, 画出来, 给我画, 帮我画, 画一个, 创建一个图, 生成一个图, 画个图说明, 用图表展示, 可视化展示
