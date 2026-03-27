# full-stack-doc 模板目录

与 `SKILL.md` 中 **根目录 11 份 + 版本目录 7 份 + 模块 3 份** 对齐；正文已合并原全生命周期 14 阶段模板与 **OctoPanel**（`partme-docs/1、OctoPanel/`）实例结构。

本目录 **直接** 包含四类子目录（复制到产品仓库时按子目录拷贝即可）：

| 子目录 | 说明 |
| :--- | :--- |
| [`root/`](root/) | 产品根目录 11 个 Markdown（含两个 `6、`） |
| [`version/`](version/) | 每个版本目录 7 个 Markdown（占位 `{Name}`、`{V}`） |
| [`module/`](module/) | 单功能模块 PRD / Stitch / UI 三件套 |
| [`delivery/`](delivery/) | 技术细分（原 10）+ 提测 / 测试 / 上线 / 运维（原 11–14；本仓库内文件名为 `1～5`） |

原 `templates/project-standard/` 与 `templates/legacy-lifecycle/` 已废弃：内容已迁入上述四类目录，**不再**嵌套一层 `project-standard`。

## 使用步骤（摘要）

1. 将 `{Name}` 替换为实际产品名；`version/` 下的 `{V}` 同步进文件名（如 `V1`）。
2. 根目录标准文件由 `root/` 中文件重命名为 `1、{Name}-命名与品牌说明.md` 等形式后放到项目根。
3. 版本标准文件放入 `{项目根}/{V}/`；模块三件套放入 `{项目根}/{V}/{序号}、{模块名}/`。
