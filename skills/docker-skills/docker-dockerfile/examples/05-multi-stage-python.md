# Python FastAPI 多阶段构建 — venv + uvicorn

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.12-alpine AS builder
RUN apk add --no-cache gcc musl-dev libffi-dev
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-alpine
RUN apk add --no-cache libffi tzdata
RUN addgroup -S pyuser && adduser -S pyuser -G pyuser
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY src/ ./src/
USER pyuser
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]
```

**requirements.txt**: `fastapi==0.115.*` `uvicorn[standard]==0.32.*` `pydantic==2.*`

**.dockerignore**: `__pycache__/ *.pyc .venv/ venv/ .git/ .env*`

| 方案 | 镜像大小 |
|------|---------|
| 单阶段 python:3.12 | ~200 MB |
| 多阶段 alpine + venv | ~80 MB |
```
