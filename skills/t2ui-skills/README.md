<div align="center">

# T2UI Skills

**PRD 界面 → ASCII / Stitch 描述 / Pencil 描述 的多格式输出**

![Version](https://img.shields.io/badge/Version-0.0.2-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-green)

</div>

## 定位与边界（无能力交叉）

**t2ui-skills** 关注如何将 **PRD 中的界面描述** 转化为三种可交付物：

| 输出 | 用途 | 下游 |
|------|------|------|
| **ASCII 界面** | 补充 PRD 文档、评审与 CLI/日志环境示意 | 插入 PRD 的界面原型关联或附录 |
| **Stitch 可执行描述** | Stitch 可识别的提示词/描述语言 | 由 [stitch-skills](https://github.com/partme-ai/stitch-skills) 消费并**绘制原型** |
| **Pencil 可执行描述** | Pencil 可执行的 PENCIL_PLAN / batch_design | 由 [pencil-skills](https://github.com/partme-ai/pencil-skills) 消费并**产出界面设计** |

- **stitch-skills**：PRD → Stitch 提示词 → **用 Stitch 画**高度还原需求的原型。
- **pencil-skills**：原型 或 (PRD + 设计说明 + 组件约束) → **用 Pencil 画**界面设计。
- **t2ui-skills**：PRD 界面 → **只产出** ASCII + Stitch 描述 + Pencil 描述；**不调用** Stitch MCP 或 Pencil MCP，不与两者能力交叉。

详见 [docs/boundary-and-outputs.md](docs/boundary-and-outputs.md)。全链路阶段映射见 [full-stack-skills/docs/pipeline-stage-to-skills.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/pipeline-stage-to-skills.md)，技能生态总览见 [full-stack-skills/docs/skills-ecosystem.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/skills-ecosystem.md)。

## 技能组成

- **tui-prd-to-descriptions**：从 PRD 的界面/屏幕描述一次性产出上述三种格式（ASCII、Stitch 描述、Pencil 描述）。见 `skills/tui-prd-to-descriptions/`。
- **tui-***（78 个组件技能）：单组件级 ASCII + COMPONENT_SPEC + PENCIL_SPEC + PENCIL_BATCH_DESIGN，作为词汇表与规范，供屏级/PRD 级描述生成时引用。

## 文档

| 文档 | 说明 |
|------|------|
| [docs/boundary-and-outputs.md](docs/boundary-and-outputs.md) | 与 stitch-skills、pencil-skills 的边界及三种输出格式 |
| [docs/prd-interface-to-multi-format.md](docs/prd-interface-to-multi-format.md) | PRD 界面 → 多格式的输入/输出约定与推荐流程 |

## 安装（Marketplace）

将本仓库添加为 Skills Marketplace 源，并启用 t2ui-skills 插件。

![Add marketplace](media/add_marketplace.png)

## 约定

- 默认网格：`cellWidthPx=8`，`cellHeightPx=16`
- 默认移动端画布：`390x844`
- ASCII 渲染默认宽度：`widthCols=70`

## License

Apache-2.0
