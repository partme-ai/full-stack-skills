# 技能生态与主文档入口

本仓库（**full-stack-skills**）为全链路**阶段→技能**映射与**基础技能**的主入口。权威映射表见 [pipeline-stage-to-skills.md](pipeline-stage-to-skills.md)。

**说明**：tui/t2ui 类技能（需求转译、ASCII 界面、Pencil 设计语言等）以 **t2ui-skills** 为准，本仓库不再保留 `skills/tui-skills`。Pencil MCP 使用与 .pen 编辑以 **pencil-skills** 为准，本仓库不再保留 `skills/pencil`。

---

## 定位：本仓库 vs 外部技能库

| 维度 | **full-stack-skills**（本仓库） | **外部技能库**（第三方 GitHub） |
|------|--------------------------------|----------------------------------|
| **目标** | 按 `skills/` 分组的全栈基础技能（语言/框架/云/测试/DevOps/文档等） | 官方示例、单栈深度、ML、设计系统、产品流程、个人精选 |
| **安装** | `/plugin marketplace add partme-ai/full-stack-skills` 后按组安装插件 | 各仓库独立 marketplace 或 `npx skills add owner/repo` |
| **组合方式** | 与 PartMe 关联仓（t2ui / stitch / pencil / tauri）+ 外部库**并行注册**，不互斥 | 按需增删；详见 [external-skills.md](external-skills.md) |

**推荐阅读**：[external-skills.md](external-skills.md)（外部库全表与安装命令）、[integration-plan.md](integration-plan.md)（可整合候选评估）。

---

## 关联技能仓库（PartMe 生态）

| 仓库 | 职责 | 阶段/用途 |
|------|------|-----------|
| [t2ui-skills](https://github.com/partme-ai/t2ui-skills) | 需求转译：PRD → ASCII 界面、Stitch 设计语言、Pencil 设计语言 | 设计阶段 |
| [stitch-skills](https://github.com/partme-ai/stitch-skills) | 原型设计：Stitch 设计语言 → Stitch MCP → 原型图 | 设计阶段 |
| [pencil-skills](https://github.com/partme-ai/pencil-skills) | 界面设计：Pencil 设计语言 → Pencil MCP → 产品图（.pen） | 设计阶段 |
| [tauri-skills](https://github.com/partme-ai/tauri-skills) | Tauri 跨平台桌面/移动应用开发 | 开发阶段（桌面/跨平台） |
| **full-stack-skills**（本仓库） | 基础技能（文档/架构/测试/部署、nvm 等）、speckit / openspec / stitch 扩展组等、阶段映射 | 全阶段 |

各仓库的 README/AGENTS 应指向本文档或 [pipeline-stage-to-skills.md](pipeline-stage-to-skills.md)。

---

## 外部技能库发现（聚合）

持续发现新技能库可使用：[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)、[heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills)、[christophacham/agent-skills-library](https://github.com/christophacham/agent-skills-library)、[agent-skills-hub/agent-skills-hub](https://github.com/agent-skills-hub/agent-skills-hub)、[ZhanlinCui/Agent-Skills-Hunter](https://github.com/ZhanlinCui/Agent-Skills-Hunter)。更多说明见 [external-skills.md](external-skills.md) 第 7 节。

---

## 本仓库内未入 marketplace 的技能组

- **threejs-skills**（18 个）：three.js 文档/导航型技能族，见 [skills/threejs-skills/README.md](../skills/threejs-skills/README.md)；与 [skill-group-mapping.md](skill-group-mapping.md) 表中说明一致。
- **vscode-skills**（4 个）：VS Code 扩展相关；同上待接入 marketplace。
- 另 **`skills/tauri-skills/tauri-app-updater`** 目录存在 `SKILL.md` 但未列入 `tauri-skills` 插件 `skills[]` 时，亦属「磁盘有、登记缺」。

## nvm 相关技能（本仓库内）

**Node 版本管理**等基础开发环境技能在 **full-stack-skills** 的 **`skills/nvm-skills/`** 组内（marketplace 插件 **nvm-skills**），例如：

- nvm、nvm-install、nvm-setup、nvm-verify、nvm-usage-basics、nvm-defaults-and-nvmrc、nvm-global-packages、nvm-mirror-and-auth、nvm-shell-integration、nvm-docker-ci、nvm-uninstall、nvm-misc、nvm-project-meta、nvm-troubleshooting-macos、nvm-troubleshooting-linux

独立 [nvm-skills](https://github.com/partme-ai/nvm-skills) 仓库仍可单独使用；本仓库内为同内容的分组副本之一。Tauri 说明见 [tauri-skills.md](tauri-skills.md)。
