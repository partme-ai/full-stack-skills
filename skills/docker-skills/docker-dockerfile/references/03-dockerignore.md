# .dockerignore 模板

## 通用
```
.git/ .gitignore *.md LICENSE .vscode/ .idea/ .env* Dockerfile* docker-compose*
```

## Node.js
```
node_modules/ dist/ build/ .next/ .nuxt/ coverage/ .pnpm-store/ *.log
```

## Java/Maven
```
target/ *.class *.jar *.war !.mvn/wrapper/maven-wrapper.jar .gradle/ build/
```

## Go
```
*.exe *.test vendor/ *.out tmp/
```

## Python
```
__pycache__/ *.py[cod] *.egg-info/ .venv/ venv/ env/ .pytest_cache/ .mypy_cache/
```

## Rust
```
target/ debug/ *.rs.bk *.pdb
```

## .NET
```
bin/ obj/ *.user packages/
```

## 规则
1. `.dockerignore` 优先于 `!` 排除
2. 不存在时使用 `.gitignore`

```bash
# 验证上下文大小
docker build --no-cache -t temp . 2>&1 | grep "sending build context"
```
```

