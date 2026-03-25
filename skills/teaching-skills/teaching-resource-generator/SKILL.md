---
name: teaching-resource-generator
description: "Generate teaching resources including slide deck outlines, progressive exercises, hands-on case studies, and learning guides with self-assessment checkpoints. Use when the user asks to create courseware, design practice exercises, build teaching materials, develop lesson content, or generate educational resources."
---

# 教学资源生成技能

Generate courseware, exercises, case studies, and learning guides for educational content.

## Workflow

1. **需求分析** - Gather requirements:
   - 确定教学目标和受众水平
   - 明确资源类型（课件/练习/案例/指南）

2. **内容设计** - Design the resource:
   - 规划内容结构
   - 编写详细内容

3. **格式优化** - Polish and format:
   - 选择合适格式，优化排版

### Example: Progressive Exercise Set

```markdown
## Exercise: Python List Comprehension (3 levels)

### Level 1 - Basic (Remember/Understand)
Convert this for loop to a list comprehension:
​```python
result = []
for x in range(10):
    result.append(x * 2)
# Answer: result = [x * 2 for x in range(10)]
​```

### Level 2 - Intermediate (Apply)
Filter and transform: get squares of even numbers from 1-20.
​```python
# Answer: squares = [x**2 for x in range(1, 21) if x % 2 == 0]
​```

### Level 3 - Advanced (Analyze)
Flatten a 2D matrix and explain when NOT to use list comprehension.
​```python
matrix = [[1,2,3], [4,5,6], [7,8,9]]
# Answer: flat = [num for row in matrix for num in row]
# Avoid when: nested comprehensions reduce readability (3+ levels)
​```
```

### Example: Slide Deck Outline

```markdown
## Slide Deck: Introduction to REST APIs (45 min)

| Slide | Content | Duration | Activity |
|-------|---------|----------|----------|
| 1-3   | What is REST? Core principles | 10 min | Discussion: APIs you use daily |
| 4-6   | HTTP methods and status codes | 10 min | Quiz: match method to operation |
| 7-9   | Designing resources and URLs | 10 min | Exercise: design a bookstore API |
| 10-12 | Authentication and error handling | 10 min | Live demo with curl |
| 13    | Summary and next steps | 5 min | Q&A |
```

## 输出格式

- **资源基本信息**: 名称、类型、适用对象
- **内容主体**: 核心教学内容
- **练习与实践**: 巩固所学知识
- **参考资料**: 延伸学习资源

## 最佳实践

- 确保内容准确、与课程目标对齐
- 设计递进式练习（由浅入深）
- 设计互动环节提高参与度
- 提供即时反馈机制

## Keywords

教学资源, 课件制作, 练习题设计, 教学案例, 学习指南, teaching materials, courseware, exercises, case study, learning guide