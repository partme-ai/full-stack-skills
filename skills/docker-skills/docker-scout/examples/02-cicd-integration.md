# GitHub Actions 集成 Docker Scout

## .github/workflows/scout.yml

```yaml
name: Docker Scout Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 8 * * 1'          # 每周一早 8 点

jobs:
  scan:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
      security-events: write     # 写入 Security 标签页

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build image
        uses: docker/build-push-action@v6
        with:
          context: .
          tags: myapp:${{ github.sha }}
          load: true
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Docker Scout scan
        id: scout
        uses: docker/scout-action@v1
        with:
          command: cves,recommendations
          image: myapp:${{ github.sha }}
          sarif-file: scout-results.sarif
          exit-code: true         # 有 Critical/High 漏洞时 CI 失败
          only-severities: critical,high

      - name: Upload SARIF to GitHub
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: scout-results.sarif
```

## 策略门禁（CI 阻断）

```yaml
- name: Docker Scout policy evaluation
  uses: docker/scout-action@v1
  with:
    command: compare
    image: myapp:${{ github.sha }}
    to: myapp:latest             # 和上一次构建比
    exit-on: policy              # 策略恶化时失败
    only-severities: critical,high
```

## 效果

- PR 提交后自动扫描，Security 标签页可查看漏洞
- 发现 Critical/High → CI 红叉，阻止合并
- 每周定时扫描，捕获新发现的 CVE
```

