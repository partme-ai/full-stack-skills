## Mermaid Agent Skills 规划清单

- mermaid-markdown-embed ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-markdown-embed 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
- `https://wiki.hiwepy.com/docs/markdown/markdown-1h02l64ugip8u`
  并严格遵循以下设计规格：
- **边界**：Mermaid 在 Markdown 中的嵌入与渲染规范（代码块、语言标识、兼容性说明）。
- **关键点**：明确 fenced code block 的最小可运行格式与常见渲染环境差异。
- **场景**：文档化交付、README/技术规范编写、知识库图文混排。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出可渲染的 Mermaid Markdown 片段。

- mermaid-flowchart ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-flowchart 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/flowchart.md`
  并严格遵循以下设计规格：
- **边界**：节点、连线、方向与子图结构的表达。
- **关键点**：强调可读布局与一致命名，避免过度堆叠。
- **场景**：业务流程梳理、系统调用路径、教学演示。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出清晰流程图。

- mermaid-sequence ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-sequence 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/sequence.md`
  并严格遵循以下设计规格：
- **边界**：参与者、消息、同步/异步与生命周期表达。
- **关键点**：保证消息顺序与参与者角色一致性。
- **场景**：接口调用链、业务流程交互、系统间通信。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出可执行的时序表达。

- mermaid-class ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-class 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/class.md`
  并严格遵循以下设计规格：
- **边界**：类、属性、方法、继承与关联关系。
- **关键点**：结构表达与实现可落地性一致。
- **场景**：领域建模、代码设计评审、对象结构表达。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型进行结构建模。

- mermaid-state ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-state 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/state.md`
  并严格遵循以下设计规格：
- **边界**：状态、转移、初始/终止状态与复合状态。
- **关键点**：避免把流程步骤误当状态机。
- **场景**：订单/设备状态管理、规则说明、状态机建模。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出状态逻辑。

- mermaid-er ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-er 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/er.md`
  并严格遵循以下设计规格：
- **边界**：实体、关系、基数与约束表达。
- **关键点**：保持命名一致与主外键关系明确。
- **场景**：数据库设计评审、领域模型对齐、数据结构说明。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型完成 ER 建模。

- mermaid-journey ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-journey 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/journey.md`
  并严格遵循以下设计规格：
- **边界**：阶段、步骤、角色与情绪评分表达。
- **关键点**：避免将流程细节塞入旅程图。
- **场景**：用户体验分析、服务触点梳理、产品改进讨论。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出用户旅程图。

- mermaid-gantt ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-gantt 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/gantt.md`
  并严格遵循以下设计规格：
- **边界**：任务、时间轴、依赖与里程碑表达。
- **关键点**：确保日期格式与依赖关系正确可渲染。
- **场景**：项目计划、版本排期、交付里程碑展示。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出项目排期图。

- mermaid-pie ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-pie 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/pie.md`
  并严格遵循以下设计规格：
- **边界**：标题、分类与数值占比表达。
- **关键点**：保持分类名称简洁并避免过多切片。
- **场景**：指标占比展示、报告图表、汇总说明。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出占比图。

- mermaid-quadrant ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-quadrant 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/quadrant.md`
  并严格遵循以下设计规格：
- **边界**：坐标轴、象限标签与点位分布表达。
- **关键点**：轴含义明确，避免点位过密。
- **场景**：产品矩阵、优先级排序、竞争分析。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出象限图。

- mermaid-mindmap ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-mindmap 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/mindmap.md`
  并严格遵循以下设计规格：
- **边界**：层级节点、缩进结构与样式表达。
- **关键点**：层级清晰与文字精简。
- **场景**：头脑风暴、课程大纲、知识结构整理。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出思维导图。

- mermaid-timeline ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-timeline 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/timeline.md`
  并严格遵循以下设计规格：
- **边界**：时间节点、阶段分组与事件说明。
- **关键点**：时间顺序一致与里程碑突出。
- **场景**：产品发展历程、项目大事记、版本演进说明。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出时间线。

- mermaid-gitgraph ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-gitgraph 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/gitgraph.md`
  并严格遵循以下设计规格：
- **边界**：分支、提交、合并与标签表达。
- **关键点**：保证分支名称与提交序列可读。
- **场景**：Git 工作流说明、分支策略评审、发布演示。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出 Git 流程图。

- mermaid-c4 ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-c4 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/c4.md`
  并严格遵循以下设计规格：
- **边界**：系统边界、容器、组件与关系表达。
- **关键点**：层级清晰与边界职责明确。
- **场景**：架构评审、系统全景说明、跨团队沟通。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出 C4 结构图。

- mermaid-requirement ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-requirement 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/requirement.md`
  并严格遵循以下设计规格：
- **边界**：需求、关系、验证与追踪表达。
- **关键点**：需求层级清晰与可追溯性。
- **场景**：需求评审、合规追踪、验收对齐。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出需求关系图。

- mermaid-sankey ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-sankey 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/sankey.md`
  并严格遵循以下设计规格：
- **边界**：流向、权重与节点表达。
- **关键点**：流量单位一致与方向清晰。
- **场景**：能量/资金流分析、转化漏斗、资源分配说明。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出桑基图。

- mermaid-xychart ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-xychart 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/xychart.md`
  并严格遵循以下设计规格：
- **边界**：坐标轴、数据序列与标签表达。
- **关键点**：数值单位一致与尺度明确。
- **场景**：趋势分析、对比展示、指标监控。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出 XY 图表。

- mermaid-zenuml ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-zenuml 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/zenuml.md`
  并严格遵循以下设计规格：
- **边界**：以代码表达顺序逻辑与方法调用的结构化描述。
- **关键点**：强调语义化步骤与可读性。
- **场景**：业务规则说明、快速时序表达、接口调用梳理。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出简洁时序表达。

- mermaid-block ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-block 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/block.md`
  并严格遵循以下设计规格：
- **边界**：方块与连接的布局表达，强调结构分组。
- **关键点**：间距与对齐保证结构清晰。
- **场景**：系统结构概览、流程块图、模块关系说明。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出方块结构图。

- mermaid-kanban ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-kanban 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/kanban.md`
  并严格遵循以下设计规格：
- **边界**：泳道、卡片与状态流转表达。
- **关键点**：状态列清晰且一致命名。
- **场景**：工作流管理、迭代节奏跟踪、团队协作看板。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出看板流程。

- mermaid-architecture ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-architecture 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/architecture.md`
  并严格遵循以下设计规格：
- **边界**：服务、资源、分组与连线表达。
- **关键点**：明确边界与依赖方向，避免线条交叉过多。
- **场景**：系统拓扑说明、部署架构沟通、云资源关系展示。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出架构图。

- mermaid-packet ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-packet 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/packet.md`
  并严格遵循以下设计规格：
- **边界**：字段范围、位宽与标题表达。
- **关键点**：位段连续性与字段语义清晰。
- **场景**：协议字段说明、网络报文解析、教学演示。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出报文字段图。

- mermaid-radar ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-radar 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/radar.md`
  并严格遵循以下设计规格：
- **边界**：维度、刻度与多序列表达。
- **关键点**：维度数量控制与尺度一致。
- **场景**：能力评估、指标对比、画像展示。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出雷达图。

- mermaid-treemap ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 mermaid-treemap 的 skills，必须参考
- `https://mermaid.ai/open-source/intro/index.html`
- `https://github.com/mermaid-js/mermaid`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid/examples/treemap.md`
  并严格遵循以下设计规格：
- **边界**：层级结构、面积权重与标签表达。
- **关键点**：避免层级过深与权重失真。
- **场景**：资源占用分布、业务结构分析、预算分配展示。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出树图。
