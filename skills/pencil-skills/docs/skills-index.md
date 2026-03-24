# Pencil Skills 索引

供 Agent 发现与加载使用。每个技能以 `name` + 简短 `description` 列出；完整说明见各技能目录下的 `SKILL.md`。规范见 [spec/agent-skills-spec.md](../spec/agent-skills-spec.md)。

## MCP 技能（pencil-mcp-{MCP 方法名}）

| name | description（概要） |
|------|---------------------|
| pencil-mcp-open-document | 打开或创建 .pen 设计文档；新建文档或打开指定文件时使用。 |
| pencil-mcp-get-editor-state | 获取当前编辑器状态（激活文件、选区、顶层节点、可复用组件）；建立 Pencil 上下文时使用。 |
| pencil-mcp-batch-design | 批量执行设计操作（插入/更新/替换/移动/删除节点）；在 .pen 上「动手」时使用。 |
| pencil-mcp-batch-get | 按模式或节点 ID 批量读取节点；了解设计树与组件时使用。 |
| pencil-mcp-snapshot-layout | 获取布局快照（位置、层级、重叠/裁剪问题）；分析布局时使用。 |
| pencil-mcp-get-screenshot | 获取节点截图；视觉校验设计结果时使用。 |
| pencil-mcp-get-guidelines | 按 topic 获取设计指南（design-system/code/tables/tailwind/landing-page）；需规则与规范时使用。 |
| pencil-mcp-get-style-guide-tags | 获取可用风格标签；需风格参考时先调用。 |
| pencil-mcp-get-style-guide | 按标签或 ID 获取风格指南内容；需风格参考时使用。 |
| pencil-mcp-get-variables | 获取 .pen 中的设计变量；读主题/ token 时使用。 |
| pencil-mcp-set-variables | 设置 .pen 中的设计变量；初始化或更新主题时使用。 |
| pencil-mcp-find-empty-space-on-canvas | 在画布上查找指定方向与尺寸的空白区域；放置新内容时使用。 |
| pencil-mcp-search-all-unique-properties | 在指定父节点下搜索属性唯一值；审计样式时使用。 |
| pencil-mcp-replace-all-matching-properties | 在指定父节点下批量替换匹配属性；主题/样式批量更新时使用。 |

## Spec 技能

| name | description（概要） |
|------|---------------------|
| pencil-ui-design-spec-generator | 将模糊需求转为动作级 PENCIL_PLAN（不执行）；每步标明 MCP 工具 + 意图 + 关键参数。 |

## 设计系统初始化技能（pencil-ui-design-system-*）

| name | description（概要） |
|------|---------------------|
| pencil-ui-design-system-layui | 初始化 Layui design system components（变量 + 组件总览帧）。 |
| pencil-ui-design-system-antd | 初始化 Ant Design design system components（变量 + 组件总览帧）。 |
| pencil-ui-design-system-bootstrap | 初始化 Bootstrap design system components（变量 + 组件总览帧）。 |
| pencil-ui-design-system-element | 初始化 Element Plus design system components（变量 + 组件总览帧）。 |
| pencil-ui-design-system-uview | 初始化 uView (2.x) design system components（变量 + 组件总览帧）。 |
| pencil-ui-design-system-uviewpro | 初始化 uView Pro design system components（变量 + 组件总览帧）。 |
| pencil-ui-design-system-vant | 初始化 Vant design system components（变量 + 组件总览帧）。 |
| pencil-ui-design-system-ucharts | 初始化 uCharts 图表占位/数据可视化 design system components。 |
| pencil-ui-design-system-echarts | 初始化 ECharts 图表占位/数据可视化 design system components。 |

## 工厂技能

| name | description（概要） |
|------|---------------------|
| pencil-skill-creator | 创建新的 pencil-ui-design-system-&lt;name&gt; 技能；含 Golden Template、references、scripts/init_pencil_design_system_skill.py。 |

## 原型/HTML→设计

| name | description（概要） |
|------|---------------------|
| pencil-design-from-stitch-html | 基于 Stitch HTML 或 Stitch 地址产出 Pencil .pen 设计；HTML→节点映射、执行顺序与 Tailwind/框架样式映射。 |

## 编排技能

| name | description（概要） |
|------|---------------------|
| pencil-ui-designer | Pencil 设计流程编排（Orchestrator）。 |

---

参数与 MCP 方法说明见 [pencil-mcp-tools.md](pencil-mcp-tools.md)。
