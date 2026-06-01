# 架构决策日志（ADL）格式

> 架构决策日志（Architecture Decision Log, ADL）是 ADR 的索引和管理系统。
> 本文档提供 ADL 的创建、维护和自动化方案。

---

## 1. ADL 索引表

```markdown
# 架构决策日志（ADL）

> 最后更新: {YYYY-MM-DD} | 总 ADR 数: {N}

## 活跃决策

| ADR# | 标题 | 状态 | 采纳日期 | 负责人 | 标签 |
|------|------|:----:|:--------:|:------:|:----:|
| 001 | 选择 COLA v5 架构 | ✅ 已采纳 | 2024-03-15 | @张三 | 架构选型 |
| 002 | CQRS L1 策略 | ✅ 已采纳 | 2024-03-20 | @李四 | CQRS |
| 003 | 事件中间件选型 | ✅ 已采纳 | 2024-03-25 | @王五 | 技术选型 |
| 004 | MySQL 选择 | ❌ 已废弃 | 2024-02-01 | @张三 | DB选型 |
| 005 | 单体 vs 微服务 | ✅ 已采纳 | 2024-04-01 | @赵六 | 架构 |

## 已废弃/已替代

| ADR# | 标题 | 被替代 | 替代者为 |
|------|------|:------:|:--------:|
| 004 | MySQL 选择 | ADR-006 | PostgreSQL 选型 |
```

## 2. ADR 目录结构

```
docs/
└── adrs/
    ├── README.md                 # ADL 索引（自动生成）
    ├── ADR-001-choose-cola.md
    ├── ADR-002-cqrs-l1-strategy.md
    ├── ADR-003-event-middleware.md
    ├── ADR-004-deprecated-mysql.md
    └── ADR-005-monolith-vs-microservices.md
```

### 文件命名规范
- 格式: `ADR-{NNN}-{kebab-case-title}.md`
- NNN: 从 001 开始的三位编号
- 标题: 英文 kebab-case，简短描述

## 3. ADL 自动化维护

### GitHub Actions 示例

```yaml
name: Update ADL Index
on:
  push:
    paths:
      - 'docs/adrs/**'

jobs:
  update-adl:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Generate ADL Index
        run: |
          echo "# 架构决策日志" > docs/adrs/README.md
          echo "" >> docs/adrs/README.md
          echo "| ADR# | 标题 | 状态 | 日期 |" >> docs/adrs/README.md
          echo "|------|------|:----:|:----:|" >> docs/adrs/README.md
          for f in docs/adrs/ADR-*.md; do
            title=$(head -1 "$f" | sed 's/# ADR-...: //')
            status=$(grep -A1 "^## 状态" "$f" | tail -1)
            num=$(echo "$f" | grep -oP 'ADR-\K\d+')
            echo "| $num | $title | $status | - |" >> docs/adrs/README.md
          done
          mv docs/adrs/README.md docs/adrs/README.md
      - name: Commit changes
        uses: stefanzweifel/git-auto-commit-action@v4
```

## 4. ADL 最佳实践

| 实践 | 说明 |
|------|------|
| **编号唯一** | ADR 编号全局唯一，废弃后不重用 |
| **索引自动化** | CI/CD 自动生成 ADL 索引 |
| **标签分类** | 为 ADR 打标签（架构选型/DB选型/安全决策） |
| **定期审查** | 每季度审查 ADL，标记过时的决策 |
| **PR 关联** | 代码 PR 关联相关 ADR |

## 5. ADL 状态机

```
                → Accepted（已采纳）
Proposed ──────┤                    Deprecated（已废弃）
    ↓          → Rejected（已拒绝）       ↓
修改后重新提交                              Superseded（已替代）
                                            ↓
                                       保留引用
```
