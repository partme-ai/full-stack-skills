---
name: ascii-terminal-animation-pack
description: Plan and generate terminal ASCII animations/screensaver-style output (FPS, refresh rules, loop policy, low-flicker guidance), with a static poster frame and an optional local demo script.
license: Complete terms in LICENSE.txt
dependencies:
  - python>=3.8
---


## When to use this skill
**CRITICAL TRIGGER RULE**
- Use this skill ONLY when the user explicitly mentions the exact skill name: `ascii-terminal-animation-pack`.

**Trigger phrases include:**
- "ascii-terminal-animation-pack"
- "use ascii-terminal-animation-pack"
- "用 ascii-terminal-animation-pack 做终端动画"
- "使用 ascii-terminal-animation-pack 生成矩阵雨 demo"

## Boundary
- Animations must be explicitly triggered demos. Never default to animated output in normal logs.
- Must provide an ASCII-only static poster frame for README/tickets.
- Must provide disable guidance: skip animations for non-interactive / redirected output.

## How to use this skill
### Inputs
- theme (matrix | waves | custom, default matrix)
- width (default 80)
- height (default 24)
- fps (default 10)
- durationSeconds (default 3)
- loop (default false)
- colorMode (none | ansi256, default ansi256)

### Outputs (required)
- animationSpec (refresh rules, FPS, loop policy, disable conditions)
- staticPosterFrame (ASCII-only)
- safetyNotes (exit/disable guidance, avoid log spam)

## Script
- `scripts/matrix_demo.py`: best-effort matrix rain demo (short-run, TTY-only)

## Examples
- `examples/spec.md`
- `examples/poster.md`

## Quality checklist
1. Non-spam by default: short duration, easy exit, disabled for non-interactive output
2. Static frame is ASCII-only and copy/paste safe
3. Animated output should not mix with normal application logs (recommend separate command or stream)

## Keywords
**English:** ascii-terminal-animation-pack, terminal animation, ascii animation, matrix rain, demo, fps, non-interactive
**中文:** ascii-terminal-animation-pack, 终端动画, ASCII 动效, 矩阵雨, 演示, 帧率, 非交互禁用
