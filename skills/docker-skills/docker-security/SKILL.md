---
name: docker-security
description: Guidance for Docker security hardening across the full lifecycle — image security (minimal base images, non-root users, pinned versions), runtime security (seccomp/AppArmor/SELinux, capabilities, read-only rootfs, no-new-privileges), secrets management (BuildKit secrets, Docker secrets in Swarm), Docker Bench Security auditing, CIS compliance checklist, and supply-chain security (image signing, content trust, SBOM). Use when the user asks about Docker security, image hardening, non-root containers, seccomp, AppArmor, Docker Bench, secrets management, or securing containers. 使用场景：docker 安全、镜像安全、非root运行、seccomp、AppArmor、security、Docker Bench、secret管理.
license: Apache-2.0
---

# Docker Security — 安全加固与防护

Comprehensive guidance for securing Docker across the full lifecycle.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "docker 安全", "镜像安全", "container security"
- "非root运行", "rootless", "least privilege"
- "seccomp", "AppArmor", "SELinux"
- "Docker Bench", "CIS"
- "secrets management", "密钥管理"
- "image signing", "content trust"

## Security Model — Layered Defense

```
Layer 1: Image Security    — minimal base, non-root, pinned versions
Layer 2: Build Security    — secret injection, noCOPY secrets
Layer 3: Runtime Security  — capabilities, seccomp, AppArmor, read-only
Layer 4: Registry Security — content trust, signing, vulnerability scan
Layer 5: Host Security     — Docker Bench, CIS, user namespace
```

## Image Security Checklist

| # | Practice | How |
|---|----------|-----|
| 1 | **Minimal base image** | Use `alpine` or `distroless` (Go → `scratch`) |
| 2 | **Non-root user** | `USER 1000:1000` at end of Dockerfile |
| 3 | **Pin versions** | `FROM alpine:3.20@sha256:...` not `alpine:latest` |
| 4 | **COPY over ADD** | ADD auto-extracts tar — unexpected behavior |
| 5 | **No secrets in image** | Use `--secret` or runtime injection |
| 6 | **`.dockerignore`** | Exclude `.env`, `.git`, credentials |

### Secure Dockerfile

```dockerfile
FROM alpine:3.20
RUN apk add --no-cache ca-certificates
RUN addgroup -S app && adduser -S -G app app
COPY --chown=app:app ./app /app
WORKDIR /app
USER app
CMD ["./server"]
```

## Runtime Security

### Capabilities (Least Privilege)

```bash
# Drop ALL capabilities, add only what's needed
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE nginx

# Common needed caps: NET_BIND_SERVICE, CHOWN, DAC_OVERRIDE
# NEVER: --privileged (gives full host access)
```

### Read-Only Root Filesystem

```bash
# Prevents container from writing anywhere (except volumes/tmpfs)
docker run --read-only --tmpfs /tmp --tmpfs /run nginx
```

### Seccomp Profile

```bash
# Custom seccomp profile (block syscalls)
docker run --security-opt seccomp=profile.json app

# Unconfined (NEVER in production)
docker run --security-opt seccomp=unconfined app
```

### No New Privileges

```bash
# Prevent privilege escalation via setuid binaries
docker run --security-opt no-new-privileges app
```

## Secrets Management

### BuildKit Secrets (build-time)

```dockerfile
# syntax=docker/dockerfile:1
FROM alpine
RUN --mount=type=secret,id=aws_creds \
  AWS_ACCESS_KEY_ID=$(cat /run/secrets/aws_creds) \
  aws s3 cp s3://bucket/file .
```

```bash
docker build --secret id=aws_creds,src=$HOME/.aws/credentials -t app .
```

### Docker Secrets (Swarm runtime)

```bash
echo "mysecretpassword" | docker secret create db_password -
docker service create --secret db_password postgres
```

## Docker Bench Security Audit

```bash
docker run --rm \
  --pid host --network host \
  -v /var/run/docker.sock:/var/run/docker.sock \
  docker/docker-bench-security
```

## Workflow — 安全加固流程

Step 1: **镜像安全**: `docker scout cves <image>` 扫描漏洞 → 更新基础镜像/依赖
Step 2: **Dockerfile 加固**: USER 非 root、COPY 优于 ADD、固定 digest
Step 3: **运行时安全**: --read-only、--cap-drop=ALL、--security-opt no-new-privileges
Step 4: **审计检查**: `docker run --rm docker/docker-bench-security` 逐条修复
Step 5: **CI 门禁**: Scout 策略阻断 critical/high CVE 合并

## Gotchas — Common Pitfalls

- **`--privileged` flag**: Gives full host access. Never use in production. → **Recovery**: Use specific `--cap-add=NET_BIND_SERVICE` instead; audit with `docker inspect --format='{{.HostConfig.Privileged}}'`.
- **API keys in Dockerfile**: `ENV API_KEY=xxx` is baked into image layers forever. → **Recovery**: Use runtime injection: `docker run -e API_KEY=$KEY` or BuildKit `--mount=type=secret`.
- **Root container**: Default user is root. Escaping the container means root on the host. → **Recovery**: Always `USER 1000:1000` in Dockerfile; verify with `docker exec myapp whoami`.
- **Docker socket mount**: `-v /var/run/docker.sock` gives container control over ALL containers. → **Recovery**: Use Docker API with TLS auth instead of socket mount; never mount socket in production.
- **Ignoring CVE remediation**: Running `docker scout` but never fixing findings. → **Recovery**: Set CI policy to block critical/high CVEs; update base images regularly.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | Dockerfile 安全加固 | USER 非 root、COPY 优先 ADD、digest 固定 |
| ✅ 能做 | 运行时安全配置 | seccomp/AppArmor/capabilities/read-only |
| ✅ 能做 | Secrets 管理 | Docker secrets + BuildKit --secret + Vault |
| ✅ 能做 | 安全审计（Docker Bench Security） | CIS 检查清单 + 逐条修复 |
| ⚠️ 需条件 | 镜像签名（Notary） | 需 `DOCKER_CONTENT_TRUST=1` 环境变量 |
| ⚠️ 需条件 | 完整合规检查 | 需结合 Scout 扫描 + 组织安全策略 |
| ❌ 超范围 | CVE 漏洞扫描 | 使用 `docker-scout` |
| ❌ 超范围 | 主机系统安全 | 操作系统层级 |
| ❌ 超范围 | 网络安全/防火墙 | 网络管理员范畴 |

## When NOT to Use This Skill

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Vulnerability scanning | `docker-scout` |
| Docker basics | `docker-basics` |
| Production deployment | `docker-production` |
| Registry management | `docker-hub` |

## Security & Stability

- All security practices are based on CIS Docker Benchmark and Docker official security guidance.
- Run Docker Bench Security regularly in CI/CD to detect configuration drift.
- Subscribe to Docker security advisories for CVE notifications.
- No executable scripts bundled. Guidance only.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker 安全 | https://docs.docker.com/security/ |
| Docker Hardened Images | https://docs.docker.com/dhi/ |
| Docker Scout | https://docs.docker.com/scout/ |
| Docker Bench Security | https://docs.docker.com/engine/security/bench/ |
| seccomp 配置 | https://docs.docker.com/engine/security/seccomp/ |
| AppArmor | https://docs.docker.com/engine/security/apparmor/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-security` — 安全加固**

**← Previous**: `docker-build` | **→ Next**: `docker-scout` / `docker-cicd`
