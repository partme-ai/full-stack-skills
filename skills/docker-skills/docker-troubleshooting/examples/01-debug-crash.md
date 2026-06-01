# Debug a crashing container

```bash
# Scenario: Container exits immediately after starting

# 1. Check status
docker ps -a
# STATUS: Exited (1) 2 seconds ago

# 2. Get exit code
docker inspect --format='{{.State.ExitCode}}' myapp
# → 1 (application error)

# 3. View logs (even for stopped containers!)
docker logs myapp
# → Error: Cannot connect to database

# 4. Override entrypoint to debug
docker run --rm -it --entrypoint sh myapp
# Now you're inside a shell — debug interactively

# 5. Check resource issues
docker inspect --format='{{.State.OOMKilled}}' myapp
# → false (not OOM this time)

# 6. Try with more memory
docker run --memory=1g myapp
```
