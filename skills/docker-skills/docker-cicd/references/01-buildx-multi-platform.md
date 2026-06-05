# Buildx Multi-Platform Build

```bash
# Create builder with multi-platform support
docker buildx create --name multiarch --use
docker buildx inspect --bootstrap

# Build for multiple platforms
docker buildx build   --platform linux/amd64,linux/arm64   -t myapp:latest   --push .

# Check platform support
docker buildx imagetools inspect myapp:latest

# GitHub Actions example: add platforms to build-push-action
# platforms: linux/amd64,linux/arm64
```
