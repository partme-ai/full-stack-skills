# Secure Dockerfile template

```dockerfile
FROM alpine:3.20@sha256:abc123...   # Pin digest

# Create non-root user
RUN addgroup -S app && adduser -S -G app app

# Install only what's needed
RUN apk add --no-cache ca-certificates

# Copy with ownership
COPY --chown=app:app . /app
WORKDIR /app

# Drop to non-root
USER app

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s   CMD wget -qO- http://localhost:8080/health || exit 1

CMD ["./server"]
```

### Run with security options
```bash
docker run -d   --read-only --tmpfs /tmp   --cap-drop=ALL --cap-add=NET_BIND_SERVICE   --security-opt no-new-privileges   --memory=256m --cpus=1   app
```
