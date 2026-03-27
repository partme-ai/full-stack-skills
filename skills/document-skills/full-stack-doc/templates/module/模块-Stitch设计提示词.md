# {Name}-{模块简称}-Stitch设计提示词（{V}）

> **标准说明**：以下为 Octo **实例中心** Stitch 提示词全文（`partme-docs/…/OctoPanel-实例中心-Stitch设计提示词.md`），将「实例中心」替换为目标模块即可。

---

## 原文标题：{Name} — 实例中心 Stitch 设计提示词

> **文档说明**：为 [{Name}-V1界面重构与研发任务清单](../../31、{Name}-V1%E7%95%8C%E9%9D%A2%E9%87%8D%E6%9E%84%E4%B8%8E%E7%A0%94%E5%8F%91%E4%BB%BB%E5%8A%A1%E6%B8%85%E5%8D%95.md) 中的“实例中心”模块提供 Stitch 设计提示词。该模块负责管理所有已纳管的智能体引擎实例（OpenClaw / ZeroClaw / OctoClaw）。

---

## 1. 文档信息

| 属性 | 内容 |
| :--- | :--- |
| 文档版本 | V1.0.0 |
| 创建日期 | 2026-03-24 |
| 设计规范 | [{Name}-视觉与交互DNA规范](../../9、{Name}-视觉与交互DNA规范.md) |

---

## 2. 设计系统摘要

- **实例状态颜色**：
  - 在线 (Online)：绿色 `#07C160`
  - 异常 (Degraded)：橙色 `#FFAA00`
  - 离线 (Offline)：红色 `#DC2626`
  - 维护中 (Upgrading)：蓝色 `#2563EB`
- **布局**：概览卡片（Summary Cards）+ 实例列表（Table）+ 实例详情（Details）
- **字体**：微软雅黑 (Microsoft YaHei)

---

## 3. 实例中心 — Stitch 提示词

### 3.1 提示词：实例列表页面

```
REQUIRED: Font Microsoft YaHei. All UI copy in Chinese.

Design an "实例中心" (Instance Center) page for {Name}.

Header:
- Title: "实例管理" (20px bold)
- Stats Row: [总实例: 12] [● 在线: 10] [● 异常: 1] [● 离线: 1]
- Buttons: [+ 部署新实例] red button #E63946, [刷新] icon.

Filter Bar:
- Engine Filter: "全部引擎", "OpenClaw", "ZeroClaw", "OctoClaw".
- Group Filter: "全部生产", "测试环境", "边缘节点".
- Search: "搜索实例名称/ID..."

Data Table:
1. 实例名称 (Icon per engine + Name + ID)
2. 引擎类型 (Badge: OpenClaw / ZeroClaw / OctoClaw)
3. 所在节点 (Host name link)
4. 健康状态 (Pill: ● 在线 Green / ● 离线 Red)
5. 运行时间 (e.g. 12d 4h)
6. 操作: [控制台] [日志] [设置] [重启/停止] (Dropdown).

Style: High density data view, clear engine distinction, hover effects on rows.
```

### 3.2 提示词：实例详情页面

```
REQUIRED: Font Microsoft YaHei. All UI copy in Chinese.

Design the "实例详情" (Instance Detail) page for {Name}.

Header:
- Breadcrumb: "实例管理 > claw-instance-01"
- Header Actions: [重启] [停止] [删除] red text.

Layout:
- Left Column (70%):
  - Card 1: 运行时概览 (CPU/RAM usage charts, Process ID, Port).
  - Card 2: 最新配置 (Read-only YAML/JSON view).
  - Card 3: 关联扩展 (List of skills/tools active for this instance).
- Right Column (30%):
  - Health History: Small timeline of status changes.
  - Recent Events: Audit logs specific to this instance.
  - Quick Info: Node location, IP address, version.

Style: Dashboard-in-dashboard, use small charts for real-time metrics, clear section titles.
```

---

**文档版本**：V1.0.0  
**最后更新**：2026-03-24  
**文档状态**：✅ 已完成
