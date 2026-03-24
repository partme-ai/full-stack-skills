# 需求→部署全链路：阶段与技能映射表

本文档固化了「需求 → PRD → 原型与设计 → 领域模型与架构 → 任务拆分 → 开发 → 测试 → 部署」各阶段对应的技能名及所属仓库，供编排 Agent 或 PartMe Claw 按需调用。当前阶段仅做技能准备，不落编排实现。

**技能来源**：speckit-skills（或 speckit-agent-skills）、t2ui-skills、stitch-skills、pencil-skills、full-stack-skills。

---

## 阶段总览（产品 / 设计 / 开发）

| 阶段 | 仓库 | 职责 | 输入 → 输出 |
|------|------|------|-------------|
| **产品阶段** | speckit-skills（即 speckit-agent-skills / 本仓库 speckit-*） | 描述需求、澄清需求 | 需求分析 → 原始需求 → PRD 文档 |
| **设计阶段** | t2ui-skills（需求转译） | 需求转译 | PRD 文档 → ASCII 界面；PRD 文档 → Stitch 设计语言；PRD 文档 → Pencil 设计语言 |
| **设计阶段** | stitch-skills | 原型设计 | Stitch 设计语言 → Stitch MCP → 原型图 |
| **设计阶段** | pencil-skills | 界面设计 | Pencil 设计语言 → Pencil MCP → 产品图 |
| **开发阶段** | speckit-skills（即 speckit-agent-skills / 本仓库 speckit-*） | 领域与架构、技术细分 | 领域模型设计、系统架构设计、技术细分 |

说明：t2ui-skills 在本链路中承担「需求转译」（text/PRD to UI 描述），只产出描述语言，不调用 Stitch/Pencil MCP。

---

## 1. 需求侧（产品阶段）

| 阶段 | 技能名 | 仓库 | 说明 |
|------|--------|------|------|
| 需求 / 一句话需求 / 需求分析 → 原始需求 | full-stack-doc | full-stack-skills | 需求分析模板、需求调研模板 |
| 需求 / PRD（what/why） | speckit-specify | speckit-agent-skills（可选） | Spec Kit：从自然语言生成/更新规格 |
| 需求澄清 / 歧义消除 | speckit-clarify | speckit-agent-skills（可选） | Spec Kit：澄清规格 |
| 清楚的原始需求 → PRD 文档 | full-stack-doc | full-stack-skills | PRD 文档模板 |
| 需求/PRD → 结构化设计输入 | stitch-ui-design-spec-generator, stitch-ui-prompt-architect | stitch-skills | 设计规范与 Stitch 提示词 |
| PRD 界面 → 多格式描述 | tui-prd-to-descriptions | t2ui-skills | ASCII 补充 PRD；Stitch 可执行描述供 stitch-skills；Pencil 可执行描述供 pencil-skills。不调用 Stitch/Pencil MCP |

**缺口**：独立「一句话需求归纳」技能可后续补充；当前可由 full-stack-doc + 对话或 speckit-clarify 覆盖。

---

## 2. 设计阶段（需求转译 → 原型 → 界面）

| 阶段 | 技能名 | 仓库 | 说明 |
|------|--------|------|------|
| **需求转译**（PRD → 多格式描述） | tui-prd-to-descriptions | t2ui-skills | PRD 文档 → ASCII 界面；PRD → Stitch 设计语言；PRD → Pencil 设计语言。不调用 MCP |
| 设计规范 / 视觉与交互 DNA | full-stack-doc, stitch-ui-design-spec-* | full-stack-skills, stitch-skills | 视觉与交互 DNA 模板；uviewpro/element 等框架设计规范 |
| **原型设计**（Stitch 设计语言 → 原型图） | stitch-mcp-*；编排：stitch-ui-designer | stitch-skills | Stitch 设计语言 → Stitch MCP → 原型图 |
| **界面设计**（Pencil 设计语言 → 产品图） | pencil-mcp-*；编排：pencil-ui-designer；pencil-design-from-stitch-html | pencil-skills | Pencil 设计语言 → Pencil MCP → 产品图（.pen）；或 Stitch HTML → .pen |
| UI 设计说明 | full-stack-doc, stitch-design-md | full-stack-skills, stitch-skills | UI 设计说明模板；从 Stitch 项目产出 DESIGN.md |
| 交互设计（规范与说明） | stitch-ued-guide, stitch-ui-design-spec-* | stitch-skills | UED 指南；框架规范 |

---

## 3. 开发阶段（领域模型 / 系统架构 / 技术细分）

| 阶段 | 技能名 | 仓库 | 说明 |
|------|--------|------|------|
| **领域模型设计** | full-stack-doc, ddd4j-project-creator, ddd-cola, plantuml；speckit-* | full-stack-skills；speckit-skills | 领域模型说明模板；DDD/COLA；PlantUML |
| **系统架构设计** | full-stack-doc, drawio-architecture, plantuml；speckit-plan | full-stack-skills；speckit-skills | 系统架构设计模板；DrawIO；PlantUML |
| **技术细分** | full-stack-doc, skill-sop-creator；speckit-tasks | full-stack-skills；speckit-skills | 任务拆分、技术细分、可执行工作项 |
| 技术策略（how） | speckit-plan | speckit-agent-skills（可选） | Spec Kit：技术方案/计划 |
| 任务列表（可执行工作项） | speckit-tasks | speckit-agent-skills（可选） | Spec Kit：生成有序任务 |
| 一致性/依赖校验 | speckit-analyze | speckit-agent-skills（可选） | Spec Kit：分析校验 |

---

## 4. 前端开发 / 后端开发

| 阶段 | 技能名 | 仓库 | 说明 |
|------|--------|------|------|
| 前端（Vue/React/uni-app，基于设计稿） | stitch-uviewpro-components, stitch-vue-element-components, stitch-react-components 等；frontend-design | stitch-skills, full-stack-skills | Stitch 屏→组件代码；前端设计 |
| 后端（Java/Node 等） | ddd4j-project-creator, spring-boot, nestjs 等 | full-stack-skills | DDD4j；Spring Boot；NestJS |
| 实现（代码落地） | speckit-implement | speckit-agent-skills（可选） | Spec Kit：按规格与任务执行实现 |

**说明**：**桌面/跨平台**开发可选用外部 [tauri-skills](https://github.com/partme-ai/tauri-skills)（Tauri 应用开发；本仓库已含 `skills/tauri-skills/`）。**Node 版本管理（nvm）** 技能已落地：本仓库 `skills/nvm-skills/`（15 个技能），marketplace 插件 **nvm-skills**；详见 [docs/nvm-skills.md](nvm-skills.md) 与 [skill-group-mapping.md](skill-group-mapping.md)。

---

## 5. 自动化测试 / 自动化部署

| 阶段 | 技能名 | 仓库 | 说明 |
|------|--------|------|------|
| 自动化测试 | test-writer, playwright, pytest, jest, webapp-testing | full-stack-skills | 测试编写；E2E/单元 |
| 自动化部署 | github-actions, gitlab-ci, jenkins, docker, kubernetes | full-stack-skills | CI/CD；容器与编排 |

---

## 6. Spec Kit 与本链路的对应关系

| Spec Kit 阶段 | 本链路阶段 | 本仓库技能 | 外部/可选 |
|---------------|------------|------------|-----------|
| Constitution | 项目原则/约束 | full-stack-doc | speckit-constitution |
| Specify | 需求/PRD（what/why） | full-stack-doc | speckit-specify |
| Clarify | 需求澄清 | — | speckit-clarify |
| Plan | 领域模型/架构/技术策略 | full-stack-doc, ddd4j, plantuml, drawio | speckit-plan |
| Analyze | 一致性校验 | — | speckit-analyze |
| Tasks | 任务拆分与工作项 | full-stack-doc（技术细分）, skill-sop-creator | speckit-tasks |
| Implement | 开发/测试/部署 | stitch-*, pencil-*, ddd4j, test-writer, github-actions 等 | speckit-implement |

使用 Spec Kit 时，可在运行环境中安装 [dceoy/speckit-agent-skills](https://github.com/dceoy/speckit-agent-skills)，将 `skills/` 与 stitch-skills、pencil-skills、full-stack-skills 一并加载。**本仓库**已在 `full-stack-skills/skills/` 内复制 speckit-* 技能，详见 [speckit-agent-skills.md](speckit-agent-skills.md)。

---

## 7. 文档与编排

- **阶段→技能**：本文档为权威映射表；后续全链路编排 Agent（如 product-dev-pipeline）按此表按需调用技能。
- **各仓库说明**：speckit-skills（speckit-agent-skills）、t2ui-skills、stitch-skills、pencil-skills、tauri-skills、full-stack-skills 的 AGENTS.md 或 README 中已注明参与本链路（或边界），并指向本文档（或 workspace 内等效路径）。
