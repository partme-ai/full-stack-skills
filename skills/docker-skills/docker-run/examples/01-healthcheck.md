# Container with health check

```dockerfile
FROM nginx:alpine
COPY default.conf /etc/nginx/conf.d/
HEALTHCHECK --interval=30s --timeout=3s --retries=3   CMD wget -qO- http://localhost/health || exit 1
```

```bash
docker build -t nginx-health .
docker run -d --name web nginx-health

# Watch health status change: starting → healthy
watch docker inspect --format='{{.State.Health.Status}}' web

# Simulate unhealthy: kill nginx inside
docker exec web nginx -s stop
# After 3 failed checks → unhealthy
```
