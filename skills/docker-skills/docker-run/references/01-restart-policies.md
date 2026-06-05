# Restart Policies

| Policy | Behavior | Recommended For |
|--------|----------|-----------------|
| `no` (default) | Never restart | One-off jobs, batch tasks |
| `on-failure[:N]` | Restart on non-zero exit, max N times | Batch jobs with retry |
| `always` | Always restart (even after daemon restart) | ⚠️ Use with caution — infinite loop risk |
| `unless-stopped` | Restart unless explicitly stopped | **Most services (recommended)** |

```bash
# Set at run time
docker run --restart unless-stopped myapp

# Change on running container
docker update --restart always myapp
```
