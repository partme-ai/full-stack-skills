# CIS Docker Benchmark — Key Checks

| # | Check | How to Verify |
|---|-------|--------------|
| 1 | Run Docker Bench | `docker run docker/docker-bench-security` |
| 2 | Non-root user | `docker inspect --format='{{.Config.User}}' container` |
| 3 | Read-only rootfs | `docker inspect --format='{{.HostConfig.ReadonlyRootfs}}' container` |
| 4 | No --privileged | Don't use `--privileged`; use `--cap-add` |
| 5 | CPU/Memory limited | `docker inspect --format='{{.HostConfig.Memory}}' container` |
| 6 | Health check defined | `docker inspect --format='{{.Config.Healthcheck}}' container` |
| 7 | Content trust enabled | `export DOCKER_CONTENT_TRUST=1` |
| 8 | Docker socket protected | `ls -la /var/run/docker.sock` (root:docker 660) |
