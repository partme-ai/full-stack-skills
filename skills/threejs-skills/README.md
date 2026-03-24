# threejs-skills

基于 [three.js 官方文档](https://threejs.org/docs/)（Core / Addons / TSL / Global）与 [Manual](https://threejs.org/manual/) 的 Agent Skills 族。结构与**叙述深度**对齐本仓库 [document-skills/mermaid/SKILL.md](../document-skills/mermaid/SKILL.md)：长 `description`、分层触发词、**与兄弟技能的分流规则**、分步骤工作流、`examples/` 与 `references/` 渐进式披露；每个 `SKILL.md` 另含 **Documentation and version**、**Agent response checklist** 及 **中英 Keywords**（与 mermaid 的英文/中文关键词风格一致）。元数据与目录约定见 [agent-skills-spec.md](../../spec/agent-skills-spec.md)。

## 深度标准（与 mermaid 对齐）

| 要素 | 要求 |
|------|------|
| YAML `description` | 多句英文，含关键 API 族名、触发场景、与相邻技能一句区分；**≤1024 字符** |
| When to use | `ALWAYS` / `Use when`、中英文触发短语、**IMPORTANT** 分流（如 materials vs node-tsl） |
| How to use | ≥5 步或分场景子步骤；显式指向本目录 `examples/` 中具体文件（若已建） |
| Doc map | 表格：**官方侧栏分组 + ≥3 条** `https://threejs.org/docs/` 链接 |
| Scope | In / Out；Out 指向应使用的 `threejs-*` 技能 id |
| Common pitfalls | 3–5 条易错点（color space、透明排序、mixer.update、WebGPU 路径等按主题选） |
| Documentation and version | 与 [three.js docs](https://threejs.org/docs/) 及用户 lockfile 版本对齐；大版本升级查 release notes |
| Agent response checklist | 与 [document-skills/mermaid/SKILL.md](../document-skills/mermaid/SKILL.md) 的「输出要求」类似：链官方页、分流兄弟技能、dispose、不臆造 API |
| Keywords | **English** + **中文** 两行，便于中英检索 |
| References（分层） | Manual 入口、`docs/` 侧栏分组、`#` 锚点、必要时 [Global](https://threejs.org/docs/#Global) 常量；长表放 `references/` |
| 篇幅 | 单 `SKILL.md` 建议 ≤200–350 行；类名长表放 `references/official-sections.md` |

## 文件约定

```
threejs-<topic>/
├── SKILL.md
├── examples/
│   └── workflow-<scenario>.md   # 步骤 + 片段 + 指向官方示例（不整库粘贴）
└── references/
    ├── official-sections.md       # 按需：docs 类名与链接表（animation/loaders/renderers/audio 等）
    └── ...                        # 如 node-tsl 的 tsl-vs-classic.md、official-links.md
```

## 技能数量：18（合并策略）

| 决策 | 说明 |
|------|------|
| **并入 `threejs-objects`** | `Raycaster`、`Layers`、`EventDispatcher` 与拾取流程在本技能中成章 |
| **并入 `threejs-geometries`** | `Curve` / `Path` / `Shape` / `ExtrudeGeometry`、Addons NURBS 等在 Scope 与 Doc map 中覆盖 |
| **独立 `threejs-webxr`** | 不并入 `threejs-renderers`，便于沉浸式任务发现 |

## 技能索引

| # | 目录名 | 主题 |
|---|--------|------|
| 1 | [threejs-dev-setup](threejs-dev-setup/SKILL.md) | 构建、导入、Manual、TypeScript、`examples/jsm` |
| 2 | [threejs-scenes](threejs-scenes/SKILL.md) | `Scene`、`Fog`、`background` |
| 3 | [threejs-camera](threejs-camera/SKILL.md) | 相机与投影 |
| 4 | [threejs-lights](threejs-lights/SKILL.md) | 光源与阴影 |
| 5 | [threejs-materials](threejs-materials/SKILL.md) | 经典材质（非 Node） |
| 6 | [threejs-node-tsl](threejs-node-tsl/SKILL.md) | Nodes、TSL、`NodeMaterial` |
| 7 | [threejs-textures](threejs-textures/SKILL.md) | 纹理与采样、PMREM |
| 8 | [threejs-geometries](threejs-geometries/SKILL.md) | 几何体、Buffer、曲线/挤出 |
| 9 | [threejs-math](threejs-math/SKILL.md) | 数学类型与空间查询 |
| 10 | [threejs-objects](threejs-objects/SKILL.md) | 场景图、Mesh、**交互拾取** |
| 11 | [threejs-animation](threejs-animation/SKILL.md) | 动画混合与轨道 |
| 12 | [threejs-audio](threejs-audio/SKILL.md) | 空间音频 |
| 13 | [threejs-loaders](threejs-loaders/SKILL.md) | 加载与导出 |
| 14 | [threejs-renderers](threejs-renderers/SKILL.md) | WebGL/WebGPU、RenderTarget |
| 15 | [threejs-postprocessing](threejs-postprocessing/SKILL.md) | EffectComposer 管线 |
| 16 | [threejs-helpers](threejs-helpers/SKILL.md) | 调试辅助体 |
| 17 | [threejs-controls](threejs-controls/SKILL.md) | Orbit / Transform 等控件 |
| 18 | [threejs-webxr](threejs-webxr/SKILL.md) | WebXR |

## 技能互查（分流速览）

| 若用户任务偏向… | 优先技能 | 勿与谁混淆 |
|------------------|----------|------------|
| 着色图节点 / TSL / WebGPU 材质 | `threejs-node-tsl` | `threejs-materials`（仅经典材质） |
| 经典 PBR / ShaderMaterial | `threejs-materials` | `threejs-node-tsl` |
| 屏幕空间后期（composer passes） | `threejs-postprocessing` | `threejs-renderers`（核心渲染器设置） |
| 节点化后期（core PostProcessing） | `threejs-node-tsl` + `threejs-renderers` | 仅 composer 的 addon 文档 |
| HDR / KTX2 / Draco / glTF 进出 | `threejs-loaders` | `threejs-textures`（GPU 纹理对象本身） |
| 纹理参数 / PMREM | `threejs-textures` | `threejs-loaders`（解码器与文件 IO） |
| 雾与背景概念 | `threejs-scenes` | 完整 HDR 工作流需 loaders + textures |
| 射线拾取 / 图层 | `threejs-objects` | `threejs-math`（仅数学对象） |
| VR/AR 会话与手柄 | `threejs-webxr` | `threejs-camera`（非 XR 投影细节） |
| 插值与关键帧轨道 | `threejs-animation` | `threejs-math`（Interpolant 归属动画） |

## 验收标准（与规划一致）

每个 `SKILL.md` 应满足：

- **description**：饱满、≤1024 字符；含关键 API 族名与相邻技能一句区分。
- **When to use**：含至少一处与兄弟技能的分流规则（IMPORTANT 表或段落）。
- **Doc map**：表格含 **≥3 条** 官方链接（`threejs.org/docs/`、`#` 锚点或 Manual 入口均可；`threejs-dev-setup` 可含 npm Manual）。
- **How to use**：**≥5 步** 或分场景子列表；显式指向本目录 `examples/*.md`（若存在）。
- **Scope**：In / Out；Out 中对应能力指向应使用的 `threejs-*` 技能 id。
- **篇幅**：单文件建议 **约 200–350 行**；类名长表放入 `references/official-sections.md` 等。

## 外部规范链接

- [Agent Skills – Specification](https://agentskills.io/specification)
- [Claude – 如何创建自定义 Skills](https://support.claude.com/zh-CN/articles/12512198-如何创建自定义-skills)
- [three.js docs](https://threejs.org/docs/)
- [three.js manual](https://threejs.org/manual/)
