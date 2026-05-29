# COLA v5 架构 — 完整目录结构参考


## 菱形架构四模块

```
project-root/
├── start/                          # 启动模块
│   ├── Application.java           # @SpringBootApplication + @EnableCola
│   └── config/                     # WebConfig, MyBatisConfig, ColaConfig
│
├── adapter/                        # 适配器层
│   ├── web/
│   │   ├── controller/            # REST 控制器
│   │   ├── dto/                   # request/, response/
│   │   │   └── converter/         # Web DTO 转换器
│   │   └── advice/                # GlobalExceptionHandler
│   ├── rpc/                       # RPC 适配器（provider/consumer/facade）
│   ├── job/                       # 定时任务
│   └── message/                   # 消息适配器（consumer/producer）
│
├── app/                            # 应用层
│   ├── executor/                   # 执行器（CQRS 强化）
│   │   ├── command/               # CustomerCreateCmdExe, OrderPayCmdExe
│   │   ├── query/                 # CustomerGetQryExe, OrderListQryExe
│   │   ├── event/                 # 事件执行器
│   │   └── extension/             # 扩展执行器
│   ├── model/
│   │   ├── command/               # 命令对象
│   │   ├── query/                 # 查询对象
│   │   ├── event/                 # 应用事件
│   │   └── dto/                   # 应用层 DTO
│   ├── service/                   # 应用服务（编排）
│   ├── eventhandler/              # 事件处理器
│   └── extension/                  # 扩展点（v5 核心特性）
│
├── domain/                         # 领域层（核心，零依赖）
│   ├── {aggregate}/               # 按聚合分包
│   │   ├── entity/                # 聚合根 + 实体
│   │   ├── valueobject/           # 值对象
│   │   ├── event/                 # 领域事件
│   │   ├── service/               # 领域服务
│   │   └── repository/            # 仓储接口（只定义）
│   └── gateway/                   # 防腐层接口
│
└── infrastructure/                 # 基础设施层
    ├── repository/                # 仓储实现
    ├── gateway/                   # 防腐层实现
    ├── converter/                 # PO ↔ DO 转换
    ├── event/                     # 事件发布实现
    └── config/                    # 基础设施配置
```

## COLA v5 核心约束

1. Domain 零依赖
2. App 层不能有业务 if/else
3. Adapter 层不能有 SQL/业务判断
4. 模块间不可循环依赖

## 源代码

