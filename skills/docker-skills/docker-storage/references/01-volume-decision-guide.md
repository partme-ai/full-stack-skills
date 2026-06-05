# Volume types: when to use what

| Scenario | Type | Command |
|----------|------|---------|
| Database storage (PostgreSQL/MySQL) | Named Volume | `-v pgdata:/var/lib/postgresql/data` |
| Config files (nginx.conf) | Bind Mount (ro) | `-v ./nginx.conf:/etc/nginx/nginx.conf:ro` |
| Dev code sync (hot reload) | Bind Mount | `-v $(pwd)/app:/app` |
| Temp/sensitive data (never disk) | Tmpfs | `--tmpfs /tmp:rw,size=64m` |
| Logs (host access needed) | Bind Mount | `-v ./logs:/var/log/app` |
| Shared data across containers | Named Volume | `-v shared:/shared` |

### Decision Flow

```
Does the data need to outlive the container?
├── NO → Tmpfs (RAM only, never touches disk)
└── YES → Does Docker need to manage it?
    ├── YES → Named Volume (production data, managed lifecycle)
    └── NO → Bind Mount (your filesystem path)
        └── Is it mutable?
            ├── NO → Read-only bind mount (:ro)
            └── YES → Read-write bind mount
```
