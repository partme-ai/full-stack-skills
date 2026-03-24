## PlantUML Agent Skills 规划清单

- plantuml-install ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-install 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并严格遵循以下设计规格：
- **边界**：本地安装前置条件与下载方式（Java 版本检查、Graphviz 安装、plantuml.jar 获取）。
- **关键点**：区分 Windows 内置 Graphviz 与 Linux/macOS 外部依赖；提供最小可运行安装路径。
- **场景**：首次接入 PlantUML、本地研发环境搭建、离线渲染准备。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型完成 PlantUML 本地安装准备。

- plantuml-quickstart ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-quickstart 的 skills，必须参考
- `https://plantuml.com/zh/`
  并严格遵循以下设计规格：
- **边界**：最小示例与基础语法（@startuml/@enduml、基本关系与输出）。
- **关键点**：覆盖 CLI 处理单文件与 GUI 目录模式的差异与产物位置。
- **场景**：新手入门、演示验证、PoC 快速出图。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型快速生成第一张图。

- plantuml-cli-output ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-cli-output 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并严格遵循以下设计规格：
- **边界**：命令行运行与输出控制（格式选择、输出目录、批量处理）。
- **关键点**：说明常见输出格式与适用场景，包含错误排查基本路径。
- **场景**：批量渲染、CI 产物生成、文档自动化输出。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型稳定生成可分发产物。

- plantuml-server-docker ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-server-docker 的 skills，必须参考
- `https://plantuml.com/zh/`
  并严格遵循以下设计规格：
- **边界**：使用官方镜像启动 PlantUML Server，并进行本地访问验证。
- **关键点**：端口映射、容器生命周期管理与基础健康检查步骤。
- **场景**：团队共享渲染服务、远程渲染、文档平台集成。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型在容器环境中启用在线渲染。

- plantuml-sequence ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-sequence 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/sequence.md`
  并严格遵循以下设计规格：
- **边界**：序列图角色、消息、同步/异步与生命周期表达。
- **关键点**：强调参与者命名与消息顺序的可读性。
- **场景**：接口调用链、业务流程交互、系统间通信。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出可执行的时序表达。

- plantuml-use-case ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-use-case 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/use-case.md`
  并严格遵循以下设计规格：
- **边界**：参与者、用例、包含/扩展关系与系统边界。
- **关键点**：避免把流程细节塞入用例图。
- **场景**：需求澄清、功能范围界定、业务与系统对齐。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型完成需求级建模。

- plantuml-class ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-class 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/class.md`
  并严格遵循以下设计规格：
- **边界**：类、属性、方法、继承与关联关系。
- **关键点**：保持领域边界清晰与可实现性。
- **场景**：领域建模、代码设计评审、对象结构表达。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型进行结构建模。

- plantuml-object ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-object 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/object.md`
  并严格遵循以下设计规格：
- **边界**：对象实例、属性快照与对象间关联。
- **关键点**：突出运行期结构而非类级结构。
- **场景**：运行期状态分析、调试沟通、实例关系说明。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型表达实例状态。

- plantuml-activity ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-activity 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/activity.md`
  并严格遵循以下设计规格：
- **边界**：活动节点、分支、并行与结束节点。
- **关键点**：流程可读性与异常路径表达。
- **场景**：业务流程梳理、流程优化、操作规程说明。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出流程图。

- plantuml-component ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-component 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/component.md`
  并严格遵循以下设计规格：
- **边界**：组件、接口、依赖与分组。
- **关键点**：强调组件边界与依赖方向。
- **场景**：系统拆分、模块划分、接口依赖沟通。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型表达模块结构。

- plantuml-deployment ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-deployment 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/deployment.md`
  并严格遵循以下设计规格：
- **边界**：节点、设备、运行环境与部署关系。
- **关键点**：区分运行节点与部署单元。
- **场景**：部署拓扑、环境说明、发布评审。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出部署结构。

- plantuml-state ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-state 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/state.md`
  并严格遵循以下设计规格：
- **边界**：状态、转移、初始/终止状态与复合状态。
- **关键点**：避免把业务流程当作状态机。
- **场景**：状态机建模、设备/订单状态管理、规则说明。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出状态逻辑。

- plantuml-timing ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-timing 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/timing.md`
  并严格遵循以下设计规格：
- **边界**：时间轴、状态变化与时间约束。
- **关键点**：强调时间精度与同步关系。
- **场景**：协议时序、硬件信号、性能分析沟通。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出时间行为。

- plantuml-json-yaml ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-json-yaml 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/json-yaml.md`
  并严格遵循以下设计规格：
- **边界**：JSON/YAML 结构可视化与层级表达。
- **关键点**：保持输入结构与输出结构一致。
- **场景**：配置说明、数据结构展示、接口示例文档。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型直观展示数据结构。

- plantuml-ebnf ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-ebnf 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/ebnf.md`
  并严格遵循以下设计规格：
- **边界**：语法规则、符号与产生式表达。
- **关键点**：强调语法完整性与可读性。
- **场景**：语言设计、协议语法说明、规则可视化。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型表达语法结构。

- plantuml-regex ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-regex 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/regex.md`
  并严格遵循以下设计规格：
- **边界**：正则表达式结构、分组与匹配路径。
- **关键点**：清晰拆解复杂正则。
- **场景**：规则审查、匹配逻辑说明、团队沟通。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型解释复杂正则。

- plantuml-math ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-math 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/math.md`
  并严格遵循以下设计规格：
- **边界**：AsciiMath/JLaTeXMath 数学表达与渲染。
- **关键点**：保持公式清晰与结构一致。
- **场景**：算法说明、科研文档、数学建模表达。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出可读公式。

- plantuml-network ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-network 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/network.md`
  并严格遵循以下设计规格：
- **边界**：网络拓扑、节点、链路与分段。
- **关键点**：保持拓扑层次清晰。
- **场景**：网络架构、基础设施规划、运维沟通。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出网络拓扑。

- plantuml-salt ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-salt 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/salt.md`
  并严格遵循以下设计规格：
- **边界**：Salt 线框控件与布局结构。
- **关键点**：保持低保真与结构化表达。
- **场景**：界面草图、交互讨论、产品评审。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出界面骨架。

- plantuml-archimate ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-archimate 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/archimate.md`
  并严格遵循以下设计规格：
- **边界**：业务/应用/技术层的 ArchiMate 表达。
- **关键点**：分层表达与关系语义。
- **场景**：企业架构规划、能力映射、治理沟通。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型生成企业架构图。

- plantuml-sdl ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-sdl 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/sdl.md`
  并严格遵循以下设计规格：
- **边界**：SDL 过程与通信结构表达。
- **关键点**：保持规范语义一致。
- **场景**：通信协议、嵌入式系统流程建模。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出 SDL 图。

- plantuml-ditaa ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-ditaa 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/ditaa.md`
  并严格遵循以下设计规格：
- **边界**：ASCII 图形与 Ditaa 语法。
- **关键点**：强调字符对齐与可读性。
- **场景**：快速框图、流程草图、技术说明。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出 ASCII 图。

- plantuml-gantt ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-gantt 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/gantt.md`
  并严格遵循以下设计规格：
- **边界**：任务、依赖、里程碑与时间轴。
- **关键点**：避免把业务逻辑嵌入排期语法。
- **场景**：项目计划、交付排期、资源协调。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出甘特图。

- plantuml-chronology ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-chronology 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/chronology.md`
  并严格遵循以下设计规格：
- **边界**：时间线事件与阶段表达。
- **关键点**：时间顺序与事件密度控制。
- **场景**：产品里程碑、事件复盘、历史演进说明。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出时间线。

- plantuml-mindmap ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-mindmap 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/mindmap.md`
  并严格遵循以下设计规格：
- **边界**：主题层级、分支与子主题结构。
- **关键点**：保持层级简洁与逻辑一致。
- **场景**：头脑风暴、知识结构整理、方案梳理。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出思维导图。

- plantuml-wbs ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-wbs 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/wbs.md`
  并严格遵循以下设计规格：
- **边界**：工作分解结构与分层任务。
- **关键点**：任务粒度一致与层级清晰。
- **场景**：项目拆解、交付范围对齐、团队任务分工。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出 WBS。

- plantuml-er ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-er 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/er.md`
  并严格遵循以下设计规格：
- **边界**：实体、属性、关系与基数。
- **关键点**：与数据库设计可映射。
- **场景**：数据建模、表结构设计、领域对象讨论。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出 ER 图。

- plantuml-ie ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-ie 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/ie.md`
  并严格遵循以下设计规格：
- **边界**：IE 表达法的实体与关系。
- **关键点**：信息工程视角的结构表达。
- **场景**：信息架构设计、数据治理、模型规范化。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出 IE 图。

- plantuml-er-chen ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-er-chen 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/er-chen.md`
  并严格遵循以下设计规格：
- **边界**：Chen 表示法的实体、关系与属性。
- **关键点**：图符表达统一与关系可读性。
- **场景**：教学场景、理论建模、模型对比说明。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出 Chen ER 图。

- plantuml-c4 ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-c4 的 skills，必须参考
- `https://plantuml.com/zh/`
- `https://github.com/plantuml/plantuml`
  并参考示例文件：
- `/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/plantuml/examples/c4.md`
  并严格遵循以下设计规格：
- **边界**：C4 Context/Container/Component/Code 层级。
- **关键点**：层级一致与系统边界清晰。
- **场景**：架构总览、跨团队沟通、系统分层说明。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出 C4 架构图。

- plantuml-theme-style ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-theme-style 的 skills，必须参考
- `https://plantuml.com/zh/`
  并严格遵循以下设计规格：
- **边界**：主题与样式控制（theme、skinparam）。
- **关键点**：输出一致性与团队视觉规范落地策略。
- **场景**：统一品牌风格、文档视觉一致性、图表标准化。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型统一样式输出。

- plantuml-richtext-icons-sprites ✅

遵循 Agent skills 规范： `https://support.claude.com/zh-CN/articles/12512198-%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89-skills` 和 `https://agentskills.io/what-are-skills`
参考 /Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid，创建一个名称为 plantuml-richtext-icons-sprites 的 skills，必须参考
- `https://github.com/plantuml/plantuml`
  并严格遵循以下设计规格：
- **边界**：富文本、超链接、表情与图标、Sprite 能力的使用。
- **关键点**：图表可读性增强的使用边界与最佳实践。
- **场景**：交互式文档、可导航架构图、信息密度提升。
严格参考
- 官方示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/skill-creator 
- 个人示例：/Users/wandl/workspaces/workspace-partme-ai/full-stack-skills/skills/mermaid 
SKILL.md 内容规划，结构清晰，触发逻辑清晰，流程完善，可以指导 大模型输出可读性更强的图表。
