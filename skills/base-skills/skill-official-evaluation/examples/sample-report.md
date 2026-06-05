# Skill 官方评估报告（Official Evaluating）

目标：`skills/document-skills/mermaid`

## 结论

- 总体结论：通过（有改进空间）
- 主要问题（Top 3）：
  1. SKILL.md 正文偏长，部分内容可迁移到 references/（渐进式披露更清晰）
  2. 触发条件写得很“强”，可能产生误触发，建议配一组 should-not-trigger 例子（描述优化）
  3. 若未来加入可执行脚本，建议补充 `--help`/结构化输出/非交互约束说明（脚本规范）

## 规范对照清单

| 项目 | 结果 | 证据 | 建议 |
| --- | --- | --- | --- |
| SKILL.md frontmatter 合规 | Pass | 含 name/description/license | 可补 compatibility（若有环境要求） |
| name/目录名一致 | Pass | name=mermaid，目录=mermaid | - |
| description 触发覆盖 | Pass | 覆盖“画图/可视化/mermaid”等意图 | 增加 near-miss 的不触发边界 |
| 渐进式披露（references/assets） | Needs improvement | SKILL.md 正文包含大量细节 | 迁移长清单到 references/，正文保留流程 |
| scripts 可执行性与非交互 | N/A | 无 scripts/ | - |
| 安全与敏感信息 | Pass | 未发现敏感信息 | - |

## 改进建议（按优先级）

1. 抽取“关键词大清单”“版本兼容细节”到 `references/`，正文只保留“选择图类型→参考示例→输出”工作流
2. 为 description 增加 should-trigger / should-not-trigger 测试集并迭代优化
3. 为未来可能的脚本型能力预留脚本接口规范（非交互、结构化输出）

