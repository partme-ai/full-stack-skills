# Awesome Agent Skills — 全技能索引

_索引生成时间：2026-05-29 | 44 个技能组 | 463 个技能_

---

## 📊 技能组总览

| 分类 | 技能组 | 技能数 | 状态 |
|------|--------|:-----:|------|
| 🏗️ 架构 | [ddd](#ddd) | 16 | ✅ 全部高质量 (TRACE 4.5+) |
| 🗄️ 数据库 | [database](#database) | 5 | ✅ 全部深度技能 |
| 🎨 前端框架 | [angular](#angular) / [react](#react) / [vue](#vue) / [svelte](#svelte) / [flutter](#flutter) / [uniapp](#uniapp) / [cocos](#cocos) / [electron](#electron) | 17 | |
| 🔧 后端 | [spring](#spring) / [go](#go) / [python](#python) / [nodejs](#nodejs) | 16 | |
| 🛠️ 工具 | [build](#build) / [docker](#docker) / [devops](#devops) / [nvm](#nvm) / [vscode](#vscode) | 37 | |
| ✅ 测试 | [testing](#testing) | 9 | |
| 📄 文档 | [document](#document) | 9 | |
| 🎨 设计 | [design](#design) / [pencil](#pencil) / [drawio](#drawio) | 37 | |
| 🧩 UI库 | [antd](#antd) / [avue](#avue) / [uview](#uview) / [vue-ui](#vue-ui) / [t2ui](#t2ui) | 112 | |
| 📊 图表 | [chart](#chart) | 2 | |
| 🎮 3D | [threejs](#threejs) | 19 | |
| 🏗️ 桌面 | [tauri](#tauri) | 54 | |
| 🔢 工具 | [ascii](#ascii) / [dev-utils](#dev-utils) / [utility](#utility) | 28 | |
| 📝 规范 | [base](#base) / [openspec](#openspec) / [speckit](#speckit) | 37 | |
| 📱 原生 | [mobile-native](#mobile-native) | 2 | |
| 🤖 AI | [jimeng](#jimeng) | 8 | |
| 👥 社交 | [social](#social) | 2 | |
| 📚 教学 | [teaching](#teaching) | 3 | |
| 🔌 集成 | [stitch](#stitch) / [ocrmypdf](#ocrmypdf) | 36 | |

---

## 🗄️ database — 数据库 (5 个，全部深度优化)

| 技能 | 内容深度 | TRACE | 说明 |
|------|:---:|:----:|------|
| [redis](skills/database-skills/redis) | ~38KB | **4.67** | 9 大数据结构 + 缓存/持久化/集群/Lua/安全 |
| [mysql](skills/database-skills/mysql) | ~76KB | **4.34** | SQL语法+80+函数+引擎+索引+复制+优化 |
| [postgresql](skills/database-skills/postgresql) | ~99KB | **4.51** | JSONB+CTE+全文搜索+扩展+窗口函数+FDW |
| [oracle](skills/database-skills/oracle) | ~85KB | **4.39** | PL/SQL+AWR+RMAN+Data Guard+RAC+分析函数 |
| [elasticsearch](skills/database-skills/elasticsearch) | ~82KB | **4.38** | 查询DSL+聚合+分词器+映射+集群+ELK |

---

## 🏗️ ddd — 领域驱动设计 (16 个，全部 TRACE 4.5+)

> 设计哲学：按用户学习路径组织 — 入门认知 → 架构选型 → 架构落地 → 领域设计 → CQRS → API → 审查 → 评估 → 文档 → 测试 → DevOps

### 入门与选型
| 技能 | 职责 | TRACE |
|------|------|:----:|
| [ddd-architecture-awesome](skills/ddd-skills/ddd-architecture-awesome) | DDD 概念入门 + 适用性评估 + 复杂度阶梯 + 架构全景 | - |
| [ddd-architecture-selector](skills/ddd-skills/ddd-architecture-selector) | 5 种架构决策矩阵 + 决策树 + 域三分法 + CQRS 级别建议 | **4.59** |

### 架构落地（5 种架构独立 Skill）
| 技能 | 架构 | 项目示例 | TRACE |
|------|------|:---:|:----:|
| [ddd-architecture-layered](skills/ddd-skills/ddd-architecture-layered) | DDD 四层分层 | 7 种规模 | **4.69** |
| [ddd-architecture-onion](skills/ddd-skills/ddd-architecture-onion) | 洋葱架构 | 7 种规模 | **4.72** |
| [ddd-architecture-hexagonal](skills/ddd-skills/ddd-architecture-hexagonal) | 六边形架构 (Ports & Adapters) | 7 种规模 | **4.68** |
| [ddd-architecture-clean](skills/ddd-skills/ddd-architecture-clean) | 整洁架构 (Robert C. Martin) | 7 种规模 | **4.68** |
| [ddd-architecture-cola](skills/ddd-skills/ddd-architecture-cola) | COLA v5 菱形架构 + ddd4j 脚手架 | 7+4 种规模 | **4.67** |

### 领域与模式
| 技能 | 职责 | TRACE |
|------|------|:----:|
| [ddd-domain-designer](skills/ddd-skills/ddd-domain-designer) | 事件风暴驱动6步领域建模 + 聚合设计五步法六原则 | **4.69** |
| [ddd-event-storming](skills/ddd-skills/ddd-event-storming) | 事件风暴工作坊引导 + 6步流程 + 便签颜色规范 | **4.64** |
| [ddd-cqrs-architecture](skills/ddd-skills/ddd-cqrs-architecture) | CQRS L1/L2/L3 落地 + Event Sourcing + 幂等设计 | **4.71** |
| [ddd-api-designer](skills/ddd-skills/ddd-api-designer) | CQRS 读写 API + PO/DO/DTO/VO 转换链 + BFF + OpenAPI | **4.78** |

### 质量与运维
| 技能 | 职责 | TRACE |
|------|------|:----:|
| [ddd-code-reviewer](skills/ddd-skills/ddd-code-reviewer) | 12 种反模式 P0/P1/P2 检测 + 充血模型验证 + 5维评分 | **4.60** |
| [ddd-architecture-evaluator](skills/ddd-skills/ddd-architecture-evaluator) | DDD 成熟度5级 + 适配度评估 + 技术债务量化 | **4.71** |
| [ddd-architecture-doc](skills/ddd-skills/ddd-architecture-doc) | C4 模型 + ADR + 领域模型文档 + API 文档 | **4.54** |
| [ddd-testing-strategist](skills/ddd-skills/ddd-testing-strategist) | 测试金字塔 + TDDD + 各架构测试策略 | **4.67** |
| [ddd-devops-integration](skills/ddd-skills/ddd-devops-integration) | CI/CD + ArchUnit 自动化 + K8s 部署 + Flyway 迁移 | **4.65** |

---

## 🎨 前端框架

### angular (1)
- [angular](skills/angular-skills/angular) — Angular 框架综合指南

### antd (4)
- [ant-design-mini](skills/antd-skills/ant-design-mini) — Ant Design Mini 小程序组件库
- [ant-design-mobile](skills/antd-skills/ant-design-mobile) — Ant Design Mobile 移动端组件库
- [ant-design-react](skills/antd-skills/ant-design-react) — Ant Design React 组件库
- [ant-design-vue](skills/antd-skills/ant-design-vue) — Ant Design Vue 组件库

### ascii (13)
- [ascii-ansi-colorizer](skills/ascii-skills/...) — ANSI 配色
- [ascii-cli-logo-banner](skills/ascii-skills/...) — CLI ASCII Logo
- [ascii-diagram-boxflow](skills/ascii-skills/...) — 盒状流程图
- [ascii-image-to-ascii](skills/ascii-skills/...) — 图像转 ASCII
- [ascii-mini-charts](skills/ascii-skills/...) — ASCII 迷你图表
- [ascii-motd-profile-banner](skills/ascii-skills/...) — MOTD Banner
- [ascii-progress-and-spinner](skills/ascii-skills/...) — 进度条
- [ascii-table-renderer](skills/ascii-skills/...) — 表格渲染
- [ascii-terminal-animation-pack](skills/ascii-skills/...) — 终端动画
- [ascii-text-art-library](skills/ascii-skills/...) — 文字艺术库
- [cli-ascii-logo](skills/ascii-skills/...) — CLI Logo 生成

### avue (3)
- [avue](skills/avue-skills/avue) — Avue 框架
- [avue-crud](skills/avue-skills/avue-crud) — Avue CRUD
- [avue-form](skills/avue-skills/avue-form) — Avue Form

### vue (7)
- [vue2](skills/vue-skills/vue2) — Vue 2
- [vue3](skills/vue-skills/vue3) — Vue 3
- [vue-router](skills/vue-skills/vue-router) — Vue Router
- [vue-router-v3](skills/vue-skills/vue-router-v3) — Vue Router v3
- [vue-router-v4](skills/vue-skills/vue-router-v4) — Vue Router v4
- [vuex-vue2](skills/vue-skills/vuex-vue2) — Vuex
- [pinia](skills/vue-skills/pinia) — Pinia

### react (6)
- [react](skills/react-skills/react) — React
- [react-hooks](skills/react-skills/react-hooks) — React Hooks
- [react-native](skills/react-skills/react-native) — React Native
- [react-native-project-creater](skills/react-skills/react-native-project-creater) — RN 项目创建
- [redux](skills/react-skills/redux) — Redux
- [nextjs](skills/react-skills/nextjs) — Next.js

### 更多前端 (13)
- svelte (1) / flutter (2) / uniapp (13) / cocos (1) / electron (3) / tauri (54) / threejs (19)
- vue-ui (4) / uview (2) / t2ui (99)

---

## 🔧 后端与基础设施

### spring (7)
- [spring-boot](skills/spring-skills/spring-boot.md) / spring-data-jpa / spring-security / spring-cloud / ...

### go (2)
- [gin](skills/go-skills/gin) / [gin-gonic](skills/go-skills/gin-gonic)

### python (3)
- [flask](skills/python-skills/flask) / [django](skills/python-skills/django) / [fastapi](skills/python-skills/fastapi)

### nodejs (4)
- [express](skills/nodejs-skills/express) / [koa](skills/nodejs-skills/koa) / [fastify](skills/nodejs-skills/fastify) / nestjs

### 构建工具 — build (6)
- [vite](skills/build-skills/vite) / [webpack](skills/build-skills/webpack) / [rollup](skills/build-skills/rollup) / [rspack](skills/build-skills/rspack) / [parcel](skills/build-skills/parcel) / [dart-sass](skills/build-skills/dart-sass)

### 容器 — docker (2)
- [docker](skills/docker-skills/docker) / [docker-compose](skills/docker-skills/docker-compose)

### DevOps (6)
- [terraform](skills/devops-skills/terraform) / [kubernetes](skills/devops-skills/kubernetes) / [ansible](skills/devops-skills/ansible) / [github-actions](skills/devops-skills/github-actions) / [gitlab-ci](skills/devops-skills/gitlab-ci) / ...

### NVM (17)
- [nvm](skills/nvm-skills/nvm) 及全套管理工具

### VSCode (6)
- 扩展开发与发布

---

## ✅ 测试 — testing (9)
- [pytest](skills/testing-skills/pytest) / [junit](skills/testing-skills/junit) / [selenium](skills/testing-skills/selenium) / [playwright](skills/testing-skills/playwright) / [appium](skills/testing-skills/appium) / [detox](skills/testing-skills/detox)

---

## 📄 文档 — document (9)
- [docx](skills/document-skills/docx) / [pptx](skills/document-skills/pptx) / [pdf](skills/document-skills/pdf) / [xlsx](skills/document-skills/xlsx)
- [mermaid](skills/document-skills/mermaid) / [plantuml](skills/document-skills/plantuml) / [full-stack-doc](skills/document-skills/full-stack-doc) / ...

---

## 🎨 设计与原型

### design (4)
- [algorithmic-art](skills/design-skills/algorithmic-art)

### drawio (2)
- [drawio-flowchart](skills/drawio-skills/drawio-flowchart) / [drawio-architecture](skills/drawio-skills/drawio-architecture)

### pencil (31)
- 完整 UI 设计原型工具链

---

## 🔢 工具辅助

### base (5) — Skill 开发质量基础设施
- [skill-trace-evaluation](skills/base-skills/skill-trace-evaluation) — TRACE 五维度评测
- [skill-official-evaluation](skills/base-skills/skill-official-evaluation) — 官方规范评测
- [skill-trace-checker](skills/base-skills/skill-trace-checker) — TRACE 检查
- [skill-awesome](skills/base-skills/skill-awesome) — Skills AWESOME 列表生成

### chart (2)
- [ucharts](skills/chart-skills/ucharts) / [lime-echart](skills/chart-skills/lime-echart)

### dev-utils (12)
- 开发者工具集

### mobile-native (2)
- [android-kotlin](skills/mobile-native-skills/android-kotlin) / [ios-swift](skills/mobile-native-skills/ios-swift)

### utility (3)
- [skill-creator](skills/utility-skills/skill-creator) / [skill-installer](skills/utility-skills/skill-installer)

---

## 📝 规范驱动 — openspec/speckit (32)
- openspec (17) + speckit (15)：Spec 驱动开发完整工具链

---

## 🤖 AI — jimeng (8)
- [jimeng-prompt-text2image](skills/jimeng-skills/...) — 文生图提示词
- [jimeng-prompt-text2video](skills/jimeng-skills/...) — 文生视频提示词
- [jimeng-cli-text2image](skills/jimeng-skills/...) — CLI 生图
- [jimeng-cli-text2video](skills/jimeng-skills/...) — CLI 生视频
- 等 8 个技能

---

## 其他
- social (2) / teaching (3) / stitch (31) / ocrmypdf (5) / spring (7)

---

## 📋 本次优化记录

| 优化内容 | 涉及技能 | 成果 |
|---------|---------|------|
| **database 全组重写** | redis/mysql/postgresql/oracle/elasticsearch | 空壳 28 行 → 深度参考 76-99KB |
| **DDD 全组重构** | 15 个 DDD 技能 | TRACE 4.54-4.78，平均 4.66 |
| **项目规模示例** | 5 个架构技能 | 各 7 种项目规模 + ddd4j 真实参考 |
| **文件序号化** | 15 个 DDD 技能 | 100% 中英文序号对齐 |
| **ddd4j 融合** | cola 吸收 project-creator | 删除冗余，保留脚手架能力 |

---

_SkillHub TRACE 评测体系 | agentskills.io 官方规范_
