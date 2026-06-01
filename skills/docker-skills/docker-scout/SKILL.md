---
name: docker-scout
description: Guidance for Docker Scout — image vulnerability scanning, SBOM generation, and policy evaluation. Covers scout quickview for CVEs, scout cves for detailed vulnerability analysis, scout sbom for software bill of materials, policy evaluation with custom rules, CI/CD integration (GitHub Actions/Jenkins), and remediation guidance. Use when the user asks about docker scout, vulnerability scanning, CVE, SBOM, image analysis, security vulnerabilities, or needs to scan Docker images for security issues. 使用场景：docker scout、漏洞扫描、CVE、SBOM、镜像安全分析、安全漏洞、软件物料清单.
license: Apache-2.0
---

# Docker Scout — 镜像漏洞扫描与 SBOM

Guidance for vulnerability scanning, SBOM generation, and policy enforcement.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "docker scout", "镜像扫描", "漏洞扫描"
- "CVE", "vulnerability", "SBOM"
- "软件物料清单"
- "镜像安全分析", "image security scan"
- "policy evaluation"

## Core Commands

```bash
# Quick vulnerability overview
docker scout quickview myimage:tag

# Detailed CVE report
docker scout cves --format table myimage:tag
docker scout cves --only-fixed myimage:tag   # Show only fixable CVEs
docker scout cves --severity critical,high myimage:tag

# SBOM (Software Bill of Materials)
docker scout sbom myimage:tag                # SPDX format
docker scout sbom --format cyclonedx myimage:tag  # CycloneDX format

# Compare two images
docker scout compare myimage:v1 --to myimage:v2

# Policy evaluation
docker scout policy myimage:tag
```

## CVE Severity Levels

| Level | Action |
|-------|--------|
| **Critical** | Fix immediately |
| **High** | Fix in current sprint |
| **Medium** | Schedule fix |
| **Low** | Monitor |
| **Unspecified** | Review |

## CI/CD Integration

### GitHub Actions

```yaml
- name: Docker Scout
  uses: docker/scout-action@v1
  with:
    command: cves,compare
    image: ${{ steps.meta.outputs.tags }}
    compare-to: registry/${{ env.IMAGE_NAME }}:latest
```

## Remediation Workflow

```
1. docker scout cves myimage:tag → Identify CVEs
2. Check if fixable: --only-fixed shows which have patches
3. Update base image: FROM alpine:3.20 (newer version)
4. Update dependencies: npm update / pip install --upgrade / apt upgrade
5. Rebuild: docker build -t myimage:v2 .
6. Verify: docker scout compare myimage:v1 --to myimage:v2
```

## Workflow — 推荐扫描流程

Step 1: **快速扫描**: `docker scout quickview <image>` 获得 CVE 摘要
Step 2: **详细分析**: `docker scout cves --only-severity critical,high <image>`
Step 3: **查看建议**: `docker scout recommendations <image>` 获取修复方案
Step 4: **修复重建**: 更新基础镜像/依赖 → `docker build` → 再次扫描验证
Step 5: **CI 集成**: `docker/scout-action` + 策略门禁阻断

## Gotchas — Common Pitfalls

- **Scout vs scan**: `docker scan` (Snyk-based, deprecated). → **Recovery**: Always use `docker scout` instead; uninstall old `docker scan` plugin.
- **Only scanning, not fixing**: Scout shows CVEs but doesn't fix them. → **Recovery**: `docker scout recommendations <image>` for fix suggestions; update base image or rebuild with newer dependencies.
- **Base image CVEs**: Many CVEs come from the base image. → **Recovery**: `docker pull alpine:3.20` (update base); pin digest to avoid accidental downgrades; monitor with `docker scout cves alpine:3.20`.
- **Multi-stage skip**: Scanner needs access to both stages. → **Recovery**: Ensure all stage artifacts are `COPY --from=...` properly; tag intermediate stages if needed.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | CVE 漏洞扫描 | CLI: `docker scout cves` + quickview |
| ✅ 能做 | SBOM 生成 | `docker scout sbom --format spdx` |
| ✅ 能做 | 策略评估与 CI 阻断 | policy evaluation + GitHub Actions |
| ⚠️ 需条件 | 私有仓库扫描 | 需 Docker Scout 订阅 |
| ⚠️ 需条件 | 跨组织比较 | 需 Scout Dashboard（Web UI） |
| ❌ 超范围 | 运行时安全 | 使用 `docker-security` |
| ❌ 超范围 | 第三方扫描器（Trivy/Grype） | 各工具独立使用 |
| ❌ 超范围 | 修复漏洞（更新依赖） | 开发者自行完成 |

## When NOT to Use This Skill

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Runtime security (seccomp/AppArmor) | `docker-security` |
| Building images | `docker-build` |
| CI/CD pipeline setup | `docker-cicd` |
| Registry management | `docker-hub` |

## Security & Stability

- Run Scout in CI/CD to catch vulnerabilities before deployment.
- Subscribe to Docker security advisories for zero-day notifications.
- No executable scripts bundled. Guidance only.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker Scout 概述 | https://docs.docker.com/scout/ |
| Scout 快速入门 | https://docs.docker.com/scout/quickstart/ |
| Scout CLI 参考 | https://docs.docker.com/reference/cli/docker/scout/ |
| 策略评估 | https://docs.docker.com/scout/policy/ |
| CI 集成 | https://docs.docker.com/scout/integrations/ci/ |
| SBOM 管理 | https://docs.docker.com/scout/explore/sbom/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-scout` — 镜像安全扫描**

**← Prev**: `docker-security` — Security hardening
**→ Next**: `docker-hub` — Registry management
