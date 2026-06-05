# Docker Architecture

```
Docker Client (CLI)
    ↓ REST API
Docker Daemon (dockerd)
    ├── Image Management (build/pull/push)
    ├── Container Runtime (via containerd)
    ├── Network Management (bridge/overlay/host)
    └── Volume Management (local/NFS/cloud)

containerd (container supervisor)
    ↓
runc (OCI runtime — creates containers)
    ↓
Linux Kernel (namespaces + cgroups)
```

## Key Linux features Docker uses

| Feature | Purpose |
|---------|---------|
| **Namespaces** | Process isolation (PID, NET, MNT, UTS, IPC, USER) |
| **Cgroups** | Resource limits (CPU, memory, I/O) |
| **UnionFS (overlay2)** | Layered filesystem for images |
