# Stitch HTML → Pencil batch_design 转换可行性

## 目标

将 Stitch 导出的页面 HTML 代码，转换为 Pencil MCP 的 **batch_design** 批量执行动作，通过**分拆为多次 batch_design 调用**，在 .pen 画布上绘制出与页面**结构一致、布局相近**的设计稿。

---

## 1. 两套体系简要对比

| 维度 | Stitch | Pencil |
|------|--------|--------|
| **产出物** | HTML（DOM + Tailwind 类） | .pen 文件（节点树） |
| **执行方式** | 无（静态 HTML） | MCP `batch_design`：I/U/R/M/D/C/G 等操作 |
| **结构** | `<header>`, `<main>`, `<section>`, `<form>`, `<input>` 等 | `frame`（layout: vertical/horizontal）, `text`, `ref`（组件实例）, `icon_font` 等 |
| **样式** | Tailwind：`p-4`, `gap-4`, `bg-white`, `rounded-xl`, `shadow-soft` | 节点属性：`padding`, `gap`, `fill`, `cornerRadius`, `stroke` 等 |
| **单次操作量** | — | 建议单次 ≤25 条操作，多块内容分多次调用 |

---

## 2. 可行性结论

**可以做到**：把 Stitch 的页面 HTML 转成**多轮 Pencil batch_design 动作**，在 .pen 里复刻出与页面**结构一致、布局和层次相近**的设计稿。

- **结构/布局**：通过「HTML 语义 + Tailwind 布局类 → .pen 节点类型 + layout/gap/padding」的映射，可以高度一致。
- **视觉「一模一样」**：取决于 Tailwind→.pen 的映射完整度（间距、颜色、圆角、字重等）以及是否使用 Pencil 设计系统组件；可做到**非常接近**，完全像素级一致需要逐项对齐与校验。

---

## 3. 转换思路概览

### 3.1 HTML → .pen 结构映射（思路）

| Stitch HTML 模式 | Pencil 操作思路 |
|------------------|-----------------|
| `<header class="sticky top-0 ...">` + 返回 + 标题 | 一个 `frame`（horizontal, height 64）, 内层 back 图标 + `text` 标题 |
| `<main class="px-4 py-4 space-y-4">` | 一个 `frame`（layout: vertical, padding: 32, gap: 32） |
| `<section class="... rounded-xl p-4 shadow-soft">` | 一个 `frame`（padding: 24, fill: $--card, cornerRadius）或设计系统 `ref: cardId` |
| `<h2 class="text-sm font-bold">` | `text` 节点（fontSize: 14, fontWeight: 600）或 Card 的 header slot |
| `<div class="grid grid-cols-3">` 多个 tab 按钮 | 一个 horizontal `frame`，3 个子节点（或 Tabs 组件 ref） |
| `<div class="grid grid-cols-2 gap-4">` 两列表单项 | `frame`（layout: horizontal, gap: 16），两列各一个子 frame（width: fill_container） |
| `<label>` + `<input>` | 一个 Input Group 的 `ref`，或 frame + `text`（label）+ frame（input 占位） |
| `<input type="checkbox">` + 开关样式 | 设计系统 Switch 的 `ref`，或简单 frame 表示占位 |
| 分割线 | `frame`（height: 1, fill: $--border）或设计系统 Divider ref |

### 3.2 分拆为多轮 batch_design（建议）

单次 `batch_design` 建议 ≤25 条操作，因此**按「区块」拆分**，例如：

1. **Batch 1 — 页面骨架**
   - 在 `document` 下插入根 `frame`（整页，vertical）。
   - 插入顶部栏 `frame`（header）。
   - 插入主内容区 `frame`（placeholder: true），后续内容都挂在这下面。
   - 约 3–5 条 I( ) 即可。

2. **Batch 2 — 顶部栏内容**
   - 在 header 下插入返回图标（icon_font）、标题 `text`、或 Tabs 的 3 个 tab。
   - 约 5–10 条。

3. **Batch 3 — 第一张卡片**
   - 在主内容区插入卡片 `frame` 或 Card ref。
   - 插入卡片标题、表单项（用 ref 或简单 frame+text）。
   - 约 10–20 条。

4. **Batch 4 — 第二张卡片**
   - 同上，第二块 section/card。
   - 依此类推，每个 section/表单块 1 次 batch_design。

5. **后续 Batch — 其余卡片、表单、按钮**
   - 每个逻辑区块 1 次调用，每次控制在 25 条以内。
   - 复杂表单可再拆（例如先插 5 个表单项，再插下一批）。

这样**一页 Stitch 页面 ≈ 5–15 次 batch_design**，即可在 Pencil 里搭出与页面一致的设计稿结构。

---

## 4. 需要解决的关键点

1. **Stitch HTML 的获取与解析**
   - 从 Stitch MCP `get_screen` 拿到 `htmlCode.downloadUrl`，下载 HTML。
   - 用 HTML 解析器（或正则）提取 DOM 树 + 每个节点的 class（Tailwind）。

2. **Tailwind → .pen 属性映射**
   - 间距：`p-4` → padding 16, `gap-4` → gap 16, `space-y-4` → 子节点间 gap。
   - 布局：`flex`, `grid grid-cols-2` → frame 的 layout（vertical/horizontal）与子节点宽度。
   - 颜色：`bg-white`, `bg-card-light` → fill（或设计变量如 `$--card`）。
   - 字色/字号：`text-sm`, `font-bold`, `text-gray-500` → text 的 fontSize、fontWeight、fill。
   - 可与现有 `tailwind-to-uviewpro` 等映射表对齐，再扩展一份「Tailwind → .pen」表。

3. **设计系统组件的使用（可选）**
   - 若 .pen 已挂载设计系统（如 pencil-ui-design-system-uviewpro），可优先把「卡片 / 表单项 / 按钮 / Tabs」映射到现有组件的 `ref`，再在 batch_design 里用 I( parent, { type: "ref", ref: "xxx", descendants: { ... } }) 插入。
   - 若不做设计系统，则全部用 `frame` + `text` + `icon_font` 等基础节点也可还原布局和层次。

4. **坐标与占位**
   - 若希望「整页」顺序与 Stitch 一致，主内容区用 `layout: "vertical"` + `gap` 即可，无需绝对坐标。
   - 若要在画布上多屏并排，可用 `find_empty_space_on_canvas` 找空白再插入根 frame。

---

## 5. 建议的产物形态

- **方案 A — 技能/流程**
  - 新增一个「Stitch HTML → Pencil」技能（或整合进现有 stitch 技能）：
    - 输入：Stitch 的 HTML（或 get_screen 的 htmlCode）。
    - 输出：多组 `batch_design` 的入参（filePath + operations 列表），按顺序执行即可在 Pencil 中画出对应设计稿。

- **方案 B — 文档 + 映射表**
  - 在 pencil-skills 下维护一份「Stitch HTML → Pencil batch_design」映射文档（本文档可视为初版）。
  - 再补充一份「Tailwind class → .pen 节点属性」表，便于手写或半自动生成 operations。

- **方案 C — 轻量脚本**
  - 写一个脚本：输入为 Stitch HTML 文件，输出为多段 JSON（每段对应一次 batch_design 的 operations），由 Agent 或人在 Pencil 中依次调用 MCP。

---

## 6. 小结

- **能否把 Stitch 页面 HTML 转成 Pencil 批量执行动作？**
  **能。** 把页面按区块拆成多轮 `batch_design`，每轮 ≤25 条操作，即可在 .pen 里画出与页面**结构一致、布局相近**的设计稿。

- **能否「一模一样」？**
  **结构可以一致；视觉非常接近是可行的**，取决于 Tailwind→.pen 的映射是否完整、以及是否使用设计系统并做一次视觉校验（例如用 Pencil 的 get_screenshot 对比）。

- **推荐下一步**
  - 选一个简单 Stitch 页面（例如一页只有 header + 2 个 section 的表单），
  - 手写 2–3 次 `batch_design` 的 operations，在 Pencil 中执行并截图对比；
  - 再据此固化「HTML 模式 → operations」的映射规则，并考虑做成技能或脚本。

---

## 7. 已实现的技能：pencil-design-from-stitch-html

本仓库已将上述方案实现为独立技能 **pencil-design-from-stitch-html**，用于把 Stitch HTML 分解为 100% 精确对应的 Pencil 绘图动作：

- **技能路径**: [skills/pencil-design-from-stitch-html](../skills/pencil-design-from-stitch-html/)
- **SKILL.md**: 技能入口、前置条件、检索与转换流程、执行步骤；内含 **Execution order and batch split**（Phase 0–N，每批 ≤25 条操作）。
- **references/html-to-pencil-mapping.md**: 基于 HTML 元素的对照规则（body/header/main/section/form/input/button/divider 等 → .pen 节点类型与 batch_design 操作）。
- **references/tailwind-to-pencil-styles.md**: 背景、颜色、尺寸、边距、内边距、阴影、圆角、描边、字体的 Tailwind → .pen 属性映射。
- **examples/usage.md**: 使用场景与步骤；**examples/sample-batch-ops.md**: 最小 HTML 对应单次 batch_design 的示例。

使用 pencil-design-from-stitch-html 时，按「解析 HTML → 应用映射 → 按执行顺序分批 → 依次调用 batch_design」即可在 Pencil 中绘制与页面一致的设计稿。原型→设计稿的职责归属 **pencil-skills**；Stitch 侧仅负责 PRD→原型。
