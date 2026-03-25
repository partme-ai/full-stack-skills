---
name: learning-assessor
description: "Create learning assessments including quizzes, exams, rubrics, and evaluation criteria aligned with learning objectives. Supports multiple question types, difficulty levels, and learning analytics. Use when the user asks to create quizzes, design tests, build grading rubrics, evaluate student learning, or generate assessment questions."
---

# 学习评估技能

Create assessments, rubrics, and evaluation tools aligned with learning objectives.

## Workflow

1. **Identify learning objectives** the assessment must measure
2. **Select question types** appropriate for each objective's cognitive level
3. **Draft questions** with answer keys and scoring criteria
4. **Create rubric** for subjective assessments
5. **Validate alignment** - each question maps to a specific objective

### Example: Multiple Choice Question

```markdown
**Q: Which HTTP status code indicates a resource was created successfully?**

A) 200 OK
B) 201 Created ✓
C) 204 No Content
D) 301 Moved Permanently

**Objective:** [Remember] Recall HTTP status codes and their meanings
**Difficulty:** Easy
**Explanation:** 201 Created is returned when a POST request successfully creates a new resource.
```

### Example: Rubric Template

```markdown
| Criteria          | Excellent (4)                     | Good (3)                | Developing (2)         | Beginning (1)         |
|-------------------|-----------------------------------|-------------------------|------------------------|-----------------------|
| Code correctness  | All tests pass, handles edge cases| All tests pass          | Most tests pass        | Few tests pass        |
| Code style        | Clean, well-documented, DRY       | Readable, some comments | Inconsistent style     | Difficult to read     |
| Problem solving   | Optimal solution, explains tradeoffs| Working solution       | Partial solution       | Minimal attempt       |

**Scoring:** Total = Sum of criteria scores. A: 10-12, B: 7-9, C: 4-6, D: below 4
```

## 题目设计原则

1. **目标对齐**: 每道题目都应对应明确的学习目标
2. **难度梯度**: 覆盖不同认知层次（记忆、理解、应用、分析、评价、创造）
3. **清晰明确**: 题目表述清晰，避免歧义
4. **有效性**: 题目应能有效测量目标知识和技能

## 输出格式

- **评估目标**: 明确要评估的内容
- **评估题目**: 具体的题目、答案和解析
- **评估标准**: 详细的评分标准或 rubric
- **分析报告**: 学习分析和反馈建议

## Keywords

学习评估, 测验设计, 评分标准, rubric, 考试题目, quiz, test, exam, grading, assessment, evaluation
