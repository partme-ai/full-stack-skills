# Agent Skills 规范符合性

遵循 [Agent Skills 规范](https://agentskills.io/specification) 与 [Claude 自定义 Skills 指南](https://support.claude.com/zh-CN/articles/12512198-如何创建自定义-skills)。

## 规范摘要

### 目录结构

每个技能是一个目录，至少包含 `SKILL.md`；可选目录：

- **examples/**：用法示例（按场景分文件，便于按需加载）
- **references/**：补充文档（REFERENCE.md、contract.md、official.md 等）
- **scripts/**：可执行脚本（如 pencil-skill-creator 的 init 脚本）
- **assets/**：静态资源（模板、图片、数据文件）

```
skill-name/
├── SKILL.md          # 必需：元数据 + 说明
├── LICENSE.txt       # 可选
├── examples/         # 可选：示例
├── references/       # 可选：参考文档
├── scripts/          # 可选：脚本
└── assets/           # 可选：资源
```

### SKILL.md 格式

**前置元数据（YAML frontmatter）**

| 字段 | 必需 | 约束 |
|------|------|------|
| `name` | 是 | 1–64 字符；小写字母、数字、连字符；与目录名一致；不以连字符开头/结尾；无连续连字符 |
| `description` | 是 | 1–1024 字符；说明技能做什么、何时使用；含关键词便于发现 |
| `license` | 否 | 许可证名称或指向 LICENSE.txt |

**正文（Markdown）**

- 无格式强制要求；建议包含：**When to use**、**How to use**、步骤或参数、**Best practices**、**Keywords**（中英文）。
- 正文建议控制在约 500 行内；长内容放入 `references/` 或 `examples/`，在 SKILL.md 中通过相对路径引用。

### 渐进式披露

1. **发现**：启动时仅加载各技能的 `name` 与 `description`。
2. **激活**：任务匹配时加载完整 `SKILL.md`。
3. **执行**：按需加载 `references/`、`examples/` 中的文件或执行 `scripts/`。

### Pencil Skills 约定

- **MCP 技能命名**：`pencil-mcp-{MCP 方法名}`，方法名下划线改为连字符（如 `open_document` → `pencil-mcp-open-document`）。
- **设计系统技能命名**：`pencil-ui-design-system-{框架名}`（如 `pencil-ui-design-system-uviewpro`）。
- **引用文档**：MCP 技能在 SKILL.md 中引用 [docs/pencil-mcp-tools.md](../docs/pencil-mcp-tools.md) 获取完整参数说明。

## 参考链接

- [Agent Skills – What are skills?](https://agentskills.io/what-are-skills)
- [Agent Skills – Specification](https://agentskills.io/specification)
- [Claude – 如何创建自定义 Skills](https://support.claude.com/zh-CN/articles/12512198-如何创建自定义-skills)
