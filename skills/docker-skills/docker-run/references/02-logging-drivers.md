# Logging Drivers

| Driver | Where Logs Go | Rotation? | Use Case |
|--------|--------------|:--:|------|
| `json-file` (default) | Host disk | Manual (--log-opt) | Development |
| `syslog` | Syslog daemon | System | Centralized logging |
| `journald` | journald | System | systemd-based systems |
| `fluentd` | Fluentd | Agent | ELK/Loki stack |
| `awslogs` | CloudWatch | AWS | AWS ECS |
| `gcplogs` | Stackdriver | GCP | GKE |

```bash
# Production log rotation (json-file)
docker run --log-opt max-size=10m --log-opt max-file=3 myapp

# Daemon-level: /etc/docker/daemon.json
{ "log-driver": "json-file", "log-opts": { "max-size": "10m", "max-file": "3" } }
```
