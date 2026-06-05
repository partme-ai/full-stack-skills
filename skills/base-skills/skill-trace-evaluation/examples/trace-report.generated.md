# TRACE 评测报告

> 评估目标：`{SKILL_PATH}` | 评估时间：{TIMESTAMP}
> 评估依据：SkillHub TRACE 评测体系
> 
> 特别说明：本报告不是官方报告，而是 TRACE 评测体系的模拟检测，最终测评结果以 SkillHub 为准。

---

## 📊 综合评分

| 维度 | 得分 | 等级 |
|------|:----:|:----:|
| **T** · Trust（可信任度） | {T_SCORE} | {T_GRADE} |
| **R** · Reliability（可靠性） | {R_SCORE} | {R_GRADE} |
| **A** · Adaptability（适用性） | {A_SCORE} | {A_GRADE} |
| **C** · Convention（规范性） | {C_SCORE} | {C_GRADE} |
| **E** · Effectiveness（有效性） | {E_SCORE} | {E_GRADE} |
| **综合** | **{OVERALL}** | **{OVERALL_GRADE}** |

> 等级阈值：≥4.7 优秀（Excellent） | ≥4.2 良好（Good） | ≥3.5 一般（Fair） | <3.5 待改进（Needs improvement）

---

## 一句结语

{ONE_SENTENCE}

---

## 🛡️ T · Trust（可信任度）— {T_SCORE} / 5.0

> 衡量 Skill 在安全、合规和可控性方面是否可信，是整个评估体系中的**红线维度**。

| 子项 | 得分 | 关键证据 | 风险/建议 |
|------|:----:|------|------|
| **T1 安全性扫描** | {T1} | {T1_EVIDENCE} | {T1_RISK} |
| **T2 国内适配性** | {T2} | {T2_EVIDENCE} | {T2_RISK} |
| **T3 边界/权限控制** | {T3} | {T3_EVIDENCE} | {T3_RISK} |
| **T4 安全声明** | {T4} | {T4_EVIDENCE} | {T4_RISK} |

### T 维总结

| 亮点 | 待改进 |
|------|--------|
| {T_STRENGTH} | {T_WEAKNESS} |

---

## 🔄 R · Reliability（可靠性）— {R_SCORE} / 5.0

> 衡量 Skill 在评测运行中的**稳定性、可复现性和交付可靠性**。

| 子项 | 得分 | 关键证据 | 风险/建议 |
|------|:----:|------|------|
| **R1 异常处理** | {R1} | {R1_EVIDENCE} | {R1_RISK} |
| **R2 可运行性** | {R2} | {R2_EVIDENCE} | {R2_RISK} |
| **R3 交付物完整性** | {R3} | {R3_EVIDENCE} | {R3_RISK} |
| **R4 降级处理** | {R4} | {R4_EVIDENCE} | {R4_RISK} |

### R 维总结

| 亮点 | 待改进 |
|------|--------|
| {R_STRENGTH} | {R_WEAKNESS} |

---

## 🎯 A · Adaptability（适用性）— {A_SCORE} / 5.0

> 衡量 Skill 是否适合其声明的使用场景，以及在真实候选环境中是否容易被**正确识别和调用**。

| 子项 | 得分 | 关键证据 | 风险/建议 |
|------|:----:|------|------|
| **A1 边界清晰度** | {A1} | {A1_EVIDENCE} | {A1_RISK} |
| **A2 Description 触发质量** | {A2} | {A2_EVIDENCE} | {A2_RISK} |
| **A3 国内适用性** | {A3} | {A3_EVIDENCE} | {A3_RISK} |
| **A4 场景覆盖广度** | {A4} | {A4_EVIDENCE} | {A4_RISK} |

### A 维总结

| 亮点 | 待改进 |
|------|--------|
| {A_STRENGTH} | {A_WEAKNESS} |

---

## 📐 C · Convention（规范性）— {C_SCORE} / 5.0

> 衡量 Skill 是否具备清晰、可维护、可复用的**结构基础**。

| 子项 | 得分 | 关键证据 | 风险/建议 |
|------|:----:|------|------|
| **C1 用途/适用说明** | {C1} | {C1_EVIDENCE} | {C1_RISK} |
| **C2 渐进披露** | {C2} | {C2_EVIDENCE} | {C2_RISK} |
| **C3 元信息结构** | {C3} | {C3_EVIDENCE} | {C3_RISK} |
| **C4 Gotchas 与指令规范** | {C4} | {C4_EVIDENCE} | {C4_RISK} |

### C 维总结

| 亮点 | 待改进 |
|------|--------|
| {C_STRENGTH} | {C_WEAKNESS} |

---

## ⚡ E · Effectiveness（有效性）— {E_SCORE} / 5.0

> 衡量 Skill 是否**真正提升任务结果**，以及这种提升是否值得付出相应代价。

| 子项 | 得分 | 关键证据 | 风险/建议 |
|------|:----:|------|------|
| **E1 任务完成度** | {E1} | {E1_EVIDENCE} | {E1_RISK} |
| **E2 正确性/权威性** | {E2} | {E2_EVIDENCE} | {E2_RISK} |
| **E3 交付物质量** | {E3} | {E3_EVIDENCE} | {E3_RISK} |
| **E4 增益归因** | {E4} | {E4_EVIDENCE} | {E4_RISK} |

### E 维总结

| 亮点 | 待改进 |
|------|--------|
| {E_STRENGTH} | {E_WEAKNESS} |

---

## 📊 no-skill 基线对比

| 对比维度 | no-skill（裸模型） | 启用此 skill | 增益 |
|----------|:---:|:---:|:---:|
| 概念准确性 | {BASELINE_ACCURACY} | {SKILL_ACCURACY} | {GAIN_ACCURACY} |
| 适用场景判断 | {BASELINE_FIT} | {SKILL_FIT} | {GAIN_FIT} |
| 反模式/错误检测 | {BASELINE_AP} | {SKILL_AP} | {GAIN_AP} |
| 知识可追溯性 | {BASELINE_TRACE} | {SKILL_TRACE} | {GAIN_TRACE} |
| Token 成本 | 0 | ~{TOKEN_COST} tokens | {COST_LEVEL} |

---

## 📋 官方规范合规（agentskills.io）

| # | 检查项 | 结果 | 证据 |
|---|--------|:----:|------|
| 1 | SKILL.md 存在 | ✅/❌ | {OFFICIAL_O1} |
| 2 | Name 与目录名一致 | ✅/❌ | {OFFICIAL_O2} |
| 3 | Name 格式有效（kebab-case） | ✅/❌ | {OFFICIAL_O3} |
| 4 | Description 有效（1-1024 chars） | ✅/❌ | {OFFICIAL_O4} |
| 5 | License 字段 | ✅/⚠️/❌ | {OFFICIAL_O5} |
| 6 | 目录结构规范 | ✅/⚠️ | {OFFICIAL_O6} |
| 7 | 渐进式披露质量 | ✅/⚠️ | {OFFICIAL_O7} |
| 8 | Description 触发质量 | ✅/⚠️ | {OFFICIAL_O8} |
| 9 | 脚本安全性 | ✅/⚠️/N/A | {OFFICIAL_O9} |
| 10 | 密钥/敏感信息扫描 | ✅/❌ | {OFFICIAL_O10} |

---

## 💡 优化建议（优先级排序）

| 优先级 | 维度 | 建议 |
|:--:|------|------|
| P1 | {P1_DIM} | {P1_SUGGESTION} |
| P2 | {P2_DIM} | {P2_SUGGESTION} |
| P3 | {P3_DIM} | {P3_SUGGESTION} |

---

## 📦 Skill 基础画像

| 指标 | 值 |
|------|-----|
| 路径 | {SKILL_PATH} |
| SKILL.md | {BODY_LINES} lines · {BODY_CHARS} chars |
| References | {REF_COUNT} files · {REF_SUBDIRS} subdirs |
| Examples | {EX_COUNT} files |
| Scripts | {SCRIPT_COUNT} files |
| License | {LICENSE} |
| Secrets | {SECRETS_DETECTED} |
| Gotchas | {GOTCHAS_COUNT} domain-specific |
| 中文化 | {CHINESE_STATUS} |
| Skill Type | {SKILL_TYPE} |

---

> 评估依据 **SkillHub TRACE 评测体系**
> 官方规范合规检查基于 **agentskills.io** 标准
> Generated {TIMESTAMP} · {SKILL_NAME}
