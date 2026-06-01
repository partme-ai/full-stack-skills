# 快速漏洞扫描

```bash
# 扫描当前镜像
docker scout quickview nginx:1.27-alpine

# 输出：
# ✓ SBOM of image already cached, 228 packages indexed
#
#   Target  │  nginx:1.27-alpine  │    0C     0H     0M     0L
#     digest│  abc123...          │
#
#   What's next:
#     View detailed results → docker scout cves nginx:1.27-alpine
```

## 查看 CVE 详情

```bash
docker scout cves nginx:1.27-alpine

# 输出：
#    0C     0H     0M     1L  nginx:1.27-alpine
#
#    ✗ LOW CVE-2024-12345 [OWASP Top Ten]
#      https://scout.docker.com/v/CVE-2024-12345
#      Affected range: <1.27.1
#      Fixed version : 1.27.1
```

## 查看推荐

```bash
docker scout recommendations nginx:1.27-alpine

# 输出建议：
# - 升级基础镜像到最新版本
# - 添加 HEALTHCHECK
# - 使用非 root 用户
# - 固定基础镜像 digest
```

## 修复后验证

```bash
# 修复 Dockerfile 后重新构建
docker build -t myapp:fixed .

# 对比前后
docker scout compare myapp:old myapp:fixed
```

## 快速命令组合

```bash
# 一键扫描 + 推荐（CI 常用）
docker scout quickview myapp:latest && docker scout recommendations myapp:latest
```
```

