---
name: ascii-table-renderer
description: Render structured data as aligned ASCII tables (column width rules, truncate/wrap, border styles, compact/readable variants) for terminal/log/email.
license: Complete terms in LICENSE.txt
dependencies:
  - python>=3.8
---


## When to use this skill
**CRITICAL TRIGGER RULE**
- Use this skill ONLY when the user explicitly mentions the exact skill name: `ascii-table-renderer`.

**Trigger phrases include:**
- "ascii-table-renderer"
- "use ascii-table-renderer"
- "用 ascii-table-renderer 把列表打印成表格"
- "使用 ascii-table-renderer 生成 ASCII 表格（对齐/列宽）"

## Boundary
- Do not fetch data (DB/API). Only render and format output.
- Default borders are ASCII-only: `+ - |`.
- Out of scope: merged cells, multi-row headers, complex spanning layouts.

## How to use this skill
### Inputs
- headers (required)
- rows (required)
- maxWidth (default 80)
- maxColWidth (default 20)
- borderStyle (light | minimal, default light)
- overflow (ellipsis | wrap, default ellipsis)
- align (left | right | center, default left)

### Outputs (required)
- tableCompact (log-friendly)
- tableReadable (interactive-friendly)
- rules (width/truncation/null/alignment rules)

### Steps
1. Compute per-column widths: `min(maxColWidth, max(contentWidth))`
2. Handle overflow:
   - ellipsis: use `...` consistently
   - wrap: wrap within column width while keeping row alignment
3. Output two variants:
   - compact: minimal or fewer separators
   - readable: clearer borders

## Script
- `scripts/render_table.py`: render tables from JSON stdin (compact/readable)

## Examples
- `examples/basic.md`

## Quality checklist
1. Columns align consistently; each line does not exceed maxWidth
2. Null values are rendered as `-`
3. Copy/paste safe (no trailing spaces)

## Keywords
**English:** ascii-table-renderer, ascii table, align, columns, rows, truncate, wrap, terminal, log
**中文:** ascii-table-renderer, ASCII 表格, 对齐, 列宽, 截断, 换行, 终端, 日志, 工单
