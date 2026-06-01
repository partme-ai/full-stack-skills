# Swarm stack file for production

```yaml
version: '3.8'
services:
  web:
    image: myapp:${TAG:-latest}
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
        failure_action: rollback
      rollback_config:
        parallelism: 1
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
    ports:
      - "80:8080"
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:8080/health"]
      interval: 30s
      timeout: 3s
      retries: 3
    networks:
      - frontend

  redis:
    image: redis:7-alpine
    deploy:
      replicas: 1
    volumes:
      - redis-data:/data
    networks:
      - backend

networks:
  frontend:
  backend:
    internal: true

volumes:
  redis-data:
```

```bash
docker stack deploy -c docker-compose.yml myapp
docker stack services myapp
docker stack ps myapp
```
