# full-stack-skills 仓库结构与技能目录总览

本文档基于当前仓库内 `skills/` 实际目录和 `.claude-plugin/marketplace.json` 生成，用于作为本仓库的结果型说明文档与目录总览入口。

## 一、当前仓库概况

- `skills/` 下共有 **42** 个技能组目录。
- 仓库内共检出 **421** 个 `SKILL.md` 文件。
- Marketplace 当前配置了 **40** 个插件，合计 **410** 个技能路径。
- 已发布插件组：angular-skills、antd-skills、ascii-skills、avue-skills、build-skills、chart-skills、cocos-skills、database-skills、ddd-skills、design-skills、dev-utils-skills、devops-skills、docker-skills、document-skills、drawio-skills、electron-skills、flutter-skills、go-skills、mobile-native-skills、nodejs-skills、nvm-skills、ocrmypdf-skills、openspec-skills、pencil-skills、python-skills、react-skills、social-skills、speckit-skills、spring-skills、stitch-skills、svelte-skills、t2ui-skills、tauri-skills、teaching-skills、testing-skills、uniapp-skills、utility-skills、uview-skills、vue-skills、vue-ui-skills。
- 文档入口建议优先查看：`README.md`、`docs/skill-group-mapping.md`、`docs/pipeline-stage-to-skills.md`、本文件。

## 二、仓库顶层结构

```text
full-stack-skills/
├── .claude-plugin/           # Claude Marketplace 配置
├── adapters/                 # 多平台适配器与转换工具
├── agents/                   # 代理角色与编排入口
├── bundles/                  # 打包与聚合产物
├── dist/                     # 分发产物
├── docs/                     # 说明文档与映射文档
├── media/                    # 截图与展示素材
├── skills/                   # 技能主目录（按组拆分）
├── spec/                     # 规范与规格说明
├── template/                 # 技能模板
├── tools/                    # 辅助工具脚本
├── AGENTS.md                 # 仓库级 Agent 约束
├── README.md                 # 项目总说明
└── README_EN.md              # 英文说明
```

## 三、技能组与发布状态

| 技能组 | 目录内技能数 | Marketplace 技能数 | 状态 | 说明 |
|---|---:|---:|---|---|
| `angular-skills` | 1 | 1 | 已发布 | — |
| `antd-skills` | 4 | 4 | 已发布 | — |
| `ascii-skills` | 13 | 13 | 已发布 | — |
| `avue-skills` | 3 | 3 | 已发布 | — |
| `build-skills` | 6 | 6 | 已发布 | — |
| `chart-skills` | 2 | 2 | 已发布 | — |
| `cocos-skills` | 1 | 1 | 已发布 | — |
| `database-skills` | 5 | 5 | 已发布 | — |
| `ddd-skills` | 6 | 6 | 已发布 | — |
| `design-skills` | 12 | 12 | 已发布 | — |
| `dev-utils-skills` | 12 | 12 | 已发布 | `full-stack-doc` 已迁至 `document-skills` |
| `devops-skills` | 6 | 6 | 已发布 | — |
| `docker-skills` | 2 | 2 | 已发布 | — |
| `document-skills` | 6 | 10 | 已发布 | 含 `full-stack-doc`；仍缺目录：docx、pptx、pdf、xlsx |
| `drawio-skills` | 2 | 2 | 已发布 | — |
| `electron-skills` | 3 | 3 | 已发布 | — |
| `flutter-skills` | 2 | 2 | 已发布 | — |
| `go-skills` | 2 | 2 | 已发布 | — |
| `mobile-native-skills` | 2 | 2 | 已发布 | — |
| `nodejs-skills` | 4 | 4 | 已发布 | — |
| `nvm-skills` | 15 | 15 | 已发布 | — |
| `ocrmypdf-skills` | 5 | 5 | 已发布 | — |
| `openspec-skills` | 15 | 15 | 已发布 | — |
| `pencil-skills` | 28 | 28 | 已发布 | — |
| `python-skills` | 3 | 3 | 已发布 | — |
| `react-skills` | 6 | 6 | 已发布 | — |
| `social-skills` | 2 | 2 | 已发布 | — |
| `speckit-skills` | 13 | 13 | 已发布 | — |
| `spring-skills` | 7 | 7 | 已发布 | — |
| `stitch-skills` | 28 | 28 | 已发布 | — |
| `svelte-skills` | 1 | 1 | 已发布 | — |
| `t2ui-skills` | 97 | 97 | 已发布 | — |
| `tauri-skills` | 52 | 51 | 已发布 | 未纳入 marketplace：tauri-app-updater |
| `teaching-skills` | 3 | 3 | 已发布 | — |
| `testing-skills` | 9 | 9 | 已发布 | — |
| `threejs-skills` | 18 | 0 | 仓库内未发布 | — |
| `uniapp-skills` | 13 | 13 | 已发布 | — |
| `utility-skills` | 3 | 3 | 已发布 | — |
| `uview-skills` | 2 | 2 | 已发布 | — |
| `vscode-skills` | 4 | 0 | 仓库内未发布 | — |
| `vue-skills` | 7 | 7 | 已发布 | — |
| `vue-ui-skills` | 4 | 4 | 已发布 | — |


## 四、未进入 Marketplace 的仓库内技能组

- `threejs-skills`：18 个技能，当前在仓库中可见，但尚未进入 `.claude-plugin/marketplace.json`。
- `vscode-skills`：4 个技能，当前在仓库中可见，但尚未进入 `.claude-plugin/marketplace.json`。

## 五、当前一致性说明

- Marketplace 当前声明 410 个技能路径，其中 406 个可在仓库中直接解析。
- `document-skills` 当前存在未落地目录引用：`docx`、`pptx`、`pdf`、`xlsx`。
- `tauri-skills` 目录下已有技能尚未纳入 Marketplace：`tauri-app-updater`。

## 六、阅读建议

- 如果你要按**技能分组**理解仓库，先看 `docs/skill-group-mapping.md`。
- 如果你要按**需求到交付流程**理解仓库，先看 `docs/pipeline-stage-to-skills.md`。
- 如果你要按**Marketplace 发布面**理解仓库，直接以 `.claude-plugin/marketplace.json` 与本文件的“技能组与发布状态”表为准。
- 如果你要做技能补充或重组，优先以 `skills/<group>/<skill>/SKILL.md` 的真实目录结构为准，而不是旧文档中的历史描述。
