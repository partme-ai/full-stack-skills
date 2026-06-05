---
name: docker-ai-ml
description: Guidance for running AI/ML workloads on Docker. Covers Docker Model Runner (docker model pull/run for local LLMs), Docker Agent (multi-agent orchestration for coding tasks), Docker Sandboxes for isolated AI agent execution, GPU acceleration (nvidia-container-toolkit, --gpus flag), AI model serving with Docker, and running open-source LLMs (Llama, Gemma, Qwen) locally. Use when the user asks about docker ai, docker model runner, local LLM, docker agent, GPU docker, sandbox, model serving, or needs to deploy AI models with Docker. 使用场景：docker ai、model runner、本地LLM、docker agent、GPU docker、sandbox、AI模型部署.
license: Apache-2.0
---

# Docker AI/ML — AI 工作负载

Guidance for running AI models and agents on Docker.

## When to Use

**ALWAYS use this skill when the user mentions:**
- "docker ai", "docker model", "model runner"
- "本地 LLM", "local model", "offline model"
- "docker agent", "AI agent"
- "GPU docker", "nvidia docker"
- "sandbox", "沙箱"
- "LLM 部署", "模型部署"

## Docker Model Runner

```bash
# List available models
docker model ls

# Pull a model
docker model pull ai/gemma3
docker model pull ai/qwen2.5

# Run inference
docker model run ai/gemma3 "Explain Docker in one sentence"

# Interactive chat
docker model run -i ai/gemma3

# API server mode
docker model serve ai/gemma3 --port 11434
# → access at http://localhost:11434/v1
```

### Install Skills for AI Coding Assistants

```bash
# Install skills for Claude Code
docker model skills --claude

# For Codex CLI
docker model skills --codex
```

## GPU Configuration

```bash
# Install NVIDIA Container Toolkit (once)
# Ubuntu/Debian:
sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker

# Run with GPU access
docker run --gpus all -it nvidia/cuda:12.6-base nvidia-smi

# Specific GPU
docker run --gpus device=0 -it nvidia/cuda:12.6-base

# GPU + Model Runner
docker model run --gpus all ai/llama3.2
```

## Docker Agent

```yaml
# agent.yaml — Define a multi-agent system
name: my-coding-agent
model:
  provider: openai
  model: gpt-4o
tools:
  - write_file
  - execute_command
  - web_search
sandbox:
  image: node:22-alpine
  workdir: /workspace
```

```bash
# Run agent with Docker
docker agent run -f agent.yaml "Fix the bug in src/app.js"
```

## Docker Sandbox

```yaml
# Isolated execution environment for AI agents
sandbox:
  image: python:3.12-slim
  network: none          # No network access
  read_only: true        # Read-only filesystem
  memory: 512m
  cpus: 1
```

## Local LLM Stack

```bash
# Ollama (open-source) as alternative
docker run -d --name ollama \
  -p 11434:11434 \
  -v ollama_data:/root/.ollama \
  --gpus all \
  ollama/ollama

# Download and run model
docker exec ollama ollama pull llama3.2
docker exec ollama ollama run llama3.2 "Hello"
```

## Workflow — 推荐使用流程

Step 1: **选择推理方案**: Docker Model Runner (`docker model`) 优先，Ollama 备选
Step 2: **检查硬件**: GPU 需 Linux + nvidia-container-toolkit；CPU 推理需 8-32GB RAM
Step 3: **拉取模型**: `docker model pull <model>` 或 `ollama pull <model>`
Step 4: **启动服务**: `docker model run` 或 `ollama serve` + 客户端
Step 5: **验证**: 发送测试 prompt 确认模型正常响应

## Gotchas — Common Pitfalls

- **GPU not available**: Docker Desktop Mac/Windows has limited GPU passthrough. → **Recovery**: Full GPU support requires Linux host + nvidia-container-toolkit; for Mac, use `docker model` which can offload inference.
- **Model download size**: LLMs are large (2-70 GB). → **Recovery**: `docker model pull` caches models in `~/.docker/models`; check `df -h` before pulling; use quantized models (Q4/Q8) for smaller footprint.
- **Memory limits**: LLM inference needs significant RAM (8-32 GB typical). → **Recovery**: `docker run --memory=16g model-runner`; check RAM: `free -h`; use smaller models (7B instead of 70B) if limited.
- **Model Runner vs Ollama**: Docker Model Runner is Docker-native. Ollama has larger ecosystem. → **Recovery**: Use `docker model` for Docker integration; use Ollama for broader model selection; both can coexist.

## Boundary — 能力边界（适用与不适用场景）

| 分类 | 场景 | 说明 |
|------|------|------|
| ✅ 能做 | 本地模型推理（Docker Model Runner / Ollama） | 拉取+运行开源 LLM，无需 API key |
| ✅ 能做 | GPU 加速推理 | Linux 宿主机 + nvidia-container-toolkit |
| ✅ 能做 | AI Agent 构建（Docker Agent / Sandboxes） | 多 agent 协作、沙箱隔离 |
| ⚠️ 需条件 | macOS GPU 推理 | Docker Desktop 支持有限，优先用 `docker model` |
| ⚠️ 需条件 | 大模型（70B+）推理 | 需 32GB+ RAM，考虑量化模型 |
| ❌ 超范围 | 训练/微调模型 | 需专用框架（PyTorch/TensorFlow），不在本技能范围 |
| ❌ 超范围 | 云端 API 调用（OpenAI/Claude） | 非本地推理，使用对应 SDK |
| ❌ 超范围 | 生产模型 Serving（K8s） | 使用 `docker-production` + K8s 部署 |

## When NOT to Use This Skill

| ❌ Skip | ✅ Use Instead |
|---------|---------------|
| Docker basics | `docker-basics` |
| Building custom model images | `docker-build` |
| Production model serving (K8s) | `docker-production` |
| Cloud AI APIs (no Docker needed) | Direct API access |

## Security & Stability

- Run model containers with `--read-only` when possible — models are read-only weights.
- Limit network access for model containers. Local inference doesn't need internet.
- GPU passthrough gives the container direct hardware access. Combine with `--security-opt` for isolation.
- Monitor GPU memory usage: `nvidia-smi` for utilization.

## 📚 官方文档参考

| 文档 | 地址 |
|------|------|
| Docker AI 概述 | https://docs.docker.com/ai-overview/ |
| Docker Model Runner | https://docs.docker.com/ai/model-runner/ |
| Docker Model Runner 入门 | https://docs.docker.com/ai/model-runner/get-started/ |
| Docker Agent | https://docs.docker.com/ai/docker-agent/ |
| Docker Sandboxes | https://docs.docker.com/ai/sandboxes/ |
| AI/ML 示例 | https://docs.docker.com/reference/samples/ai-ml/ |

## 🧭 Docker Skills Journey

> 📍 **You are here: `docker-ai-ml` — AI/ML 工作负载**

**← Prev**: `docker-testcontainers` — Integration testing
