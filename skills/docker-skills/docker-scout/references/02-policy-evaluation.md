# Docker Scout 策略评估

## 策略文件结构

```yaml
# .docker/scout/policy.yaml
apiVersion: docker.com/v1alpha1
kind: Policy
metadata:
  name: production-policy
spec:
  policies:
    - id: no-critical-cves
      description: No critical CVEs allowed
      rules:
        - type: cve
          params:
            severity: critical
            max: 0

    - id: max-high-cves
      description: Maximum 5 high CVEs
      rules:
        - type: cve
          params:
            severity: high
            max: 5

    - id: only-official-images
      description: Base images must be from trusted sources
      rules:
        - type: base-image
          params:
            allowed: [docker.io/library/*, ghcr.io/*, public.ecr.aws/*]

    - id: approved-licenses
      description: Only approved licenses
      rules:
        - type: license
          params:
            allowed: [MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC]
            denied: [GPL-2.0, GPL-3.0, AGPL-3.0]
```

## CI 门禁集成

```bash
# 本地验证
docker scout policy --policy .docker/scout/policy.yaml myapp:latest

# GitHub Actions
- uses: docker/scout-action@v1
  with:
    command: policy
    image: myapp:${{ github.sha }}
    policy: .docker/scout/policy.yaml
    exit-on: policy
```

## 策略恶化检测

对比基线镜像，仅在新漏洞变多时阻断：

```bash
docker scout compare \
  --to myapp:latest \
  --exit-on policy \
  myapp:${{ github.sha }}
```

## 严重级别阈值

| 级别 | 建议阈值 | 场景 |
|------|:--:|------|
| Critical | 0 | 所有生产环境 |
| High | 0-3 | 生产 / 有修复计划 |
| Medium | < 10 | 开发环境 / 有缓解措施 |
| Low | < 20 | 信息性 / 追踪即可 |
```

