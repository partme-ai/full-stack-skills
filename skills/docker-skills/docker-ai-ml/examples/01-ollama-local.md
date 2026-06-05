# Run Ollama with Docker + GPU

```bash
# Start Ollama with GPU support
docker run -d --name ollama   --gpus all   -p 11434:11434   -v ollama_data:/root/.ollama   ollama/ollama

# Pull and run a model
docker exec ollama ollama pull llama3.2
docker exec -it ollama ollama run llama3.2

# API access
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Explain Docker in one sentence"
}'
```
