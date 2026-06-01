# Container lifecycle demo

```bash
# Create (doesn't start)
docker create --name demo nginx:alpine

# Start
docker start demo

# Check status
docker ps
docker ps -a

# Stop
docker stop demo

# Start again (no data loss with volumes)
docker start demo

# Remove
docker stop demo && docker rm demo

# One-liner: create, start, auto-remove on stop
docker run --rm -d --name demo nginx:alpine
```
