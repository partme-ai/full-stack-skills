---
name: "pencil"
description: "用于通过 Pencil MCP 读取/修改 .pen 设计文件并校验布局。用户提到 pencil/.pen/设计稿编辑、需要列出工具或执行 batch_get/batch_design 时调用。"
---

# Pencil（MCP：pencil）

本 Skill 负责与 Pencil MCP Server 交互，读取/编辑加密的 `.pen` 设计文件，并提供可复制的调用模板与最佳实践。

## 关键边界与安全规则

- `.pen` 文件内容是加密的：禁止用普通文件读取/搜索方式解析 `.pen` 内容；只能通过 pencil MCP tools 访问与修改。
- 优先“先读后写”：写入前先用 `get_editor_state` / `batch_get` 了解当前文档结构与选区。
- `batch_design` 单次最多 25 条操作；超过时按“结构→内容→样式→验收”拆分多次执行。
- 任何会造成大范围变更的能力（`replace_all_matching_properties`、大批量 `batch_design`）都必须先输出变更计划，再执行。

## MCP Server 配置（参考）

```json
{
  "pencil": {
    "name": "pencil",
    "transport": "stdio",
    "command": "/Users/wandl/.trae/extensions/highagency.pencildev-0.6.15-universal/out/mcp-server-darwin-arm64",
    "args": ["--ws-port", "61405"],
    "env": {}
  }
}
```

## 使用流程（推荐）

1. `get_editor_state(include_schema=false)`：确认当前是否已打开 `.pen`、当前选区。
2. 如无文档：`open_document(filePathOrTemplate)` 打开或新建。
3. 读结构：`batch_get(...)` 获取目标节点树、组件、变量等。
4. 设计/修改：`batch_design(filePath, operations)`（≤25 ops/次）。
5. 验收：`snapshot_layout(...)` 检查布局问题；必要时 `get_screenshot(...)` 截图复核。

## 工具列表（Tools）与主要参数用途

以下为 pencil MCP 当前支持的工具（prompts/resources 不支持）。

### 1) get_editor_state

- 用途：获取当前编辑器状态、激活文档、当前选中节点等上下文。
- 参数：
  - `include_schema: boolean`：是否附带 `.pen` schema。
- 调用模板：

```json
{ "name": "get_editor_state", "arguments": { "include_schema": false } }
```

### 2) open_document

- 用途：打开或创建 `.pen` 文件。
- 参数：
  - `filePathOrTemplate: string`：`.pen` 文件路径或 `"new"`。
- 调用模板：

```json
{ "name": "open_document", "arguments": { "filePathOrTemplate": "new" } }
```

### 3) batch_get

- 用途：批量读取/搜索节点（读结构、读组件、读实例）。
- 关键参数：
  - `filePath: string`（必填）
  - `nodeIds?: string[]`：按 ID 读取
  - `parentId?: string`：限定在某节点子树内搜索
  - `patterns?: object[]`：按模式搜索（如 `name` 正则、`type`、`reusable`）
  - `includePathGeometry?: boolean`：是否返回完整 path 几何（默认会用 `...` 缩略）
  - `readDepth?: number`：读取展开深度（建议 ≤3）
  - `searchDepth?: number`：搜索深度
  - `resolveInstances?: boolean`：展开实例
  - `resolveVariables?: boolean`：解析变量为当前值
- 调用模板（按 pattern 搜索可复用组件）：

```json
{
  "name": "batch_get",
  "arguments": {
    "filePath": "designs/app.pen",
    "patterns": [{ "reusable": true }],
    "readDepth": 2,
    "searchDepth": 3
  }
}
```

### 4) batch_design

- 用途：批量执行插入/复制/更新/替换/移动/删除/图片等操作。
- 关键参数：
  - `filePath: string`（必填）
  - `operations: string`（必填）：操作脚本（每行一个 op，可绑定变量名；≤25 ops/次）。
- 调用模板（示意）：

```json
{
  "name": "batch_design",
  "arguments": {
    "filePath": "designs/app.pen",
    "operations": "root=G()\\nframe=I(root,{type:\\\"frame\\\",name:\\\"Home\\\"})\\nU(frame,{width:390,height:844})"
  }
}
```

### 5) snapshot_layout

- 用途：检查布局结构与常见问题（重叠、裁剪等），可只返回问题节点。
- 关键参数：
  - `filePath: string`（必填）
  - `parentId?: string`：仅检查子树
  - `maxDepth?: number`：检查深度
  - `problemsOnly?: boolean`：仅输出有问题的节点
- 调用模板：

```json
{
  "name": "snapshot_layout",
  "arguments": { "filePath": "designs/app.pen", "maxDepth": 2, "problemsOnly": true }
}
```

### 6) get_screenshot

- 用途：对指定节点截图（视觉验收）。
- 参数：
  - `filePath: string`（必填）
  - `nodeId: string`（必填）
- 调用模板：

```json
{
  "name": "get_screenshot",
  "arguments": { "filePath": "designs/app.pen", "nodeId": "node_123" }
}
```

### 7) get_guidelines

- 用途：获取设计指南/规则。
- 参数：
  - `topic: \"code\" | \"table\" | \"tailwind\" | \"landing-page\" | \"design-system\"`（必填）
- 调用模板：

```json
{ "name": "get_guidelines", "arguments": { "topic": "design-system" } }
```

### 8) get_style_guide_tags

- 用途：获取可用风格标签集合。
- 调用模板：

```json
{ "name": "get_style_guide_tags", "arguments": {} }
```

### 9) get_style_guide

- 用途：按 tags 或 id 获取风格指南。
- 参数（可选）：
  - `tags?: string[]`
  - `id?: string`
- 调用模板：

```json
{ "name": "get_style_guide", "arguments": { "tags": ["mobile", "minimal", "fresh"] } }
```

### 10) get_variables

- 用途：读取 `.pen` 文件的变量与主题（用于生成全局样式/代码映射）。
- 参数：
  - `filePath: string`（必填）
- 调用模板：

```json
{ "name": "get_variables", "arguments": { "filePath": "designs/app.pen" } }
```

### 11) set_variables

- 用途：更新 `.pen` 文件的变量与主题。
- 参数：
  - `filePath: string`（必填）
  - `variables: object`（必填）
  - `replace?: boolean`：是否全量替换（默认合并）。
- 调用模板：

```json
{
  "name": "set_variables",
  "arguments": { "filePath": "designs/app.pen", "replace": false, "variables": {} }
}
```

### 12) find_empty_space_on_canvas

- 用途：在画布或某节点周边查找指定尺寸的空白区域。
- 参数：
  - `filePath: string`（必填）
  - `width: number`（必填）
  - `height: number`（必填）
  - `padding: number`（必填）
  - `direction: \"top\" | \"right\" | \"bottom\" | \"left\"`（必填）
  - `nodeId?: string`：以某节点为参照（可选）
- 调用模板：

```json
{
  "name": "find_empty_space_on_canvas",
  "arguments": {
    "filePath": "designs/app.pen",
    "width": 390,
    "height": 844,
    "padding": 24,
    "direction": "right"
  }
}
```

### 13) search_all_unique_properties

- 用途：统计指定子树里若干属性（颜色/字体/间距等）的唯一值集合，用于分析是否一致。
- 参数：
  - `filePath: string`（必填）
  - `parents: string[]`（必填）
  - `properties: string[]`（必填；枚举：fillColor/textColor/strokeColor/strokeThickness/cornerRadius/padding/gap/fontSize/fontFamily/fontWeight）
- 调用模板：

```json
{
  "name": "search_all_unique_properties",
  "arguments": {
    "filePath": "designs/app.pen",
    "parents": ["root_frame"],
    "properties": ["fillColor", "fontFamily", "fontSize"]
  }
}
```

### 14) replace_all_matching_properties

- 用途：在指定子树里批量替换匹配属性（换色/换字体/调整间距等）。
- 参数：
  - `filePath: string`（必填）
  - `parents: string[]`（必填）
  - `properties: object`（必填）：按属性名提供 from/to 替换规则列表
- 调用模板：

```json
{
  "name": "replace_all_matching_properties",
  "arguments": {
    "filePath": "designs/app.pen",
    "parents": ["root_frame"],
    "properties": {
      "fontFamily": [{ "from": "Inter", "to": "SF Pro" }],
      "fontSize": [{ "from": 14, "to": 15 }]
    }
  }
}
```

## 常见任务提示词（给大模型的执行指令模板）

### A) “打开并分析当前设计结构”

1) 调用 `get_editor_state(include_schema=false)` 获取 activeFilePath 与 selection  
2) 用 `batch_get` 读取选中节点与其子树（readDepth=2）  
3) 用 `snapshot_layout(problemsOnly=true)` 输出布局问题清单  
4) 必要时 `get_screenshot` 对问题节点截图确认

### B) “批量换主题/换字体/统一间距”

1) `search_all_unique_properties` 先统计现状（输出唯一值集合与分布）  
2) 提出变更计划（from→to 映射、影响范围、回滚策略）  
3) `replace_all_matching_properties` 执行替换  
4) `snapshot_layout` + `get_screenshot` 验收
