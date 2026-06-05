# Docker Model Runner

```bash
# List available models
docker model ls

# Pull common models
docker model pull ai/gemma3
docker model pull ai/qwen2.5

# Interactive chat
docker model run -i ai/gemma3

# One-shot
docker model run ai/gemma3 "What is containerization?"

# Serve as API
docker model serve ai/gemma3 --port 11434
# → http://localhost:11434/v1/chat/completions

# Install skills for AI coding tools
docker model skills --claude    # Claude Code
docker model skills --codex     # OpenAI Codex CLI
```
