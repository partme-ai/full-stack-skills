# Spec Kit 技能整合说明

本仓库在 `skills/` 下已复制 [dceoy/speckit-agent-skills](https://github.com/dceoy/speckit-agent-skills) 的 **speckit-*** 技能，用于与「需求→部署」全链路映射表配合使用。

## 技能列表

| 技能名 | 说明 |
|--------|------|
| speckit-constitution | 定义项目原则与约束 |
| speckit-specify | 从自然语言生成/更新功能规格（what/why） |
| speckit-clarify | 澄清规格歧义 |
| speckit-baseline | 从现有代码生成规格（可选入口） |
| speckit-plan | 生成技术方案（how） |
| speckit-analyze | 一致性/依赖校验 |
| speckit-tasks | 生成有序工作项 |
| speckit-taskstoissues | 任务转 Issue（如 GitHub） |
| speckit-checklist | 检查清单 |
| speckit-implement | 按规格与任务执行实现 |

## 与本链路的关系

- **阶段→技能映射**：见 [pipeline-stage-to-skills.md](pipeline-stage-to-skills.md)；其中需求/PRD、领域模型/架构/任务拆分、实现等阶段均列出可选 speckit-* 对应项。
- **上游**：原始技能与 Spec Kit 工作流见 [speckit-agent-skills README](https://github.com/dceoy/speckit-agent-skills)。若需 `.specify/` 模板或脚本，可从该仓库另行复制或通过 [Spec Kit](https://github.com/github/spec-kit) 安装使用。

## 使用方式

- 与 stitch-skills、pencil-skills、full-stack-skills 其他技能一并加载，由编排 Agent 或人工按阶段按需调用。
- 各 speckit-* 的 SKILL.md 保持上游格式；仅在本仓库文档中说明其与全链路阶段的对应关系。
- 独立仓库 **speckit-skills**（PartMeAI）提供与 speckit-agent-skills 对齐的 10 个技能及 Claude Code/Cursor 插件市场配置，可与 full-stack、t2ui、stitch、pencil 技能一并使用。
