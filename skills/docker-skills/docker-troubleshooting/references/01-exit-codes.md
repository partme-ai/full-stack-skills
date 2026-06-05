# Docker Exit Code Reference

| Code | Meaning | Common Cause | Debug Action |
|------|---------|-------------|-------------|
| 0 | Success | Normal exit | — |
| 1 | Application error | App crashed, wrong config | `docker logs` |
| 125 | Docker daemon error | `docker run` failed | Check daemon |
| 126 | Permission denied | CMD/ENTRYPOINT not executable | `chmod +x` in Dockerfile |
| 127 | Command not found | Wrong path in CMD | `docker run --entrypoint sh` |
| 137 | SIGKILL | OOM killed or `docker kill` | Check `OOMKilled` in inspect; increase memory |
| 139 | SIGSEGV | Segfault (app bug) | Check app code |
| 143 | SIGTERM | Graceful shutdown timeout | Check healthcheck timeout |
