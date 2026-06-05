# 存储驱动对比与选型

## 驱动总览

| 驱动 | 后端文件系统 | 写时复制 | 推荐度 |
|------|:--:|:--:|:--:|
| **overlay2** | overlay | ✅ | ⭐⭐⭐⭐⭐ |
| **fuse-overlayfs** | overlay（非特权） | ✅ | ⭐⭐⭐ |
| **btrfs** | btrfs | ✅ | ⭐⭐ |
| **zfs** | zfs | ✅ | ⭐⭐ |
| **devicemapper** | thin provisioning | ✅ | ⭐（已弃用） |
| **vfs** | 无 | ❌ | ⭐（仅测试） |
| **aufs** | aufs | ✅ | ⭐（已弃用） |

## 推荐：overlay2

```bash
# 检查当前驱动
docker info | grep "Storage Driver"
# Storage Driver: overlay2

# 检查 overlay 支持
lsmod | grep overlay
grep overlay /proc/filesystems
```

## 决策树

```
使用 Linux 4.x+？
├── 是 → overlay2（默认、推荐）
│
└── 否 → 升级内核。

使用 btrfs/zfs 作为宿主机文件系统？
├── btrfs → btrfs 驱动（快照优势）
└── zfs → zfs 驱动（快照+压缩优势）

Rootless 模式？
└── fuse-overlayfs（非特权 overlay）
```

## 性能对比（定性）

| 指标 | overlay2 | btrfs | zfs |
|------|:--:|:--:|:--:|
| 读写速度 | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 磁盘利用率 | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 快照/克隆 | - | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 稳定性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

## 磁盘空间管理

```bash
docker system df         # 汇总
docker system df -v      # 详细
docker system prune -a   # 清理（慎用！删除所有未运行镜像和未使用卷）
docker image prune       # 清理 dangling 镜像
docker volume prune      # 清理未使用卷
```
```

