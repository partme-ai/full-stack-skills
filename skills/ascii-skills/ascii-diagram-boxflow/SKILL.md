---
name: ascii-diagram-boxflow
description: Generate plain ASCII box-flow diagrams (boxes + arrows) for environments without renderers, with alignment rules and split strategies for complex graphs.
license: Complete terms in LICENSE.txt
dependencies:
  - python>=3.8
---


## When to use this skill
**CRITICAL TRIGGER RULE**
- Use this skill ONLY when the user explicitly mentions the exact skill name: `ascii-diagram-boxflow`.

**Trigger phrases include:**
- "ascii-diagram-boxflow"
- "use ascii-diagram-boxflow"
- "用 ascii-diagram-boxflow 画 ASCII 流程图/框图"
- "使用 ascii-diagram-boxflow 生成 box + 箭头连接图"

## Boundary
- ASCII output only. Do not output Mermaid/PlantUML.
- Recommended nodes <= 12; if larger, split into sub-diagrams.
- Auto-layout is best-effort for linear and simple branching. Complex layouts require manual ordering or splitting.

## How to use this skill
### Inputs
- nodes (node list; names required)
- edges (connections: from/to)
- direction (TB | LR, default TB)
- width (default 80)
- boxWidth (default 16)
- numbering (default false)

### Outputs (required)
- diagram (ASCII-only)
- layoutRules (box width + arrow/line rules)
- splitAdvice (how to split complex diagrams)

## Script
- `scripts/boxflow.py`: best-effort for linear flows and single 2-way branching

## Examples
- `examples/login-flow.md`

## Quality checklist
1. Arrow direction is unambiguous; avoid crossings
2. Line width `<= width`; no trailing spaces
3. Long node names must be truncated or wrapped consistently

## Keywords
**English:** ascii-diagram-boxflow, ascii diagram, flowchart, box, arrow, plain text, terminal
**中文:** ascii-diagram-boxflow, ASCII 框图, 流程图, 纯文本, 盒子, 箭头, 终端
