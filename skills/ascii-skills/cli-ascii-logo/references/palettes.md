# 配色与兼容性

## 内置配色（`--palette`）

- `spec-kit`：青 → 紫（推荐，用于 Spec Kit 风格）
- `cyan-purple`：青 → 紫（更偏紫）
- `cyan-blue`：青 → 蓝
- `orange-pink`：橙 → 粉
- `green-cyan`：绿 → 青
- `mono`：单色白（也可用于调试）

## 颜色开关建议

- 通过 `--no-color` 显式关闭颜色
- 尊重 `NO_COLOR=1`（脚本默认遵守）
- 在 CI / 日志场景建议默认关闭，必要时用 `--force-color` 打开

## 终端兼容性

- ANSI TrueColor（24-bit）在 macOS Terminal、iTerm2、VS Code 终端中通常可用
- 如果用户终端只支持 256 色，TrueColor 也可能“看起来还行”，但渐变会变粗糙

