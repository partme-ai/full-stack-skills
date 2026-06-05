# Docker 安装指南

## macOS

| 方案 | 特点 | 推荐度 |
|------|------|:--:|
| **Docker Desktop** | GUI + 自动更新 + K8s 集成 | ⭐⭐⭐ |
| **OrbStack** | 轻量、快速、原生文件共享 | ⭐⭐⭐⭐ |
| **Colima** | 免费开源、CLI 驱动 | ⭐⭐⭐ |

### Docker Desktop

```bash
brew install --cask docker
# 启动 Docker Desktop.app，根据向导完成
```

### OrbStack

```bash
brew install orbstack
# 启动 OrbStack.app
```

### Colima

```bash
brew install colima docker docker-compose
colima start --cpu 4 --memory 8 --disk 60
docker ps   # 验证
```

## Linux

```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER
newgrp docker

# CentOS/RHEL/Fedora
sudo dnf install docker-ce docker-ce-cli containerd.io
sudo systemctl enable --now docker
```

## Windows

- WSL 2 + Docker Desktop（推荐）
- `winget install Docker.DockerDesktop`

## 验证安装

```bash
docker --version
docker compose version
docker run --rm hello-world
```

## 卸载

```bash
# macOS（Docker Desktop）
brew uninstall --cask docker

# Linux
sudo apt purge docker-ce docker-ce-cli containerd.io
sudo rm -rf /var/lib/docker /var/lib/containerd
```
```

