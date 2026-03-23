---
name: plantuml
description: Provides comprehensive guidance for creating PlantUML diagrams. PlantUML is a component that allows you to create various UML diagrams through simple textual descriptions. From sequence diagrams to deployment diagrams and beyond, PlantUML provides an easy way to create visual representations of complex systems. PlantUML is primarily focused on UML standards and is ideal for UML diagrams, enterprise architecture, C4 models, and diagrams requiring precise UML notation. Use when the user wants to draw, create, generate, make, build, or visualize any UML diagram, architecture diagram, or PlantUML-supported diagram type. This skill covers ALL PlantUML diagram types: UML Diagrams (sequence, use case, class, object, activity, component, deployment, state, timing diagrams), and Non-UML Diagrams (JSON/YAML data, EBNF, regex, network diagrams, Salt wireframes, Archimate, SDL, Ditaa, Gantt, chronology, mindmap, WBS, mathematical notations, ER diagrams, IE diagrams, ER Chen's notation, C4 model diagrams). Always use this skill when the user mentions PlantUML, UML diagrams, or complex architecture diagrams that require precise UML notation or C4 model support.
license: Complete terms in LICENSE.txt
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**
- PlantUML, UML diagrams, or explicitly requests PlantUML syntax
- Complex architecture diagrams, C4 model diagrams, or enterprise-level diagrams
- Standard UML diagrams: class diagrams, sequence diagrams, component diagrams, deployment diagrams, state diagrams, activity diagrams, use case diagrams
- Architecture documentation requiring precise UML notation
- Diagrams that need advanced customization, styling, or layout control
- Enterprise system architecture, microservices architecture, or distributed system diagrams
- Any request to "用 PlantUML 画图" (draw with PlantUML), "用 UML 图" (use UML diagram), "画类图" (draw class diagram), "画组件图" (draw component diagram)

**Trigger phrases include:**
- "用 PlantUML" (use PlantUML), "用 PlantUML 画" (draw with PlantUML), "PlantUML 语法" (PlantUML syntax)
- "UML 图" (UML diagram), "类图" (class diagram), "时序图" (sequence diagram), "组件图" (component diagram), "部署图" (deployment diagram)
- "C4 模型" (C4 model), "架构图" (architecture diagram), "系统架构图" (system architecture diagram)
- "活动图" (activity diagram), "状态图" (state diagram), "用例图" (use case diagram)
- "画 UML" (draw UML), "UML 类图" (UML class diagram), "UML 时序图" (UML sequence diagram)
- Any mention of "PlantUML", "UML", "class diagram", "sequence diagram", "component diagram", "deployment diagram", "C4 model"

**IMPORTANT: PlantUML vs Mermaid - Two Different Diagramming Tools:**

PlantUML and Mermaid are two different diagramming tools with different purposes:

- **PlantUML**: A component that allows you to create various UML diagrams through simple textual descriptions. From sequence diagrams to deployment diagrams and beyond, PlantUML provides an easy way to create visual representations of complex systems. PlantUML is primarily focused on UML standards and is ideal for UML diagrams, enterprise architecture, C4 models, and diagrams requiring precise UML notation. Output format is `@startuml`/`@enduml` blocks or `.puml` files.

- **Mermaid**: A JavaScript-based diagramming and charting tool that uses Markdown-inspired text definitions. The main purpose of Mermaid is to help documentation catch up with development. Mermaid is particularly well-suited for use in Markdown documents, GitHub, GitLab, wikis, and blogs. Output format is fenced Markdown code blocks with the `mermaid` language tag.

**When both PlantUML and Mermaid skills are matched:**
- If the user explicitly mentions "PlantUML", "UML diagram", or "C4 model", use this skill (PlantUML)
- If the user explicitly mentions "Mermaid" or "Markdown diagram", use the Mermaid skill instead
- If the user references UML standards or `.puml`, default to PlantUML
- If the user references Markdown contexts (README, wiki, GitHub/GitLab, blog), default to Mermaid
- If the user mentions both or neither, **ALWAYS ask the user to choose**: "I can create this diagram using either PlantUML (@startuml) or Mermaid (Markdown code block). Which output format do you prefer?"

## How to use this skill

**CRITICAL: PlantUML is a UML-focused diagramming tool. This skill should be triggered when the user explicitly mentions PlantUML, UML diagrams, or needs complex architecture diagrams with precise UML notation.**

**Trigger this skill when you see:**
- User says "用 PlantUML" (use PlantUML), "PlantUML 画图" (draw with PlantUML), "UML 图" (UML diagram)
- User mentions UML diagram types: class diagram, sequence diagram, component diagram, deployment diagram, etc.
- User needs C4 model diagrams or enterprise architecture diagrams
- User explicitly requests PlantUML syntax or mentions PlantUML
- User needs diagrams with precise UML notation or standard UML compliance

**When both PlantUML and Mermaid are matched, ALWAYS ask the user to choose the output format or tool, as they are two different diagramming tools with different purposes.**

To create a PlantUML diagram:

1. **Identify the diagram type** from the user's request:
   
   **UML Diagrams:**
   - Sequence diagram/时序图 → `@startuml` ... `@enduml` with `participant` or `actor`
   - Use case diagram/用例图 → `@startuml` ... `@enduml` with `actor`, `usecase`
   - Class diagram/类图 → `@startuml` ... `@enduml` with `class`
   - Object diagram/对象图 → `@startuml` ... `@enduml` with `object`
   - Activity diagram/活动图 → `@startuml` ... `@enduml` with `start`, `stop`, `if`, `while`, etc.
   - Component diagram/组件图 → `@startuml` ... `@enduml` with `component`, `interface`, `package`
   - Deployment diagram/部署图 → `@startuml` ... `@enduml` with `node`, `database`, `cloud`
   - State diagram/状态图 → `@startuml` ... `@enduml` with `state`, `[*]`
   - Timing diagram/时序图 → `@startuml` ... `@enduml` with `concise` or `robust`
   
   **Non-UML Diagrams:**
   - JSON data/JSON 数据图 → `@startjson` ... `@endjson`
   - YAML data/YAML 数据图 → `@startyaml` ... `@endyaml`
   - EBNF (Extended Backus-Naur Form)/EBNF 图 → `@startebnf` ... `@endebnf`
   - Regex (Regular Expression)/正则表达式图 → `@startregex` ... `@endregex`
   - Network diagram (nwdiag)/网络图 → `@startuml` ... `@enduml` with network elements
   - Salt (Wireframe graphical interface)/线框图 → `@startsalt` ... `@endsalt`
   - Archimate diagram/架构图 → `@startuml` ... `@enduml` with Archimate elements
   - SDL (Specification and Description Language)/SDL 图 → `@startsdl` ... `@endsdl`
   - Ditaa diagram/Ditaa 图 → `@startditaa` ... `@endditaa`
   - Gantt diagram/甘特图 → `@startgantt` ... `@endgantt`
   - Chronology diagram/时间线图 → `@startuml` ... `@enduml` with chronology syntax
   - MindMap diagram/思维导图 → `@startmindmap` ... `@endmindmap`
   - WBS (Work Breakdown Structure)/工作分解结构图 → `@startwbs` ... `@endwbs`
   - Mathematical Notations (AsciiMath, JLaTeXMath)/数学公式图 → `@startmath` ... `@endmath` or `@startlatex` ... `@endlatex`
   - Entity Relationship (ER) diagram/实体关系图 → `@startuml` ... `@enduml` with `entity`
   - Information Engineering (IE) diagram/信息工程图 → `@startuml` ... `@enduml` with IE notation
   - Entity Relationship (ER) diagram (Chen's notation)/ER 图（陈氏表示法） → `@startuml` ... `@enduml` with Chen's notation
   - C4 diagram/C4 模型图 → `@startuml` ... `@enduml` with C4-PlantUML library

2. **Load the appropriate example file** from the `examples/` directory:
   
   **UML Diagrams:**
   - `examples/sequence.md` - For sequence diagrams showing interactions
   - `examples/use-case.md` - For use case diagrams
   - `examples/class.md` - For class diagrams and object-oriented designs
   - `examples/object.md` - For object diagrams
   - `examples/activity.md` - For activity diagrams and workflows
   - `examples/component.md` - For component diagrams and system architecture
   - `examples/deployment.md` - For deployment diagrams and infrastructure
   - `examples/state.md` - For state diagrams and state machines
   - `examples/timing.md` - For timing diagrams
   
   **Non-UML Diagrams:**
   - `examples/json-yaml.md` - For JSON/YAML data visualization
   - `examples/ebnf.md` - For EBNF grammar diagrams
   - `examples/regex.md` - For regular expression diagrams
   - `examples/network.md` - For network diagrams (nwdiag)
   - `examples/salt.md` - For Salt wireframes and UI mockups
   - `examples/archimate.md` - For Archimate architecture diagrams
   - `examples/sdl.md` - For SDL (Specification and Description Language) diagrams
   - `examples/ditaa.md` - For Ditaa ASCII art diagrams
   - `examples/gantt.md` - For Gantt charts and project timelines
   - `examples/chronology.md` - For chronology and timeline diagrams
   - `examples/mindmap.md` - For mindmaps
   - `examples/wbs.md` - For work breakdown structure diagrams
   - `examples/math.md` - For mathematical notations (AsciiMath, LaTeX)
   - `examples/er.md` - For Entity-Relationship diagrams
   - `examples/ie.md` - For Information Engineering diagrams
   - `examples/er-chen.md` - For ER diagrams using Chen's notation
   - `examples/c4.md` - For C4 model architecture diagrams

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - PlantUML requires Java runtime environment and Graphviz (or PlantUML server) for rendering
   - All PlantUML diagrams must be wrapped in `@startuml` ... `@enduml` (or diagram-specific tags)
   - Use `!include` directive to include external files or libraries (e.g., C4-PlantUML)
   - Use `!define` and `!include` for reusable components and themes
   - PlantUML supports extensive styling with `skinparam` directives
   - For C4 diagrams, use `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml`

4. **Generate the PlantUML code** wrapped in a Markdown code block with proper syntax highlighting:
   
   **IMPORTANT**: Always wrap the PlantUML code in a Markdown code block with `plantuml` language tag. This ensures the format is preserved when users copy the content.
   
   **Example format** (use actual PlantUML syntax, not placeholders):
   ```plantuml
   @startuml
   Alice -> Bob: Hello
   Bob -> Alice: Hi
   @enduml
   ```
   
   **Output Format Requirements**:
   - Always use triple backticks (```) with `plantuml` language tag
   - Never output raw PlantUML code without code block markers
   - The code block must be complete and properly formatted
   - Use actual valid PlantUML syntax, not placeholders like `<diagram-type>` or `...diagram content...`
   - Always include `@startuml` and `@enduml` tags (or diagram-specific start/end tags)
   - This ensures users can copy the code without losing formatting

5. **Include styling and configuration** when needed:
   - Use `skinparam` directives for global styling
   - Use `skinparam <element> { }` for element-specific styling
   - Use `!theme` directive for predefined themes
   - Use `!define` for custom colors and styles
   - Use `!include` for external libraries and components

6. **Validate the syntax**:
   - Ensure all required elements are present
   - Check that `@startuml` and `@enduml` tags are properly paired
   - Verify relationships and connections are properly defined
   - For class diagrams: Check visibility modifiers (`+`, `-`, `#`, `~`)
   - For sequence diagrams: Verify participant declarations and message syntax
   - For activity diagrams: Ensure proper control flow syntax
   - For component diagrams: Verify component and interface definitions
   - For C4 diagrams: Ensure C4-PlantUML library is included

7. **Save the diagram to project directory**:
   - **Default behavior**: When generating a PlantUML diagram, save it to the current project directory
   - **Recommended locations**:
     - `docs/diagrams/` - For documentation diagrams
     - `docs/` - For general documentation
     - `diagrams/` - For standalone diagram files
     - Current directory (`.`) - If no specific directory structure exists
   - **File naming**: Use descriptive names like `system-architecture.puml`, `user-flow.puml`, `database-schema.puml`, etc.
   - **File format**: Save as `.puml` file (PlantUML standard extension)
   - **Example**: If user requests a system architecture diagram, save it as `docs/diagrams/system-architecture.puml` or `diagrams/system-architecture.puml`
   - **Ask if needed**: If the project structure is unclear, ask the user where they'd like the diagram saved, but default to creating a `docs/` or `diagrams/` directory if it doesn't exist

**Output Format and File Saving**:

When generating a diagram, follow this response structure:

1. **Save the file first**: Create the diagram file in the project directory (e.g., `docs/diagrams/system-architecture.puml`)

2. **Inform the user**: Tell them where the file was saved

3. **Display the diagram**: Show the PlantUML code in a properly formatted Markdown code block with `plantuml` language tag

**Example Response Structure**:
- First line: "I've created the PlantUML diagram and saved it to `docs/diagrams/system-architecture.puml`."
- Then show the diagram wrapped in a code block:
  - Start with: three backticks + `plantuml` + newline
  - Then the PlantUML code (with `@startuml` and `@enduml` tags)
  - End with: three backticks + newline

**Critical Requirements**:
- The PlantUML code block MUST ALWAYS be properly formatted with triple backticks (```) and `plantuml` language tag
- NEVER output raw PlantUML code without code block markers
- The code block must be complete (opening and closing backticks)
- Always include `@startuml` and `@enduml` tags (or diagram-specific start/end tags)
- This ensures users can copy the code without losing formatting
- Always save the diagram file to the current project directory (default: `docs/diagrams/` or `diagrams/`)
- Use `.puml` file extension for PlantUML files

If the diagram type doesn't match any existing example, refer to the PlantUML documentation (https://plantuml.com/zh/) or ask the user for clarification about the desired visualization.

## PlantUML vs Mermaid - Key Differences

**PlantUML (This Skill):**
- **Purpose**: Component for creating various UML diagrams through simple textual descriptions
- **Main Use Case**: From sequence diagrams to deployment diagrams and beyond, PlantUML provides an easy way to create visual representations of complex systems
- **Focus**: Primarily focused on UML standards
- **Best For**:
  - Complex UML diagrams requiring precise notation (class, component, deployment diagrams)
  - Enterprise architecture diagrams and C4 model diagrams
  - Standard UML compliance requirements
  - Diagrams requiring advanced customization, styling, or layout control
  - When the user explicitly requests PlantUML or UML diagrams

**Mermaid (Different Skill):**
- **Purpose**: JavaScript-based diagramming and charting tool that uses Markdown-inspired text definitions
- **Main Use Case**: Help documentation catch up with development
- **Focus**: Markdown documentation and Markdown renderers
- **Best For**:
  - Markdown documents, GitHub, GitLab, wikis, blogs
  - Quick diagrams that render directly in Markdown renderers
  - Simple flowcharts, sequence diagrams, basic charts
  - Rapid prototyping and iteration
  - When the user explicitly requests Mermaid or needs Markdown-compatible diagrams

**When Both Skills Are Matched:**
- **ALWAYS ask the user to choose**: "I can create this diagram using either PlantUML or Mermaid. PlantUML is focused on UML diagrams and enterprise architecture. Mermaid is a JavaScript-based tool designed for Markdown documentation and renders directly in GitHub/GitLab. Which would you prefer?"
- These are two different diagramming tools with different purposes - do not automatically choose one
- If the user explicitly mentions one tool, use that tool
- If the user mentions both or neither, ask the user to choose based on their needs

## Resources

- **Official Documentation**: https://plantuml.com/zh/
- **GitHub Repository**: https://github.com/plantuml/plantuml
- **C4-PlantUML Library**: https://github.com/plantuml-stdlib/C4-PlantUML
- **PlantUML Guide**: https://plantuml.com/zh/guide
- **PlantUML Language Reference**: https://plantuml.com/zh/guide

## Best Practices

1. **Always use code blocks**: Wrap all PlantUML code in Markdown code blocks with `plantuml` language tag
2. **Include proper tags**: Always include `@startuml` and `@enduml` (or diagram-specific tags)
3. **Use includes for libraries**: Use `!include` for C4-PlantUML and other standard libraries
4. **Organize files**: Save diagrams in appropriate directories (`docs/diagrams/` or `diagrams/`)
5. **Use descriptive names**: Name diagram files clearly (e.g., `system-architecture.puml`, `user-flow.puml`)
6. **Leverage styling**: Use `skinparam` and themes for consistent styling
7. **Validate syntax**: Check PlantUML syntax before saving to ensure proper rendering
8. **Consider rendering**: Note that PlantUML requires Java and Graphviz (or PlantUML server) for rendering

## Keywords

**English keywords:**
plantuml, UML, class diagram, sequence diagram, use case diagram, activity diagram, component diagram, state diagram, deployment diagram, object diagram, timing diagram, network diagram, Archimate diagram, Gantt chart, mindmap, WBS diagram, JSON diagram, YAML diagram, EBNF, regex, regular expression, Salt wireframe, SDL, Ditaa, chronology diagram, mathematical notation, AsciiMath, LaTeX, ER diagram, entity relationship diagram, IE diagram, information engineering diagram, Chen's notation, C4 model, C4 diagram, architecture diagram, system architecture, enterprise architecture, microservices architecture, draw, create, generate, make, build, visualize, visualization, drawing, UML notation, standard UML

**Chinese keywords (中文关键词):**
PlantUML, UML, 类图, 时序图, 用例图, 活动图, 组件图, 状态图, 部署图, 对象图, 时序图, 网络图, 架构图, 甘特图, 思维导图, 工作分解结构图, JSON 图, YAML 图, EBNF 图, 正则表达式图, 线框图, SDL 图, Ditaa 图, 时间线图, 数学公式图, 实体关系图, ER 图, 信息工程图, IE 图, 陈氏表示法, C4 模型, C4 图, 架构图, 系统架构图, 企业架构图, 微服务架构图, 画图, 绘图, 生成图, 创建图, 制作图, 画类图, 画时序图, 画组件图, 画部署图, 画活动图, 画状态图, 画用例图, 画对象图, 画网络图, 画线框图, 画 ER 图, 用 PlantUML, PlantUML 语法, UML 图, UML 类图, UML 时序图, 可视化, 图表, 图形, 示意图, 设计图, 系统图, 用图表示, 画出来, 给我画, 帮我画, 画一个, 创建一个图, 生成一个图, 画个图说明, 用图表展示, 可视化展示
