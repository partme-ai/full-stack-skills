# COLA 项目规模示例：微服务复杂的单体项目

> 适用场景：微服务架构，网关/核心服务内部采用 COLA 单体结构，基础设施复杂（认证、限流、加密、路由），基于 ddd4j-gateway 真实结构。

## 参考项目

本示例基于真实项目 `ddd4j-gateway`（`io.ddd4j:ddd4j-gateway`）的结构提取。

## 项目目录树

```
ddd4j-gateway/                                     # API 网关微服务 — 单体 COLA 结构
├── pom.xml                                        # 继承 ddd4j-boot-parent
│                                                  # 依赖：spring-boot, spring-cloud-gateway,
│                                                  #       sa-token, redisson, fastjson2,
│                                                  #       guava, hutool, kaptcha, commons-lang3
├── src/
│   ├── main/java/io/ddd4j/gateway/
│   │   │
│   │   ├── start/                                 # 启动 + 装配
│   │   │   ├── GatewayApplication.java            # @EnableCola 启动类
│   │   │   └── assembler/
│   │   │       └── GatewayAssembler.java          # 启动时的组件装配
│   │   │
│   │   ├── adapter/                               # 适配层 (6 个 Java 文件)
│   │   │   ├── web/
│   │   │   │   ├── route/
│   │   │   │   │   └── GatewayRouteController.java   # 路由管理 REST 接口
│   │   │   │   └── dto/
│   │   │   │       ├── request/
│   │   │   │       │   ├── RouteSaveRequest.java
│   │   │   │       │   └── CryptoKeyRequest.java
│   │   │   │       └── response/
│   │   │   │           ├── RouteResponse.java
│   │   │   │           └── CryptoKeyResponse.java
│   │   │   └── advice/
│   │   │       └── GlobalExceptionHandler.java    # 统一异常处理
│   │   │
│   │   ├── app/                                   # 应用层 (11 个 Java 文件)
│   │   │   ├── executor/
│   │   │   │   ├── command/                       # 命令执行器
│   │   │   │   │   ├── crypto/
│   │   │   │   │   │   ├── GenerateKeyCmdExe.java      # 生成密钥
│   │   │   │   │   │   └── RotateKeyCmdExe.java        # 密钥轮转
│   │   │   │   │   └── route/
│   │   │   │   │       ├── SaveRouteCmdExe.java        # 保存路由配置
│   │   │   │   │       └── RefreshRouteCmdExe.java     # 刷新路由缓存
│   │   │   │   └── query/                        # 查询执行器
│   │   │   │       ├── crypto/
│   │   │   │       │   └── QueryKeyQryExe.java
│   │   │   │       └── route/
│   │   │   │           └── QueryRouteQryExe.java
│   │   │   ├── model/                            # 命令/查询/DTO 对象
│   │   │   │   ├── command/
│   │   │   │   │   ├── GenerateKeyCmd.java
│   │   │   │   │   ├── SaveRouteCmd.java
│   │   │   │   │   └── RefreshRouteCmd.java
│   │   │   │   └── query/
│   │   │   │       ├── QueryKeyQry.java
│   │   │   │       └── QueryRouteQry.java
│   │   │   ├── handler/                          # 处理器
│   │   │   │   └── GatewayRouteHandler.java
│   │   │   ├── extension/                        # COLA 扩展点
│   │   │   │   └── RateLimitExtension.java
│   │   │   └── config/
│   │   │       └── AppConfig.java
│   │   │
│   │   ├── domain/                                # 领域层 ★ (30 个 Java 文件)
│   │   │   ├── repository/                        # 仓储接口
│   │   │   │   ├── RouteRepository.java          # 路由仓储
│   │   │   │   └── CryptoKeyRepository.java      # 密钥仓储
│   │   │   └── util/
│   │   │       ├── RouteValidator.java            # 路由校验逻辑
│   │   │       └── CryptoAlgorithm.java           # 加密算法领域逻辑
│   │   │
│   │   └── infrastructure/                        # 基础设施层 (52 个 Java 文件)
│   │       ├── config/                            # 配置
│   │       │   ├── GatewayConfig.java
│   │       │   ├── RedisConfig.java
│   │       │   └── ThreadPoolConfig.java
│   │       ├── component/                         # 技术组件
│   │       │   ├── crypto/                        # 加密组件
│   │       │   │   ├── CryptoComponent.java       # 加解密主组件
│   │       │   │   ├── cache/
│   │       │   │   │   └── CryptoKeyCache.java    # 密钥缓存
│   │       │   │   └── strategy/
│   │       │   │       ├── AesCryptoStrategy.java
│   │       │   │       └── RsaCryptoStrategy.java
│   │       │   ├── ratelimit/                     # 限流组件
│   │       │   │   ├── RateLimitManager.java
│   │       │   │   └── key/
│   │       │   │       ├── IpRateLimitKeyResolver.java
│   │       │   │       └── UserRateLimitKeyResolver.java
│   │       │   ├── satoken/                       # 认证/鉴权
│   │       │   │   ├── SaTokenConfig.java
│   │       │   │   └── StpInterfaceImpl.java
│   │       │   ├── filter/                        # 网关过滤器 (Spring Cloud Gateway)
│   │       │   │   ├── log/
│   │       │   │   │   └── AccessLogFilter.java
│   │       │   │   ├── global/
│   │       │   │   │   ├── AuthGlobalFilter.java
│   │       │   │   │   └── RateLimitGlobalFilter.java
│   │       │   │   ├── factory/
│   │       │   │   │   └── CryptoGatewayFilterFactory.java
│   │       │   │   └── gateway/
│   │       │   │       └── RouteCacheGatewayFilter.java
│   │       │   └── error/
│   │       │       └── GatewayErrorHandler.java
│   │       ├── constant/                          # 常量
│   │       │   └── redis/
│   │       │       └── RedisKeyConstants.java
│   │       ├── persistence/                       # 持久化
│   │       │   ├── RouteRepositoryImpl.java
│   │       │   └── CryptoKeyRepositoryImpl.java
│   │       └── util/
│   │           ├── IpUtils.java
│   │           └── RouteUtils.java
│   │
│   ├── main/resources/
│   │   ├── application.yml                        # 主配置
│   │   ├── i18n/                                  # 国际化
│   │   │   ├── messages_zh_CN.properties
│   │   │   └── messages_en_US.properties
│   │   └── conf/
│   │       └── logback-spring.xml
│   └── test/java/io/ddd4j/gateway/
│       └── start/
│           └── GatewayApplicationTest.java
```

## 包结构分析

ddd4j-gateway 是典型的"微服务复杂的单体"COLA 项目，具有以下特点：

| 层级 | 文件数 | 复杂度特征 |
|------|:------:|-----------|
| **start** | 2 | 标准启动入口，带 Assembler 组件装配 |
| **adapter** | 6 | REST 接口少，主要是路由管理和密钥管理 |
| **app** | 11 | CQRS 执行器分离，按 crypto/route 子域分组 |
| **domain** | 30 | 领域对象丰富，Repository 接口 + 领域工具类 |
| **infrastructure** | 52 | **最复杂层**：加密/限流/认证/过滤器/持久化等大量技术组件 |

文件分布比例：`infrastructure(52) > domain(30) > app(11) > adapter(6) > start(2)`

## COLA 四层职责分工

| 层 | 职责 | 网关服务特殊性 |
|----|------|--------------|
| **Adapter** | 路由管理 API、密钥管理 API | 网关的 Adapter 提供管理面 REST 接口，数据面由 Spring Cloud Gateway 过滤器处理 |
| **Application** | 路由和密钥的 CRUD 编排、缓存刷新 | 命令执行器内触发路由刷新、密钥轮转等副作用 |
| **Domain** ★ | 路由校验规则、加密算法选择 | 网关的路由合法性校验、加密策略选择体现在领域层 |
| **Infrastructure** | 过滤器链、加密实现（AES/RSA）、限流、认证（Sa-Token）、Redis 缓存 | Gateway 高度依赖过滤器链路，Infrastructure 承载大量技术基础设施 |

## 模块间依赖关系

```
┌─────────┐     ┌──────────┐
│  start   │────→│ adapter  │
└─────────┘     └────┬─────┘
                      │
                      ▼
┌────────────────────────────────────┐
│              app                   │
│  GenerateKeyCmdExe                 │
│  SaveRouteCmdExe                   │
│  RefreshRouteCmdExe                │
│  QueryKeyQryExe / QueryRouteQryExe │
└──────┬─────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────┐
│                  domain ★                     │
│  RouteRepository (接口)                       │
│  CryptoKeyRepository (接口)                   │
│  RouteValidator / CryptoAlgorithm             │
└──────────────────────────────────────────────┘
       ▲
       │
┌──────┴──────────────────────────────────────┐
│              infrastructure                  │
│  RouteRepositoryImpl                         │
│  CryptoKeyRepositoryImpl                     │
│  CryptoComponent (Aes/Rsa)                   │
│  RateLimitManager                            │
│  SaTokenConfig (认证)                         │
│  AuthGlobalFilter / RateLimitGlobalFilter     │
│  CryptoGatewayFilterFactory                  │
└──────────────────────────────────────────────┘
```

## 适用场景

- 网关类微服务（API Gateway / BFF），需要丰富的过滤器链
- 认证授权服务（OAuth2 / Sa-Token）
- 基础设施复杂度高（加密/限流/断路器/日志/链路追踪）
- 业务逻辑相对简单但技术组件非常丰富
- 单模块即可容纳所有功能区（Maven 多模块反而增加模块间协调成本）

## ddd4j-gateway 的技术栈

| 组件 | 用途 | 所在层 |
|------|------|--------|
| Spring Cloud Gateway | API 网关核心 | Infrastructure (filter/) |
| Sa-Token | 认证鉴权 | Infrastructure (component/satoken/) |
| Redisson | 分布式锁 + 缓存 | Infrastructure (component/crypto/cache/) |
| Fastjson2 | JSON 序列化 | 全局（common 依赖） |
| Guava | 本地缓存、集合工具 | Infrastructure (component/) |
| Hutool | 通用工具 | Infrastructure (util/) |
| Kaptcha | 验证码 | Infrastructure (component/) |

## 相比 ddd4j-rednote/ddd4j-pay 的区别

| 特征 | ddd4j-gateway (单体) | ddd4j-rednote/ddd4j-pay (多模块) |
|------|:---------------------:|:---------------------------------:|
| 模块数 | 1 | 5+ (含 BOM + Dependencies) |
| 业务复杂度 | 低（路由管理） | 中-高（业务领域） |
| 基础设施复杂度 | 极高（过滤器、加密、限流） | 中 |
| 适用场景 | 网关/基础设施服务 | 业务服务 |

## 优点

- 对于基础设施密集型微服务，单体结构避免模块间接口抽象开销
- 过滤器、组件、配置集中在同一代码库，调试方便
- 构建和部署简单（单 jar）
- Spring Cloud Gateway 的过滤器链天然适合在 Infrastructure 层实现

## 缺点

- Infrastructure 层文件过多（52/101 = 51%），需要严格 package 划分
- 纯业务逻辑少的服务容易演变为"重量级基础设施+空领域"，违背 DDD 初衷
- 缺少 Maven 编译时依赖约束，需依赖 ArchUnit 运行时校验
