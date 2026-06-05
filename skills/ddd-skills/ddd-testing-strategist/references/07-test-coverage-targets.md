# Test Coverage Targets

## 分层覆盖率目标

| 层 | 覆盖率目标 | 关键覆盖点 | 工具建议 |
|----|:--------:|-----------|---------|
| Value Object | ≥ 95% | 构造验证、运算逻辑、等值比较、不变式 | JaCoCo / Istanbul |
| Aggregate Root | ≥ 95% | 状态转移（每个路径）、不变量、领域事件 | JaCoCo / Istanbul |
| Domain Service | ≥ 90% | 跨实体编排、外部数据获取 + 计算 | JaCoCo / Istanbul |
| Application | ≥ 80% | Use Case 完整路径 + 异常路径 | JaCoCo / Istanbul |
| Repository | ≥ 80% | 保存 + 加载聚合完整性、N+1 查询 | JaCoCo / Istanbul |
| Adapter (API) | ≥ 70% | 协议转换、参数校验、错误映射 | JaCoCo / Istanbul |
| E2E | 关键路径 | 核心用户旅程（3-5 个） | Cucumber / Cypress |

## 代码行 vs 分支覆盖率

```java
// 代码行覆盖率 100%，但分支覆盖率 50%
public void pay(Order order) {
    if (order.canBePaid()) {   // 分支 1: true
        order.setStatus(PAID); // 只测了 true 分支
    }
    // 分支 2: false — 没测试
}
```

**建议**：优先追踪**分支覆盖率（Branch Coverage）**，Domain 层的分支覆盖率目标 ≥ 90%。

## 测试优先级矩阵

| 优先级 | 覆盖内容 | 比例 |
|--------|---------|:---:|
| **P0 — 必须覆盖** | 聚合根状态转移、领域事件、不变量（invariant） | 60% |
| **P1 — 建议覆盖** | 领域服务编排、Value Object 运算、仓储加载 | 25% |
| **P2 — 按需覆盖** | Application Service 路径、API 错误映射 | 10% |
| **P3 — 可选覆盖** | 异常消息格式、日志输出 | 5% |

## 覆盖率检查配置

### JaCoCo (Java)

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <configuration>
        <excludes>
            <exclude>**/dto/**</exclude>
            <exclude>**/config/**</exclude>
        </excludes>
        <rules>
            <rule>
                <element>PACKAGE</element>
                <limits>
                    <limit>
                        <counter>BRANCH</counter>
                        <value>COVEREDRATIO</value>
                        <minimum>0.80</minimum>
                    </limit>
                </limits>
            </rule>
        </rules>
    </configuration>
</plugin>
```

### Istanbul (TypeScript/JavaScript)

```json
{
  "nyc": {
    "branches": 80,
    "lines": 85,
    "functions": 85,
    "exclude": ["**/*.dto.ts", "**/config/**"]
  }
}
```
