# Pencil MCP 工具方法说明

以 [Pencil MCP.md](./Pencil%20MCP.md) 为主整理的 Pencil MCP 工具说明。在 Cursor / Claude 中，工具名带前缀 `mcp__pencil__`（例如 `mcp__pencil__batch_design`）。

---

## 1. 设计管理

### 1.1 `get_editor_state()` — 获取编辑器状态

获取当前激活的画布编辑器、当前用户选区及其他设计任务所需的基础信息。

**参数：**

| 参数 | 说明 |
|------|------|
| `include_schema` | 设为 `true` 时在返回中包含 .pen 文件 schema；若已了解 schema 可设为 `false` |

---

### 1.2 `open_document()` — 打开/创建文档

若无激活的编辑器，可传 `'new'` 创建新文档；若用户要求打开指定 .pen 文件，则传入该文件路径。

**参数：**

| 参数 | 说明 |
|------|------|
| `filePathOrTemplate` | 已有 .pen 文件的路径，或 `'new'` 表示新建文档。仅此两种有效。 |

---

### 1.3 `batch_design()` — 批量设计操作

在一次调用中执行多条插入/复制/更新/移动/删除/图片等操作。

**使用要点：**

- 单次调用建议**最多 25 条操作**，以保证性能；更大界面按逻辑区块拆成多次 `batch_design`（如先屏幕结构，再侧栏，再主内容）。
- 避免构造过大的单条操作（如带大量 descendants 的 insert），尽量拆成多条小操作。
- 若其中一条失败，该次调用内已执行的操作会整体回滚。
- **每条操作列表都要用新的 binding 名称，不要在不同操作列表间复用 binding 名称。**
- 返回中会列出可能问题，应在下一次 `batch_design` 中修正。

**组件实例使用：**

1. **更新属性** — 用 `U()` 与实例路径：  
   `card=I(body, {type:"ref", ref:"CardComp"})` → `U(card+"/titleText", {content: "New Title"})`
2. **整体替换子节点** — 用 `R()` 与实例路径：  
   `newTitle=R(card+"/headerSlot", {type:"text", content: "Custom Title"})`
3. **新增子节点** — 在普通 frame 或 document root 上用 `I()`：  
   `container=I(body, {type:"frame", layout:"vertical"})` → `item=I(container, {type:"text", content: "New item"})`

---

### 1.4 `batch_get()` — 批量获取节点

按搜索模式或节点 ID 批量读取节点。

**使用要点：**

- **重要：** 将多种搜索模式与多个节点 ID 的读取合并到**一次**调用中；需要连续多次搜索/按 ID 读取时，也合并成一次调用。
- 若既不指定 `patterns` 也不指定 `nodeIds`，则返回文档顶层子节点。
- 使用设计系统组件时，**不要逐个读取组件**，应在一轮工具调用中列出设计系统 frame 内所有可复用节点，以了解可用组件；适合在开始时用来列出设计系统/设计套件的组件。
- 返回的是匹配节点及其直接子节点；用 `searchDepth` 控制向下搜索层数。`readDepth` 大于 3 时容易返回过多数据占满上下文，建议用较小值。
- 路径几何默认为缩写；需要完整几何时设 `includePathGeometry=true`。设 `resolveVariables=true` 可得到计算后的值而非变量引用。

**大文档遍历：**

1. 先读顶层节点或已知 ID 的节点以了解整体结构。
2. 判断已有数据是否足够完成当前任务。
3. 若需更多数据且子节点显示为 `".."`，再针对这些子节点 ID 发起新的读取。

**参数（示意）：** `filePath`（可选）、搜索模式/节点 ID 相关参数、`searchDepth`、`readDepth`、`includePathGeometry`、`resolveVariables` 等。

---

### 1.5 `snapshot_layout()` — 布局快照

查看 .pen 文件当前的布局结构。

**注意：** 不传 `maxDepth` 时需小心，过大的 `maxDepth` 会返回大量数据。若只关心重叠、被裁剪等问题，可使用 `problemsOnly` 参数。

**示例：** `maxDepth=0` 只返回顶层节点布局，常用于在画布上为新 frame 找空间。

**参数：**

| 参数 | 说明 |
|------|------|
| `filePath` | 可选，要访问的 .pen 文件路径 |
| `maxDepth` | 在节点树中下探的最大深度；不传则仅限该节点及其直接子节点。到达 maxDepth 后子节点以 `"..."` 表示。深度过大易产生大量数据，建议显式指定。 |
| `parentId` | 只返回该节点子树内的布局矩形；不传则返回整份文档的布局 |
| `problemsOnly` | 仅返回存在布局问题的节点（如被父节点裁剪）。默认 `false` |

---

### 1.6 `get_screenshot()` — 获取截图

返回 .pen 文件中某节点的截图。

**使用要点：**

- **重要：** 应对返回的截图做分析，确认生成结果正确、满足设计要求且无视觉错误、错位或错位。
- **重要：** 收到截图后仔细检查，发现可能的设计问题或不一致。
- 可用于根据节点/frame ID 获取截图，用于对比布局与设计；也可检查元素和设计系统组件的布局与外观。

**参数：**

| 参数 | 说明 |
|------|------|
| `filePath` | 可选，要访问的 .pen 文件路径 |
| `nodeId` | 要截图的节点 ID |

---

## 2. 风格与指南

### 2.1 `get_guidelines()` — 获取设计指南

返回与 .pen 文件相关的设计指南与规则。

**使用要点：**

- **重要：** 应遵循这些指南与设计规则完成任务。可按不同 `topic` 多次调用，按接下来要做的任务获取对应指南。
- 内容涵盖 .pen 文件 schema、组件、布局、定位、排版等设计规则。

**可选 topic：**

| topic | 说明 |
|-------|------|
| `design-system` | 使用设计系统组件组合界面、仪表盘等。适用于用现有可复用组件做 SaaS、仪表盘或界面。 |
| `code` | 从 .pen 生成代码的规范。任务涉及从设计生成代码或实现时使用。 |
| `tables` | 在 .pen 中插入、更新、移动表格或仪表盘的指南。 |
| `tailwind` | 使用 Tailwind CSS 实现设计时的规范（Tailwind v4）。 |
| `landing-page` | 从零设计高转化落地页的指南。适用于落地页、营销站、宣传页等。 |

**参数：**

| 参数 | 说明 |
|------|------|
| `topic` | 要获取的设计指南主题，每次仅能选一个。 |

---

### 2.2 `get_style_guide_tags()` — 获取风格标签

返回当前可用的样式指南标签列表。

**使用要点：**

- 需要创意方向或视觉参考时使用；做落地页、营销站、仪表盘、应用界面时可用。
- 用户提出特定风格、氛围或情绪时使用；从零设计、空白画布或探索新方向时使用；重混、改风格或做变体时也可用。
- 仅在任务为纯组合（如「在这里加个按钮」）且已有设计系统时可以考虑跳过。
- 可能的话尽量包含 mobile、website 或 webapp 等标签。
- **仅使用**此前「get style guide tags」返回的标签。若用户明确提供了样式指南 ID，则用 `id` 参数直接按 ID 获取。
- 先调用本工具，再将得到的 tags 或样式指南 ID 传给 `get_style_guide`。

**参数：** 无（或见实际 MCP 定义）。

---

### 2.3 `get_style_guide()` — 获取风格指南

根据标签或样式指南 ID 返回对应的样式指南内容（设计灵感与视觉参考）。

**使用要点：**

- 适用场景与 `get_style_guide_tags` 相同（创意方向、落地页、仪表盘、特定风格/情绪、从零设计、重混与变体等）。
- 纯组合任务且已有设计系统时可考虑跳过。
- 先调用 `get_style_guide_tags`，再用其返回的 tags 或样式指南 ID 调用本工具。

**参数：**

| 参数 | 说明 |
|------|------|
| `id` | 可选，按样式指南 ID 获取指定样式指南（与 tags 二选一） |
| `tags` | 可选，5–10 个与当前设计任务最匹配的标签，须来自「get style guide tags」返回的集合 |

---

## 3. 变量管理

### 3.1 `get_variables()` — 获取设计变量

获取当前 .pen 文件中定义的变量与主题。

用于在代码库中生成全局 CSS 等；从设计生成代码时，用本工具获取与设计相关的全局样式规则。

**参数：**

| 参数 | 说明 |
|------|------|
| `filePath` | 可选，要访问的 .pen 文件路径 |

---

### 3.2 `set_variables()` — 设置设计变量

更新 .pen 文件中定义的变量与主题。

若变量使用 theming，文档中尚未存在的 theme 轴与值会被自动注册。  
**注意：** 变量名为任意字符串，不必以美元符号开头。

**参数：**

| 参数 | 说明 |
|------|------|
| `filePath` | 可选，要访问的 .pen 文件路径 |
| `replace` | 默认将变量与文档已有变量定义合并。传 `true` 则完全替换文档现有变量定义。 |
| `variables` | 遵循 .pen 文件 schema 中的变量定义。不熟悉 schema 时可通过「通用指南」获取。 |

---

## 4. 画布操作

### 4.1 `find_empty_space_on_canvas()` — 查找空白区域

在指定方向和所需尺寸下，在 .pen 文件中查找空白区域。

若提供 `nodeId`，则在以该节点为参考的周围查找；不传则在整张画布内容周围查找。

**参数：**

| 参数 | 说明 |
|------|------|
| `direction` | 相对于节点的查找方向 |
| `filePath` | 可选，要访问的 .pen 文件路径 |
| `height` | 所需空白区域高度 |
| `nodeId` | 可选，作为起点的节点 ID；不传则基于整张画布内容查找 |
| `padding` | 与其他元素的最小间距 |
| `width` | 所需空白区域宽度 |

---

### 4.2 `search_all_unique_properties()` — 搜索属性

在指定父节点下的整棵节点树中递归搜索，汇总指定属性的所有唯一值。

**参数：**

| 参数 | 说明 |
|------|------|
| `filePath` | 可选，要访问的 .pen 文件路径 |
| `parents` | 要搜索的父节点 ID 列表 |
| `properties` | 要搜索的属性名列表 |

---

### 4.3 `replace_all_matching_properties()` — 批量替换属性

在指定父节点下的整棵节点树中递归替换所有匹配的属性。

**参数：**

| 参数 | 说明 |
|------|------|
| `filePath` | 可选，要访问的 .pen 文件路径 |
| `parents` | 要操作的父节点 ID 列表 |
| `properties` | 每个属性的替换规则列表 |

---

## 5. 工具名前缀与一览

| 环境 | 前缀 | 示例 |
|------|------|------|
| Cursor / Claude | `mcp__pencil__` | `mcp__pencil__batch_design` |
| Codex 等 | `pencil__` | `pencil__batch_design` |

### Pencil MCP 技能命名规范

**技能名必须为** `pencil-mcp-{MCP 方法名}`，其中 MCP 方法名中的下划线改为连字符（kebab-case）。例如：

- MCP 方法 `open_document` → 技能名 **pencil-mcp-open-document**
- MCP 方法 `get_editor_state` → 技能名 **pencil-mcp-get-editor-state**
- MCP 方法 `batch_design` → 技能名 **pencil-mcp-batch-design**
- MCP 方法 `find_empty_space_on_canvas` → 技能名 **pencil-mcp-find-empty-space-on-canvas**

**方法一览（与 Pencil MCP.md 一致）：**

| 分类 | 方法名 | 简要说明 |
|------|--------|----------|
| 设计管理 | `get_editor_state` | 获取编辑器状态 |
| 设计管理 | `open_document` | 打开/创建文档 |
| 设计管理 | `batch_design` | 批量设计操作（增删改移等） |
| 设计管理 | `batch_get` | 批量获取节点 |
| 设计管理 | `snapshot_layout` | 布局快照 |
| 设计管理 | `get_screenshot` | 获取截图 |
| 风格与指南 | `get_guidelines` | 获取设计指南（按 topic） |
| 风格与指南 | `get_style_guide_tags` | 获取风格标签 |
| 风格与指南 | `get_style_guide` | 获取风格指南（按 tags/id） |
| 变量管理 | `get_variables` | 获取设计变量 |
| 变量管理 | `set_variables` | 设置设计变量 |
| 画布操作 | `find_empty_space_on_canvas` | 查找空白区域 |
| 画布操作 | `search_all_unique_properties` | 搜索属性唯一值 |
| 画布操作 | `replace_all_matching_properties` | 批量替换属性 |

以上说明以 [Pencil MCP.md](./Pencil%20MCP.md) 为主整理，具体参数与行为以 Cursor「Tools & MCP」中 Pencil 工具为准。
