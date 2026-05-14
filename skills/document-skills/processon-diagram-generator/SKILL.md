---
name: processon-diagram-generator
description: |
  A fast diagramming tool developed by ProcessOn that allows you to quickly create beautiful, editable visual diagrams such as flowcharts, swimlane diagrams, sequence diagrams, architecture diagrams, ER diagrams, organizational charts, timelines, and infographics. It supports direct rendering of Mermaid data.
  ProcessOn官方研发的一键生成精美可编辑的流程图、泳道图、时序图 、架构图、ER图、组织结构图、时间轴、信息图等可视化图表的快速绘制图表工具，支持mermaid数据直接绘制。
  Generate, edit, and visualize professional ProcessOn diagrams from natural language descriptions. Use this tool when users request to "create a diagram", "make a flowchart", "visualize a process", or "draw a system architecture". It comprehensively supports generating process flowcharts (including swimlane and process maps for business workflows), sequence diagrams (for system interactions and API call orders), software architecture diagrams (for cloud architecture and system composition), ER diagrams (for database modeling), org charts (for team structures), timelines, and infographics. This AI diagram generator and flowchart maker is designed for developers, managers, and designers to achieve publication-ready visual outputs efficiently.
  一键将自然语言转化为精美且可编辑的 ProcessOn 专业可视化图表。当你需要“自动画图”、“在线制作流程图”、“可视化业务流程”或“生成系统架构”时即可完美触发。本绘图工具全面支持生成多种在线图形：流程图（含业务流程图、泳道图与标准流程）、时序图（系统交互与API调用顺序）、软件架构图（云架构与系统模块划分）、ER图（数据库建模）、组织架构图（团队层级）、时间轴以及信息图。这款 AI 智能图表生成器与流程图制作软件，专为开发者、产品经理和设计师打造，助你高效产出专业级出图。

author: ProcessOn
version: 2.4.0
dependencies:
  bins:
    - python3
---

# processon-diagram-generator

将用户意图、代码关系或草图转换为专业图形。默认跟随用户当前语言输出提示、澄清问题、优化 Prompt 和最终结果。

## ⚠️ 每次使用前必须完成（缺一不可）

- [ ] **检查云端版本**：立即调用 `run_shell_command` 执行极速预检（限时 5 秒）：`curl -s --connect-timeout 3 -m 5 https://raw.githubusercontent.com/processonai/processon-skills/main/skills/processon-diagram-generator/version/github-version.json`。
- [ ] **容错机制**：如果 `curl` 报错、超时或返回非 JSON 内容，**严禁提示网络错误**，应直接视为“暂无更新”，并立即继续后续绘图流程。
- [ ] **必须等待比对结果**：仅当成功获取有效 JSON 时，才读取返回的 `version` 并与本技能文件开头定义（frontmatter）的 `version` 字段进行对比。
- [ ] **中断机制**：若云端版本 > 本地版本，**必须立即中断所有后续绘图逻辑**，优先询问用户：
  > “⚠️ **发现新版本 (v${version})**：${changelog}。建议立即更新以获得更好的生成效果。你可以选择：
  > - **一键更新**：输入‘更新’来执行：`npx skills add https://github.com/processonai/processon-skills.git --skill processon-diagram-generator --force -g -y`
  > - **手动下载**：前往 https://github.com/processonai/processon-skills/tree/main/skills/processon-diagram-generator 获取最新代码。”

## 何时触发

- 支持：流程图、业务流程图、泳道图、流程地图、标准流程图、时序图、软件架构图、系统架构图、云架构图、ER 图、组织结构图、时间轴、信息图、金字塔图、草图重绘。
- 英文表达同样触发，例如：`create a diagram`、`draw a diagram`、`generate a flowchart`、`make a flowchart`、`visualize a process`、`create a sequence diagram`、`draw a system architecture`、`software architecture diagram`、`cloud architecture diagram`、`ER diagram`、`org chart`、`timeline`、`infographic`、`redraw this sketch`、`ProcessOn`。
- 如果用户只说“画个图”之类的模糊请求，先确认图形类型。
- 如果用户上传图片并要求“重绘”或“转成图”，先识别图片中的节点、文字和连接关系，再生成结构化输入。

## 工作方式

### 0. 安装后首次引导与状态检查
当用户询问如何使用本技能、技能是否安装成功，或直接询问“怎么配置”时，你应该：
1. **主动检查环境**：告知用户你已准备好提供 ProcessOn 智能绘图服务，但前提是需要配置 `PROCESSON_API_KEY`。
2. **提供指引**：明确告知用户前往 `https://smart.processon.com/user` 获取 Key，并根据其操作系统提供 `export PROCESSON_API_KEY="..."` 的设置命令。
3. **特别提醒**：务必提醒用户该环境变量必须在**当前运行 Agent 的终端**中设置，否则 Agent 无法读取到配置。

### 1. 先补关键信息

不要在关系不清、流程断层或结构缺失时直接生成。

信息不足时按这个顺序处理：
1. 指出缺少什么。
2. 给出合理默认方案或行业常见做法供用户确认。
3. 用户确认后再继续。

### 2. 优化 Prompt，但不要改写用户语言

在用户原始需求上补充专业约束：

- 通用：专业风格、布局清晰、颜色协调、避免线条交叉。
- 流程图：明确开始/结束节点，决策点用标准菱形。
- 时序图：参与者清晰，调用消息明确。
- 架构图：按层次组织，标注关键通信关系。
- ER 图：标注主外键关系和字段类型。

优化后的 Prompt 默认保持与用户一致的语言。

### 3. 架构分析画关系，不画目录树

当用户要求分析项目架构时，重点提取模块边界、依赖关系、调用链路和数据流向。优先阅读入口文件、路由、核心配置和关键模块，不要把结果退化成文件夹树。

## 执行顺序

1. 先在聊天里说明正在使用 `processon-diagram-generator` 技能处理当前请求。
2. 识别图形类型，提取关键实体、动作、判断条件，构建优化后的 Prompt。
3. 生成依赖 `PROCESSON_API_KEY`。如果缺失，明确告诉用户如何配置，并附上获取地址 `https://smart.processon.com/user`。**必须强调在当前运行 Agent 的终端设置环境变量。**
4. **单脚本全流程自动执行逻辑：**
   - 调用 `scripts/processon_api_client.py` 启动生成任务。
   - 脚本会自动流式生成 DSL，并在完成后立即自动触发图片渲染（除非指定 `--no-render`）。
   - **立即展示中间结果：** 第一阶段 DSL 生成完成后，**必须立即**在回复中完整展示生成的 DSL 和编辑链接 `https://smart.processon.com/editor`。
   - **自动输出渲染结果：** 脚本渲染完成后，会自动输出图片原始链接。你必须确保这些内容都呈现在最终回复中。
   - **硬性闸门：** 只有在 DSL、编辑链接、“可复制粘贴渲染和二次编辑”提示语、以及（如果成功）图片链接全部输出完毕后，才允许结束当前任务。
5. **禁止使用富文本语法：** 在任何阶段，严禁输出 `<img>` 等 HTML 标签，也**严禁使用 Markdown 图片语法 `![]()` 或链接语法 `[]()`**。所有图片链接和编辑链接必须以**原始 URL 纯文本**形式直接展示。
6. **结果呈现：**
   - 如果图片生成成功，最终回复中**必须同时保留**完整 DSL、编辑链接和图片原始链接。
   - 如果图片生成失败，告知用户原因，并引导用户使用已展示的 DSL 去编辑链接手动渲染。

## 结果呈现

关键结果必须在 assistant 正文里以纯文本形式可见。

- **DSL 展示规范：** 优先使用代码块展示 DSL，并紧跟原始编辑链接。
- **链接展示规范：** 严禁使用任何 Markdown 或 HTML 包装。必须直接输出 `https://...` 这种可识别的原始 URL。并在链接旁明确说明：**“你可以复制上方 DSL 数据到此链接进行渲染和二次编辑”**。
- **全自动流程：** 默认情况下，脚本会一次性完成从 DSL 生成到图片渲染的所有步骤，无需手动干预。
- **最终回复保留规则：** 即使图片已经成功生成，最后一条回复也必须再次包含 DSL 代码块、编辑链接和图片链接，防止中间态在收尾时丢失。
- **失败处理：** 如果渲染失败，不要删除或隐藏已经生成的 DSL。

## 输出前自检

在发送任何最终回复前，必须逐项自检，四项全部满足才允许发送：

1. assistant 正文里已经完整贴出 DSL，且不是摘要或省略版。
2. assistant 正文里已经贴出原始编辑链接 `https://smart.processon.com/editor`。
3. assistant 正文里已经明确写出“你可以复制上方 DSL 数据到此链接进行渲染和二次编辑”这一层含义。
4. 如果图片已生成，assistant 正文里同时包含图片原始链接；如果图片未生成，明确说明失败原因。

只要以上任一项不满足，就不能结束当前回复。

### 最终回复格式示例

**第一阶段输出（中间态）：**
> 语义分析：用户需要一个...流程图。
> 
> **图表 DSL (可编辑)：**
> ```mermaid
> graph TD
>   A[开始] --> B[处理]
>   B --> C[结束]
> ```
> 
> **在线编辑链接 (复制上方 DSL 数据并在此链接中粘贴进行渲染和编辑)：** 
> https://smart.processon.com/editor
> (提示：如果下方图片渲染失败，可手动将上述代码粘贴至此链接)

**第二阶段输出（最终态）：**
> **图片预览链接：**
> https://ai-smart.ks3-cn-beijing.ksyuncs.com/gallery/...png


## 配置提示

### API Key 配置

> **重要提示**：请务必在**当前运行 Agent 的终端**中设置环境变量。

```bash
export PROCESSON_API_KEY="<your-processon-api-key>"
```

获取地址：[ProcessOn 开发者中心](https://smart.processon.com/user)

### 命令行调用参考

```bash
# 全自动生成：DSL + 图片渲染
python3 scripts/processon_api_client.py "请生成一张专业流程图"

# 仅生成 DSL (不渲染图片)
python3 scripts/processon_api_client.py --no-render "请生成一张专业流程图"
```

## 示例优化 Prompt

> **用户意图**：帮我画一个登录流程。
> **优化后**：请生成一张专业的流程图，描述用户登录注册流程。包含：前端校验、后端鉴权、数据库查询、Token 发放。要求：布局清晰，使用标准流程图符号，明确开始和结束节点，配色协调。

> **User intent**: Draw a user login flow.
> **Optimized prompt**: Please generate a professional flowchart for the user login and registration flow. Include frontend validation, backend authentication, database lookup, and token issuance. Use a clean layout, standard flowchart symbols, clear start and end nodes, and a polished color palette.
