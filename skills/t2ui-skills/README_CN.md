<div align="center">

# TUI Skills（Alpha）

**面向产品设计的 ASCII / 文本 UI（TUI）组件技能集合**

![Version](https://img.shields.io/badge/Version-0.0.2-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-green)

</div>

## 简介

**TUI Skills** 用于生成可读、像素精确的 ASCII/文本界面，适合 CLI/SSH/日志等无图形环境下展示与沟通设计方案。

每个技能都会输出四个必选块：
- `TUI_RENDER`：纯等宽字体渲染结果
- `COMPONENT_SPEC`：组件 bbox、布局、样式、状态、热键
- `PENCIL_SPEC`：结构化规格（包含画布与网格信息）
- `PENCIL_BATCH_DESIGN`：可执行的 `batch_design` 计划（每个 CALL 不超过 25 个操作）

## 包含内容

- `./skills/tui-*` 下共 78 个组件技能（对齐整理后的组件清单）

## 安装（技能市场）

将本仓库作为 Skills Marketplace 源添加，并启用 `t2ui-skills` 插件。

![Add marketplace](media/add_marketplace.png)

## 快速上手

### 1）用 `tui-input` 生成一个组件

```json
{
  "widthCols": 70,
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "props": { "label": "Email", "placeholder": "name@example.com", "clearable": true },
  "modelValue": "ada@example.com",
  "state": { "focused": true, "disabled": false, "loading": false, "error": null }
}
```

### 2）可选：在 Pencil 中绘制与验证

如果你的环境里启用了 Pencil MCP：
- 按顺序执行 `PENCIL_BATCH_DESIGN` 的各个 CALL 块
- 用 `snapshot_layout(..., problemsOnly=true)` 与 `get_screenshot(...)` 做验收

## 约定

- 默认网格：`cellWidthPx=8`、`cellHeightPx=16`
- 默认移动端画布：`390x844`
- 默认渲染宽度：`widthCols=70`

## License

Apache-2.0
