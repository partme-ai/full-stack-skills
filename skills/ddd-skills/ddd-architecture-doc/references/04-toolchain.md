# 架构文档工具链

> 推荐的工具和最佳实践，帮助团队高效维护架构文档。

---

## 1. 图表工具

### Structurizr（推荐）
- **类型**: C4 模型专用工具
- **特点**: 代码定义架构图、版本控制友好、支持多视图
- **适用**: 中大型项目，需要 C4 模型全量维护
- **地址**: [structurizr.com](https://structurizr.com)

```java
// Structurizr DSL 示例
workspace {
    model {
        user = person "顾客" "系统用户"
        softwareSystem = softwareSystem "电商平台" "在线购物系统"
        user -> softwareSystem "下订单"
    }
    views {
        systemContext softwareSystem {
            include *
        }
    }
}
```

### Mermaid（轻量）
- **类型**: Markdown 内嵌图表
- **特点**: 无额外工具、直接写在 Markdown 中
- **适用**: 小型项目，文档与代码同仓库
- **支持**: GitHub / GitLab / 多数 Markdown 编辑器

### PlantUML（开发者友好）
- **类型**: 代码驱动图表
- **特点**: 丰富的图类型（时序、活动、组件、类图）
- **适用**: 需要多种 UML 图型的项目
- **集成**: VS Code 插件、CI/CD 自动渲染

### draw.io / diagrams.net
- **类型**: 可视化拖拽工具
- **特点**: 操作直观、开源、可嵌入 Confluence
- **适用**: 快速原型、非技术团队合作

## 2. ADR 管理工具

### ADR Tools（CLI）
- **特点**: 命令行创建和管理 ADR
- **安装**: `npm install -g adr-tools`
- **用法**:
  ```bash
  adr new "选择 COLA 架构"
  adr list
  adr supersede 4 6  # ADR-4 被 ADR-6 替代
  ```

### Log4brains
- **特点**: ADR Web 界面 + 自动索引
- **安装**: `npm init log4brains`
- **适用**: 团队需要可视化的 ADR 浏览

## 3. 文档平台

| 平台 | 适用场景 | 优势 |
|------|---------|------|
| GitHub Wiki | 开发者团队 | 代码同仓库，PR 驱动文档变更 |
| Confluence | 大型团队 | 富文本编辑，跨团队可见 |
| Notion | 中等团队 | 灵活排版，数据库视图 |
| 语雀 | 国内团队 | 中文友好，知识库管理 |
| MkDocs | 技术团队 | Markdown 驱动，自动部署 |

## 4. 自动化检查

### ArchUnit
- **用途**: Java 层依赖方向自动检查
- **集成**: JUnit 测试 + CI/CD

```java
@Test
void testLayerDependencies() {
    layeredArchitecture()
        .layer("Adapter").definedBy("..adapter..")
        .layer("App").definedBy("..app..")
        .layer("Domain").definedBy("..domain..")
        .layer("Infrastructure").definedBy("..infrastructure..")
        .whereLayer("Adapter").mayOnlyBeAccessedByLayers("App")
        .whereLayer("App").mayOnlyBeAccessedByLayers("Adapter")
        .whereLayer("Domain").mayOnlyBeAccessedByLayers("App", "Infrastructure")
        .check(importedClasses);
}
```

### ADR 合规检查
- ADR 必须与代码一致
- 定期 CI 检查 ADR 索引 vs 实际代码实现
- 架构变更必须有对应的 ADR 更新

## 5. 推荐工作流

```
代码变更 → 影响架构？→ 是 → 更新 ADR / 更新 C4 图 / 更新架构文档
                                  ↓
                               PR 评审包含文档变更
                                  ↓
                              合并后自动部署文档站
```

### 文档与代码同步策略

| 策略 | 适用 | 执行方式 |
|------|------|---------|
| PR 强制关联 | 严格团队 | PR 模板含文档更新确认框 |
| 文档 AI 检测 | 自动化 | CI 检测代码架构变更 → 自动提示更新文档 |
| 定期人工审查 | 宽松团队 | 每 sprint 审查一次架构文档 |
