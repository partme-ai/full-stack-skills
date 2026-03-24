---
name: cli-ascii-logo
description: 生成 CLI 的 ASCII 艺术 Logo/Banner（支持 box drawing 边框、█ 块字符、ANSI 24-bit 渐变色）并提供可运行脚本与集成代码。适用于“做一个像 Spec Kit CLI 的终端 Logo / 彩色 ASCII banner / figlet 风格标题 / CLI 启动欢迎页”等需求。
---

# CLI ASCII Logo

## 目标

- 生成可直接在终端输出的 ASCII 艺术 Logo（含边框与渐变色）
- 输出“可复制粘贴”的结果（纯文本/带 ANSI 颜色），并提供在 CLI 启动时展示的集成方式
- 提供可运行的生成脚本：`scripts/generate_logo.py`

## 工作流

1. 明确输入
   - 名称：如 `auto-cli`
   - 副标题：如 `Command Line Interface`
   - 终端宽度：默认 80（可根据项目/CI 输出调整）
   - 风格：粗块（`█`）/ 细线条（`#`/`*`）/ 无颜色
   - 边框：`╔═╗║ ║╚═╝` 或纯文本
   - 配色：青 → 紫（Spec Kit 风格）、青 → 蓝、橙 → 粉等

2. 生成结果
   - 直接运行脚本生成（最可靠）：见下方“快速开始”
   - 或按需在目标语言里生成（Node/Python/Go），核心是：
     - 先得到“等宽字符画”（多行字符串）
     - 再做边框拼接
     - 再做逐字符渐变（输出 ANSI TrueColor 序列）

3. 集成到 CLI
   - 运行入口（`main`/`bin`/`__main__`）启动时输出一次
   - 支持禁用颜色：
     - 尊重 `NO_COLOR=1`
     - 提供 `--no-color` 参数
     - CI 环境默认关闭（可按需打开）

## 快速开始（脚本）

在支持 TrueColor 的终端（macOS Terminal / iTerm2 / VS Code 终端）效果最佳。

```bash
python3 scripts/generate_logo.py --text auto-cli --subtitle "Command Line Interface"
```

常用参数：

```bash
python3 scripts/generate_logo.py \
  --text auto-cli \
  --subtitle "Command Line Interface" \
  --width 46 \
  --palette spec-kit \
  --frame box
```

## 交付格式

- 纯文本（无颜色）：适合 README / 日志 / 不支持 ANSI 的环境
- ANSI 颜色文本：适合 CLI 启动页（建议提供 `--no-color` 切换）
- 建议同时提供：
  - `banner.txt`（无颜色）
  - `banner.ansi.txt`（带颜色）
  - `renderBanner()`（在你的 CLI 里按环境输出）

## 参考

- 配色与兼容性建议见 [palettes.md](references/palettes.md)
