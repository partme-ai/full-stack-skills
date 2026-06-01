# Volume 管理全命令

## 基本操作

```bash
docker volume create myvolume
docker volume ls
docker volume inspect myvolume
docker volume rm myvolume
docker volume prune     # 删除所有未使用的 volume
```

## 挂载到容器

```bash
# 命名卷
docker run -d -v myvolume:/data alpine

# bind mount（绝对路径）
docker run -d -v /host/path:/container/path:ro alpine

# bind mount（相对路径，需 --mount）
docker run -d --mount type=bind,src=./data,target=/data alpine

# tmpfs
docker run -d --tmpfs /tmp:rw,size=128M alpine
```

## 备份与恢复

```bash
# 备份
docker run --rm \
  -v db_data:/source \
  -v $(pwd):/backup \
  alpine tar czf /backup/db_data_backup.tar.gz -C /source .

# 恢复
docker run --rm \
  -v db_data:/target \
  -v $(pwd):/backup \
  alpine tar xzf /backup/db_data_backup.tar.gz -C /target
```

## 迁移 Volume

```bash
# 从旧主机导出
docker run --rm -v old_data:/data alpine tar czf - -C /data . > data.tar.gz

# 传输到新主机
scp data.tar.gz new-host:

# 在新主机导入
docker volume create new_data
docker run --rm -v new_data:/data -v $(pwd):/backup alpine \
  tar xzf /backup/data.tar.gz -C /data
```

## 查看 Volume 占用

```bash
docker system df -v      # 含 volume 详情
docker volume ls -q | xargs docker volume inspect --format '{{.Name}}: {{.Mountpoint}}'
```

## NFS Volume 驱动

```bash
docker volume create \
  --driver local \
  --opt type=nfs \
  --opt o=addr=192.168.1.100,nolock,rw \
  --opt device=:/exports/data \
  nfs_data
```
```

