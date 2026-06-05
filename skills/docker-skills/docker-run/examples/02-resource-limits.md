# Production-grade resource limits

```bash
docker run -d --name app   --memory=512m --memory-swap=512m \   # Hard limit, no swap
  --memory-reservation=256m \          # Soft limit for scheduler
  --cpus=2 \                           # Max 2 CPU cores
  --cpu-shares=1024 \                  # Relative weight (default 1024)
  --pids-limit=100 \                   # Prevent fork bombs
  --ulimit nofile=65536:65536 \        # Max open files
  --read-only \                        # Read-only root filesystem
  --tmpfs /tmp:rw,noexec,nosuid \      # Writable /tmp in RAM
  myapp:1.0.0
```
