# Docker Network Modes

| Mode | Command | DNS | Cross-Host | Use Case |
|------|---------|:--:|:--:|------|
| bridge (default) | — | ❌ | ❌ | Legacy single-host |
| **custom bridge** | `--network mynet` | ✅ | ❌ | **Single-host recommended** |
| host | `--network host` | ❌ | ❌ | Max performance (no isolation) |
| overlay | `--network my-overlay` | ✅ | ✅ | Swarm multi-host |
| none | `--network none` | ❌ | ❌ | No network needed |
| macvlan | `--network macnet` | ❌ | ✅ | Legacy apps needing physical IP |
