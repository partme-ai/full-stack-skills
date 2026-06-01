# Docker Skills 生态体系设计说明

> 版本：v1.2 | 涵盖 Docker 全生命周期：概念 → Dockerfile → 构建 → run → 编排 → 安全 → 生产 → AI/ML — 共 16 个技能

---

## 一、设计哲学

### 1.1 为什么需要 Docker Skills 生态

现有的 2 个 skill（`docker`、`docker-compose`）内容过于简略，每个仅 ~25 行，缺乏：
- 结构化的知识体系（渐进披露）
- 分场景的深入指导（Dockerfile 最佳实践、多阶段构建、安全加固等）
- 生产级实践（资源限制、健康检查、日志管理、编排迁移）
- Docker 生态新能力（Build Cloud、Scout、Model Runner、Sandboxes）

用户真正想知道的是：

| 用户真正想问的 | 现有状态 | v1.0 改进 |
|--------------|---------|----------|
| "怎么写出好的 Dockerfile？" | 一句带过 | **独立 Skill：`docker-dockerfile`** |
| "多容器应用怎么编排？" | 有 compose，但太简 | 保留 `docker-compose`，重写为 Compose 文件完整参考 |
| "docker build 怎么用？怎么多平台构建？" | 未覆盖 | **新增 `docker-buildx`（构建引擎+多平台+加速）** |
| "docker build 基础怎么用？" | 未覆盖 | **新增 `docker-build`（构建命令+标签+推送）** |
| "镜像怎么瘦身？怎么分层？" | 未覆盖 | **`docker-dockerfile` 深入覆盖** |
| "网络怎么配？容器间怎么通信？" | 未覆盖 | **新增 `docker-networking`** |
| "数据怎么持久化？卷怎么管理？" | 未覆盖 | **新增 `docker-storage`** |
| "镜像安全漏洞怎么扫？" | 未覆盖 | **新增 `docker-security`** |
| "怎么在 CI/CD 中用 Docker？" | 未覆盖 | **新增 `docker-cicd`** |
| "Docker 怎么跑 AI 模型？" | 未覆盖 | **新增 `docker-ai-ml`** |
| "生产环境怎么部署和监控？" | 未覆盖 | **新增 `docker-production`** |
| "Docker 基础概念是什么？" | 未覆盖 | **新增 `docker-basics`（第一入口）** |

### 1.2 v1.1 设计原则

**技能按用户学习和使用路径组织**：

```
用户旅程：Docker是什么 → 写Dockerfile → 构建镜像 → 多平台构建 → 运行容器 → 编排多容器 → 配置网络存储 → 安全加固 → CI/CD → 生产部署 → AI/ML
                    │                                      │
                    ├── basics (第一入口)                    ├── compose (多容器)
                    ├── dockerfile (Dockerfile编写)          ├── networking
                    ├── build (docker build基础)             ├── storage
                    ├── buildx (构建引擎+多平台)              ├── cicd
                    ├── run (容器管理)                       ├── production
                    └── security (安全扫描+加固)             ├── ai-ml
                                                            └── troubleshooting
```

| 原则 | 说明 |
|------|------|
| **渐进学习** | `basics` 是第一入口，从零教 Docker，不假设已有知识 |
| **按需取用** | 每个 skill 可独立使用，不需要走完整链路 |
| **输出可操作** | 每个 skill 输出 Dockerfile、compose 配置、命令行等 |
| **安全内建** | 每个 skill 内置安全最佳实践和 Gotchas |
| **生产导向** | 不只是开发用，也覆盖 CI/CD、生产部署、监控 |

---

## 二、技能全景图

### 2.1 按用户旅程排列（v1.2）

```
第1步：Docker 基础概念
        │
        ▼
  ┌─────────────────────────────────────────────┐
  │  docker-basics                               │
  │  Docker 概念、架构、安装、基础命令             │
  │  "什么是Docker？Container vs VM？"            │
  └────────────────────┬────────────────────────┘
                       │
第2步：写 Dockerfile
        │              ▼
        │   ┌─────────────────────────────────────────┐
        │   │  docker-dockerfile                        │
        │   │  每条指令详解、多语言多阶段模板、层优化      │
        │   │  "怎么写好Dockerfile？怎么优化镜像大小？"    │
        │   └────────────────────┬────────────────────┘
        │                        │
第3步：构建镜像（docker build）   │
        │              ▼         │
        │   ┌─────────────────────────────────────────┐
        │   │  docker-build                             │
        │   │  docker build/tag/push、镜像管理、清理      │
        │   │  "docker build 怎么用？怎么打标签推送？"     │
        │   └────────────────────┬────────────────────┘
        │                        │
第4步：构建引擎与多平台          │
        │              ▼         │
        │   ┌─────────────────────────────────────────┐
        │   │  docker-buildx                            │
        │   │  BuildKit、多平台构建、Build Cloud加速     │
        │   │  "怎么构建arm64/amd64双架构镜像？"         │
        │   └────────────────────┬────────────────────┘
        │                        │
第5步：运行和管理容器             │
        │   ┌────────────────────┼────────────────────┐
        │   ▼                    ▼                    ▼
        │  ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐
        │  │docker-run    │ │docker-network│ │docker-storage    │
        │  │容器生命周期  │ │  ing         │ │                  │
        │  │资源限制      │ │网络模式      │ │Volume/Bind/Tmpfs │
        │  │健康检查      │ │跨容器通信    │ │数据持久化        │
        │  │日志管理      │ │端口映射      │ │备份恢复          │
        │  └──────┬───────┘ └──────┬───────┘ └────────┬─────────┘
        │         │               │                   │
第6步：多容器编排                 │                   │
        │         └───────────────┼───────────────────┘
        │                         ▼
        │  ┌─────────────────────────────────────────────┐
        │  │  docker-compose (现有，大幅增强)              │
        │  │  多服务定义、环境变量、依赖顺序、profiles       │
        │  │  "docker-compose.yml怎么写？"                 │
        │  └────────────────────┬────────────────────────┘
        │                       │
第7步：安全加固                 │
        │  ┌────────────────────┼────────────────────────┐
        │  ▼                    ▼                        ▼
        │  ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐
        │  │docker-securit│ │docker-scout  │ │docker-hub        │
        │  │ y            │ │              │ │                  │
        │  │镜像签名      │ │镜像漏洞扫描   │ │镜像仓库管理       │
        │  │非root运行    │ │SBOM生成      │ │发布拉取          │
        │  │secrets管理   │ │策略评估      │ │私有仓库          │
        │  │Docker Bench  │ │CVE追踪       │ │镜像标签策略       │
        │  └──────┬───────┘ └──────┬───────┘ └────────┬─────────┘
        │         │               │                   │
第8步：CI/CD与生产               │                   │
        │         └───────────────┼───────────────────┘
        │                         ▼
        │  ┌──────────┬──────────┬──────────┬──────────────┐
        │  ▼          ▼          ▼          ▼              │
        │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────────┐ │
        │  │docker- │ │docker- │ │docker- │ │docker-     │ │
        │  │cicd    │ │product │ │trouble │ │testcontain │ │
        │  │        │ │ ion    │ │shooting│ │ers         │ │
        │  │GitHub  │ │        │ │        │ │            │ │
        │  │Actions │ │Swarm   │ │日志排查│ │Java/Python │ │
        │  │Jenkins │ │K8s     │ │资源问题│ │集成测试    │ │
        │  │镜像仓库│ │资源配额│ │网络调试│ │数据库测试  │ │
        │  └────────┘ └────────┘ └────────┘ └────────────┘ │
        │                                                  │
第9步：AI/ML 场景                                          │
        │                                                  │
        └──────────────────────────────────────────────────┘
                               ▼
        ┌──────────────────────────────────────────────────┐
        │  docker-ai-ml                                     │
        │  Model Runner、Agent、Sandboxes、GPU支持           │
        │  "怎么用 Docker 跑本地 LLM？"                      │
        └──────────────────────────────────────────────────┘
```

### 2.2 技能调用路径

| 用户类型 | 推荐路径 |
|----------|---------|
| **Docker 新手** | basics → dockerfile → build → buildx → run → compose |
| **后端开发** | basics → dockerfile → build → run → networking → compose |
| **DevOps/SRE** | basics → dockerfile → build → buildx → run → compose → security → cicd → production |
| **安全工程师** | security → scout → hub |
| **AI/ML 工程师** | basics → dockerfile → build → ai-ml |
| **全栈/架构师** | basics → dockerfile → build → buildx → run → networking → storage → compose → security → cicd → production |
| **Java 开发者** | basics → dockerfile → build → run → testcontainers |
| **镜像安全扫描** | scout (独立使用) + security |
| **CI/CD 流水线** | dockerfile + build + buildx + cicd + security |
| **生产部署** | compose + production + troubleshooting |
| **微服务调试** | run + networking + compose + troubleshooting |
| **跨平台构建** | dockerfile + build + buildx |

---

## 三、目录结构约定

```
skills/
├── docker-skills/
│   ├── README.md                    # 本文件
│   ├── docker-basics/               # Skill 1：Docker 概念与基础
│   ├── docker-dockerfile/           # Skill 2：Dockerfile 完整编写指南
│   ├── docker-build/                # Skill 3：docker build 构建镜像+标签+推送
│   ├── docker-buildx/               # Skill 4：构建引擎+多平台+Build Cloud
│   ├── docker-run/                  # Skill 5：容器运行与管理
│   ├── docker-networking/           # Skill 6：网络配置
│   ├── docker-storage/              # Skill 7：存储与数据持久化
│   ├── docker-compose/              # Skill 8：Compose 文件+多容器编排
│   ├── docker-security/             # Skill 9：安全加固
│   ├── docker-scout/                # Skill 10：镜像漏洞扫描
│   ├── docker-hub/                  # Skill 11：镜像仓库管理
│   ├── docker-cicd/                 # Skill 12：CI/CD 集成
│   ├── docker-production/           # Skill 13：生产部署
│   ├── docker-troubleshooting/      # Skill 14：问题排查
│   ├── docker-testcontainers/       # Skill 15：测试容器
│   └── docker-ai-ml/                # Skill 16：AI/ML 工作负载
```

---

## 四、Skill 详细设计

---

### Skill 1：docker-basics

**定位**：Docker 入门教学 — 生态的第一入口

**触发词**：`Docker 入门`、`什么是 Docker`、`容器概念`、`Docker vs VM`、`Docker 安装`、`docker 基础`、`container basics`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| 什么是 Docker？ | 容器化平台定义 + Container vs VM 对比 |
| 核心概念有哪些？ | Image/Container/Registry/Engine 四大概念 |
| 怎么安装？ | Linux/Mac/Windows 安装指引 |
| Docker 架构？ | Client-Server 架构 + Docker daemon |
| 第一个容器？ | `docker run hello-world` 实操 |

**目录结构**：

```
docker-basics/
├── SKILL.md
├── examples/
│   ├── 01-first-container.md
│   └── 02-image-inspection.md
└── references/
    ├── 01-docker-architecture.md
    ├── 02-container-vs-vm.md
    └── 03-installation-guide.md
```

---

### Skill 2：docker-dockerfile

**定位**：Dockerfile 完整编写指南 — 每条指令详解 + 多语言最佳实践

**触发词**：`Dockerfile`、`Dockerfile 编写`、`Dockerfile 优化`、`Dockerfile 最佳实践`、`多阶段构建`、`镜像瘦身`、`layer 缓存`、`dockerfile怎么写`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| Dockerfile 指令大全？ | FROM/RUN/COPY/ADD/ENV/ARG/EXPOSE/CMD/ENTRYPOINT/WORKDIR/HEALTHCHECK/VOLUME/USER/SHELL 每条指令语法、最佳实践、常见错误 |
| 多阶段构建怎么写？ | Go+Rust / Java / Spring Boot 层优化 / Node.js / Python 五种语言模板 |
| 怎么利用层缓存？ | 先 COPY 依赖再 COPY 源码、RUN 合并、--mount=type=cache |
| .dockerignore 怎么写？ | 按语言分类的 .dockerignore 模板 + dockerignore 优先级规则 |
| 镜像怎么从 1GB 瘦到 50MB？ | 多阶段 + distroless + Alpine + 清理技巧 |

**目录结构**：

```
docker-dockerfile/
├── SKILL.md
├── examples/
│   ├── 01-multi-stage-go.md
│   ├── 02-multi-stage-java.md
│   ├── 03-spring-boot-layers.md
│   ├── 04-multi-stage-node.md
│   └── 05-multi-stage-python.md
└── references/
    ├── 01-dockerfile-instructions.md
    ├── 02-layer-caching.md
    ├── 03-dockerignore.md
    ├── 04-image-size-optimization.md
    └── 05-multi-stage-patterns.md
```

---

### Skill 3：docker-build

**定位**：镜像构建与生命周期管理 — `docker build`/`tag`/`push`/`images` 一站式掌握

**触发词**：`docker build`、`docker build 命令`、`docker tag`、`docker push`、`镜像构建`、`镜像标签`、`docker images`、`docker image`、`构建参数`、`--build-arg`、`镜像清理`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| docker build 怎么用？ | 完整命令语法、所有参数、上下文管理、多 tag 构建 |
| 怎么打标签推送？ | docker tag 命名规范 + docker push 流程 + registry 登录 |
| 怎么管理本地镜像？ | docker images/inspect/history/prune/rmi 全命令 |
| 构建参数怎么传？ | --build-arg 完整用法 + ARG vs ENV + 多环境构建 |
| 镜像怎么导出导入？ | docker save/load 完整流程 + 压缩传输 |
| BuildKit 基础怎么用？ | 启用 BuildKit → 并行构建 → registry 缓存 → 输出模式 |

**目录结构**：

```
docker-build/
├── SKILL.md
├── examples/
│   ├── 01-build-tag-push.md
│   ├── 02-build-args.md
│   └── 03-target-stage.md
└── references/
    ├── 01-build-command-reference.md
    ├── 02-tag-strategy.md
    └── 03-buildkit-basics.md
```

---

### Skill 4：docker-buildx

**定位**：构建引擎+多平台构建+Build Cloud 加速

**触发词**：`docker buildx`、`多平台构建`、`多架构`、`arm64 构建`、`BuildKit`、`Build Cloud`、`构建加速`、`跨平台编译`、`linux/amd64`、`linux/arm64`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| buildx 怎么用？ | docker buildx create/use/build 完整流程 |
| 怎么构建多平台镜像？ | --platform linux/amd64,linux/arm64 + QEMU/binfmt |
| BuildKit 有哪些高级特性？ | --mount=type=secret/cache/ssh、内联缓存、并行构建 |
| 怎么加速 CI 构建？ | Docker Build Cloud + registry cache + GHA cache |
| GitHub Actions 多平台构建？ | docker/build-push-action + docker/setup-buildx-action 实战 |

**目录结构**：

```
docker-buildx/
├── SKILL.md
├── examples/
│   ├── 01-multi-platform-build.md
│   ├── 02-buildkit-secrets.md
│   ├── 03-buildkit-cache-mount.md
│   ├── 04-buildkit-ssh-forward.md
│   └── 05-github-actions-multi-platform.md
└── references/
    ├── 01-buildx-architecture.md
    ├── 02-buildkit-drivers.md
    ├── 03-multi-platform-strategies.md
    └── 04-build-cloud-setup.md
```

---

### Skill 5：docker-run

**定位**：容器运行与生命周期管理

**触发词**：`docker run`、`docker ps`、`docker stop`、`容器管理`、`资源限制`、`健康检查`、`重启策略`、`docker exec`、`docker logs`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| 怎么运行容器？ | docker run 完整参数：-d/-p/-v/-e/--name/--restart |
| 怎么限制资源？ | --memory/--cpus/--cpuset-cpus |
| 怎么做健康检查？ | HEALTHCHECK 指令 + docker inspect 查看状态 |
| 怎么管理日志？ | docker logs + 日志驱动 (json-file/syslog/fluentd) |
| 容器退出怎么办？ | 重启策略：no/on-failure/always/unless-stopped |
| 怎么进入容器调试？ | docker exec -it / docker attach |

**目录结构**：

```
docker-run/
├── SKILL.md
├── examples/
│   ├── 01-basic-run.md
│   ├── 02-resource-limits.md
│   └── 03-healthcheck.md
└── references/
    ├── 01-run-reference.md
    ├── 02-resource-management.md
    ├── 03-healthcheck-patterns.md
    └── 04-logging-drivers.md
```

---

### Skill 6：docker-networking

**定位**：Docker 网络配置与容器间通信

**触发词**：`docker network`、`容器网络`、`bridge`、`overlay`、`端口映射`、`容器通信`、`网络模式`、`host network`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| 网络模式有哪些？ | bridge/host/overlay/none/macvlan 对比选型 |
| 怎么让容器互通？ | 自定义 bridge 网络 + DNS 解析 |
| 怎么暴露端口？ | -p host:container + EXPOSE 指令 |
| 跨主机通信？ | overlay 网络 (Swarm) + Weave/Calico |
| 网络怎么排查？ | docker network inspect + ping/nslookup 调试 |

**目录结构**：

```
docker-networking/
├── SKILL.md
├── examples/
│   ├── 01-bridge-network.md
│   └── 02-custom-network.md
└── references/
    ├── 01-network-modes.md
    ├── 02-port-mapping.md
    └── 03-network-troubleshooting.md
```

---

### Skill 7：docker-storage

**定位**：Docker 存储与数据持久化

**触发词**：`docker volume`、`数据持久化`、`bind mount`、`tmpfs`、`存储驱动`、`备份恢复`、`数据卷`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| 数据怎么不丢失？ | Volume vs Bind Mount vs Tmpfs 对比 + 场景选型 |
| Volume 怎么管理？ | docker volume create/ls/inspect/prune |
| 怎么备份恢复？ | docker run --volumes-from + tar 备份 |
| 存储驱动选哪个？ | overlay2/devicemapper 对比 |
| 数据库容器怎么持久化？ | PostgreSQL/MySQL Volume 最佳实践 |

**目录结构**：

```
docker-storage/
├── SKILL.md
├── examples/
│   ├── 01-volume-basics.md
│   └── 02-database-persistence.md
└── references/
    ├── 01-storage-types.md
    ├── 02-volume-management.md
    └── 03-storage-drivers.md
```

---

### Skill 8：docker-compose（现有，大幅增强）

**定位**：多容器应用编排

**触发词**：`docker compose`、`docker-compose.yml`、`多容器`、`服务编排`、`compose 配置`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| compose 文件怎么写？ | services/networks/volumes/secrets/configs 完整语法 |
| 环境变量怎么管？ | .env / env_file / environment 三种方式 |
| 依赖顺序怎么控？ | depends_on + healthcheck + wait-for-it 模式 |
| 怎么区分环境？ | override 文件 + profiles 可选服务 |
| 怎么迁移到 K8s？ | kompose 工具 + 差异对比 |

**目录结构**：

```
docker-compose/
├── SKILL.md (增强)
├── examples/
│   ├── 01-lamp-stack.md (新增)
│   ├── 02-microservices.md (新增)
│   └── 03-monitoring-stack.md (新增)
└── references/
    ├── 01-compose-file-reference.md
    ├── 02-environment-management.md
    ├── 03-networking-in-compose.md
    └── 04-production-compose.md
```

---

### Skill 9：docker-security

**定位**：Docker 安全加固 — 镜像、运行时、供应链

**触发词**：`docker 安全`、`镜像安全`、`非root运行`、`seccomp`、`AppArmor`、`capabilities`、`docker bench`、`secret管理`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| 镜像怎么安全加固？ | 最小基础镜像、非root用户、固定版本tag |
| 运行时怎么隔离？ | seccomp/AppArmor/SELinux/capabilities |
| secrets 怎么管理？ | Docker secrets (Swarm) + BuildKit --secret |
| 怎么做安全审计？ | Docker Bench Security + CIS 检查清单 |
| Dockerfile 安全怎么写？ | COPY 优于 ADD、不暴露敏感信息、USER 指令 |

**目录结构**：

```
docker-security/
├── SKILL.md
├── examples/
│   ├── 01-secure-dockerfile.md
│   └── 02-docker-bench.md
└── references/
    ├── 01-image-security.md
    ├── 02-runtime-security.md
    ├── 03-secrets-management.md
    └── 04-cis-checklist.md
```

---

### Skill 10：docker-scout

**定位**：镜像漏洞扫描与 SBOM

**触发词**：`docker scout`、`漏洞扫描`、`CVE`、`SBOM`、`镜像分析`、`安全漏洞`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| 镜像有漏洞吗？ | docker scout quickview/cve |
| 怎么生成 SBOM？ | docker scout sbom |
| 怎么设置策略？ | Policy evaluation + 门禁规则 |
| 怎么集成到 CI？ | GitHub Actions / Jenkins 集成 |

---

### Skill 11：docker-hub

**定位**：镜像仓库管理 — 发布、拉取、私有仓库

**触发词**：`docker hub`、`镜像仓库`、`docker push`、`docker pull`、`私有仓库`、`registry`、`镜像标签`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| 怎么发布镜像？ | docker push + tag 策略 |
| 怎么搭建私有仓库？ | Docker Registry 容器 + Harbor 方案 |
| 标签怎么管理？ | semver + sha256 digest 固定 |
| 怎么加速拉取？ | registry-mirrors + Build Cloud |

---

### Skill 12：docker-cicd

**定位**：CI/CD 流水线中的 Docker 集成

**触发词**：`docker ci`、`docker cd`、`GitHub Actions docker`、`Jenkins docker`、`镜像构建流水线`、`Build Cloud`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| GitHub Actions 怎么用 Docker？ | docker/build-push-action + 多平台构建 |
| Jenkins Pipeline 怎么写？ | Docker agent + docker build + push |
| 怎么加速构建？ | Docker Build Cloud + 层缓存 + registry cache |
| 怎么多平台构建？ | docker buildx + qemu + multi-arch |

**目录结构**：

```
docker-cicd/
├── SKILL.md
├── examples/
│   ├── 01-github-actions.md
│   ├── 02-jenkins-pipeline.md
│   └── 03-multi-arch-build.md
└── references/
    ├── 01-build-cloud.md
    └── 02-buildx-multi-platform.md
```

---

### Skill 13：docker-production

**定位**：生产环境部署 — Swarm、K8s 迁移、监控

**触发词**：`生产部署`、`docker swarm`、`docker stack`、`k8s 迁移`、`docker 生产`、`容器编排`、`资源配额`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| 单机怎么部署？ | compose + systemd 自启动 |
| Swarm 集群怎么搭？ | docker swarm init/join + stack deploy |
| 怎么迁移到 K8s？ | kompose 转换 + 差异处理 + Helm Chart |
| 生产怎么监控？ | Prometheus + cAdvisor + Grafana |
| 怎么做零停机部署？ | rolling update + healthcheck + rollback |

---

### Skill 14：docker-troubleshooting

**定位**：问题排查与调试

**触发词**：`docker 排查`、`容器问题`、`docker debug`、`OOM`、`磁盘满`、`网络不通`、`启动失败`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| 容器启动失败？ | docker logs + Exit Code 速查 + inspect 状态 |
| 磁盘满了？ | docker system df/prune + 日志清理 |
| 网络不通？ | docker network inspect + iptables 排查 |
| OOM 了？ | --memory 限制 + docker stats + cAdvisor |

---

### Skill 15：docker-testcontainers

**定位**：测试容器 — Java/Python/Go 集成测试

**触发词**：`testcontainers`、`集成测试`、`docker 测试`、`数据库测试`、`Testcontainer`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| Java 集成测试怎么做？ | @Testcontainers + PostgreSQL/Redis/Kafka 模板 |
| Python 怎么做？ | testcontainers-python |
| 怎么管理测试生命周期？ | Singleton container + Ryuk 自动清理 |
| CI 中怎么用？ | DinD + 资源优化 |

---

### Skill 16：docker-ai-ml

**定位**：Docker 上的 AI/ML 工作负载 — 模型运行、Agent、Sandbox

**触发词**：`docker ai`、`model runner`、`本地模型`、`docker agent`、`GPU docker`、`sandbox`、`LLM 部署`

**核心能力**：

| 用户问 | 回答 |
|--------|------|
| 怎么跑本地 LLM？ | docker model pull/run + GPU 直通 |
| 怎么构建 AI Agent？ | Docker Agent 框架 + 多 agent 协作 |
| GPU 怎么配置？ | nvidia-container-toolkit + --gpus |
| 怎么做沙箱隔离？ | Docker Sandboxes + 安全限制 |

---

## 五、知识来源

| 来源 | 用途 |
|------|------|
| [Docker Documentation](https://docs.docker.com/) | 官方文档 — 命令参考、Dockerfile 语法、最佳实践 |
| [Docker Build](https://docs.docker.com/build/) | 构建系统 — BuildKit、多阶段、缓存策略 |
| [Docker Compose](https://docs.docker.com/compose/) | 编排 — compose 文件语法、环境管理 |
| [Docker Scout](https://docs.docker.com/scout/) | 安全扫描 — CVE、SBOM、策略 |
| [Docker Security](https://docs.docker.com/security/) | 安全基线 — CIS、seccomp、AppArmor |
| [Docker AI](https://docs.docker.com/ai-overview/) | AI/ML — Model Runner、Agent、Sandboxes |
| [Testcontainers](https://docs.docker.com/testcontainers/) | 测试 — Java/Python 集成测试 |
| [Docker Best Practices](https://docs.docker.com/build/building/best-practices/) | 构建最佳实践 |

---

## 六、实施优先级

| 优先级 | 技能 | 理由 |
|:--:|------|------|
| **P0** | docker-basics, docker-dockerfile, docker-build, docker-run | 核心基础，覆盖 80% 日常使用 |
| **P1** | docker-buildx, docker-compose, docker-networking, docker-storage | 多平台构建+多容器场景必备 |
| **P2** | docker-security, docker-cicd | 生产必备 |
| **P3** | docker-scout, docker-hub, docker-production | 企业级需求 |
| **P4** | docker-troubleshooting, docker-testcontainers | 专项场景 |
| **P5** | docker-ai-ml | 新兴场景，快速迭代 |

---

> 📋 参考 [ddd-skills/README.md](../ddd-skills/README.md) 的设计模式和 [Agent Skills 规范](https://agentskills.io/specification)
