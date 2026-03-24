# 可整合技能库评估（草案）

本文档评估若干**未并入** [full-stack-skills](https://github.com/partme-ai/full-stack-skills) 的外部仓库，是否适合将部分技能迁入 `skills/<组>/`，供维护者决策。执行整合前须核对：**许可证**、**与现有技能重复度**、**目录规范**（见 [skill-group-mapping.md](skill-group-mapping.md)）。

---

## 1. mattpocock/skills

| 项 | 说明 |
|----|------|
| **仓库** | [github.com/mattpocock/skills](https://github.com/mattpocock/skills) |
| **性质** | 个人导出的 `.claude` 技能目录，内容随作者变更 |
| **整合价值** | 若含 TypeScript 高级模式、Zod、教学向短文等，可挑选与 **typescript** / **dev-utils** 不重复条目 |
| **风险** | 许可证需逐条确认；更新节奏与个人偏好强绑定 |
| **建议优先级** | **低**：优先保持「外链 + 用户自行克隆」；确有高频缺失再单技能迁入 |

---

## 2. Dimillian/Skills

| 项 | 说明 |
|----|------|
| **仓库** | [github.com/Dimillian/Skills](https://github.com/Dimillian/Skills) |
| **性质** | 个人 Codex 技能 |
| **整合价值** | 若含 SwiftUI/iOS、独立开发者工作流，可补充本仓库 **mobile-native-skills** 之上层模式 |
| **风险** | 与本仓库 **ios-swift** 等可能重叠；需 diff 后迁入 |
| **建议优先级** | **低～中**：先文档外链，确认社区需求后再选 1～2 个技能试点 |

---

## 3. Ceeon/videocut-skills

| 项 | 说明 |
|----|------|
| **仓库** | [github.com/Ceeon/videocut-skills](https://github.com/Ceeon/videocut-skills) |
| **性质** | 视频剪辑 Agent（Claude Code Skills） |
| **整合价值** | 可新建组如 **media-skills** 或归入 **dev-utils-skills** 下的「内容工程」子集 |
| **风险** | 依赖 FFmpeg/剪辑链路，体积与维护成本较高 |
| **建议优先级** | **低**：全栈核心路径非必需；更适合 **external-skills.md** 外链 |

---

## 4. 执行整合的检查清单（若决定迁入）

1. 目标路径：`skills/<组目录>/<skill-name>/`，且 `SKILL.md` 的 `name` 与目录名一致  
2. 更新 [.claude-plugin/marketplace.json](../.claude-plugin/marketplace.json) 对应插件的 `skills` 数组  
3. 更新 [skill-group-mapping.md](skill-group-mapping.md)  
4. 在 [external-skills.md](external-skills.md) 将该项从「可整合」改为「已整合（本仓库）」并保留上游致谢链接  

---

## 5. 结论摘要

| 仓库 | 建议 |
|------|------|
| mattpocock/skills | 维持外链；有明确缺口再单技能评估 |
| Dimillian/Skills | 维持外链；iOS/Swift 深度需求时再评估 |
| Ceeon/videocut-skills | 维持外链；不优先并入 monorepo |

本文件随社区反馈迭代；整合决策以仓库维护者 PR 与审阅为准。
