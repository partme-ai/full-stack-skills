# ascii-terminal-animation-pack：动画规格示例（matrix）

## animationSpec（建议）
- theme: matrix
- width: 80
- height: 24
- fps: 10（8-15 更舒适）
- durationSeconds: 3（demo 默认短时）
- loop: false（默认不循环）
- 禁用条件：
  - 非交互终端（stdout 不是 TTY）
  - 输出重定向到文件
  - 用户显式设置 NO_COLOR / --no-ansi（可选语义）

## Refresh strategy（低闪烁）
- 避免频繁全屏清空；尽量使用“光标定位 + 局部重绘”
- 帧间隔 = 1 / fps；不要超过 20fps
