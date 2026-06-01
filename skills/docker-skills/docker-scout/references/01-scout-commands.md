# Docker Scout 命令速查

## 核心命令

| 命令 | 说明 |
|------|------|
| `docker scout quickview` | 快速摘要（CVE 计数） |
| `docker scout cves` | CVE 详细列表 |
| `docker scout recommendations` | 修复建议 |
| `docker scout sbom` | 生成 SBOM |
| `docker scout compare` | 对比两个镜像 |
| `docker scout policy` | 策略评估 |
| `docker scout enroll` | 注册组织 |
| `docker scout cache` | 管理 SBOM 缓存 |

## quickview

```bash
docker scout quickview nginx:1.27-alpine

# 输出：
#    0C     0H     1M     2L  nginx:1.27-alpine
#    ↑      ↑      ↑      ↑
#  Critical High  Medium  Low
```

## cves

```bash
# 基本用法
docker scout cves nginx:1.27-alpine

# 仅显示目标严重级别
docker scout cves --only-severity critical,high nginx:1.27-alpine

# 仅显示已修复的
docker scout cves --only-fixed nginx:1.27-alpine

# 忽略基础镜像中的 CVE
docker scout cves --ignore-base nginx:1.27-alpine

# JSON 输出（CI 集成）
docker scout cves --format json nginx:1.27-alpine
```

## recommendations

```bash
docker scout recommendations nginx:1.27-alpine

# 输出：
# Recommendation 1 of 3: Use a specific tag
# 使用 :latest 可能引入意外变更，改为 :1.27-alpine
```

## sbom

```bash
# 生成 SPDX 格式 SBOM
docker scout sbom --format spdx nginx:1.27-alpine

# 输出 SBOM 到文件
docker scout sbom --output nginx-sbom.spdx.json nginx:1.27-alpine
```

## compare

```bash
# 对比两个镜像
docker scout compare nginx:1.26-alpine nginx:1.27-alpine

# 对比同一镜像的两个版本
docker scout compare myapp:v1 myapp:v2 --ignore-base
```

## policy

```bash
# 评估策略合规性
docker scout policy myapp:latest

# 输出：
# ✓ Policies passed (12/12)
#   No critical or high CVEs (0/0)
#   No non-official base images
#   Approved licenses only
```

## 常用组合

```bash
# CI 一键扫描
docker scout quickview myapp:latest && \
  docker scout cves --only-severity critical,high myapp:latest && \
  docker scout recommendations myapp:latest
```
```

