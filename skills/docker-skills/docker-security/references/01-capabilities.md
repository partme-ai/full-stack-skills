# Linux Capabilities Reference

| Capability | Allows | Keep? |
|-----------|--------|:--:|
| NET_BIND_SERVICE | Bind to ports < 1024 | ✅ Often needed |
| CHOWN | Change file ownership | ⚠️ If writing files |
| DAC_OVERRIDE | Bypass file permissions | ❌ Drop |
| SYS_ADMIN | Almost root — mount, swapon, etc. | ❌ NEVER keep |
| SYS_PTRACE | Debug other processes | ❌ Drop |
| NET_RAW | Raw sockets (ping) | ⚠️ If needed |

```bash
# Drop all, add only what's needed
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE app
```
